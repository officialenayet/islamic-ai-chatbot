from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
import secrets
import time
import openai
import json
import re

from src.models.database import db, User, ChatSession, Message, QuranVerse, Hadith, Fatwa

chat_bp = Blueprint('chat', __name__)

def generate_session_token():
    return secrets.token_urlsafe(32)

def get_islamic_context(query, language='bn'):
    """
    Search for relevant Islamic content based on the query
    """
    context = []
    
    # Search in Quran verses
    quran_results = QuranVerse.query.filter(
        db.or_(
            QuranVerse.arabic_text.contains(query),
            QuranVerse.bengali_translation.contains(query) if language == 'bn' else None,
            QuranVerse.english_translation.contains(query) if language == 'en' else None
        )
    ).limit(3).all()
    
    for verse in quran_results:
        context.append({
            'type': 'verse',
            'reference': f"সূরা {verse.surah_number}, আয়াত {verse.verse_number}",
            'arabic_text': verse.arabic_text,
            'translation': verse.bengali_translation if language == 'bn' else verse.english_translation,
            'source': f"কোরআন - সূরা {verse.surah_number}:{verse.verse_number}"
        })
    
    # Search in Hadith
    hadith_results = Hadith.query.filter(
        db.or_(
            Hadith.arabic_text.contains(query),
            Hadith.bengali_translation.contains(query) if language == 'bn' else None,
            Hadith.english_translation.contains(query) if language == 'en' else None
        )
    ).limit(2).all()
    
    for hadith in hadith_results:
        context.append({
            'type': 'hadith',
            'reference': f"{hadith.book.name if hadith.book else 'Unknown'} - {hadith.hadith_number}",
            'arabic_text': hadith.arabic_text,
            'translation': hadith.bengali_translation if language == 'bn' else hadith.english_translation,
            'narrator': hadith.narrator,
            'grade': hadith.grade,
            'source': f"হাদিস - {hadith.book.name if hadith.book else 'Unknown'} #{hadith.hadith_number}"
        })
    
    # Search in Fatwa
    fatwa_results = Fatwa.query.filter(
        db.or_(
            Fatwa.question.contains(query),
            Fatwa.answer.contains(query)
        )
    ).filter_by(language=language).limit(2).all()
    
    for fatwa in fatwa_results:
        context.append({
            'type': 'fatwa',
            'reference': f"ফতোয়া - {fatwa.scholar.name if fatwa.scholar else 'Unknown Scholar'}",
            'question': fatwa.question,
            'answer': fatwa.answer[:500] + "..." if len(fatwa.answer) > 500 else fatwa.answer,
            'scholar': fatwa.scholar.name if fatwa.scholar else None,
            'source': f"ফতোয়া - {fatwa.scholar.name if fatwa.scholar else 'Unknown'}"
        })
    
    return context

def generate_ai_response(user_message, context, language='bn'):
    """
    Generate AI response using OpenAI with Islamic context
    """
    try:
        # Create system prompt based on language
        if language == 'bn':
            system_prompt = """আপনি একজন ইসলামিক AI সহায়ক। আপনার কাজ হল ইসলামিক প্রশ্নের উত্তর দেওয়া কোরআন, হাদিস এবং ইসলামিক স্কলারদের মতামতের ভিত্তিতে।

নিয়মাবলী:
1. সবসময় কোরআন ও সহীহ হাদিসের রেফারেন্স দিন
2. উত্তর বাংলায় দিন
3. আরবি টেক্সট অন্তর্ভুক্ত করুন যেখানে প্রয়োজন
4. বিতর্কিত বিষয়ে একাধিক মতামত উল্লেখ করুন
5. সর্বদা আল্লাহ ও রাসূল (সা.) এর প্রতি সম্মান প্রদর্শন করুন
6. যদি নিশ্চিত না হন, তাহলে স্কলারদের সাথে পরামর্শ করতে বলুন"""
        else:
            system_prompt = """You are an Islamic AI assistant. Your job is to answer Islamic questions based on the Quran, Hadith, and opinions of Islamic scholars.

Guidelines:
1. Always provide references from Quran and authentic Hadith
2. Answer in English
3. Include Arabic text where necessary
4. Mention multiple opinions on controversial issues
5. Always show respect for Allah and Prophet Muhammad (PBUH)
6. If uncertain, advise consulting with scholars"""

        # Prepare context for AI
        context_text = ""
        sources = []
        
        for item in context:
            if item['type'] == 'verse':
                context_text += f"\nকোরআনের আয়াত: {item['reference']}\nআরবি: {item['arabic_text']}\nঅনুবাদ: {item['translation']}\n"
                sources.append({
                    'type': 'verse',
                    'reference': item['reference'],
                    'text': item['translation'],
                    'arabic': item['arabic_text']
                })
            elif item['type'] == 'hadith':
                context_text += f"\nহাদিস: {item['reference']}\nআরবি: {item['arabic_text']}\nঅনুবাদ: {item['translation']}\nবর্ণনাকারী: {item['narrator']}\nগ্রেড: {item['grade']}\n"
                sources.append({
                    'type': 'hadith',
                    'reference': item['reference'],
                    'text': item['translation'],
                    'arabic': item['arabic_text'],
                    'narrator': item['narrator'],
                    'grade': item['grade']
                })
            elif item['type'] == 'fatwa':
                context_text += f"\nফতোয়া: {item['reference']}\nপ্রশ্ন: {item['question']}\nউত্তর: {item['answer']}\n"
                sources.append({
                    'type': 'fatwa',
                    'reference': item['reference'],
                    'question': item['question'],
                    'answer': item['answer'],
                    'scholar': item['scholar']
                })

        # Create user prompt
        user_prompt = f"প্রশ্ন: {user_message}\n\nসংশ্লিষ্ট ইসলামিক তথ্য:\n{context_text}\n\nঅনুগ্রহ করে উপরের তথ্যের ভিত্তিতে একটি বিস্তারিত উত্তর দিন।"

        # Call OpenAI API
        client = openai.OpenAI(
            api_key=current_app.config['OPENAI_API_KEY'],
            base_url=current_app.config['OPENAI_API_BASE']
        )
        
        start_time = time.time()
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        
        response_time = int((time.time() - start_time) * 1000)
        
        ai_response = response.choices[0].message.content
        tokens_used = response.usage.total_tokens if hasattr(response, 'usage') else 0
        
        return ai_response, sources, response_time, tokens_used
        
    except Exception as e:
        current_app.logger.error(f"AI response error: {str(e)}")
        
        # Fallback response
        fallback_response = "দুঃখিত, এই মুহূর্তে AI সেবা উপলব্ধ নেই। অনুগ্রহ করে পরে আবার চেষ্টা করুন।" if language == 'bn' else "Sorry, AI service is currently unavailable. Please try again later."
        return fallback_response, [], 0, 0

@chat_bp.route('/start', methods=['POST'])
@jwt_required()
def start_chat():
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
        
        data = request.get_json() or {}
        title = data.get('title', 'নতুন চ্যাট')
        
        # Create new chat session
        session_token = generate_session_token()
        new_session = ChatSession(
            user_id=current_user_id,
            session_token=session_token,
            title=title
        )
        
        db.session.add(new_session)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Chat session started',
            'data': {
                'session_id': new_session.id,
                'session_token': session_token,
                'title': title,
                'created_at': new_session.created_at.isoformat()
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Start chat error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to start chat session'
            }
        }), 500

@chat_bp.route('/message', methods=['POST'])
@jwt_required()
def send_message():
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
        if not data.get('session_id') or not data.get('message'):
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Session ID and message are required'
                }
            }), 400
        
        session_id = data['session_id']
        user_message = data['message'].strip()
        language = data.get('language', user.preferred_language)
        
        # Validate message length
        if len(user_message) > 1000:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Message too long (max 1000 characters)'
                }
            }), 400
        
        # Find chat session
        session = ChatSession.query.filter_by(
            id=session_id,
            user_id=current_user_id,
            is_active=True
        ).first()
        
        if not session:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'SESSION_NOT_FOUND',
                    'message': 'Chat session not found'
                }
            }), 404
        
        # Get Islamic context for the question
        context = get_islamic_context(user_message, language)
        
        # Generate AI response
        ai_response, sources, response_time, tokens_used = generate_ai_response(
            user_message, context, language
        )
        
        # Create message record
        new_message = Message(
            session_id=session_id,
            user_message=user_message,
            bot_response=ai_response,
            response_time=response_time,
            tokens_used=tokens_used,
            model_used='gpt-4'
        )
        
        # Set sources
        new_message.set_sources(sources)
        
        # Update session
        session.updated_at = datetime.utcnow()
        
        # Update session title if it's the first message
        if not session.title or session.title == 'নতুন চ্যাট':
            # Generate title from first few words of the message
            title_words = user_message.split()[:5]
            session.title = ' '.join(title_words) + ('...' if len(title_words) == 5 else '')
        
        db.session.add(new_message)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': {
                'message_id': new_message.id,
                'user_message': user_message,
                'bot_response': ai_response,
                'sources': sources,
                'response_time': response_time,
                'tokens_used': tokens_used,
                'created_at': new_message.created_at.isoformat()
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Send message error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to send message'
            }
        }), 500

@chat_bp.route('/history', methods=['GET'])
@jwt_required()
def get_chat_history():
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
        session_id = request.args.get('session_id')
        limit = min(int(request.args.get('limit', 20)), 100)
        offset = int(request.args.get('offset', 0))
        
        if session_id:
            # Get specific session history
            session = ChatSession.query.filter_by(
                id=session_id,
                user_id=current_user_id
            ).first()
            
            if not session:
                return jsonify({
                    'success': False,
                    'error': {
                        'code': 'SESSION_NOT_FOUND',
                        'message': 'Chat session not found'
                    }
                }), 404
            
            messages = Message.query.filter_by(session_id=session_id)\
                .order_by(Message.created_at.desc())\
                .limit(limit).offset(offset).all()
            
            return jsonify({
                'success': True,
                'data': {
                    'session': session.to_dict(),
                    'messages': [msg.to_dict() for msg in messages],
                    'total_messages': len(session.messages)
                }
            }), 200
        
        else:
            # Get all sessions for user
            sessions = ChatSession.query.filter_by(user_id=current_user_id)\
                .order_by(ChatSession.updated_at.desc())\
                .limit(limit).offset(offset).all()
            
            sessions_data = []
            for session in sessions:
                session_dict = session.to_dict()
                # Get latest messages for preview
                latest_messages = Message.query.filter_by(session_id=session.id)\
                    .order_by(Message.created_at.desc()).limit(3).all()
                session_dict['messages'] = [msg.to_dict() for msg in latest_messages]
                sessions_data.append(session_dict)
            
            total_sessions = ChatSession.query.filter_by(user_id=current_user_id).count()
            total_messages = Message.query.join(ChatSession)\
                .filter(ChatSession.user_id == current_user_id).count()
            
            return jsonify({
                'success': True,
                'data': {
                    'sessions': sessions_data,
                    'total_sessions': total_sessions,
                    'total_messages': total_messages
                }
            }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get chat history error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get chat history'
            }
        }), 500

@chat_bp.route('/session/<session_id>', methods=['DELETE'])
@jwt_required()
def delete_session(session_id):
    try:
        current_user_id = get_jwt_identity()
        
        # Find session
        session = ChatSession.query.filter_by(
            id=session_id,
            user_id=current_user_id
        ).first()
        
        if not session:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'SESSION_NOT_FOUND',
                    'message': 'Chat session not found'
                }
            }), 404
        
        # Delete session (messages will be deleted due to cascade)
        db.session.delete(session)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Chat session deleted successfully'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Delete session error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to delete chat session'
            }
        }), 500

@chat_bp.route('/session/<session_id>/title', methods=['PUT'])
@jwt_required()
def update_session_title(session_id):
    try:
        current_user_id = get_jwt_identity()
        
        data = request.get_json()
        if not data.get('title'):
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Title is required'
                }
            }), 400
        
        # Find session
        session = ChatSession.query.filter_by(
            id=session_id,
            user_id=current_user_id
        ).first()
        
        if not session:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'SESSION_NOT_FOUND',
                    'message': 'Chat session not found'
                }
            }), 404
        
        # Update title
        session.title = data['title'].strip()[:200]  # Limit to 200 chars
        session.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Session title updated successfully',
            'data': session.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Update session title error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to update session title'
            }
        }), 500

