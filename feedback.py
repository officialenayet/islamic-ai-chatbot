from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_required
from datetime import datetime

from src.models.database import db, User, Message, Feedback

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/', methods=['POST'])
@jwt_required(optional=True)
def submit_feedback():
    try:
        # Get current user (optional for anonymous feedback)
        current_user_id = get_jwt_identity()
        
        data = request.get_json()
        
        # Validate required fields
        if not data.get('rating'):
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Rating is required'
                }
            }), 400
        
        rating = data['rating']
        comment = data.get('comment', '').strip()
        feedback_type = data.get('feedback_type', 'general')
        message_id = data.get('message_id')
        
        # Validate rating
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Rating must be between 1 and 5'
                }
            }), 400
        
        # Validate feedback type
        valid_types = ['accuracy', 'helpfulness', 'relevance', 'general']
        if feedback_type not in valid_types:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': f'Invalid feedback type. Must be one of: {", ".join(valid_types)}'
                }
            }), 400
        
        # Verify message exists if message_id provided
        if message_id:
            message = Message.query.get(message_id)
            if not message:
                return jsonify({
                    'success': False,
                    'error': {
                        'code': 'MESSAGE_NOT_FOUND',
                        'message': 'Message not found'
                    }
                }), 404
            
            # If user is logged in, verify they own the message
            if current_user_id:
                if message.session.user_id != current_user_id:
                    return jsonify({
                        'success': False,
                        'error': {
                            'code': 'FORBIDDEN',
                            'message': 'You can only provide feedback for your own messages'
                        }
                    }), 403
        
        # Create feedback
        new_feedback = Feedback(
            user_id=current_user_id,
            message_id=message_id,
            rating=rating,
            comment=comment,
            feedback_type=feedback_type
        )
        
        db.session.add(new_feedback)
        
        # Update message feedback if message_id provided
        if message_id:
            message = Message.query.get(message_id)
            message.feedback_rating = rating
            message.feedback_comment = comment
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Feedback submitted successfully',
            'data': {
                'feedback_id': new_feedback.id
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Submit feedback error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to submit feedback'
            }
        }), 500

@feedback_bp.route('/message/<message_id>', methods=['POST'])
@jwt_required()
def submit_message_feedback(message_id):
    try:
        current_user_id = get_jwt_identity()
        
        # Find message
        message = Message.query.get(message_id)
        if not message:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'MESSAGE_NOT_FOUND',
                    'message': 'Message not found'
                }
            }), 404
        
        # Verify user owns the message
        if message.session.user_id != current_user_id:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'FORBIDDEN',
                    'message': 'You can only provide feedback for your own messages'
                }
            }), 403
        
        data = request.get_json()
        
        # Validate required fields
        if not data.get('rating'):
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Rating is required'
                }
            }), 400
        
        rating = data['rating']
        comment = data.get('comment', '').strip()
        
        # Validate rating
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Rating must be between 1 and 5'
                }
            }), 400
        
        # Update message feedback
        message.feedback_rating = rating
        message.feedback_comment = comment
        
        # Check if feedback already exists for this message
        existing_feedback = Feedback.query.filter_by(
            user_id=current_user_id,
            message_id=message_id
        ).first()
        
        if existing_feedback:
            # Update existing feedback
            existing_feedback.rating = rating
            existing_feedback.comment = comment
            existing_feedback.created_at = datetime.utcnow()  # Update timestamp
        else:
            # Create new feedback
            new_feedback = Feedback(
                user_id=current_user_id,
                message_id=message_id,
                rating=rating,
                comment=comment,
                feedback_type='helpfulness'
            )
            db.session.add(new_feedback)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Feedback updated successfully'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Submit message feedback error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to submit feedback'
            }
        }), 500

@feedback_bp.route('/my-feedback', methods=['GET'])
@jwt_required()
def get_my_feedback():
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'USER_NOT_FOUND',
                    'message': 'User not found'
                }
            }), 404
        
        # Get query parameters
        limit = min(int(request.args.get('limit', 20)), 100)
        offset = int(request.args.get('offset', 0))
        feedback_type = request.args.get('type')
        
        # Build query
        query = Feedback.query.filter_by(user_id=current_user_id)
        
        if feedback_type:
            query = query.filter_by(feedback_type=feedback_type)
        
        # Get total count
        total_feedback = query.count()
        
        # Get paginated results
        feedback_list = query.order_by(Feedback.created_at.desc())\
            .limit(limit).offset(offset).all()
        
        # Format results
        results = []
        for feedback in feedback_list:
            feedback_dict = feedback.to_dict()
            
            # Add message details if available
            if feedback.message_id:
                message = Message.query.get(feedback.message_id)
                if message:
                    feedback_dict['message'] = {
                        'user_message': message.user_message,
                        'bot_response': message.bot_response[:200] + '...' if len(message.bot_response) > 200 else message.bot_response,
                        'created_at': message.created_at.isoformat() if message.created_at else None
                    }
            
            results.append(feedback_dict)
        
        return jsonify({
            'success': True,
            'data': {
                'feedback': results,
                'total_feedback': total_feedback
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get my feedback error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get feedback'
            }
        }), 500

@feedback_bp.route('/stats', methods=['GET'])
def get_feedback_stats():
    try:
        # Get overall feedback statistics (public endpoint)
        total_feedback = Feedback.query.count()
        
        if total_feedback == 0:
            return jsonify({
                'success': True,
                'data': {
                    'total_feedback': 0,
                    'average_rating': 0,
                    'rating_distribution': {
                        '1': 0, '2': 0, '3': 0, '4': 0, '5': 0
                    }
                }
            }), 200
        
        # Calculate average rating
        avg_rating = db.session.query(db.func.avg(Feedback.rating)).scalar()
        
        # Get rating distribution
        rating_distribution = {}
        for i in range(1, 6):
            count = Feedback.query.filter_by(rating=i).count()
            rating_distribution[str(i)] = count
        
        # Get feedback by type
        feedback_by_type = {}
        for feedback_type in ['accuracy', 'helpfulness', 'relevance', 'general']:
            count = Feedback.query.filter_by(feedback_type=feedback_type).count()
            feedback_by_type[feedback_type] = count
        
        return jsonify({
            'success': True,
            'data': {
                'total_feedback': total_feedback,
                'average_rating': round(float(avg_rating), 2) if avg_rating else 0,
                'rating_distribution': rating_distribution,
                'feedback_by_type': feedback_by_type
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get feedback stats error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get feedback statistics'
            }
        }), 500

