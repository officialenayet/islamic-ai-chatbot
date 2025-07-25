import sqlite3
import os
from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import openai

chat_enhanced_bp = Blueprint('chat_enhanced', __name__)

# Enhanced database path
ENHANCED_DB_PATH = os.path.join(os.path.dirname(__file__), '../../islamic_comprehensive.db')

def get_enhanced_db_connection():
    """Get connection to enhanced Islamic database"""
    return sqlite3.connect(ENHANCED_DB_PATH)

def search_quran_context(query, limit=3):
    """Search Quran for relevant context"""
    conn = get_enhanced_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT surah_number, ayah_number, arabic_text, bengali_translation, 
               english_translation, tafseer_bengali
        FROM quran_enhanced 
        WHERE bengali_translation LIKE ? OR english_translation LIKE ? 
           OR arabic_text LIKE ? OR tafseer_bengali LIKE ?
        LIMIT ?
    ''', (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', limit))
    
    results = cursor.fetchall()
    conn.close()
    
    return [
        {
            'type': 'quran',
            'surah': row[0],
            'ayah': row[1],
            'arabic': row[2],
            'bengali': row[3],
            'english': row[4],
            'tafseer': row[5],
            'reference': f'সূরা {row[0]}, আয়াত {row[1]}'
        } for row in results
    ]

def search_hadith_context(query, limit=3):
    """Search Hadith for relevant context"""
    conn = get_enhanced_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT collection_name, book_name, hadith_number, arabic_text, 
               bengali_translation, english_translation, narrator, grade, theme, reference
        FROM hadith_enhanced 
        WHERE bengali_translation LIKE ? OR english_translation LIKE ? 
           OR theme LIKE ? OR keywords LIKE ?
        LIMIT ?
    ''', (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', limit))
    
    results = cursor.fetchall()
    conn.close()
    
    return [
        {
            'type': 'hadith',
            'collection': row[0],
            'book': row[1],
            'number': row[2],
            'arabic': row[3],
            'bengali': row[4],
            'english': row[5],
            'narrator': row[6],
            'grade': row[7],
            'theme': row[8],
            'reference': row[9]
        } for row in results
    ]

def search_fatwa_context(query, limit=2):
    """Search Fatwa for relevant context"""
    conn = get_enhanced_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT title, question, answer, scholar_name, institution, 
               category, madhab, references_text
        FROM fatwa_enhanced 
        WHERE title LIKE ? OR question LIKE ? OR answer LIKE ? 
           OR category LIKE ? OR keywords LIKE ?
        LIMIT ?
    ''', (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', limit))
    
    results = cursor.fetchall()
    conn.close()
    
    return [
        {
            'type': 'fatwa',
            'title': row[0],
            'question': row[1],
            'answer': row[2],
            'scholar': row[3],
            'institution': row[4],
            'category': row[5],
            'madhab': row[6],
            'references': row[7]
        } for row in results
    ]

def generate_enhanced_ai_response(user_message, context_data):
    """Generate AI response with enhanced Islamic context"""
    
    # Prepare context for AI
    context_text = "ইসলামিক তথ্যসূত্র:\n\n"
    
    # Add Quran context
    for item in context_data:
        if item['type'] == 'quran':
            context_text += f"**কুরআন - {item['reference']}:**\n"
            context_text += f"আরবি: {item['arabic']}\n"
            context_text += f"বাংলা: {item['bengali']}\n"
            if item['tafseer']:
                context_text += f"তাফসীর: {item['tafseer']}\n"
            context_text += "\n"
        
        elif item['type'] == 'hadith':
            context_text += f"**হাদিস - {item['reference']}:**\n"
            context_text += f"আরবি: {item['arabic']}\n"
            context_text += f"বাংলা: {item['bengali']}\n"
            context_text += f"বর্ণনাকারী: {item['narrator']}\n"
            context_text += f"গ্রেড: {item['grade']}\n\n"
        
        elif item['type'] == 'fatwa':
            context_text += f"**ফতোয়া - {item['title']}:**\n"
            context_text += f"প্রশ্ন: {item['question']}\n"
            context_text += f"উত্তর: {item['answer'][:300]}...\n"
            context_text += f"আলেম: {item['scholar']} ({item['institution']})\n"
            context_text += f"মাযহাব: {item['madhab']}\n\n"
    
    # Enhanced AI prompt
    system_prompt = f"""আপনি একজন বিশেষজ্ঞ ইসলামিক AI সহায়ক। আপনার কাজ হল:

1. কুরআন, হাদিস এবং ইসলামিক ফতোয়ার ভিত্তিতে বিস্তারিত ও নির্ভুল উত্তর প্রদান করা
2. সকল উত্তরে উৎস ও রেফারেন্স সহ তথ্য প্রদান করা
3. বাংলা ভাষায় সহজ ও বোধগম্য ভাষায় ব্যাখ্যা করা
4. বিভিন্ন মাযহাবের মতামত থাকলে তা উল্লেখ করা
5. সন্দেহজনক বিষয়ে আলেমদের পরামর্শ নিতে বলা

নিম্নলিখিত ইসলামিক তথ্যসূত্র ব্যবহার করুন:

{context_text}

উত্তরের ফরম্যাট:
- বিস্তারিত ব্যাখ্যা
- কুরআনের রেফারেন্স (যদি থাকে)
- হাদিসের রেফারেন্স (যদি থাকে)
- ফতোয়া বা আলেমদের মতামত (যদি থাকে)
- অতিরিক্ত পরামর্শ (যদি প্রয়োজন হয়)"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        # Add source references
        sources = []
        for item in context_data:
            if item['type'] == 'quran':
                sources.append(f"কুরআন: {item['reference']}")
            elif item['type'] == 'hadith':
                sources.append(f"হাদিস: {item['reference']}")
            elif item['type'] == 'fatwa':
                sources.append(f"ফতোয়া: {item['scholar']} ({item['institution']})")
        
        return {
            'response': ai_response,
            'sources': sources,
            'context_used': len(context_data)
        }
        
    except Exception as e:
        return {
            'response': 'দুঃখিত, এই মুহূর্তে AI সেবা উপলব্ধ নেই। অনুগ্রহ করে পরে চেষ্টা করুন।',
            'sources': [],
            'context_used': 0,
            'error': str(e)
        }

@chat_enhanced_bp.route('/send', methods=['POST'])
@jwt_required()
def send_message():
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        user_id = get_jwt_identity()
        
        # Search for relevant Islamic context
        quran_context = search_quran_context(message)
        hadith_context = search_hadith_context(message)
        fatwa_context = search_fatwa_context(message)
        
        # Combine all context
        all_context = quran_context + hadith_context + fatwa_context
        
        # Generate AI response with context
        ai_result = generate_enhanced_ai_response(message, all_context)
        
        # Save chat history (using simple database)
        from ..models.simple_database import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Save user message
        cursor.execute('''
            INSERT INTO chat_messages (user_id, message, message_type, created_at)
            VALUES (?, ?, ?, ?)
        ''', (user_id, message, 'user', datetime.now()))
        
        # Save AI response
        cursor.execute('''
            INSERT INTO chat_messages (user_id, message, message_type, sources, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, ai_result['response'], 'assistant', 
              ', '.join(ai_result['sources']), datetime.now()))
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'response': ai_result['response'],
            'sources': ai_result['sources'],
            'context_used': ai_result['context_used'],
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chat_enhanced_bp.route('/history', methods=['GET'])
@jwt_required()
def get_chat_history():
    try:
        user_id = get_jwt_identity()
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        from ..models.simple_database import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        
        offset = (page - 1) * per_page
        
        cursor.execute('''
            SELECT message, message_type, sources, created_at
            FROM chat_messages 
            WHERE user_id = ?
            ORDER BY created_at DESC
            LIMIT ? OFFSET ?
        ''', (user_id, per_page, offset))
        
        messages = []
        for row in cursor.fetchall():
            messages.append({
                'message': row[0],
                'type': row[1],
                'sources': row[2].split(', ') if row[2] else [],
                'timestamp': row[3]
            })
        
        conn.close()
        
        return jsonify({
            'success': True,
            'messages': messages,
            'page': page,
            'per_page': per_page
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chat_enhanced_bp.route('/sessions', methods=['GET'])
@jwt_required()
def get_chat_sessions():
    try:
        user_id = get_jwt_identity()
        
        from ..models.simple_database import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT DATE(created_at) as date, COUNT(*) as message_count,
                   MIN(created_at) as first_message
            FROM chat_messages 
            WHERE user_id = ?
            GROUP BY DATE(created_at)
            ORDER BY date DESC
            LIMIT 10
        ''', (user_id,))
        
        sessions = []
        for row in cursor.fetchall():
            sessions.append({
                'date': row[0],
                'message_count': row[1],
                'first_message_time': row[2]
            })
        
        conn.close()
        
        return jsonify({
            'success': True,
            'sessions': sessions
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

