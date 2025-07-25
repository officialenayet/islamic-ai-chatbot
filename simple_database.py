import sqlite3
import os
from datetime import datetime

def get_db_connection():
    """Get database connection for simple operations"""
    db_path = os.path.join(os.path.dirname(__file__), '../../islamic_data.db')
    return sqlite3.connect(db_path)

def init_simple_db():
    """Initialize simple database for chat messages"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create chat_messages table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            message TEXT NOT NULL,
            message_type TEXT NOT NULL,
            sources TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_simple_db()
    print("Simple database initialized!")

