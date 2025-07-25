from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
import json

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100))
    preferred_language = db.Column(db.String(10), default='bn')
    timezone = db.Column(db.String(50), default='Asia/Dhaka')
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_active = db.Column(db.DateTime)
    
    # Relationships
    chat_sessions = db.relationship('ChatSession', backref='user', lazy=True, cascade='all, delete-orphan')
    bookmarks = db.relationship('UserBookmark', backref='user', lazy=True, cascade='all, delete-orphan')
    search_history = db.relationship('SearchHistory', backref='user', lazy=True, cascade='all, delete-orphan')
    feedback = db.relationship('Feedback', backref='user', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'preferred_language': self.preferred_language,
            'timezone': self.timezone,
            'is_active': self.is_active,
            'is_verified': self.is_verified,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_active': self.last_active.isoformat() if self.last_active else None
        }

class ChatSession(db.Model):
    __tablename__ = 'chat_sessions'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    session_token = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    messages = db.relationship('Message', backref='session', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'session_token': self.session_token,
            'title': self.title,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'message_count': len(self.messages)
        }

class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    session_id = db.Column(db.String(36), db.ForeignKey('chat_sessions.id'), nullable=False)
    user_message = db.Column(db.Text, nullable=False)
    bot_response = db.Column(db.Text, nullable=False)
    sources = db.Column(db.Text)  # JSON string
    feedback_rating = db.Column(db.Integer)
    feedback_comment = db.Column(db.Text)
    response_time = db.Column(db.Integer)  # in milliseconds
    tokens_used = db.Column(db.Integer)
    model_used = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    feedback = db.relationship('Feedback', backref='message', lazy=True, cascade='all, delete-orphan')

    def get_sources(self):
        if self.sources:
            try:
                return json.loads(self.sources)
            except:
                return []
        return []

    def set_sources(self, sources_list):
        self.sources = json.dumps(sources_list) if sources_list else None

    def to_dict(self):
        return {
            'id': self.id,
            'session_id': self.session_id,
            'user_message': self.user_message,
            'bot_response': self.bot_response,
            'sources': self.get_sources(),
            'feedback_rating': self.feedback_rating,
            'feedback_comment': self.feedback_comment,
            'response_time': self.response_time,
            'tokens_used': self.tokens_used,
            'model_used': self.model_used,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class QuranVerse(db.Model):
    __tablename__ = 'quran_verses'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    surah_number = db.Column(db.Integer, nullable=False)
    verse_number = db.Column(db.Integer, nullable=False)
    arabic_text = db.Column(db.Text, nullable=False)
    bengali_translation = db.Column(db.Text)
    english_translation = db.Column(db.Text)
    urdu_translation = db.Column(db.Text)
    transliteration = db.Column(db.Text)
    revelation_place = db.Column(db.String(20))
    juz_number = db.Column(db.Integer)
    hizb_number = db.Column(db.Integer)
    rub_number = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('surah_number', 'verse_number'),)

    def to_dict(self):
        return {
            'id': self.id,
            'surah_number': self.surah_number,
            'verse_number': self.verse_number,
            'arabic_text': self.arabic_text,
            'bengali_translation': self.bengali_translation,
            'english_translation': self.english_translation,
            'urdu_translation': self.urdu_translation,
            'transliteration': self.transliteration,
            'revelation_place': self.revelation_place,
            'juz_number': self.juz_number,
            'hizb_number': self.hizb_number,
            'rub_number': self.rub_number
        }

class QuranSurah(db.Model):
    __tablename__ = 'quran_surahs'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    surah_number = db.Column(db.Integer, unique=True, nullable=False)
    arabic_name = db.Column(db.Text, nullable=False)
    english_name = db.Column(db.String(100), nullable=False)
    bengali_name = db.Column(db.String(100))
    meaning = db.Column(db.Text)
    total_verses = db.Column(db.Integer, nullable=False)
    revelation_place = db.Column(db.String(20))
    revelation_order = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'surah_number': self.surah_number,
            'arabic_name': self.arabic_name,
            'english_name': self.english_name,
            'bengali_name': self.bengali_name,
            'meaning': self.meaning,
            'total_verses': self.total_verses,
            'revelation_place': self.revelation_place,
            'revelation_order': self.revelation_order
        }

class HadithBook(db.Model):
    __tablename__ = 'hadith_books'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), unique=True, nullable=False)
    arabic_name = db.Column(db.Text)
    author = db.Column(db.String(100))
    total_hadith = db.Column(db.Integer)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    chapters = db.relationship('HadithChapter', backref='book', lazy=True, cascade='all, delete-orphan')
    hadith = db.relationship('Hadith', backref='book', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'arabic_name': self.arabic_name,
            'author': self.author,
            'total_hadith': self.total_hadith,
            'description': self.description
        }

class HadithChapter(db.Model):
    __tablename__ = 'hadith_chapters'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    book_id = db.Column(db.String(36), db.ForeignKey('hadith_books.id'), nullable=False)
    chapter_number = db.Column(db.Integer, nullable=False)
    arabic_title = db.Column(db.Text)
    english_title = db.Column(db.String(200))
    bengali_title = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('book_id', 'chapter_number'),)

    def to_dict(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'chapter_number': self.chapter_number,
            'arabic_title': self.arabic_title,
            'english_title': self.english_title,
            'bengali_title': self.bengali_title
        }

class Hadith(db.Model):
    __tablename__ = 'hadith'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    book_id = db.Column(db.String(36), db.ForeignKey('hadith_books.id'), nullable=False)
    chapter_id = db.Column(db.String(36), db.ForeignKey('hadith_chapters.id'))
    hadith_number = db.Column(db.Integer, nullable=False)
    arabic_text = db.Column(db.Text, nullable=False)
    bengali_translation = db.Column(db.Text)
    english_translation = db.Column(db.Text)
    urdu_translation = db.Column(db.Text)
    narrator = db.Column(db.String(200))
    grade = db.Column(db.String(50))
    reference = db.Column(db.String(200))
    source_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('book_id', 'hadith_number'),)

    def to_dict(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'chapter_id': self.chapter_id,
            'hadith_number': self.hadith_number,
            'arabic_text': self.arabic_text,
            'bengali_translation': self.bengali_translation,
            'english_translation': self.english_translation,
            'urdu_translation': self.urdu_translation,
            'narrator': self.narrator,
            'grade': self.grade,
            'reference': self.reference,
            'source_url': self.source_url
        }

class FatwaCategory(db.Model):
    __tablename__ = 'fatwa_categories'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), unique=True, nullable=False)
    arabic_name = db.Column(db.Text)
    bengali_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    parent_category_id = db.Column(db.String(36), db.ForeignKey('fatwa_categories.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    fatwa = db.relationship('Fatwa', backref='category', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'arabic_name': self.arabic_name,
            'bengali_name': self.bengali_name,
            'description': self.description,
            'parent_category_id': self.parent_category_id
        }

class Scholar(db.Model):
    __tablename__ = 'scholars'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(200), nullable=False)
    arabic_name = db.Column(db.Text)
    title = db.Column(db.String(100))
    biography = db.Column(db.Text)
    specialization = db.Column(db.Text)
    institution = db.Column(db.String(200))
    country = db.Column(db.String(100))
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    fatwa = db.relationship('Fatwa', backref='scholar', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'arabic_name': self.arabic_name,
            'title': self.title,
            'biography': self.biography,
            'specialization': self.specialization,
            'institution': self.institution,
            'country': self.country,
            'is_verified': self.is_verified
        }

class Fatwa(db.Model):
    __tablename__ = 'fatwa'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    scholar_id = db.Column(db.String(36), db.ForeignKey('scholars.id'))
    category_id = db.Column(db.String(36), db.ForeignKey('fatwa_categories.id'))
    language = db.Column(db.String(10), nullable=False)
    tags = db.Column(db.Text)  # JSON string
    source_url = db.Column(db.String(500))
    date_issued = db.Column(db.Date)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_tags(self):
        if self.tags:
            try:
                return json.loads(self.tags)
            except:
                return []
        return []

    def set_tags(self, tags_list):
        self.tags = json.dumps(tags_list) if tags_list else None

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'scholar_id': self.scholar_id,
            'category_id': self.category_id,
            'language': self.language,
            'tags': self.get_tags(),
            'source_url': self.source_url,
            'date_issued': self.date_issued.isoformat() if self.date_issued else None,
            'is_verified': self.is_verified
        }

class UserBookmark(db.Model):
    __tablename__ = 'user_bookmarks'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    content_type = db.Column(db.String(20), nullable=False)  # verse, hadith, fatwa
    content_id = db.Column(db.String(36), nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('user_id', 'content_type', 'content_id'),)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'content_type': self.content_type,
            'content_id': self.content_id,
            'notes': self.notes,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class SearchHistory(db.Model):
    __tablename__ = 'search_history'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    query = db.Column(db.Text, nullable=False)
    search_type = db.Column(db.String(20))  # general, verse, hadith, fatwa
    results_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'query': self.query,
            'search_type': self.search_type,
            'results_count': self.results_count,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Feedback(db.Model):
    __tablename__ = 'feedback'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'))
    message_id = db.Column(db.String(36), db.ForeignKey('messages.id'))
    rating = db.Column(db.Integer)  # 1-5
    comment = db.Column(db.Text)
    feedback_type = db.Column(db.String(20))  # accuracy, helpfulness, relevance, general
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'message_id': self.message_id,
            'rating': self.rating,
            'comment': self.comment,
            'feedback_type': self.feedback_type,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class APIUsage(db.Model):
    __tablename__ = 'api_usage'
    
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'))
    endpoint = db.Column(db.String(100), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    status_code = db.Column(db.Integer)
    response_time = db.Column(db.Integer)
    tokens_used = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'endpoint': self.endpoint,
            'method': self.method,
            'status_code': self.status_code,
            'response_time': self.response_time,
            'tokens_used': self.tokens_used,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

