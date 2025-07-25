#!/usr/bin/env python3
"""
Sample data script for Islamic Chatbot API
This script populates the database with sample Islamic content
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.main import app
from src.models.database import db, QuranSurah, QuranVerse, HadithBook, HadithChapter, Hadith, FatwaCategory, Scholar, Fatwa

def create_sample_data():
    """Create sample Islamic content data"""
    
    with app.app_context():
        # Clear existing data
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        # Create Quran Surahs
        print("Creating Quran Surahs...")
        surahs_data = [
            {
                'surah_number': 1,
                'arabic_name': 'الفاتحة',
                'english_name': 'Al-Fatihah',
                'bengali_name': 'আল-ফাতিহা',
                'meaning': 'The Opening',
                'total_verses': 7,
                'revelation_place': 'Mecca',
                'revelation_order': 5
            },
            {
                'surah_number': 2,
                'arabic_name': 'البقرة',
                'english_name': 'Al-Baqarah',
                'bengali_name': 'আল-বাকারা',
                'meaning': 'The Cow',
                'total_verses': 286,
                'revelation_place': 'Medina',
                'revelation_order': 87
            },
            {
                'surah_number': 112,
                'arabic_name': 'الإخلاص',
                'english_name': 'Al-Ikhlas',
                'bengali_name': 'আল-ইখলাস',
                'meaning': 'The Sincerity',
                'total_verses': 4,
                'revelation_place': 'Mecca',
                'revelation_order': 22
            }
        ]
        
        for surah_data in surahs_data:
            surah = QuranSurah(**surah_data)
            db.session.add(surah)
        
        # Create Quran Verses
        print("Creating Quran Verses...")
        verses_data = [
            {
                'surah_number': 1,
                'verse_number': 1,
                'arabic_text': 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ',
                'bengali_translation': 'পরম করুণাময় ও অসীম দয়ালু আল্লাহর নামে।',
                'english_translation': 'In the name of Allah, the Most Gracious, the Most Merciful.',
                'transliteration': 'Bismillahir Rahmanir Raheem',
                'revelation_place': 'Mecca',
                'juz_number': 1
            },
            {
                'surah_number': 1,
                'verse_number': 2,
                'arabic_text': 'الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ',
                'bengali_translation': 'সমস্ত প্রশংসা আল্লাহর জন্য, যিনি সকল জগতের প্রতিপালক।',
                'english_translation': 'All praise is due to Allah, the Lord of all the worlds.',
                'transliteration': 'Alhamdulillahi Rabbil Alameen',
                'revelation_place': 'Mecca',
                'juz_number': 1
            },
            {
                'surah_number': 2,
                'verse_number': 183,
                'arabic_text': 'يَا أَيُّهَا الَّذِينَ آمَنُوا كُتِبَ عَلَيْكُمُ الصِّيَامُ كَمَا كُتِبَ عَلَى الَّذِينَ مِن قَبْلِكُمْ لَعَلَّكُمْ تَتَّقُونَ',
                'bengali_translation': 'হে মুমিনগণ! তোমাদের উপর রোজা ফরজ করা হয়েছে, যেমনি ফরজ করা হয়েছিল তোমাদের পূর্ববর্তীদের উপর, যাতে তোমরা তাকওয়া অর্জন করতে পার।',
                'english_translation': 'O you who believe! Fasting is prescribed for you as it was prescribed for those before you, that you may become righteous.',
                'transliteration': 'Ya ayyuhal lazeena aamanu kutiba alaikumus siyamu kama kutiba alal lazeena min qablikum la allakum tattaqoon',
                'revelation_place': 'Medina',
                'juz_number': 2
            },
            {
                'surah_number': 112,
                'verse_number': 1,
                'arabic_text': 'قُلْ هُوَ اللَّهُ أَحَدٌ',
                'bengali_translation': 'বল, তিনি আল্লাহ, এক।',
                'english_translation': 'Say: He is Allah, the One!',
                'transliteration': 'Qul huwa Allahu ahad',
                'revelation_place': 'Mecca',
                'juz_number': 30
            }
        ]
        
        for verse_data in verses_data:
            verse = QuranVerse(**verse_data)
            db.session.add(verse)
        
        # Create Hadith Books
        print("Creating Hadith Books...")
        books_data = [
            {
                'name': 'Sahih Bukhari',
                'arabic_name': 'صحيح البخاري',
                'author': 'Imam Bukhari',
                'total_hadith': 7563,
                'description': 'The most authentic collection of hadith'
            },
            {
                'name': 'Sahih Muslim',
                'arabic_name': 'صحيح مسلم',
                'author': 'Imam Muslim',
                'total_hadith': 3033,
                'description': 'Second most authentic collection of hadith'
            }
        ]
        
        for book_data in books_data:
            book = HadithBook(**book_data)
            db.session.add(book)
        
        db.session.commit()
        
        # Get book IDs for chapters and hadith
        bukhari = HadithBook.query.filter_by(name='Sahih Bukhari').first()
        muslim = HadithBook.query.filter_by(name='Sahih Muslim').first()
        
        # Create Hadith Chapters
        print("Creating Hadith Chapters...")
        chapters_data = [
            {
                'book_id': bukhari.id,
                'chapter_number': 1,
                'arabic_title': 'بدء الوحي',
                'english_title': 'Revelation',
                'bengali_title': 'ওহীর সূচনা'
            },
            {
                'book_id': bukhari.id,
                'chapter_number': 2,
                'arabic_title': 'الإيمان',
                'english_title': 'Faith',
                'bengali_title': 'ঈমান'
            }
        ]
        
        for chapter_data in chapters_data:
            chapter = HadithChapter(**chapter_data)
            db.session.add(chapter)
        
        db.session.commit()
        
        # Get chapter IDs
        revelation_chapter = HadithChapter.query.filter_by(book_id=bukhari.id, chapter_number=1).first()
        
        # Create Hadith
        print("Creating Hadith...")
        hadith_data = [
            {
                'book_id': bukhari.id,
                'chapter_id': revelation_chapter.id,
                'hadith_number': 1,
                'arabic_text': 'إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى',
                'bengali_translation': 'নিশ্চয়ই সকল কাজ নিয়তের উপর নির্ভরশীল এবং প্রত্যেক ব্যক্তি তার নিয়ত অনুযায়ী ফল পাবে।',
                'english_translation': 'Actions are but by intention and every man shall have only that which he intended.',
                'narrator': 'Umar ibn al-Khattab',
                'grade': 'Sahih',
                'reference': 'Bukhari 1'
            },
            {
                'book_id': bukhari.id,
                'chapter_id': revelation_chapter.id,
                'hadith_number': 8,
                'arabic_text': 'أُمِرْتُ أَنْ أُقَاتِلَ النَّاسَ حَتَّى يَشْهَدُوا أَنْ لَا إِلَهَ إِلَّا اللَّهُ وَأَنَّ مُحَمَّدًا رَسُولُ اللَّهِ',
                'bengali_translation': 'আমি মানুষের সাথে যুদ্ধ করার জন্য আদিষ্ট হয়েছি যতক্ষণ না তারা সাক্ষ্য দেয় যে আল্লাহ ছাড়া কোন উপাস্য নেই এবং মুহাম্মদ আল্লাহর রাসূল।',
                'english_translation': 'I have been ordered to fight the people until they testify that there is no deity worthy of worship except Allah and that Muhammad is the Messenger of Allah.',
                'narrator': 'Ibn Umar',
                'grade': 'Sahih',
                'reference': 'Bukhari 8'
            }
        ]
        
        for hadith_item in hadith_data:
            hadith = Hadith(**hadith_item)
            db.session.add(hadith)
        
        # Create Fatwa Categories
        print("Creating Fatwa Categories...")
        categories_data = [
            {
                'name': 'Prayer',
                'arabic_name': 'الصلاة',
                'bengali_name': 'নামাজ',
                'description': 'Questions related to prayer and worship'
            },
            {
                'name': 'Fasting',
                'arabic_name': 'الصيام',
                'bengali_name': 'রোজা',
                'description': 'Questions about fasting and Ramadan'
            },
            {
                'name': 'Zakat',
                'arabic_name': 'الزكاة',
                'bengali_name': 'যাকাত',
                'description': 'Questions about charity and alms'
            }
        ]
        
        for category_data in categories_data:
            category = FatwaCategory(**category_data)
            db.session.add(category)
        
        # Create Scholars
        print("Creating Scholars...")
        scholars_data = [
            {
                'name': 'Sheikh Ibn Baz',
                'arabic_name': 'الشيخ ابن باز',
                'title': 'Grand Mufti',
                'biography': 'Former Grand Mufti of Saudi Arabia',
                'specialization': 'Fiqh, Hadith',
                'institution': 'Islamic University of Medina',
                'country': 'Saudi Arabia',
                'is_verified': True
            },
            {
                'name': 'Sheikh Ibn Uthaymeen',
                'arabic_name': 'الشيخ ابن عثيمين',
                'title': 'Islamic Scholar',
                'biography': 'Renowned Islamic scholar and teacher',
                'specialization': 'Fiqh, Tafseer',
                'institution': 'Islamic University of Medina',
                'country': 'Saudi Arabia',
                'is_verified': True
            }
        ]
        
        for scholar_data in scholars_data:
            scholar = Scholar(**scholar_data)
            db.session.add(scholar)
        
        db.session.commit()
        
        # Get IDs for fatwa
        prayer_category = FatwaCategory.query.filter_by(name='Prayer').first()
        fasting_category = FatwaCategory.query.filter_by(name='Fasting').first()
        ibn_baz = Scholar.query.filter_by(name='Sheikh Ibn Baz').first()
        ibn_uthaymeen = Scholar.query.filter_by(name='Sheikh Ibn Uthaymeen').first()
        
        # Create Fatwa
        print("Creating Fatwa...")
        fatwa_data = [
            {
                'question': 'নামাজের সময় কি কি নিয়ম মানতে হয়?',
                'answer': 'নামাজের সময় নিম্নলিখিত নিয়মগুলো মানতে হয়:\n\n১. অজু করা - পবিত্রতা অর্জন করা\n২. পবিত্র কাপড় পরিধান করা\n৩. কিবলামুখী হওয়া\n৪. নিয়ত করা\n৫. নির্ধারিত সময়ে নামাজ পড়া\n৬. নামাজের রুকন ও ওয়াজিবসমূহ আদায় করা\n\nএই নিয়মগুলো কোরআন ও হাদিসে স্পষ্টভাবে উল্লেখ রয়েছে।',
                'scholar_id': ibn_baz.id,
                'category_id': prayer_category.id,
                'language': 'bn',
                'tags': '["নামাজ", "নিয়ম", "অজু", "কিবলা"]',
                'is_verified': True
            },
            {
                'question': 'রমজান মাসে রোজার নিয়ম কি?',
                'answer': 'রমজান মাসে রোজার মূল নিয়মাবলী:\n\n১. সুবহে সাদিক থেকে সূর্যাস্ত পর্যন্ত পানাহার থেকে বিরত থাকা\n২. স্ত্রী সহবাস থেকে বিরত থাকা\n৩. সেহরি খাওয়া (সুন্নত)\n৪. ইফতার করা\n৫. তারাবীহ নামাজ পড়া\n৬. লাইলাতুল কদর তালাশ করা\n\nরোজা ইসলামের পাঁচটি স্তম্ভের একটি এবং এটি আল্লাহর নিকট অত্যন্ত প্রিয় ইবাদত।',
                'scholar_id': ibn_uthaymeen.id,
                'category_id': fasting_category.id,
                'language': 'bn',
                'tags': '["রোজা", "রমজান", "সেহরি", "ইফতার"]',
                'is_verified': True
            }
        ]
        
        for fatwa_item in fatwa_data:
            fatwa = Fatwa(**fatwa_item)
            db.session.add(fatwa)
        
        db.session.commit()
        
        print("Sample data created successfully!")
        print(f"Created {QuranSurah.query.count()} Surahs")
        print(f"Created {QuranVerse.query.count()} Verses")
        print(f"Created {HadithBook.query.count()} Hadith Books")
        print(f"Created {HadithChapter.query.count()} Hadith Chapters")
        print(f"Created {Hadith.query.count()} Hadith")
        print(f"Created {FatwaCategory.query.count()} Fatwa Categories")
        print(f"Created {Scholar.query.count()} Scholars")
        print(f"Created {Fatwa.query.count()} Fatwa")

if __name__ == '__main__':
    create_sample_data()

