# ইসলামিক AI চ্যাটবট | Islamic AI Chatbot

<div align="center">

![Islamic AI Chatbot](https://img.shields.io/badge/Islamic-AI%20Chatbot-green?style=for-the-badge&logo=islam&logoColor=white)
![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/status-Production%20Ready-success?style=for-the-badge)

**একটি সম্পূর্ণ নির্ভরযোগ্য AI চ্যাটবট যা কুরআন, হাদিস ও ইসলামিক ফতোয়ার ভিত্তিতে বিস্তারিত উত্তর প্রদান করে**

[🚀 Live Demo](#) | [📖 Documentation](#installation) | [🤝 Contributing](#contributing) | [📧 Support](#support)

</div>

---

## 📋 সূচিপত্র | Table of Contents

- [🌟 বৈশিষ্ট্যসমূহ](#-বৈশিষ্ট্যসমূহ--features)
- [🎯 প্রকল্পের উদ্দেশ্য](#-প্রকল্পের-উদ্দেশ্য--project-objectives)
- [🏗️ প্রযুক্তিগত আর্কিটেকচার](#️-প্রযুক্তিগত-আর্কিটেকচার--technical-architecture)
- [⚡ দ্রুত শুরু](#-দ্রুত-শুরু--quick-start)
- [🔧 বিস্তারিত ইনস্টলেশন](#-বিস্তারিত-ইনস্টলেশন--detailed-installation)
- [🎮 ব্যবহারের নির্দেশনা](#-ব্যবহারের-নির্দেশনা--usage-guide)
- [📊 ডেটাবেস স্ট্রাকচার](#-ডেটাবেস-স্ট্রাকচার--database-structure)
- [🔌 API ডকুমেন্টেশন](#-api-ডকুমেন্টেশন--api-documentation)
- [🎨 UI/UX ডিজাইন](#-uiux-ডিজাইন--uiux-design)
- [🚀 ডিপ্লয়মেন্ট গাইড](#-ডিপ্লয়মেন্ট-গাইড--deployment-guide)
- [🧪 টেস্টিং](#-টেস্টিং--testing)
- [🤝 অবদান রাখুন](#-অবদান-রাখুন--contributing)
- [📄 লাইসেন্স](#-লাইসেন্স--license)
- [📞 সাপোর্ট](#-সাপোর্ট--support)

---

## 🌟 বৈশিষ্ট্যসমূহ | Features

### 🤖 AI-চালিত ইসলামিক সহায়তা
- **বিস্তারিত উত্তর**: কুরআন, হাদিস ও ফতোয়ার ভিত্তিতে বিশাল ও তথ্যবহুল উত্তর
- **উৎস রেফারেন্স**: প্রতিটি উত্তরে সুনির্দিষ্ট সূত্র ও রেফারেন্স
- **বহুভাষিক সাপোর্ট**: বাংলা, আরবি ও ইংরেজি ভাষায় সেবা
- **প্রসঙ্গভিত্তিক অনুসন্ধান**: স্মার্ট অনুসন্ধান যা প্রাসঙ্গিক তথ্য খুঁজে বের করে

### 📚 বিস্তৃত ইসলামিক ডেটাবেস
- **পূর্ণাঙ্গ কুরআন**: ১১৪ সূরার সম্পূর্ণ আয়াত, অনুবাদ ও তাফসীর
- **হাদিস সংগ্রহ**: সহীহ বুখারী, সহীহ মুসলিম, আবু দাউদ, তিরমিযী, ইবনে মাজাহ
- **ফতোয়া ডেটাবেস**: বিশ্বস্ত আলেমদের ফতোয়া ও ইসলামিক রুলিং
- **তাফসীর ও ব্যাখ্যা**: বিভিন্ন তাফসীরকারকদের ব্যাখ্যা

### 🎨 আধুনিক ও সুন্দর ইন্টারফেস
- **রেসপনসিভ ডিজাইন**: মোবাইল, ট্যাবলেট ও ডেস্কটপে নিখুঁত অভিজ্ঞতা
- **ইসলামিক থিম**: ইসলামিক নন্দনতত্ত্ব অনুসরণকারী সুন্দর ডিজাইন
- **ডার্ক/লাইট মোড**: ব্যবহারকারীর পছন্দ অনুযায়ী থিম পরিবর্তন
- **সহজ নেভিগেশন**: ব্যবহার-বান্ধব ইন্টারফেস

### 🔐 নিরাপত্তা ও গোপনীয়তা
- **JWT Authentication**: নিরাপদ ব্যবহারকারী প্রমাণীকরণ
- **ডেটা এনক্রিপশন**: সংবেদনশীল তথ্যের এনক্রিপশন
- **প্রাইভেসি ফার্স্ট**: ব্যবহারকারীর গোপনীয়তা সর্বোচ্চ অগ্রাধিকার
- **সিকিউর API**: HTTPS ও CORS সাপোর্ট

### 📱 অতিরিক্ত ফিচার
- **বুকমার্ক সিস্টেম**: গুরুত্বপূর্ণ উত্তর সংরক্ষণ
- **সার্চ হিস্টরি**: পূর্বের অনুসন্ধানের ইতিহাস
- **ফিডব্যাক সিস্টেম**: ব্যবহারকারীর মতামত ও পরামর্শ
- **অফলাইন সাপোর্ট**: ইন্টারনেট ছাড়াই মৌলিক ফিচার ব্যবহার

---



## 🎯 প্রকল্পের উদ্দেশ্য | Project Objectives

ইসলামিক AI চ্যাটবট প্রকল্পটি তৈরি করা হয়েছে আধুনিক প্রযুক্তির সাথে ইসলামিক জ্ঞানের সমন্বয় ঘটিয়ে মুসলিম উম্মাহর সেবা করার জন্য। এই প্রকল্পের মূল উদ্দেশ্যগুলি হলো:

### 🎓 শিক্ষামূলক উদ্দেশ্য
আমাদের প্রাথমিক লক্ষ্য হলো ইসলামিক শিক্ষাকে সহজলভ্য ও আকর্ষণীয় করে তোলা। অনেক মুসলিম ভাই-বোন কুরআন ও হাদিসের বিশাল ভাণ্ডার থেকে সঠিক তথ্য খুঁজে পেতে অসুবিধার সম্মুখীন হন। এই চ্যাটবট সেই সমস্যার সমাধান প্রদান করে তাৎক্ষণিক ও নির্ভুল ইসলামিক তথ্য সরবরাহ করে।

### 🌐 প্রযুক্তিগত উদ্দেশ্য
আর্টিফিশিয়াল ইন্টেলিজেন্স ও মেশিন লার্নিং প্রযুক্তিকে ইসলামিক শিক্ষার ক্ষেত্রে প্রয়োগ করে একটি অগ্রগামী সমাধান তৈরি করা। এই প্রকল্পে ব্যবহৃত হয়েছে সর্বাধুনিক OpenAI GPT মডেল, যা কুরআন ও হাদিসের গভীর জ্ঞানের সাথে প্রশিক্ষিত।

### 🤝 সামাজিক উদ্দেশ্য
বিশ্বব্যাপী মুসলিম কমিউনিটির মধ্যে ইসলামিক জ্ঞান বিতরণে সহায়তা করা এবং ভাষাগত বাধা দূর করা। বিশেষত বাংলাভাষী মুসলিমদের জন্য একটি নির্ভরযোগ্য ইসলামিক তথ্যের উৎস প্রদান করা।

---

## 🏗️ প্রযুক্তিগত আর্কিটেকচার | Technical Architecture

### 🎨 ফ্রন্টএন্ড আর্কিটেকচার

আমাদের ফ্রন্টএন্ড React.js ফ্রেমওয়ার্কের উপর ভিত্তি করে তৈরি, যা আধুনিক ওয়েব অ্যাপ্লিকেশনের জন্য সর্বোত্তম পারফরমেন্স ও ব্যবহারকারী অভিজ্ঞতা প্রদান করে।

**মূল প্রযুক্তিসমূহ:**
- **React 18.2+**: কম্পোনেন্ট-ভিত্তিক আর্কিটেকচার
- **Tailwind CSS**: ইউটিলিটি-ফার্স্ট CSS ফ্রেমওয়ার্ক
- **shadcn/ui**: আধুনিক UI কম্পোনেন্ট লাইব্রেরি
- **Vite**: দ্রুত বিল্ড টুল ও ডেভেলপমেন্ট সার্ভার
- **React Router**: ক্লায়েন্ট-সাইড রাউটিং

**কম্পোনেন্ট স্ট্রাকচার:**
```
src/
├── components/
│   ├── Header.jsx          # নেভিগেশন হেডার
│   ├── Sidebar.jsx         # সাইডবার মেনু
│   ├── ChatInterface.jsx   # চ্যাট ইন্টারফেস
│   ├── AuthPage.jsx        # লগইন/রেজিস্ট্রেশন
│   ├── ProfilePage.jsx     # ব্যবহারকারী প্রোফাইল
│   ├── BookmarksPage.jsx   # বুকমার্ক পেজ
│   └── SearchPage.jsx      # অনুসন্ধান পেজ
├── hooks/
│   ├── useAuth.jsx         # অথেন্টিকেশন হুক
│   └── useChat.jsx         # চ্যাট ম্যানেজমেন্ট হুক
└── App.jsx                 # মূল অ্যাপ্লিকেশন
```

### ⚙️ ব্যাকএন্ড আর্কিটেকচার

ব্যাকএন্ড Flask ফ্রেমওয়ার্কের উপর ভিত্তি করে তৈরি, যা Python এর শক্তিশালী ইকোসিস্টেমের সুবিধা নিয়ে একটি মজবুত API সার্ভার প্রদান করে।

**মূল প্রযুক্তিসমূহ:**
- **Flask 2.3+**: মাইক্রো ওয়েব ফ্রেমওয়ার্ক
- **Flask-SQLAlchemy**: ORM ও ডেটাবেস ম্যানেজমেন্ট
- **Flask-JWT-Extended**: JWT টোকেন ভিত্তিক অথেন্টিকেশন
- **OpenAI API**: GPT-3.5/4 ইন্টিগ্রেশন
- **SQLite**: লাইটওয়েট ডেটাবেস সিস্টেম

**API স্ট্রাকচার:**
```
src/
├── routes/
│   ├── auth.py             # অথেন্টিকেশন API
│   ├── chat.py             # চ্যাট API
│   ├── chat_enhanced.py    # উন্নত চ্যাট API
│   ├── islamic_content.py  # ইসলামিক কন্টেন্ট API
│   ├── user.py             # ব্যবহারকারী ম্যানেজমেন্ট
│   └── feedback.py         # ফিডব্যাক সিস্টেম
├── models/
│   ├── database.py         # ডেটাবেস মডেল
│   └── simple_database.py  # সিম্পল ডেটাবেস কানেকশন
└── main.py                 # মূল অ্যাপ্লিকেশন
```

### 🗄️ ডেটাবেস আর্কিটেকচার

আমাদের ডেটাবেস স্ট্রাকচার ইসলামিক কন্টেন্টের জটিলতা ও বৈচিত্র্যকে মাথায় রেখে ডিজাইন করা হয়েছে।

**প্রধান টেবিলসমূহ:**

| টেবিল | উদ্দেশ্য | রেকর্ড সংখ্যা |
|--------|----------|--------------|
| `quran_enhanced` | কুরআনের আয়াত, অনুবাদ ও তাফসীর | ৬,২৩৬+ |
| `hadith_enhanced` | হাদিস সংগ্রহ ও গ্রেডিং | ১০,০০০+ |
| `fatwa_enhanced` | ইসলামিক ফতোয়া ও রুলিং | ৫০০+ |
| `islamic_sources` | তথ্যসূত্র ও রেফারেন্স | ১০০+ |
| `islamic_topics` | বিষয়ভিত্তিক শ্রেণীবিভাগ | ২০০+ |

### 🤖 AI ইন্টিগ্রেশন আর্কিটেকচার

আমাদের AI সিস্টেম একটি হাইব্রিড অ্যাপ্রোচ ব্যবহার করে যা ঐতিহ্যগত ডেটাবেস অনুসন্ধান ও আধুনিক AI প্রযুক্তির সমন্বয় ঘটায়।

**AI ওয়ার্কফ্লো:**
1. **কনটেক্সট অনুসন্ধান**: ব্যবহারকারীর প্রশ্ন অনুযায়ী প্রাসঙ্গিক কুরআন, হাদিস ও ফতোয়া খুঁজে বের করা
2. **প্রম্পট ইঞ্জিনিয়ারিং**: ইসলামিক কনটেক্সট সহ AI প্রম্পট তৈরি
3. **AI প্রসেসিং**: OpenAI GPT মডেল দিয়ে উত্তর জেনারেশন
4. **রেফারেন্স ম্যাপিং**: উত্তরের সাথে সংশ্লিষ্ট সূত্র যুক্ত করা
5. **কোয়ালিটি চেক**: উত্তরের গুণগত মান যাচাই

---


## ⚡ দ্রুত শুরু | Quick Start

### 🚀 ৫ মিনিটে চালু করুন

```bash
# রিপোজিটরি ক্লোন করুন
git clone https://github.com/yourusername/islamic-ai-chatbot.git
cd islamic-ai-chatbot

# ব্যাকএন্ড সেটআপ
cd islamic-chatbot-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# ডেটাবেস ইনিশিয়ালাইজ করুন
python src/enhanced_data.py

# ব্যাকএন্ড সার্ভার চালু করুন
python src/main.py

# নতুন টার্মিনালে ফ্রন্টএন্ড সেটআপ
cd ../islamic-chatbot-frontend
npm install
npm run dev

# ব্রাউজারে http://localhost:5173 এ যান
```

### 🔑 পরিবেশ ভেরিয়েবল

`.env` ফাইল তৈরি করুন:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE=https://api.openai.com/v1

# Flask Configuration
FLASK_SECRET_KEY=your_secret_key_here
JWT_SECRET_KEY=your_jwt_secret_key_here

# Database Configuration
DATABASE_URL=sqlite:///islamic_data.db

# Development Settings
FLASK_ENV=development
DEBUG=True
```

---

## 🔧 বিস্তারিত ইনস্টলেশন | Detailed Installation

### 📋 সিস্টেম প্রয়োজনীয়তা

**ন্যূনতম প্রয়োজনীয়তা:**
- **অপারেটিং সিস্টেম**: Windows 10+, macOS 10.15+, Ubuntu 18.04+
- **Python**: 3.8 বা তার উপরে
- **Node.js**: 16.0 বা তার উপরে
- **RAM**: ৪ GB (৮ GB প্রস্তাবিত)
- **স্টোরেজ**: ২ GB ফ্রি স্পেস

**প্রস্তাবিত প্রয়োজনীয়তা:**
- **Python**: 3.11+
- **Node.js**: 18.0+
- **RAM**: ৮ GB বা তার বেশি
- **SSD**: দ্রুত পারফরমেন্সের জন্য

### 🐍 ব্যাকএন্ড ইনস্টলেশন

#### ধাপ ১: Python পরিবেশ প্রস্তুতি

```bash
# Python ভার্সন চেক করুন
python --version  # 3.8+ প্রয়োজন

# প্রকল্প ডিরেক্টরিতে যান
cd islamic-chatbot-api

# ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন
python -m venv venv

# ভার্চুয়াল এনভায়রনমেন্ট অ্যাক্টিভেট করুন
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

#### ধাপ ২: ডিপেন্ডেন্সি ইনস্টল

```bash
# প্রয়োজনীয় প্যাকেজ ইনস্টল করুন
pip install --upgrade pip
pip install -r requirements.txt

# ডেভেলপমেন্ট ডিপেন্ডেন্সি (ঐচ্ছিক)
pip install -r requirements-dev.txt
```

#### ধাপ ৩: ডেটাবেস সেটআপ

```bash
# ইসলামিক ডেটাবেস তৈরি ও পপুলেট করুন
python src/enhanced_data.py

# সিম্পল ডেটাবেস ইনিশিয়ালাইজ করুন
python src/models/simple_database.py

# ডেটাবেস স্ট্যাটাস চেক করুন
python -c "
import sqlite3
conn = sqlite3.connect('islamic_comprehensive.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM hadith_enhanced')
print(f'হাদিস রেকর্ড: {cursor.fetchone()[0]}')
conn.close()
"
```

#### ধাপ ৪: কনফিগারেশন

```bash
# .env ফাইল তৈরি করুন
cp .env.example .env

# .env ফাইল এডিট করুন
nano .env  # অথবা আপনার পছন্দের এডিটর
```

### 🌐 ফ্রন্টএন্ড ইনস্টলেশন

#### ধাপ ১: Node.js সেটআপ

```bash
# Node.js ভার্সন চেক করুন
node --version  # 16.0+ প্রয়োজন
npm --version

# প্রকল্প ডিরেক্টরিতে যান
cd islamic-chatbot-frontend
```

#### ধাপ ২: ডিপেন্ডেন্সি ইনস্টল

```bash
# npm ডিপেন্ডেন্সি ইনস্টল করুন
npm install

# অথবা yarn ব্যবহার করুন (ঐচ্ছিক)
yarn install
```

#### ধাপ ৩: ডেভেলপমেন্ট সার্ভার

```bash
# ডেভেলপমেন্ট সার্ভার চালু করুন
npm run dev

# অথবা yarn দিয়ে
yarn dev

# সার্ভার http://localhost:5173 এ চালু হবে
```

### 🔧 অতিরিক্ত কনফিগারেশন

#### SSL সার্টিফিকেট (প্রোডাকশনের জন্য)

```bash
# Let's Encrypt SSL সার্টিফিকেট
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

#### ডেটাবেস ব্যাকআপ

```bash
# ডেটাবেস ব্যাকআপ স্ক্রিপ্ট
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
cp islamic_comprehensive.db "backups/islamic_db_backup_$DATE.db"
echo "ব্যাকআপ সম্পন্ন: islamic_db_backup_$DATE.db"
```

### ❗ সাধারণ সমস্যা ও সমাধান

#### সমস্যা ১: Python ভার্সন সমস্যা
```bash
# সমাধান: pyenv ব্যবহার করুন
curl https://pyenv.run | bash
pyenv install 3.11.0
pyenv local 3.11.0
```

#### সমস্যা ২: Node.js ভার্সন সমস্যা
```bash
# সমাধান: nvm ব্যবহার করুন
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18
```

#### সমস্যা ৩: OpenAI API কী সমস্যা
```bash
# API কী টেস্ট করুন
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.openai.com/v1/models
```

---


## 🎮 ব্যবহারের নির্দেশনা | Usage Guide

### 👤 ব্যবহারকারী নিবন্ধন ও লগইন

#### নতুন অ্যাকাউন্ট তৈরি
1. **নিবন্ধন পেজে যান**: হোমপেজের "নিবন্ধন" বাটনে ক্লিক করুন
2. **তথ্য পূরণ করুন**:
   - পূর্ণ নাম (আরবি/বাংলা/ইংরেজি)
   - ব্যবহারকারী নাম (ইউনিক হতে হবে)
   - ইমেইল ঠিকানা
   - নিরাপদ পাসওয়ার্ড (৮+ অক্ষর, বিশেষ চিহ্ন সহ)
3. **যাচাইকরণ**: ইমেইল যাচাইকরণ লিংকে ক্লিক করুন
4. **প্রোফাইল সেটআপ**: ভাষা পছন্দ ও টাইমজোন নির্বাচন করুন

#### লগইন প্রক্রিয়া
```javascript
// API কল উদাহরণ
const loginResponse = await fetch('/api/v1/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'your_username',
    password: 'your_password'
  })
});
```

### 💬 চ্যাট ইন্টারফেস ব্যবহার

#### মৌলিক চ্যাট ব্যবহার
1. **প্রশ্ন টাইপ করুন**: চ্যাট বক্সে আপনার ইসলামিক প্রশ্ন লিখুন
2. **Send বাটন**: প্রশ্ন পাঠাতে এন্টার চাপুন বা Send বাটনে ক্লিক করুন
3. **উত্তর পর্যালোচনা**: AI থেকে বিস্তারিত উত্তর ও রেফারেন্স পাবেন
4. **ফলো-আপ**: প্রয়োজনে অতিরিক্ত প্রশ্ন করুন

#### উন্নত চ্যাট ফিচার
- **ভয়েস ইনপুট**: মাইক্রোফোন আইকনে ক্লিক করে কথা বলুন
- **ইমেজ আপলোড**: আরবি টেক্সট বা ইসলামিক ইমেজ আপলোড করুন
- **ভাষা পরিবর্তন**: বাংলা, আরবি, ইংরেজিতে প্রশ্ন করুন
- **কনটেক্সট মেমোরি**: পূর্বের কথোপকথন মনে রাখে

### 🔍 অনুসন্ধান ফিচার

#### কুরআন অনুসন্ধান
```bash
# উদাহরণ অনুসন্ধান
"নামাজের গুরুত্ব"          # বিষয়ভিত্তিক
"সূরা বাকারা ২৫৫"          # নির্দিষ্ট আয়াত
"আয়াতুল কুরসি"           # নাম দিয়ে
"prayer importance"        # ইংরেজিতে
```

#### হাদিস অনুসন্ধান
```bash
# হাদিস অনুসন্ধানের উদাহরণ
"সহীহ বুখারী ১"           # হাদিস নম্বর দিয়ে
"নিয়তের হাদিস"           # বিষয় দিয়ে
"আবু হুরায়রা"             # বর্ণনাকারী দিয়ে
"ইমাম বুখারী"             # সংকলনকারী দিয়ে
```

### 📚 বুকমার্ক ও হিস্টরি

#### বুকমার্ক ব্যবস্থাপনা
1. **বুকমার্ক যোগ**: উত্তরের পাশে ⭐ আইকনে ক্লিক করুন
2. **বুকমার্ক দেখুন**: সাইডবারের "বুকমার্ক" সেকশনে যান
3. **ক্যাটেগরি তৈরি**: বুকমার্কগুলো বিষয়ভিত্তিক সাজান
4. **শেয়ার করুন**: বুকমার্ক অন্যদের সাথে শেয়ার করুন

#### হিস্টরি ব্যবহার
- **সার্চ হিস্টরি**: পূর্বের সব অনুসন্ধান দেখুন
- **চ্যাট হিস্টরি**: পুরানো কথোপকথন পুনরায় দেখুন
- **এক্সপোর্ট**: হিস্টরি PDF বা JSON ফরম্যাটে ডাউনলোড করুন

---

## 🔌 API ডকুমেন্টেশন | API Documentation

### 🔐 অথেন্টিকেশন API

#### POST `/api/v1/auth/register`
নতুন ব্যবহারকারী নিবন্ধন

**Request Body:**
```json
{
  "full_name": "মোহাম্মদ আহমেদ",
  "username": "ahmed123",
  "email": "ahmed@example.com",
  "password": "SecurePass123!",
  "preferred_language": "bn"
}
```

**Response:**
```json
{
  "success": true,
  "message": "User registered successfully",
  "data": {
    "user_id": "uuid-here",
    "username": "ahmed123",
    "email": "ahmed@example.com",
    "access_token": "jwt-token-here",
    "refresh_token": "refresh-token-here",
    "expires_in": 3600
  }
}
```

#### POST `/api/v1/auth/login`
ব্যবহারকারী লগইন

**Request Body:**
```json
{
  "username": "ahmed123",
  "password": "SecurePass123!"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "access_token": "jwt-token-here",
    "refresh_token": "refresh-token-here",
    "expires_in": 3600,
    "user": {
      "id": "uuid-here",
      "username": "ahmed123",
      "full_name": "মোহাম্মদ আহমেদ",
      "email": "ahmed@example.com"
    }
  }
}
```

### 💬 চ্যাট API

#### POST `/api/v1/chat-enhanced/send`
উন্নত AI চ্যাট মেসেজ পাঠানো

**Headers:**
```
Authorization: Bearer jwt-token-here
Content-Type: application/json
```

**Request Body:**
```json
{
  "message": "যাকাত দেওয়ার নিয়ম কি? কুরআন ও হাদিসের রেফারেন্স সহ বিস্তারিত জানতে চাই।",
  "language": "bn",
  "context_limit": 5
}
```

**Response:**
```json
{
  "success": true,
  "response": "যাকাত ইসলামের পাঁচটি স্তম্ভের একটি এবং এটি প্রতিটি সামর্থ্যবান মুসলিমের উপর ফরজ...",
  "sources": [
    "কুরআন: সূরা তওবা, আয়াত ১০৩",
    "হাদিস: সহীহ বুখারী: ১৪৫৪",
    "ফতোয়া: মুফতি তাকি উসমানী (দারুল উলুম করাচি)"
  ],
  "context_used": 3,
  "timestamp": "2025-07-25T08:44:50.696383",
  "message_id": "msg-uuid-here"
}
```

#### GET `/api/v1/chat-enhanced/history`
চ্যাট হিস্টরি পুনরুদ্ধার

**Query Parameters:**
- `page`: পেজ নম্বর (ডিফল্ট: 1)
- `per_page`: প্রতি পেজে রেকর্ড (ডিফল্ট: 20)
- `date_from`: শুরুর তারিখ (YYYY-MM-DD)
- `date_to`: শেষের তারিখ (YYYY-MM-DD)

**Response:**
```json
{
  "success": true,
  "messages": [
    {
      "message": "যাকাত দেওয়ার নিয়ম কি?",
      "type": "user",
      "sources": [],
      "timestamp": "2025-07-25T08:44:45.123456"
    },
    {
      "message": "যাকাত ইসলামের পাঁচটি স্তম্ভের একটি...",
      "type": "assistant",
      "sources": ["কুরআন: সূরা তওবা, আয়াত ১০৩"],
      "timestamp": "2025-07-25T08:44:50.696383"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 150,
    "pages": 8
  }
}
```

### 📖 ইসলামিক কন্টেন্ট API

#### GET `/api/v1/quran/search`
কুরআন অনুসন্ধান

**Query Parameters:**
- `q`: অনুসন্ধান টেক্সট
- `language`: ভাষা (bn/ar/en)
- `surah`: সূরা নম্বর (ঐচ্ছিক)
- `limit`: ফলাফলের সীমা (ডিফল্ট: 10)

**Example:**
```bash
GET /api/v1/quran/search?q=নামাজ&language=bn&limit=5
```

**Response:**
```json
{
  "success": true,
  "results": [
    {
      "surah_number": 2,
      "ayah_number": 43,
      "arabic_text": "وَأَقِيمُوا الصَّلَاةَ وَآتُوا الزَّكَاةَ",
      "bengali_translation": "আর নামাজ কায়েম কর এবং যাকাত দাও",
      "english_translation": "And establish prayer and give zakah",
      "revelation_place": "মদিনা",
      "juz_number": 1,
      "reference": "সূরা বাকারা, আয়াত ৪৩"
    }
  ],
  "total_found": 127,
  "search_time": "0.045s"
}
```

#### GET `/api/v1/hadith/search`
হাদিস অনুসন্ধান

**Query Parameters:**
- `q`: অনুসন্ধান টেক্সট
- `collection`: হাদিস সংকলন (bukhari/muslim/abudawud/tirmidhi/ibnmajah)
- `grade`: হাদিসের গ্রেড (sahih/hasan/daif)
- `language`: ভাষা (bn/ar/en)
- `limit`: ফলাফলের সীমা

**Response:**
```json
{
  "success": true,
  "results": [
    {
      "collection_name": "সহীহ বুখারী",
      "book_name": "ঈমান",
      "hadith_number": 1,
      "arabic_text": "إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ",
      "bengali_translation": "সকল কাজ নিয়তের উপর নির্ভরশীল",
      "narrator": "উমর ইবনুল খাত্তাব (রা.)",
      "grade": "সহীহ",
      "theme": "নিয়ত",
      "reference": "সহীহ বুখারী: ১"
    }
  ],
  "total_found": 45,
  "search_time": "0.032s"
}
```

### 📊 স্ট্যাটিস্টিক্স API

#### GET `/api/v1/stats/overview`
সিস্টেম পরিসংখ্যান

**Response:**
```json
{
  "success": true,
  "data": {
    "total_users": 1250,
    "total_messages": 15670,
    "total_quran_verses": 6236,
    "total_hadiths": 10000,
    "total_fatwas": 500,
    "daily_active_users": 89,
    "popular_topics": [
      {"topic": "নামাজ", "count": 450},
      {"topic": "যাকাত", "count": 320},
      {"topic": "রোজা", "count": 280}
    ]
  }
}
```

### ❌ এরর হ্যান্ডলিং

সব API রেসপন্স একই ফরম্যাট অনুসরণ করে:

**সফল রেসপন্স:**
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation completed successfully"
}
```

**এরর রেসপন্স:**
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input parameters",
    "details": {
      "field": "email",
      "reason": "Invalid email format"
    }
  }
}
```

**সাধারণ এরর কোডসমূহ:**
- `AUTHENTICATION_REQUIRED`: অথেন্টিকেশন প্রয়োজন
- `INVALID_TOKEN`: টোকেন অবৈধ বা মেয়াদোত্তীর্ণ
- `VALIDATION_ERROR`: ইনপুট ভ্যালিডেশন ব্যর্থ
- `NOT_FOUND`: রিসোর্স পাওয়া যায়নি
- `RATE_LIMIT_EXCEEDED`: রেট লিমিট অতিক্রম
- `INTERNAL_ERROR`: সার্ভার ত্রুটি

---


## 🚀 ডিপ্লয়মেন্ট গাইড | Deployment Guide

### 🌐 প্রোডাকশন ডিপ্লয়মেন্ট

#### Heroku ডিপ্লয়মেন্ট

**ব্যাকএন্ড ডিপ্লয়মেন্ট:**
```bash
# Heroku CLI ইনস্টল করুন
npm install -g heroku

# Heroku অ্যাপ তৈরি করুন
heroku create islamic-chatbot-api

# পরিবেশ ভেরিয়েবল সেট করুন
heroku config:set OPENAI_API_KEY=your_key_here
heroku config:set FLASK_SECRET_KEY=your_secret_here
heroku config:set JWT_SECRET_KEY=your_jwt_secret_here

# ডিপ্লয় করুন
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

**ফ্রন্টএন্ড ডিপ্লয়মেন্ট (Vercel):**
```bash
# Vercel CLI ইনস্টল
npm install -g vercel

# ডিপ্লয় করুন
cd islamic-chatbot-frontend
vercel --prod

# কাস্টম ডোমেইন যোগ করুন
vercel domains add yourdomain.com
```

#### Docker ডিপ্লয়মেন্ট

**Dockerfile (ব্যাকএন্ড):**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.main:app"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  backend:
    build: ./islamic-chatbot-api
    ports:
      - "5000:5000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - FLASK_SECRET_KEY=${FLASK_SECRET_KEY}
    volumes:
      - ./data:/app/data

  frontend:
    build: ./islamic-chatbot-frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - frontend
      - backend
```

#### AWS ডিপ্লয়মেন্ট

**EC2 ইনস্ট্যান্স সেটআপ:**
```bash
# EC2 ইনস্ট্যান্সে কানেক্ট করুন
ssh -i your-key.pem ubuntu@your-ec2-ip

# প্রয়োজনীয় সফটওয়্যার ইনস্টল
sudo apt update
sudo apt install python3 python3-pip nodejs npm nginx

# প্রকল্প ক্লোন করুন
git clone https://github.com/yourusername/islamic-ai-chatbot.git
cd islamic-ai-chatbot

# ব্যাকএন্ড সেটআপ
cd islamic-chatbot-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# ফ্রন্টএন্ড বিল্ড
cd ../islamic-chatbot-frontend
npm install
npm run build

# Nginx কনফিগারেশন
sudo cp nginx.conf /etc/nginx/sites-available/islamic-chatbot
sudo ln -s /etc/nginx/sites-available/islamic-chatbot /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

### 🔧 পারফরমেন্স অপটিমাইজেশন

#### ডেটাবেস অপটিমাইজেশন
```sql
-- ইনডেক্স তৈরি করুন
CREATE INDEX idx_quran_bengali ON quran_enhanced(bengali_translation);
CREATE INDEX idx_hadith_theme ON hadith_enhanced(theme);
CREATE INDEX idx_fatwa_category ON fatwa_enhanced(category);

-- ফুল-টেক্সট সার্চ সক্ষম করুন
CREATE VIRTUAL TABLE quran_fts USING fts5(
    surah_number, ayah_number, arabic_text, bengali_translation
);
```

#### ক্যাশিং স্ট্র্যাটেজি
```python
# Redis ক্যাশিং
import redis
from functools import wraps

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_result(expiration=3600):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            cached_result = redis_client.get(cache_key)
            
            if cached_result:
                return json.loads(cached_result)
            
            result = func(*args, **kwargs)
            redis_client.setex(cache_key, expiration, json.dumps(result))
            return result
        return wrapper
    return decorator
```

### 📊 মনিটরিং ও লগিং

#### Prometheus মেট্রিক্স
```python
from prometheus_client import Counter, Histogram, generate_latest

# মেট্রিক্স ডিফাইন করুন
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests')
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')

@app.route('/metrics')
def metrics():
    return generate_latest()
```

#### ELK Stack লগিং
```yaml
# docker-compose.yml এ যোগ করুন
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.14.0
    environment:
      - discovery.type=single-node
    ports:
      - "9200:9200"

  logstash:
    image: docker.elastic.co/logstash/logstash:7.14.0
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf

  kibana:
    image: docker.elastic.co/kibana/kibana:7.14.0
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch
```

---

## 🧪 টেস্টিং | Testing

### 🔍 ইউনিট টেস্ট

#### ব্যাকএন্ড টেস্ট
```python
# tests/test_chat.py
import pytest
from src.main import app
from src.models.database import db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_chat_send_message(client):
    # টেস্ট ব্যবহারকারী তৈরি
    response = client.post('/api/v1/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'TestPass123!',
        'full_name': 'Test User'
    })
    
    token = response.json['data']['access_token']
    
    # চ্যাট মেসেজ পাঠান
    response = client.post('/api/v1/chat-enhanced/send', 
        headers={'Authorization': f'Bearer {token}'},
        json={'message': 'নামাজের গুরুত্ব কি?'}
    )
    
    assert response.status_code == 200
    assert response.json['success'] == True
    assert len(response.json['sources']) > 0
```

#### ফ্রন্টএন্ড টেস্ট
```javascript
// tests/ChatInterface.test.jsx
import { render, screen, fireEvent } from '@testing-library/react';
import ChatInterface from '../src/components/ChatInterface';

test('sends message when send button is clicked', () => {
  render(<ChatInterface />);
  
  const messageInput = screen.getByPlaceholderText('আপনার প্রশ্ন লিখুন...');
  const sendButton = screen.getByText('Send');
  
  fireEvent.change(messageInput, { target: { value: 'নামাজের নিয়ম কি?' } });
  fireEvent.click(sendButton);
  
  expect(screen.getByText('নামাজের নিয়ম কি?')).toBeInTheDocument();
});
```

### 🔄 ইন্টিগ্রেশন টেস্ট

```python
# tests/test_integration.py
def test_full_chat_workflow(client):
    # ১. ব্যবহারকারী নিবন্ধন
    register_response = client.post('/api/v1/auth/register', json={
        'username': 'integrationtest',
        'email': 'integration@test.com',
        'password': 'IntegrationTest123!',
        'full_name': 'Integration Test User'
    })
    
    assert register_response.status_code == 201
    token = register_response.json['data']['access_token']
    
    # ২. চ্যাট মেসেজ পাঠানো
    chat_response = client.post('/api/v1/chat-enhanced/send',
        headers={'Authorization': f'Bearer {token}'},
        json={'message': 'যাকাতের নিসাব কত?'}
    )
    
    assert chat_response.status_code == 200
    assert 'যাকাত' in chat_response.json['response']
    
    # ৩. চ্যাট হিস্টরি চেক
    history_response = client.get('/api/v1/chat-enhanced/history',
        headers={'Authorization': f'Bearer {token}'}
    )
    
    assert history_response.status_code == 200
    assert len(history_response.json['messages']) >= 2
```

### 🚀 পারফরমেন্স টেস্ট

```python
# tests/test_performance.py
import time
import concurrent.futures

def test_concurrent_requests():
    def send_request():
        start_time = time.time()
        response = client.post('/api/v1/chat-enhanced/send',
            headers={'Authorization': f'Bearer {token}'},
            json={'message': 'নামাজের সময় কখন?'}
        )
        end_time = time.time()
        return response.status_code, end_time - start_time
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(send_request) for _ in range(50)]
        results = [future.result() for future in futures]
    
    # সব রিকোয়েস্ট সফল হয়েছে কিনা চেক
    assert all(status == 200 for status, _ in results)
    
    # গড় রেসপন্স টাইম ৫ সেকেন্ডের কম কিনা চেক
    avg_response_time = sum(time for _, time in results) / len(results)
    assert avg_response_time < 5.0
```

---

## 🤝 অবদান রাখুন | Contributing

### 🎯 অবদানের নির্দেশনা

আমরা কমিউনিটির অবদানকে স্বাগত জানাই! এই প্রকল্পে অবদান রাখার জন্য নিম্নলিখিত নির্দেশনা অনুসরণ করুন:

#### 🔄 কন্ট্রিবিউশন ওয়ার্কফ্লো

1. **ফর্ক করুন**: প্রকল্পটি আপনার GitHub অ্যাকাউন্টে ফর্ক করুন
2. **ব্রাঞ্চ তৈরি করুন**: নতুন ফিচারের জন্য আলাদা ব্রাঞ্চ তৈরি করুন
3. **কোড লিখুন**: আমাদের কোডিং স্ট্যান্ডার্ড অনুসরণ করুন
4. **টেস্ট করুন**: আপনার পরিবর্তনগুলো টেস্ট করুন
5. **পুল রিকোয়েস্ট**: বিস্তারিত বর্ণনা সহ PR তৈরি করুন

```bash
# প্রকল্প ফর্ক ও ক্লোন করুন
git clone https://github.com/yourusername/islamic-ai-chatbot.git
cd islamic-ai-chatbot

# নতুন ব্রাঞ্চ তৈরি করুন
git checkout -b feature/new-islamic-feature

# পরিবর্তন করুন ও কমিট করুন
git add .
git commit -m "Add: নতুন ইসলামিক ফিচার যোগ করা হয়েছে"

# পুশ করুন
git push origin feature/new-islamic-feature

# GitHub এ পুল রিকোয়েস্ট তৈরি করুন
```

#### 📝 কোডিং স্ট্যান্ডার্ড

**Python (ব্যাকএন্ড):**
```python
# PEP 8 অনুসরণ করুন
# ফাংশন ও ভেরিয়েবল নাম snake_case এ লিখুন
# ক্লাস নাম PascalCase এ লিখুন
# কমেন্ট বাংলা ও ইংরেজি দুটোতেই লিখতে পারেন

def get_quran_verse(surah_number: int, ayah_number: int) -> dict:
    """
    কুরআনের নির্দিষ্ট আয়াত পুনরুদ্ধার করে
    
    Args:
        surah_number: সূরা নম্বর (১-১১৪)
        ayah_number: আয়াত নম্বর
    
    Returns:
        dict: আয়াতের তথ্য সহ ডিকশনারি
    """
    pass
```

**JavaScript (ফ্রন্টএন্ড):**
```javascript
// camelCase ব্যবহার করুন
// JSDoc কমেন্ট ব্যবহার করুন
// ES6+ ফিচার ব্যবহার করুন

/**
 * ইসলামিক কন্টেন্ট সার্চ করে
 * @param {string} query - সার্চ কোয়েরি
 * @param {string} type - কন্টেন্ট টাইপ (quran/hadith/fatwa)
 * @returns {Promise<Object>} সার্চ রেজাল্ট
 */
const searchIslamicContent = async (query, type = 'all') => {
  // Implementation here
};
```

#### 🐛 বাগ রিপোর্ট

বাগ রিপোর্ট করার সময় নিম্নলিখিত তথ্য অন্তর্ভুক্ত করুন:

```markdown
## বাগ বর্ণনা
সংক্ষেপে বাগটি কি তা বর্ণনা করুন।

## পুনরুৎপাদনের ধাপ
1. '...' এ যান
2. '....' এ ক্লিক করুন
3. '....' পর্যন্ত স্ক্রল করুন
4. ত্রুটি দেখুন

## প্রত্যাশিত আচরণ
কি হওয়ার কথা ছিল তা বর্ণনা করুন।

## স্ক্রিনশট
যদি প্রযোজ্য হয়, সমস্যা ব্যাখ্যা করতে স্ক্রিনশট যোগ করুন।

## পরিবেশ:
 - OS: [e.g. Ubuntu 20.04]
 - Browser: [e.g. Chrome 91]
 - Version: [e.g. 1.0.0]
```

#### 💡 ফিচার রিকোয়েস্ট

```markdown
## ফিচার বর্ণনা
আপনি যে ফিচারটি চান তার স্পষ্ট ও সংক্ষিপ্ত বর্ণনা।

## সমস্যা
এই ফিচারটি কি সমস্যার সমাধান করবে? উদাহরণ: আমি সবসময় হতাশ হই যখন [...]

## সমাধান
আপনি যে সমাধান চান তার বর্ণনা।

## বিকল্প
আপনি যে বিকল্প সমাধানগুলো বিবেচনা করেছেন তার বর্ণনা।

## অতিরিক্ত প্রসঙ্গ
ফিচার রিকোয়েস্ট সম্পর্কে অন্য কোনো প্রসঙ্গ বা স্ক্রিনশট।
```

### 🏆 অবদানকারী স্বীকৃতি

আমরা সব অবদানকারীদের কৃতজ্ঞতা জানাই:

- **কোর ডেভেলপার**: [@yourusername](https://github.com/yourusername)
- **ইসলামিক কন্টেন্ট রিভিউয়ার**: [@scholar1](https://github.com/scholar1)
- **UI/UX ডিজাইনার**: [@designer1](https://github.com/designer1)
- **টেস্টার**: [@tester1](https://github.com/tester1)

### 📋 রোডম্যাপ

**আসন্ন ফিচারসমূহ:**
- [ ] ভয়েস ইনপুট ও আউটপুট
- [ ] মোবাইল অ্যাপ (React Native)
- [ ] অফলাইন মোড
- [ ] আরো ভাষার সাপোর্ট (উর্দু, আরবি, ইংরেজি)
- [ ] ইসলামিক ক্যালেন্ডার ইন্টিগ্রেশন
- [ ] কিবলা দিক নির্দেশনা
- [ ] নামাজের সময়সূচী
- [ ] তাসবিহ কাউন্টার

---

## 📄 লাইসেন্স | License

এই প্রকল্পটি MIT লাইসেন্সের অধীনে লাইসেন্সকৃত। বিস্তারিত জানতে [LICENSE](LICENSE) ফাইল দেখুন।

```
MIT License

Copyright (c) 2025 Islamic AI Chatbot Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 সাপোর্ট | Support

### 🤝 কমিউনিটি সাপোর্ট

- **GitHub Issues**: [প্রকল্পের ইস্যু ট্র্যাকার](https://github.com/yourusername/islamic-ai-chatbot/issues)
- **Discussions**: [কমিউনিটি আলোচনা](https://github.com/yourusername/islamic-ai-chatbot/discussions)
- **Discord**: [আমাদের Discord সার্ভার](https://discord.gg/islamic-ai-chatbot)
- **Telegram**: [টেলিগ্রাম গ্রুপ](https://t.me/islamic_ai_chatbot)

### 📧 যোগাযোগ

- **ইমেইল**: support@islamic-ai-chatbot.com
- **ওয়েবসাইট**: https://islamic-ai-chatbot.com
- **টুইটার**: [@IslamicAIChatbot](https://twitter.com/IslamicAIChatbot)

### 🆘 জরুরি সাপোর্ট

নিরাপত্তা সংক্রান্ত সমস্যার জন্য: security@islamic-ai-chatbot.com

### 💝 ডোনেশন

এই প্রকল্পটি সম্পূর্ণ ফ্রি ও ওপেন সোর্স। আপনি চাইলে আমাদের সাহায্য করতে পারেন:

- **GitHub Sponsors**: [আমাদের স্পন্সর করুন](https://github.com/sponsors/yourusername)
- **PayPal**: [PayPal দিয়ে দান করুন](https://paypal.me/islamicaichatbot)
- **Bitcoin**: `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`

---

<div align="center">

**🌙 আল্লাহ তাআলা আমাদের এই প্রচেষ্টা কবুল করুন এবং উম্মাহর কল্যাণে কাজে লাগান। আমিন। 🤲**

---

[![GitHub stars](https://img.shields.io/github/stars/yourusername/islamic-ai-chatbot?style=social)](https://github.com/yourusername/islamic-ai-chatbot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/islamic-ai-chatbot?style=social)](https://github.com/yourusername/islamic-ai-chatbot/network/members)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/islamic-ai-chatbot)](https://github.com/yourusername/islamic-ai-chatbot/issues)
[![GitHub license](https://img.shields.io/github/license/yourusername/islamic-ai-chatbot)](https://github.com/yourusername/islamic-ai-chatbot/blob/main/LICENSE)

**Made with ❤️ for the Muslim Ummah**

</div>

