from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_required
from sqlalchemy import or_, and_, func
import random

from src.models.database import db, User, QuranVerse, QuranSurah, Hadith, HadithBook, HadithChapter, Fatwa, FatwaCategory, Scholar, SearchHistory

islamic_bp = Blueprint('islamic', __name__)

def log_search(user_id, query, search_type, results_count):
    """Log user search for analytics"""
    try:
        if user_id:
            search_log = SearchHistory(
                user_id=user_id,
                query=query,
                search_type=search_type,
                results_count=results_count
            )
            db.session.add(search_log)
            db.session.commit()
    except Exception as e:
        current_app.logger.error(f"Search logging error: {str(e)}")

@islamic_bp.route('/quran/search', methods=['GET'])
def search_quran():
    try:
        # Get query parameters
        query = request.args.get('q', '').strip()
        if not query:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Search query is required'
                }
            }), 400
        
        language = request.args.get('language', 'bn')
        surah = request.args.get('surah', type=int)
        limit = min(int(request.args.get('limit', 10)), 50)
        offset = int(request.args.get('offset', 0))
        
        # Build search query
        search_conditions = []
        
        if language == 'bn':
            search_conditions.append(QuranVerse.bengali_translation.contains(query))
        elif language == 'en':
            search_conditions.append(QuranVerse.english_translation.contains(query))
        elif language == 'ur':
            search_conditions.append(QuranVerse.urdu_translation.contains(query))
        
        # Always search in Arabic text
        search_conditions.append(QuranVerse.arabic_text.contains(query))
        
        # Always search in transliteration
        search_conditions.append(QuranVerse.transliteration.contains(query))
        
        base_query = QuranVerse.query.filter(or_(*search_conditions))
        
        # Filter by surah if specified
        if surah:
            base_query = base_query.filter(QuranVerse.surah_number == surah)
        
        # Get total count
        total_results = base_query.count()
        
        # Get paginated results
        verses = base_query.order_by(QuranVerse.surah_number, QuranVerse.verse_number)\
            .limit(limit).offset(offset).all()
        
        # Get surah information for each verse
        results = []
        for verse in verses:
            surah_info = QuranSurah.query.filter_by(surah_number=verse.surah_number).first()
            verse_dict = verse.to_dict()
            verse_dict['surah_name'] = surah_info.english_name if surah_info else f"Surah {verse.surah_number}"
            verse_dict['surah_bengali_name'] = surah_info.bengali_name if surah_info else None
            results.append(verse_dict)
        
        # Log search
        user_id = None
        try:
            user_id = get_jwt_identity()
        except:
            pass
        
        log_search(user_id, query, 'verse', total_results)
        
        return jsonify({
            'success': True,
            'data': {
                'results': results,
                'total_results': total_results,
                'query': query,
                'language': language
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Quran search error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Search failed'
            }
        }), 500

@islamic_bp.route('/quran/verse/<int:surah_number>/<int:verse_number>', methods=['GET'])
def get_verse(surah_number, verse_number):
    try:
        language = request.args.get('language', 'bn')
        include_tafseer = request.args.get('include_tafseer', 'false').lower() == 'true'
        
        # Validate surah and verse numbers
        if surah_number < 1 or surah_number > 114:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Invalid surah number (1-114)'
                }
            }), 400
        
        # Get verse
        verse = QuranVerse.query.filter_by(
            surah_number=surah_number,
            verse_number=verse_number
        ).first()
        
        if not verse:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'NOT_FOUND',
                    'message': 'Verse not found'
                }
            }), 404
        
        # Get surah information
        surah_info = QuranSurah.query.filter_by(surah_number=surah_number).first()
        
        result = verse.to_dict()
        result['surah_name'] = surah_info.english_name if surah_info else f"Surah {surah_number}"
        result['surah_bengali_name'] = surah_info.bengali_name if surah_info else None
        result['surah_arabic_name'] = surah_info.arabic_name if surah_info else None
        
        # Add tafseer if requested (placeholder - would need actual tafseer data)
        if include_tafseer:
            result['tafseer'] = [
                {
                    'tafseer_name': 'তাফসীর ইবনে কাসীর',
                    'author': 'ইমাম ইবনে কাসীর',
                    'content': 'তাফসীর তথ্য এখানে থাকবে...'
                }
            ]
        
        return jsonify({
            'success': True,
            'data': result
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get verse error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get verse'
            }
        }), 500

@islamic_bp.route('/hadith/search', methods=['GET'])
def search_hadith():
    try:
        # Get query parameters
        query = request.args.get('q', '').strip()
        if not query:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Search query is required'
                }
            }), 400
        
        book = request.args.get('book')
        grade = request.args.get('grade')
        language = request.args.get('language', 'bn')
        limit = min(int(request.args.get('limit', 10)), 50)
        offset = int(request.args.get('offset', 0))
        
        # Build search query
        search_conditions = []
        
        if language == 'bn':
            search_conditions.append(Hadith.bengali_translation.contains(query))
        elif language == 'en':
            search_conditions.append(Hadith.english_translation.contains(query))
        elif language == 'ur':
            search_conditions.append(Hadith.urdu_translation.contains(query))
        
        # Always search in Arabic text
        search_conditions.append(Hadith.arabic_text.contains(query))
        
        base_query = Hadith.query.filter(or_(*search_conditions))
        
        # Filter by book if specified
        if book:
            book_obj = HadithBook.query.filter_by(name=book).first()
            if book_obj:
                base_query = base_query.filter(Hadith.book_id == book_obj.id)
        
        # Filter by grade if specified
        if grade:
            base_query = base_query.filter(Hadith.grade == grade)
        
        # Get total count
        total_results = base_query.count()
        
        # Get paginated results
        hadith_list = base_query.order_by(Hadith.hadith_number)\
            .limit(limit).offset(offset).all()
        
        # Format results
        results = []
        for hadith in hadith_list:
            hadith_dict = hadith.to_dict()
            hadith_dict['book_name'] = hadith.book.name if hadith.book else 'Unknown'
            
            # Get chapter info if available
            if hadith.chapter_id:
                chapter = HadithChapter.query.get(hadith.chapter_id)
                hadith_dict['chapter_title'] = chapter.bengali_title if chapter and language == 'bn' else chapter.english_title if chapter else None
            
            results.append(hadith_dict)
        
        # Log search
        user_id = None
        try:
            user_id = get_jwt_identity()
        except:
            pass
        
        log_search(user_id, query, 'hadith', total_results)
        
        return jsonify({
            'success': True,
            'data': {
                'results': results,
                'total_results': total_results,
                'query': query
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Hadith search error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Search failed'
            }
        }), 500

@islamic_bp.route('/hadith/<book_name>/<int:hadith_number>', methods=['GET'])
def get_hadith(book_name, hadith_number):
    try:
        language = request.args.get('language', 'bn')
        
        # Find book
        book = HadithBook.query.filter_by(name=book_name).first()
        if not book:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'NOT_FOUND',
                    'message': 'Hadith book not found'
                }
            }), 404
        
        # Find hadith
        hadith = Hadith.query.filter_by(
            book_id=book.id,
            hadith_number=hadith_number
        ).first()
        
        if not hadith:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'NOT_FOUND',
                    'message': 'Hadith not found'
                }
            }), 404
        
        result = hadith.to_dict()
        result['book_name'] = book.name
        
        # Get chapter info if available
        if hadith.chapter_id:
            chapter = HadithChapter.query.get(hadith.chapter_id)
            result['chapter_title'] = chapter.bengali_title if chapter and language == 'bn' else chapter.english_title if chapter else None
        
        return jsonify({
            'success': True,
            'data': result
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get hadith error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get hadith'
            }
        }), 500

@islamic_bp.route('/fatwa/search', methods=['GET'])
def search_fatwa():
    try:
        # Get query parameters
        query = request.args.get('q', '').strip()
        if not query:
            return jsonify({
                'success': False,
                'error': {
                    'code': 'VALIDATION_ERROR',
                    'message': 'Search query is required'
                }
            }), 400
        
        category = request.args.get('category')
        scholar = request.args.get('scholar')
        language = request.args.get('language', 'bn')
        limit = min(int(request.args.get('limit', 10)), 50)
        offset = int(request.args.get('offset', 0))
        
        # Build search query
        search_conditions = [
            or_(
                Fatwa.question.contains(query),
                Fatwa.answer.contains(query)
            )
        ]
        
        base_query = Fatwa.query.filter(and_(*search_conditions))
        
        # Filter by language
        base_query = base_query.filter(Fatwa.language == language)
        
        # Filter by category if specified
        if category:
            category_obj = FatwaCategory.query.filter_by(name=category).first()
            if category_obj:
                base_query = base_query.filter(Fatwa.category_id == category_obj.id)
        
        # Filter by scholar if specified
        if scholar:
            scholar_obj = Scholar.query.filter_by(name=scholar).first()
            if scholar_obj:
                base_query = base_query.filter(Fatwa.scholar_id == scholar_obj.id)
        
        # Get total count
        total_results = base_query.count()
        
        # Get paginated results
        fatwa_list = base_query.order_by(Fatwa.created_at.desc())\
            .limit(limit).offset(offset).all()
        
        # Format results
        results = []
        for fatwa in fatwa_list:
            fatwa_dict = fatwa.to_dict()
            fatwa_dict['scholar_name'] = fatwa.scholar.name if fatwa.scholar else 'Unknown Scholar'
            fatwa_dict['category_name'] = fatwa.category.bengali_name if fatwa.category and language == 'bn' else fatwa.category.name if fatwa.category else None
            results.append(fatwa_dict)
        
        # Log search
        user_id = None
        try:
            user_id = get_jwt_identity()
        except:
            pass
        
        log_search(user_id, query, 'fatwa', total_results)
        
        return jsonify({
            'success': True,
            'data': {
                'results': results,
                'total_results': total_results,
                'query': query
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Fatwa search error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Search failed'
            }
        }), 500

@islamic_bp.route('/content/random', methods=['GET'])
def get_random_content():
    try:
        content_type = request.args.get('type')
        language = request.args.get('language', 'bn')
        
        if content_type == 'verse' or not content_type:
            # Get random verse
            verse_count = QuranVerse.query.count()
            if verse_count > 0:
                random_verse = QuranVerse.query.offset(random.randint(0, verse_count - 1)).first()
                if random_verse:
                    surah_info = QuranSurah.query.filter_by(surah_number=random_verse.surah_number).first()
                    verse_dict = random_verse.to_dict()
                    verse_dict['surah_name'] = surah_info.english_name if surah_info else f"Surah {random_verse.surah_number}"
                    verse_dict['surah_bengali_name'] = surah_info.bengali_name if surah_info else None
                    
                    return jsonify({
                        'success': True,
                        'data': {
                            'type': 'verse',
                            'content': verse_dict
                        }
                    }), 200
        
        elif content_type == 'hadith':
            # Get random hadith
            hadith_count = Hadith.query.count()
            if hadith_count > 0:
                random_hadith = Hadith.query.offset(random.randint(0, hadith_count - 1)).first()
                if random_hadith:
                    hadith_dict = random_hadith.to_dict()
                    hadith_dict['book_name'] = random_hadith.book.name if random_hadith.book else 'Unknown'
                    
                    return jsonify({
                        'success': True,
                        'data': {
                            'type': 'hadith',
                            'content': hadith_dict
                        }
                    }), 200
        
        elif content_type == 'fatwa':
            # Get random fatwa
            fatwa_count = Fatwa.query.filter_by(language=language).count()
            if fatwa_count > 0:
                random_fatwa = Fatwa.query.filter_by(language=language)\
                    .offset(random.randint(0, fatwa_count - 1)).first()
                if random_fatwa:
                    fatwa_dict = random_fatwa.to_dict()
                    fatwa_dict['scholar_name'] = random_fatwa.scholar.name if random_fatwa.scholar else 'Unknown Scholar'
                    
                    return jsonify({
                        'success': True,
                        'data': {
                            'type': 'fatwa',
                            'content': fatwa_dict
                        }
                    }), 200
        
        # Fallback - return a default verse
        return jsonify({
            'success': True,
            'data': {
                'type': 'verse',
                'content': {
                    'surah_number': 1,
                    'verse_number': 1,
                    'arabic_text': 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ',
                    'bengali_translation': 'পরম করুণাময় ও অসীম দয়ালু আল্লাহর নামে।',
                    'english_translation': 'In the name of Allah, the Most Gracious, the Most Merciful.',
                    'surah_name': 'Al-Fatihah',
                    'surah_bengali_name': 'আল-ফাতিহা'
                }
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Random content error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get random content'
            }
        }), 500

@islamic_bp.route('/books', methods=['GET'])
def get_books():
    try:
        # Get available Hadith books
        books = HadithBook.query.all()
        
        return jsonify({
            'success': True,
            'data': {
                'hadith_books': [book.to_dict() for book in books]
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get books error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get books'
            }
        }), 500

@islamic_bp.route('/categories', methods=['GET'])
def get_categories():
    try:
        # Get fatwa categories
        categories = FatwaCategory.query.all()
        
        return jsonify({
            'success': True,
            'data': {
                'fatwa_categories': [category.to_dict() for category in categories]
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get categories error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get categories'
            }
        }), 500

@islamic_bp.route('/scholars', methods=['GET'])
def get_scholars():
    try:
        # Get scholars
        scholars = Scholar.query.filter_by(is_verified=True).all()
        
        return jsonify({
            'success': True,
            'data': {
                'scholars': [scholar.to_dict() for scholar in scholars]
            }
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Get scholars error: {str(e)}")
        return jsonify({
            'success': False,
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'Failed to get scholars'
            }
        }), 500

