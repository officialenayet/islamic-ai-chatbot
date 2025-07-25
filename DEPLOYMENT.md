# 🚀 ইসলামিক AI চ্যাটবট ডিপ্লয়মেন্ট গাইড

এই গাইডে আপনি শিখবেন কিভাবে ইসলামিক AI চ্যাটবট বিভিন্ন প্ল্যাটফর্মে ডিপ্লয় করতে হয়।

## 📋 সূচিপত্র

- [🌐 GitHub Pages ডিপ্লয়মেন্ট](#-github-pages-ডিপ্লয়মেন্ট)
- [🔥 Firebase ডিপ্লয়মেন্ট](#-firebase-ডিপ্লয়মেন্ট)
- [⚡ Vercel ডিপ্লয়মেন্ট](#-vercel-ডিপ্লয়মেন্ট)
- [🌊 Netlify ডিপ্লয়মেন্ট](#-netlify-ডিপ্লয়মেন্ট)
- [🐳 Docker ডিপ্লয়মেন্ট](#-docker-ডিপ্লয়মেন্ট)
- [☁️ AWS ডিপ্লয়মেন্ট](#️-aws-ডিপ্লয়মেন্ট)
- [🔧 কনফিগারেশন](#-কনফিগারেশন)

## 🌐 GitHub Pages ডিপ্লয়মেন্ট

GitHub Pages এ ফ্রি হোস্টিংয়ের জন্য:

### ধাপ ১: রিপোজিটরি প্রস্তুতি

```bash
# আপনার GitHub রিপোজিটরিতে কোড পুশ করুন
git add .
git commit -m "Initial commit for deployment"
git push origin main
```

### ধাপ ২: GitHub Actions সেটআপ

`.github/workflows/deploy.yml` ফাইল তৈরি করুন:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  pull_request:
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
        
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        
    - name: Install Backend Dependencies
      run: |
        cd islamic-chatbot-api
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        
    - name: Install Frontend Dependencies
      run: |
        cd islamic-chatbot-frontend
        npm ci
        
    - name: Build Frontend
      run: |
        cd islamic-chatbot-frontend
        npm run build
        
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./islamic-chatbot-frontend/dist
```

### ধাপ ৩: GitHub Pages সক্রিয় করুন

1. GitHub রিপোজিটরিতে যান
2. Settings > Pages এ যান
3. Source: "Deploy from a branch" নির্বাচন করুন
4. Branch: "gh-pages" নির্বাচন করুন
5. Save করুন

## 🔥 Firebase ডিপ্লয়মেন্ট

### ধাপ ১: Firebase CLI ইনস্টল

```bash
npm install -g firebase-tools
firebase login
```

### ধাপ ২: Firebase প্রকল্প তৈরি

```bash
# নতুন Firebase প্রকল্প তৈরি করুন
firebase init

# নিম্নলিখিত অপশন নির্বাচন করুন:
# - Hosting: Configure files for Firebase Hosting
# - Functions: Configure a Cloud Functions directory
# - Firestore: Configure security rules and indexes files
```

### ধাপ ৩: firebase.json কনফিগারেশন

```json
{
  "hosting": {
    "public": "islamic-chatbot-frontend/dist",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  },
  "functions": {
    "source": "islamic-chatbot-api",
    "runtime": "python311"
  },
  "firestore": {
    "rules": "firestore.rules",
    "indexes": "firestore.indexes.json"
  }
}
```

### ধাপ ৪: ডিপ্লয় করুন

```bash
# ফ্রন্টএন্ড বিল্ড করুন
cd islamic-chatbot-frontend
npm run build
cd ..

# Firebase এ ডিপ্লয় করুন
firebase deploy
```

## ⚡ Vercel ডিপ্লয়মেন্ট

### ধাপ ১: Vercel CLI ইনস্টল

```bash
npm install -g vercel
vercel login
```

### ধাপ ২: ফ্রন্টএন্ড ডিপ্লয়

```bash
cd islamic-chatbot-frontend

# Vercel এ ডিপ্লয় করুন
vercel --prod

# কাস্টম ডোমেইন যোগ করুন (ঐচ্ছিক)
vercel domains add yourdomain.com
```

### ধাপ ৩: ব্যাকএন্ড ডিপ্লয় (Vercel Functions)

`islamic-chatbot-api/vercel.json` তৈরি করুন:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "src/main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "src/main.py"
    }
  ],
  "env": {
    "OPENAI_API_KEY": "@openai_api_key",
    "FLASK_SECRET_KEY": "@flask_secret_key"
  }
}
```

## 🌊 Netlify ডিপ্লয়মেন্ট

### ধাপ ১: Netlify CLI ইনস্টল

```bash
npm install -g netlify-cli
netlify login
```

### ধাপ ২: netlify.toml কনফিগারেশন

```toml
[build]
  base = "islamic-chatbot-frontend"
  publish = "dist"
  command = "npm run build"

[build.environment]
  NODE_VERSION = "18"

[[redirects]]
  from = "/api/*"
  to = "https://your-backend-url.herokuapp.com/api/:splat"
  status = 200
  force = true

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### ধাপ ৩: ডিপ্লয় করুন

```bash
# ফ্রন্টএন্ড ডিপ্লয় করুন
cd islamic-chatbot-frontend
netlify deploy --prod
```

## 🐳 Docker ডিপ্লয়মেন্ট

### ব্যাকএন্ড Dockerfile

`islamic-chatbot-api/Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# সিস্টেম ডিপেন্ডেন্সি ইনস্টল
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python ডিপেন্ডেন্সি ইনস্টল
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# অ্যাপ্লিকেশন কপি করুন
COPY . .

# ডেটাবেস ইনিশিয়ালাইজ করুন
RUN python src/enhanced_data.py

EXPOSE 5000

# Gunicorn দিয়ে অ্যাপ চালান
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "src.main:app"]
```

### ফ্রন্টএন্ড Dockerfile

`islamic-chatbot-frontend/Dockerfile`:

```dockerfile
# Build stage
FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Docker Compose

`docker-compose.yml`:

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
      - JWT_SECRET_KEY=${JWT_SECRET_KEY}
    volumes:
      - ./data:/app/data
    restart: unless-stopped

  frontend:
    build: ./islamic-chatbot-frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    restart: unless-stopped

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    restart: unless-stopped

volumes:
  data:
```

### ডিপ্লয় করুন

```bash
# Docker images বিল্ড ও রান করুন
docker-compose up -d

# লগ দেখুন
docker-compose logs -f

# স্টপ করুন
docker-compose down
```

## ☁️ AWS ডিপ্লয়মেন্ট

### EC2 ইনস্ট্যান্স সেটআপ

```bash
# EC2 ইনস্ট্যান্সে কানেক্ট করুন
ssh -i your-key.pem ubuntu@your-ec2-ip

# সিস্টেম আপডেট করুন
sudo apt update && sudo apt upgrade -y

# প্রয়োজনীয় সফটওয়্যার ইনস্টল করুন
sudo apt install -y python3 python3-pip nodejs npm nginx git

# Docker ইনস্টল করুন (ঐচ্ছিক)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
```

### অ্যাপ্লিকেশন ডিপ্লয়

```bash
# প্রকল্প ক্লোন করুন
git clone https://github.com/yourusername/islamic-ai-chatbot.git
cd islamic-ai-chatbot

# ব্যাকএন্ড সেটআপ
cd islamic-chatbot-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/enhanced_data.py

# ফ্রন্টএন্ড বিল্ড
cd ../islamic-chatbot-frontend
npm install
npm run build

# Nginx কনফিগারেশন
sudo cp nginx.conf /etc/nginx/sites-available/islamic-chatbot
sudo ln -s /etc/nginx/sites-available/islamic-chatbot /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```

### Systemd Service সেটআপ

`/etc/systemd/system/islamic-chatbot.service`:

```ini
[Unit]
Description=Islamic AI Chatbot Backend
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/islamic-ai-chatbot/islamic-chatbot-api
Environment=PATH=/home/ubuntu/islamic-ai-chatbot/islamic-chatbot-api/venv/bin
ExecStart=/home/ubuntu/islamic-ai-chatbot/islamic-chatbot-api/venv/bin/gunicorn --bind 127.0.0.1:5000 src.main:app
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Service সক্রিয় করুন
sudo systemctl daemon-reload
sudo systemctl enable islamic-chatbot
sudo systemctl start islamic-chatbot
sudo systemctl status islamic-chatbot
```

## 🔧 কনফিগারেশন

### পরিবেশ ভেরিয়েবল

প্রোডাকশনের জন্য `.env` ফাইল:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_production_openai_key
OPENAI_API_BASE=https://api.openai.com/v1

# Flask Configuration
FLASK_ENV=production
FLASK_SECRET_KEY=your_very_secure_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
JWT_ACCESS_TOKEN_EXPIRES=3600

# Database Configuration
DATABASE_URL=sqlite:///islamic_data.db

# Security
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
RATE_LIMIT_PER_MINUTE=60

# Monitoring
SENTRY_DSN=your_sentry_dsn
LOG_LEVEL=INFO
```

### SSL সার্টিফিকেট

```bash
# Let's Encrypt SSL সার্টিফিকেট
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal সেটআপ
sudo crontab -e
# নিম্নলিখিত লাইন যোগ করুন:
# 0 12 * * * /usr/bin/certbot renew --quiet
```

### Nginx কনফিগারেশন

`nginx.conf`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    # Frontend
    location / {
        root /home/ubuntu/islamic-ai-chatbot/islamic-chatbot-frontend/dist;
        try_files $uri $uri/ /index.html;
        
        # Cache static assets
        location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
            expires 1y;
            add_header Cache-Control "public, immutable";
        }
    }

    # Backend API
    location /api/ {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;
}
```

### ডেটাবেস ব্যাকআপ

```bash
#!/bin/bash
# backup.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/home/ubuntu/backups"
DB_PATH="/home/ubuntu/islamic-ai-chatbot/islamic-chatbot-api/islamic_comprehensive.db"

mkdir -p $BACKUP_DIR

# ডেটাবেস ব্যাকআপ
cp $DB_PATH "$BACKUP_DIR/islamic_db_backup_$DATE.db"

# পুরানো ব্যাকআপ মুছে ফেলুন (৭ দিনের বেশি পুরানো)
find $BACKUP_DIR -name "islamic_db_backup_*.db" -mtime +7 -delete

echo "ব্যাকআপ সম্পন্ন: islamic_db_backup_$DATE.db"
```

```bash
# ক্রন জব সেটআপ (দৈনিক ব্যাকআপ)
crontab -e
# যোগ করুন: 0 2 * * * /home/ubuntu/backup.sh
```

### মনিটরিং সেটআপ

```bash
# PM2 ইনস্টল (প্রসেস ম্যানেজমেন্টের জন্য)
npm install -g pm2

# অ্যাপ্লিকেশন চালান
pm2 start ecosystem.config.js

# PM2 স্টার্টআপ সেটআপ
pm2 startup
pm2 save
```

`ecosystem.config.js`:

```javascript
module.exports = {
  apps: [{
    name: 'islamic-chatbot-backend',
    script: 'venv/bin/gunicorn',
    args: '--bind 127.0.0.1:5000 --workers 4 src.main:app',
    cwd: '/home/ubuntu/islamic-ai-chatbot/islamic-chatbot-api',
    env: {
      NODE_ENV: 'production',
      FLASK_ENV: 'production'
    },
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    log_file: './logs/combined.log',
    time: true
  }]
};
```

এই গাইড অনুসরণ করে আপনি সফলভাবে ইসলামিক AI চ্যাটবট বিভিন্ন প্ল্যাটফর্মে ডিপ্লয় করতে পারবেন। কোনো সমস্যা হলে GitHub Issues এ জানান।

