# 🚀 গিটহাবে ইসলামিক AI চ্যাটবট হোস্ট করার সম্পূর্ণ গাইড

## 📋 ধাপে ধাপে গিটহাব সেটআপ

### ধাপ ১: গিটহাব রিপোজিটরি তৈরি করুন

1. **GitHub.com এ যান** এবং লগইন করুন
2. **"New repository"** বাটনে ক্লিক করুন
3. **Repository name**: `islamic-ai-chatbot` (বা আপনার পছন্দের নাম)
4. **Description**: `একটি সম্পূর্ণ AI-চালিত ইসলামিক চ্যাটবট - কুরআন, হাদিস ও ফতোয়ার রেফারেন্স সহ`
5. **Public** নির্বাচন করুন (ফ্রি হোস্টিংয়ের জন্য)
6. **"Create repository"** ক্লিক করুন

### ধাপ ২: লোকাল প্রজেক্ট গিটহাবে আপলোড করুন

```bash
# প্রজেক্ট ডিরেক্টরিতে যান
cd /home/ubuntu

# Git initialize করুন
git init

# সব ফাইল add করুন
git add .

# প্রথম commit করুন
git commit -m "Initial commit: Complete Islamic AI Chatbot

- Full-stack application with React frontend and Flask backend
- Comprehensive Islamic database (Quran, Hadith, Fatwa)
- AI-powered chat with OpenAI integration
- Modern UI/UX with Islamic design principles
- JWT authentication and user management
- Complete documentation and deployment guides"

# GitHub repository যুক্ত করুন (আপনার username দিয়ে replace করুন)
git remote add origin https://github.com/YOUR_USERNAME/islamic-ai-chatbot.git

# Main branch এ push করুন
git branch -M main
git push -u origin main
```

---

## 🔑 API Key ও Configuration সেটআপ

### ১. OpenAI API Key সেটআপ

#### ব্যাকএন্ড এ API Key সেটআপ:

**ফাইল**: `islamic-chatbot-api/.env`
```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
OPENAI_API_BASE=https://api.openai.com/v1

# Flask Configuration
FLASK_SECRET_KEY=your-very-secure-secret-key-here-minimum-32-characters
JWT_SECRET_KEY=your-jwt-secret-key-here-also-32-characters-minimum

# Database Configuration
DATABASE_URL=sqlite:///islamic_comprehensive.db

# Security Settings
CORS_ORIGINS=http://localhost:3000,http://localhost:5173,https://yourdomain.com
```

#### ফ্রন্টএন্ড এ API URL সেটআপ:

**ফাইল**: `islamic-chatbot-frontend/.env`
```env
# Backend API URL
VITE_API_BASE_URL=http://localhost:5000/api/v1
# প্রোডাকশনে: VITE_API_BASE_URL=https://your-backend-domain.com/api/v1

# App Configuration
VITE_APP_NAME=ইসলামিক AI চ্যাটবট
VITE_APP_VERSION=1.0.0
```

### ২. কোথায় কোথায় এডিট করতে হবে:

#### 🔧 ব্যাকএন্ড কনফিগারেশন:

**ফাইল**: `islamic-chatbot-api/src/main.py`
```python
# Line 15-20 এর কাছাকাছি
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'your-default-secret-key')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-default-jwt-key')

# Line 25-30 এর কাছাকাছি - CORS সেটআপ
CORS(app, origins=[
    "http://localhost:3000",
    "http://localhost:5173", 
    "https://yourdomain.com",  # আপনার ডোমেইন দিন
    "https://your-app.vercel.app"  # Vercel ডোমেইন দিন
])
```

**ফাইল**: `islamic-chatbot-api/src/routes/chat_enhanced.py`
```python
# Line 10-15 এর কাছাকাছি
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = os.getenv('OPENAI_API_BASE', 'https://api.openai.com/v1')
```

#### 🌐 ফ্রন্টএন্ড কনফিগারেশন:

**ফাইল**: `islamic-chatbot-frontend/src/hooks/useAuth.jsx`
```javascript
// Line 5-10 এর কাছাকাছি
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api/v1';
```

**ফাইল**: `islamic-chatbot-frontend/src/hooks/useChat.jsx`
```javascript
// Line 5-10 এর কাছাকাছি
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api/v1';
```

---

## 🌐 বিভিন্ন প্ল্যাটফর্মে হোস্টিং

### 🔥 **সবচেয়ে সহজ: Vercel (প্রস্তাবিত)**

#### ব্যাকএন্ড ডিপ্লয়মেন্ট:

1. **Vercel.com এ যান** এবং GitHub দিয়ে সাইন আপ করুন
2. **"New Project"** ক্লিক করুন
3. আপনার `islamic-ai-chatbot` repository select করুন
4. **Root Directory**: `islamic-chatbot-api` সেট করুন
5. **Environment Variables** যোগ করুন:
   ```
   OPENAI_API_KEY = sk-your-actual-key-here
   FLASK_SECRET_KEY = your-secret-key-here
   JWT_SECRET_KEY = your-jwt-key-here
   ```
6. **Deploy** ক্লিক করুন

#### ফ্রন্টএন্ড ডিপ্লয়মেন্ট:

1. আরেকটি **"New Project"** তৈরি করুন
2. একই repository select করুন
3. **Root Directory**: `islamic-chatbot-frontend` সেট করুন
4. **Environment Variables**:
   ```
   VITE_API_BASE_URL = https://your-backend-app.vercel.app/api/v1
   ```
5. **Deploy** ক্লিক করুন

### 🌊 **Netlify দিয়ে হোস্টিং**

#### ফ্রন্টএন্ড:
1. **Netlify.com এ যান**
2. **"New site from Git"** ক্লিক করুন
3. GitHub repository connect করুন
4. **Base directory**: `islamic-chatbot-frontend`
5. **Build command**: `npm run build`
6. **Publish directory**: `dist`
7. **Environment variables** সেট করুন
8. **Deploy** করুন

#### ব্যাকএন্ড:
- Netlify Functions ব্যবহার করুন অথবা
- Heroku/Railway এ ব্যাকএন্ড ডিপ্লয় করুন

### 🔥 **Firebase Hosting**

```bash
# Firebase CLI install করুন
npm install -g firebase-tools

# Firebase login করুন
firebase login

# প্রজেক্ট initialize করুন
firebase init

# Hosting select করুন
# Public directory: islamic-chatbot-frontend/dist
# Single-page app: Yes

# Build করুন
cd islamic-chatbot-frontend
npm run build

# Deploy করুন
firebase deploy
```

### 🐙 **GitHub Pages (শুধু ফ্রন্টএন্ড)**

**ফাইল**: `.github/workflows/deploy.yml`
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@v3
      
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        
    - name: Install and Build
      run: |
        cd islamic-chatbot-frontend
        npm ci
        npm run build
        
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./islamic-chatbot-frontend/dist
```

---

## 🔐 Environment Variables সেটআপ

### Vercel এ Environment Variables:

1. **Vercel Dashboard** এ যান
2. আপনার project select করুন
3. **Settings** > **Environment Variables**
4. নিম্নলিখিত variables যোগ করুন:

**ব্যাকএন্ড এর জন্য:**
```
OPENAI_API_KEY = sk-your-openai-api-key
FLASK_SECRET_KEY = your-flask-secret-key-32-chars-minimum
JWT_SECRET_KEY = your-jwt-secret-key-32-chars-minimum
DATABASE_URL = sqlite:///islamic_comprehensive.db
CORS_ORIGINS = https://your-frontend.vercel.app
```

**ফ্রন্টএন্ড এর জন্য:**
```
VITE_API_BASE_URL = https://your-backend.vercel.app/api/v1
VITE_APP_NAME = ইসলামিক AI চ্যাটবট
```

### Netlify এ Environment Variables:

1. **Netlify Dashboard** এ যান
2. **Site settings** > **Environment variables**
3. উপরের মতো same variables যোগ করুন

---

## 🌍 কাস্টম ডোমেইন সেটআপ

### Vercel এ কাস্টম ডোমেইন:

1. **Vercel Dashboard** > **Settings** > **Domains**
2. আপনার ডোমেইন নাম লিখুন (যেমন: `islamicai.com`)
3. DNS records আপডেট করুন:
   ```
   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   
   Type: A
   Name: @
   Value: 76.76.19.61
   ```

### Netlify এ কাস্টম ডোমেইন:

1. **Site settings** > **Domain management**
2. **Add custom domain**
3. DNS records সেট করুন:
   ```
   Type: CNAME
   Name: www
   Value: your-site-name.netlify.app
   
   Type: A
   Name: @
   Value: 75.2.60.5
   ```

---

## 🔧 প্রোডাকশন কনফিগারেশন চেকলিস্ট

### ✅ ব্যাকএন্ড:
- [ ] OpenAI API key সেট করা হয়েছে
- [ ] Flask secret key সেট করা হয়েছে
- [ ] JWT secret key সেট করা হয়েছে
- [ ] CORS origins আপডেট করা হয়েছে
- [ ] Database path সঠিক আছে
- [ ] Environment variables সব সেট আছে

### ✅ ফ্রন্টএন্ড:
- [ ] API base URL আপডেট করা হয়েছে
- [ ] Build command কাজ করছে
- [ ] Environment variables সেট আছে
- [ ] Routing সঠিকভাবে কাজ করছে

### ✅ ডোমেইন ও SSL:
- [ ] কাস্টম ডোমেইন যোগ করা হয়েছে
- [ ] SSL certificate সক্রিয় আছে
- [ ] DNS records সঠিক আছে
- [ ] HTTPS redirect সক্রিয় আছে

---

## 🚨 গুরুত্বপূর্ণ নোট

### 🔐 সিকিউরিটি:
- **কখনোই** `.env` ফাইল গিটহাবে push করবেন না
- API keys সবসময় environment variables এ রাখুন
- Strong secret keys ব্যবহার করুন (32+ characters)

### 💰 খরচ:
- **OpenAI API**: Pay-per-use (প্রতি request এর জন্য)
- **Vercel**: ফ্রি টায়ার যথেষ্ট
- **Netlify**: ফ্রি টায়ার যথেষ্ট
- **Domain**: বছরে $10-15 (ঐচ্ছিক)

### 🎯 পরবর্তী ধাপ:
1. প্রথমে localhost এ টেস্ট করুন
2. তারপর staging environment এ deploy করুন
3. সব কিছু ঠিক থাকলে production এ deploy করুন
4. Monitoring ও analytics সেটআপ করুন

---

## 📞 সাহায্য প্রয়োজন হলে:

- **GitHub Issues**: Repository তে issue তৈরি করুন
- **Documentation**: README.md ও DEPLOYMENT.md দেখুন
- **Community**: Discord/Telegram গ্রুপে যোগ দিন

**আল্লাহর সাহায্যে আপনার প্রজেক্ট সফল হোক! 🤲**

