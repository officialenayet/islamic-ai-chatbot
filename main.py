import os
import sys
from datetime import timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from src.models.database import db
from src.routes.auth import auth_bp
from src.routes.chat import chat_bp
from src.routes.islamic_content import islamic_bp
from src.routes.user import user_bp
from src.routes.chat_enhanced import chat_enhanced_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'islamic-chatbot-secret-key-2024')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key-islamic-chatbot')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# OpenAI configuration
app.config['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
app.config['OPENAI_API_BASE'] = os.getenv('OPENAI_API_BASE')

# Initialize extensions
CORS(app, origins="*", allow_headers=["Content-Type", "Authorization"])
jwt = JWTManager(app)
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
app.register_blueprint(chat_bp, url_prefix='/api/v1/chat')
app.register_blueprint(islamic_bp, url_prefix='/api/v1')
app.register_blueprint(user_bp, url_prefix='/api/v1/user')
app.register_blueprint(chat_enhanced_bp, url_prefix='/api/v1/chat-enhanced')

# Create database tables
with app.app_context():
    db.create_all()

# Health check endpoint
@app.route('/api/v1/health')
def health_check():
    return jsonify({
        'success': True,
        'data': {
            'status': 'healthy',
            'version': '1.0.0',
            'database': 'connected',
            'ai_service': 'available' if app.config['OPENAI_API_KEY'] else 'unavailable'
        }
    })

# Public configuration endpoint
@app.route('/api/v1/config')
def get_config():
    return jsonify({
        'success': True,
        'data': {
            'app_name': 'Islamic AI Chatbot',
            'app_version': '1.0.0',
            'supported_languages': ['bn', 'ar', 'en', 'ur'],
            'max_message_length': 1000,
            'features': {
                'voice_input': False,
                'bookmarks': True,
                'search_history': True
            }
        }
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': {
            'code': 'NOT_FOUND',
            'message': 'Resource not found'
        }
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': {
            'code': 'INTERNAL_ERROR',
            'message': 'Internal server error'
        }
    }), 500

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'success': False,
        'error': {
            'code': 'TOKEN_EXPIRED',
            'message': 'Token has expired'
        }
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'success': False,
        'error': {
            'code': 'INVALID_TOKEN',
            'message': 'Invalid token'
        }
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'success': False,
        'error': {
            'code': 'UNAUTHORIZED',
            'message': 'Authorization token is required'
        }
    }), 401

# Frontend serving
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return jsonify({
                'success': True,
                'message': 'Islamic AI Chatbot API is running',
                'endpoints': {
                    'health': '/api/v1/health',
                    'config': '/api/v1/config',
                    'auth': '/api/v1/auth/*',
                    'chat': '/api/v1/chat/*',
                    'islamic_content': '/api/v1/quran/*, /api/v1/hadith/*, /api/v1/fatwa/*'
                }
            })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

