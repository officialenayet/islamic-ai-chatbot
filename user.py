from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

from src.models.database import db, User, UserBookmark, SearchHistory, QuranVerse, Hadith, Fatwa

user_bp = Blueprint('user', __name__)

@user_bp.route('/bookmarks', methods=['GET'])
@jwt_required()
def get_bookmarks():
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
        content_type = request.args.get('type')
        limit = min(int(request.args.get('limit', 20)), 100)
        offset = int(request.args.get('offset', 0))
        
        # Build query
        query = UserBookmark.query.filter_by(user_id=current_user_id)
        
        if content_type:
            query = query.filter_by(content_type=content_type)
        
        # Get total count
        total_bookmarks = query.count()
        
        # Get paginated results
        bookmarks = query.order_by(UserBookmark.created_at.desc())\
            .limit(limit).offset(offset).all()
        
        # Format results with content details
        results = []
        for bookmark in bookmarks:
            bookmark_dict = bookmark.to_dict()
            
            # Get content details based on type
            if bookmark.content_type == 'verse':
                verse = QuranVerse.query.get(bookmark.content_id)
                if verse:
                    bookmark_dict['content'] = verse.to_dict()
            elif bookmark.content_type == 'hadith':
                hadith = Hadith.query.get(bookmark.content_id)
                if hadith:
                    hadith_dict = hadith.to_dict()
                    hadith_dict['book_name'] = hadith.book.name if hadith.book else 'Unknown'
                    bookmark_dict['content'] = hadith_dict
            elif bookmark.content_type == 'fatwa':
                fatwa = Fatwa.query.get(bookmark.content_id)
                if fatwa:
                    fatwa_dict = fatwa.to_dict()
                    fatwa_dict['scholar_name'] = fatwa.scholar.name if fatwa.scholar else 'Unknown Scholar'
                    bookmark_dict['content'] = fatwa_dict
            
            results.append(bookmark_dict)
        
        return jsonify({
            'success': True,
            'data': {
                'bookmarks': results,
                'total_bookmarks': total_bookmarks
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get bookmarks error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get bookmarks'
            }
        }), 500

@user_bp.route('/bookmarks', methods=['POST'])
@jwt_required()
def add_bookmark():
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
        
        data = request.get_json()
        
        # Validate required fields
        if not data.get('content_type') or not data.get('content_id'):
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Content type and content ID are required'
                }
            }), 400
        
        content_type = data['content_type']
        content_id = data['content_id']
        notes = data.get('notes', '').strip()
        
        # Validate content type
        if content_type not in ['verse', 'hadith', 'fatwa']:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Invalid content type'
                }
            }), 400
        
        # Verify content exists
        content_exists = False
        if content_type == 'verse':
            content_exists = QuranVerse.query.get(content_id) is not None
        elif content_type == 'hadith':
            content_exists = Hadith.query.get(content_id) is not None
        elif content_type == 'fatwa':
            content_exists = Fatwa.query.get(content_id) is not None
        
        if not content_exists:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'NOT_FOUND',
                    'message': 'Content not found'
                }
            }), 404
        
        # Check if bookmark already exists
        existing_bookmark = UserBookmark.query.filter_by(
            user_id=current_user_id,
            content_type=content_type,
            content_id=content_id
        ).first()
        
        if existing_bookmark:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'BOOKMARK_EXISTS',
                    'message': 'Content already bookmarked'
                }
            }), 409
        
        # Create bookmark
        new_bookmark = UserBookmark(
            user_id=current_user_id,
            content_type=content_type,
            content_id=content_id,
            notes=notes
        )
        
        db.session.add(new_bookmark)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Bookmark added successfully',
            'data': {
                'bookmark_id': new_bookmark.id
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Add bookmark error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to add bookmark'
            }
        }), 500

@user_bp.route('/bookmarks/<bookmark_id>', methods=['DELETE'])
@jwt_required()
def remove_bookmark(bookmark_id):
    try:
        current_user_id = get_jwt_identity()
        
        # Find bookmark
        bookmark = UserBookmark.query.filter_by(
            id=bookmark_id,
            user_id=current_user_id
        ).first()
        
        if not bookmark:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'BOOKMARK_NOT_FOUND',
                    'message': 'Bookmark not found'
                }
            }), 404
        
        # Delete bookmark
        db.session.delete(bookmark)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Bookmark removed successfully'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Remove bookmark error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to remove bookmark'
            }
        }), 500

@user_bp.route('/bookmarks/<bookmark_id>', methods=['PUT'])
@jwt_required()
def update_bookmark(bookmark_id):
    try:
        current_user_id = get_jwt_identity()
        
        # Find bookmark
        bookmark = UserBookmark.query.filter_by(
            id=bookmark_id,
            user_id=current_user_id
        ).first()
        
        if not bookmark:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'BOOKMARK_NOT_FOUND',
                    'message': 'Bookmark not found'
                }
            }), 404
        
        data = request.get_json()
        
        # Update notes
        if 'notes' in data:
            bookmark.notes = data['notes'].strip()
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Bookmark updated successfully',
            'data': bookmark.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Update bookmark error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to update bookmark'
            }
        }), 500

@user_bp.route('/search-history', methods=['GET'])
@jwt_required()
def get_search_history():
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
        
        # Get search history
        total_searches = SearchHistory.query.filter_by(user_id=current_user_id).count()
        
        searches = SearchHistory.query.filter_by(user_id=current_user_id)\
            .order_by(SearchHistory.created_at.desc())\
            .limit(limit).offset(offset).all()
        
        return jsonify({
            'success': True,
            'data': {
                'searches': [search.to_dict() for search in searches],
                'total_searches': total_searches
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get search history error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get search history'
            }
        }), 500

@user_bp.route('/stats', methods=['GET'])
@jwt_required()
def get_user_stats():
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
        
        # Get user statistics
        total_sessions = len(user.chat_sessions)
        total_bookmarks = len(user.bookmarks)
        total_searches = len(user.search_history)
        
        # Get message count
        total_messages = 0
        for session in user.chat_sessions:
            total_messages += len(session.messages)
        
        # Get bookmark breakdown
        bookmark_breakdown = {
            'verse': UserBookmark.query.filter_by(user_id=current_user_id, content_type='verse').count(),
            'hadith': UserBookmark.query.filter_by(user_id=current_user_id, content_type='hadith').count(),
            'fatwa': UserBookmark.query.filter_by(user_id=current_user_id, content_type='fatwa').count()
        }
        
        return jsonify({
            'success': True,
            'data': {
                'total_sessions': total_sessions,
                'total_messages': total_messages,
                'total_bookmarks': total_bookmarks,
                'total_searches': total_searches,
                'bookmark_breakdown': bookmark_breakdown,
                'member_since': user.created_at.isoformat() if user.created_at else None,
                'last_active': user.last_active.isoformat() if user.last_active else None
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get user stats error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get user statistics'
            }
        }), 500

