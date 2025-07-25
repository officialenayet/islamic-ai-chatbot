# 🤝 অবদান গাইডলাইন | Contributing Guidelines

ইসলামিক AI চ্যাটবট প্রকল্পে আপনার অবদানকে স্বাগত জানাই! এই গাইড আপনাকে সাহায্য করবে কিভাবে কার্যকরভাবে এই প্রকল্পে অবদান রাখতে হয়।

## 📋 সূচিপত্র

- [🎯 অবদানের ধরন](#-অবদানের-ধরন)
- [🔄 কন্ট্রিবিউশন ওয়ার্কফ্লো](#-কন্ট্রিবিউশন-ওয়ার্কফ্লো)
- [📝 কোডিং স্ট্যান্ডার্ড](#-কোডিং-স্ট্যান্ডার্ড)
- [🧪 টেস্টিং গাইডলাইন](#-টেস্টিং-গাইডলাইন)
- [🐛 বাগ রিপোর্ট](#-বাগ-রিপোর্ট)
- [💡 ফিচার রিকোয়েস্ট](#-ফিচার-রিকোয়েস্ট)
- [📚 ডকুমেন্টেশন](#-ডকুমেন্টেশন)
- [🌍 অনুবাদ](#-অনুবাদ)
- [🎨 ডিজাইন](#-ডিজাইন)

## 🎯 অবদানের ধরন

### 💻 কোড অবদান
- নতুন ফিচার যোগ করা
- বাগ ফিক্স করা
- পারফরমেন্স উন্নতি
- কোড রিফ্যাক্টরিং
- টেস্ট কেস লেখা

### 📖 ইসলামিক কন্টেন্ট
- কুরআনের আয়াত যাচাইকরণ
- হাদিসের সত্যতা যাচাই
- ফতোয়া রিভিউ
- তাফসীর ও ব্যাখ্যা যোগ করা
- আরবি টেক্সট সংশোধন

### 🎨 ডিজাইন ও UI/UX
- ইন্টারফেস ডিজাইন উন্নতি
- মোবাইল রেসপনসিভনেস
- অ্যাক্সেসিবিলিটি উন্নতি
- আইকন ও গ্রাফিক্স ডিজাইন

### 📚 ডকুমেন্টেশন
- README আপডেট
- API ডকুমেন্টেশন
- টিউটোরিয়াল লেখা
- কোড কমেন্ট উন্নতি

### 🌍 স্থানীয়করণ
- নতুন ভাষার সাপোর্ট
- অনুবাদ উন্নতি
- স্থানীয় সংস্কৃতির সাথে মানানসই করা

## 🔄 কন্ট্রিবিউশন ওয়ার্কফ্লো

### ধাপ ১: প্রকল্প ফর্ক করুন

```bash
# GitHub এ প্রকল্পটি ফর্ক করুন
# তারপর আপনার লোকাল মেশিনে ক্লোন করুন
git clone https://github.com/yourusername/islamic-ai-chatbot.git
cd islamic-ai-chatbot

# অরিজিনাল রিপোজিটরি যোগ করুন
git remote add upstream https://github.com/originalusername/islamic-ai-chatbot.git
```

### ধাপ ২: ডেভেলপমেন্ট এনভায়রনমেন্ট সেটআপ

```bash
# ব্যাকএন্ড সেটআপ
cd islamic-chatbot-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # ডেভেলপমেন্ট ডিপেন্ডেন্সি

# ফ্রন্টএন্ড সেটআপ
cd ../islamic-chatbot-frontend
npm install

# প্রি-কমিট হুক সেটআপ
cd ..
pip install pre-commit
pre-commit install
```

### ধাপ ৩: নতুন ব্রাঞ্চ তৈরি

```bash
# মেইন ব্রাঞ্চ আপডেট করুন
git checkout main
git pull upstream main

# নতুন ফিচার ব্রাঞ্চ তৈরি করুন
git checkout -b feature/your-feature-name

# অথবা বাগ ফিক্সের জন্য
git checkout -b bugfix/issue-number-description
```

### ধাপ ৪: পরিবর্তন করুন

```bash
# আপনার কোড লিখুন
# টেস্ট চালান
# কমিট করুন

git add .
git commit -m "Add: নতুন ইসলামিক ফিচার যোগ করা হয়েছে

- কুরআন সার্চ ফিচার উন্নত করা হয়েছে
- হাদিস ফিল্টারিং যোগ করা হয়েছে
- UI/UX উন্নতি করা হয়েছে

Closes #123"
```

### ধাপ ৫: পুল রিকোয়েস্ট তৈরি

```bash
# আপনার ফর্কে পুশ করুন
git push origin feature/your-feature-name

# GitHub এ গিয়ে Pull Request তৈরি করুন
```

## 📝 কোডিং স্ট্যান্ডার্ড

### 🐍 Python (ব্যাকএন্ড)

#### কোড স্টাইল
```python
# PEP 8 অনুসরণ করুন
# Black formatter ব্যবহার করুন
# Type hints ব্যবহার করুন

from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

def get_quran_verse(
    surah_number: int, 
    ayah_number: int,
    language: str = 'bn'
) -> Optional[Dict[str, str]]:
    """
    কুরআনের নির্দিষ্ট আয়াত পুনরুদ্ধার করে।
    
    Args:
        surah_number: সূরা নম্বর (১-১১৪)
        ayah_number: আয়াত নম্বর
        language: ভাষা কোড (bn/ar/en)
    
    Returns:
        আয়াতের তথ্য সহ ডিকশনারি অথবা None
        
    Raises:
        ValueError: অবৈধ সূরা বা আয়াত নম্বরের জন্য
    """
    if not (1 <= surah_number <= 114):
        raise ValueError(f"অবৈধ সূরা নম্বর: {surah_number}")
    
    try:
        # Implementation here
        logger.info(f"আয়াত পুনরুদ্ধার: সূরা {surah_number}, আয়াত {ayah_number}")
        return {"arabic": "...", "bengali": "...", "reference": "..."}
    except Exception as e:
        logger.error(f"আয়াত পুনরুদ্ধারে ত্রুটি: {e}")
        return None
```

#### ডেটাবেস মডেল
```python
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class QuranVerse(Base):
    """কুরআনের আয়াত মডেল"""
    __tablename__ = 'quran_verses'
    
    id = Column(Integer, primary_key=True)
    surah_number = Column(Integer, nullable=False, index=True)
    ayah_number = Column(Integer, nullable=False)
    arabic_text = Column(Text, nullable=False)
    bengali_translation = Column(Text)
    english_translation = Column(Text)
    revelation_place = Column(String(20))  # মক্কা/মদিনা
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<QuranVerse(সূরা={self.surah_number}, আয়াত={self.ayah_number})>"
    
    def to_dict(self) -> Dict[str, Any]:
        """মডেলকে ডিকশনারিতে রূপান্তর"""
        return {
            'surah_number': self.surah_number,
            'ayah_number': self.ayah_number,
            'arabic_text': self.arabic_text,
            'bengali_translation': self.bengali_translation,
            'reference': f"সূরা {self.surah_number}, আয়াত {self.ayah_number}"
        }
```

### 🌐 JavaScript/React (ফ্রন্টএন্ড)

#### কোড স্টাইল
```javascript
// ESLint ও Prettier ব্যবহার করুন
// JSDoc কমেন্ট ব্যবহার করুন
// Modern ES6+ syntax ব্যবহার করুন

import React, { useState, useEffect, useCallback } from 'react';
import PropTypes from 'prop-types';

/**
 * ইসলামিক কন্টেন্ট সার্চ কম্পোনেন্ট
 * @param {Object} props - কম্পোনেন্ট props
 * @param {string} props.initialQuery - প্রাথমিক সার্চ কোয়েরি
 * @param {Function} props.onResults - রেজাল্ট কলব্যাক ফাংশন
 * @returns {JSX.Element} সার্চ কম্পোনেন্ট
 */
const IslamicSearch = ({ initialQuery = '', onResults }) => {
  const [query, setQuery] = useState(initialQuery);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  /**
   * ইসলামিক কন্টেন্ট সার্চ করে
   * @param {string} searchQuery - সার্চ কোয়েরি
   * @param {string} contentType - কন্টেন্ট টাইপ (quran/hadith/fatwa)
   */
  const searchContent = useCallback(async (searchQuery, contentType = 'all') => {
    if (!searchQuery.trim()) return;

    setLoading(true);
    setError(null);

    try {
      const response = await fetch('/api/v1/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify({
          query: searchQuery,
          type: contentType,
          language: 'bn'
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setResults(data.results);
      onResults?.(data.results);
    } catch (err) {
      setError('সার্চ করতে সমস্যা হয়েছে। আবার চেষ্টা করুন।');
      console.error('Search error:', err);
    } finally {
      setLoading(false);
    }
  }, [onResults]);

  useEffect(() => {
    if (initialQuery) {
      searchContent(initialQuery);
    }
  }, [initialQuery, searchContent]);

  return (
    <div className="islamic-search">
      <div className="search-input-container">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && searchContent(query)}
          placeholder="কুরআন, হাদিস বা ফতোয়া অনুসন্ধান করুন..."
          className="search-input"
          disabled={loading}
        />
        <button
          onClick={() => searchContent(query)}
          disabled={loading || !query.trim()}
          className="search-button"
        >
          {loading ? 'অনুসন্ধান করছে...' : 'অনুসন্ধান'}
        </button>
      </div>

      {error && (
        <div className="error-message" role="alert">
          {error}
        </div>
      )}

      {results.length > 0 && (
        <div className="search-results">
          {results.map((result, index) => (
            <SearchResultItem key={result.id || index} result={result} />
          ))}
        </div>
      )}
    </div>
  );
};

IslamicSearch.propTypes = {
  initialQuery: PropTypes.string,
  onResults: PropTypes.func
};

export default IslamicSearch;
```

#### কাস্টম হুক
```javascript
// hooks/useIslamicContent.js
import { useState, useEffect } from 'react';
import { useAuth } from './useAuth';

/**
 * ইসলামিক কন্টেন্ট ম্যানেজমেন্ট হুক
 * @returns {Object} কন্টেন্ট স্টেট ও ফাংশনসমূহ
 */
export const useIslamicContent = () => {
  const { token } = useAuth();
  const [content, setContent] = useState({
    quran: [],
    hadith: [],
    fatwa: []
  });
  const [loading, setLoading] = useState(false);

  const fetchContent = async (type, params = {}) => {
    setLoading(true);
    try {
      const queryString = new URLSearchParams(params).toString();
      const response = await fetch(`/api/v1/${type}?${queryString}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });

      const data = await response.json();
      setContent(prev => ({
        ...prev,
        [type]: data.results
      }));
    } catch (error) {
      console.error(`Error fetching ${type}:`, error);
    } finally {
      setLoading(false);
    }
  };

  return {
    content,
    loading,
    fetchQuran: (params) => fetchContent('quran', params),
    fetchHadith: (params) => fetchContent('hadith', params),
    fetchFatwa: (params) => fetchContent('fatwa', params)
  };
};
```

## 🧪 টেস্টিং গাইডলাইন

### Python টেস্ট

```python
# tests/test_quran_service.py
import pytest
from unittest.mock import Mock, patch
from src.services.quran_service import QuranService

class TestQuranService:
    """কুরআন সেবা টেস্ট ক্লাস"""
    
    def setup_method(self):
        """প্রতিটি টেস্টের আগে চালানো হয়"""
        self.quran_service = QuranService()
    
    def test_get_verse_valid_input(self):
        """বৈধ ইনপুটের জন্য আয়াত পুনরুদ্ধার টেস্ট"""
        result = self.quran_service.get_verse(2, 255)  # আয়াতুল কুরসি
        
        assert result is not None
        assert result['surah_number'] == 2
        assert result['ayah_number'] == 255
        assert 'arabic_text' in result
        assert 'bengali_translation' in result
    
    def test_get_verse_invalid_surah(self):
        """অবৈধ সূরা নম্বরের জন্য টেস্ট"""
        with pytest.raises(ValueError, match="অবৈধ সূরা নম্বর"):
            self.quran_service.get_verse(115, 1)  # ১১৪ এর বেশি
    
    @patch('src.services.quran_service.database')
    def test_search_verses(self, mock_db):
        """আয়াত অনুসন্ধান টেস্ট"""
        # Mock ডেটা
        mock_db.search.return_value = [
            {'surah_number': 2, 'ayah_number': 43, 'bengali_translation': 'নামাজ কায়েম কর'}
        ]
        
        results = self.quran_service.search_verses('নামাজ')
        
        assert len(results) > 0
        assert any('নামাজ' in result['bengali_translation'] for result in results)
        mock_db.search.assert_called_once_with('নামাজ')
```

### JavaScript টেস্ট

```javascript
// tests/components/IslamicSearch.test.js
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { rest } from 'msw';
import { setupServer } from 'msw/node';
import IslamicSearch from '../src/components/IslamicSearch';

// Mock API সার্ভার সেটআপ
const server = setupServer(
  rest.post('/api/v1/search', (req, res, ctx) => {
    return res(
      ctx.json({
        success: true,
        results: [
          {
            id: 1,
            type: 'quran',
            surah_number: 2,
            ayah_number: 255,
            bengali_translation: 'আল্লাহ ছাড়া কোনো ইলাহ নেই...'
          }
        ]
      })
    );
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

describe('IslamicSearch Component', () => {
  test('renders search input and button', () => {
    render(<IslamicSearch />);
    
    expect(screen.getByPlaceholderText(/কুরআন, হাদিস বা ফতোয়া অনুসন্ধান/)).toBeInTheDocument();
    expect(screen.getByText('অনুসন্ধান')).toBeInTheDocument();
  });

  test('performs search when button is clicked', async () => {
    const user = userEvent.setup();
    const mockOnResults = jest.fn();
    
    render(<IslamicSearch onResults={mockOnResults} />);
    
    const searchInput = screen.getByPlaceholderText(/কুরআন, হাদিস বা ফতোয়া অনুসন্ধান/);
    const searchButton = screen.getByText('অনুসন্ধান');
    
    await user.type(searchInput, 'আয়াতুল কুরসি');
    await user.click(searchButton);
    
    await waitFor(() => {
      expect(mockOnResults).toHaveBeenCalledWith(
        expect.arrayContaining([
          expect.objectContaining({
            type: 'quran',
            surah_number: 2,
            ayah_number: 255
          })
        ])
      );
    });
  });

  test('shows loading state during search', async () => {
    const user = userEvent.setup();
    
    render(<IslamicSearch />);
    
    const searchInput = screen.getByPlaceholderText(/কুরআন, হাদিস বা ফতোয়া অনুসন্ধান/);
    const searchButton = screen.getByText('অনুসন্ধান');
    
    await user.type(searchInput, 'নামাজ');
    await user.click(searchButton);
    
    expect(screen.getByText('অনুসন্ধান করছে...')).toBeInTheDocument();
  });
});
```

## 🐛 বাগ রিপোর্ট

### বাগ রিপোর্ট টেমপ্লেট

```markdown
---
name: 🐛 বাগ রিপোর্ট
about: একটি বাগ রিপোর্ট তৈরি করুন
title: '[BUG] সংক্ষিপ্ত বাগ বর্ণনা'
labels: bug
assignees: ''
---

## 🐛 বাগ বর্ণনা
সংক্ষেপে বাগটি কি তা বর্ণনা করুন।

## 🔄 পুনরুৎপাদনের ধাপ
1. '...' এ যান
2. '....' এ ক্লিক করুন
3. '....' পর্যন্ত স্ক্রল করুন
4. ত্রুটি দেখুন

## ✅ প্রত্যাশিত আচরণ
কি হওয়ার কথা ছিল তা বর্ণনা করুন।

## ❌ বাস্তব আচরণ
আসলে কি হয়েছে তা বর্ণনা করুন।

## 📸 স্ক্রিনশট
যদি প্রযোজ্য হয়, সমস্যা ব্যাখ্যা করতে স্ক্রিনশট যোগ করুন।

## 🖥️ পরিবেশ:
- **OS**: [e.g. Ubuntu 20.04, Windows 10, macOS Big Sur]
- **Browser**: [e.g. Chrome 91, Firefox 89, Safari 14]
- **Version**: [e.g. 1.0.0]
- **Device**: [e.g. Desktop, Mobile, Tablet]

## 📋 অতিরিক্ত প্রসঙ্গ
বাগ সম্পর্কে অন্য কোনো প্রসঙ্গ যোগ করুন।

## 🔍 লগ বা এরর মেসেজ
```
এখানে কোনো এরর মেসেজ বা লগ পেস্ট করুন
```

## ✅ চেকলিস্ট
- [ ] আমি existing issues চেক করেছি
- [ ] আমি latest version ব্যবহার করছি
- [ ] আমি documentation পড়েছি
- [ ] আমি বাগটি reproduce করতে পেরেছি
```

## 💡 ফিচার রিকোয়েস্ট

### ফিচার রিকোয়েস্ট টেমপ্লেট

```markdown
---
name: 💡 ফিচার রিকোয়েস্ট
about: এই প্রকল্পের জন্য একটি আইডিয়া প্রস্তাব করুন
title: '[FEATURE] নতুন ফিচারের নাম'
labels: enhancement
assignees: ''
---

## 💡 ফিচার বর্ণনা
আপনি যে ফিচারটি চান তার স্পষ্ট ও সংক্ষিপ্ত বর্ণনা।

## 🎯 সমস্যা
এই ফিচারটি কি সমস্যার সমাধান করবে? 
উদাহরণ: আমি সবসময় হতাশ হই যখন [...]

## 💭 প্রস্তাবিত সমাধান
আপনি যে সমাধান চান তার বর্ণনা।

## 🔄 বিকল্প সমাধান
আপনি যে বিকল্প সমাধানগুলো বিবেচনা করেছেন তার বর্ণনা।

## 📊 ব্যবহারকারী গল্প
একজন [ব্যবহারকারীর ধরন] হিসেবে, আমি [লক্ষ্য] চাই যাতে [কারণ]।

## 🎨 UI/UX মকআপ (ঐচ্ছিক)
যদি UI পরিবর্তন জড়িত থাকে, তাহলে mockup বা wireframe যোগ করুন।

## 🔧 প্রযুক্তিগত বিবেচনা
- কোন API বা লাইব্রেরি প্রয়োজন হতে পারে?
- পারফরমেন্সে কোনো প্রভাব আছে কি?
- ডেটাবেস পরিবর্তন প্রয়োজন কি?

## 📈 সাফল্যের মাপকাঠি
কিভাবে বুঝবেন যে এই ফিচার সফল হয়েছে?

## ✅ চেকলিস্ট
- [ ] আমি existing features চেক করেছি
- [ ] আমি roadmap দেখেছি
- [ ] এই ফিচার Islamic principles এর সাথে সামঞ্জস্যপূর্ণ
- [ ] আমি implementation complexity বিবেচনা করেছি
```

## 📚 ডকুমেন্টেশন

### ডকুমেন্টেশন স্ট্যান্ডার্ড

```markdown
# ফাংশন/ক্লাস ডকুমেন্টেশন

## উদ্দেশ্য
এই ফাংশন/ক্লাসের মূল উদ্দেশ্য কি?

## প্যারামিটার
- `param1` (string): প্যারামিটারের বর্ণনা
- `param2` (int, optional): ঐচ্ছিক প্যারামিটার, ডিফল্ট: 10

## রিটার্ন
- `dict`: রিটার্ন ভ্যালুর বর্ণনা

## উদাহরণ
```python
result = function_name("example", 20)
print(result)  # {'key': 'value'}
```

## এরর
- `ValueError`: কখন এই এরর হয়
- `TypeError`: কখন এই এরর হয়

## নোট
- গুরুত্বপূর্ণ তথ্য
- সীমাবদ্ধতা
- পারফরমেন্স বিবেচনা
```

## 🌍 অনুবাদ

### নতুন ভাষা যোগ করা

1. `locales/` ডিরেক্টরিতে নতুন ভাষার ফোল্ডার তৈরি করুন
2. `messages.json` ফাইল তৈরি করুন
3. সব টেক্সট অনুবাদ করুন
4. RTL ভাষার জন্য CSS আপডেট করুন

```json
// locales/ur/messages.json (উর্দুর জন্য)
{
  "app_title": "اسلامی AI چیٹ بوٹ",
  "search_placeholder": "قرآن، حدیث یا فتویٰ تلاش کریں...",
  "login": "لاگ ان",
  "register": "رجسٹر",
  "chat": "چیٹ",
  "bookmarks": "بک مارکس",
  "settings": "سیٹنگز"
}
```

### অনুবাদ গাইডলাইন

- **সঠিকতা**: ইসলামিক পরিভাষা সঠিকভাবে অনুবাদ করুন
- **সংস্কৃতি**: স্থানীয় সংস্কৃতির সাথে মানানসই করুন
- **সংক্ষিপ্ততা**: UI এর জন্য সংক্ষিপ্ত রাখুন
- **সামঞ্জস্য**: একই পরিভাষা সব জায়গায় ব্যবহার করুন

## 🎨 ডিজাইন

### ডিজাইন নীতিমালা

1. **ইসলামিক নন্দনতত্ত্ব**: ইসলামিক শিল্পকলার অনুপ্রেরণা
2. **সরলতা**: সহজ ও পরিষ্কার ইন্টারফেস
3. **অ্যাক্সেসিবিলিটি**: সবার জন্য ব্যবহারযোগ্য
4. **রেসপনসিভনেস**: সব ডিভাইসে কাজ করে

### কালার প্যালেট

```css
:root {
  /* Primary Colors */
  --islamic-green: #2E8B57;
  --islamic-gold: #DAA520;
  --islamic-blue: #4682B4;
  
  /* Neutral Colors */
  --text-primary: #2C3E50;
  --text-secondary: #7F8C8D;
  --background: #F8F9FA;
  --surface: #FFFFFF;
  
  /* Semantic Colors */
  --success: #27AE60;
  --warning: #F39C12;
  --error: #E74C3C;
  --info: #3498DB;
}
```

### টাইপোগ্রাফি

```css
/* ফন্ট স্ট্যাক */
.arabic-text {
  font-family: 'Amiri', 'Traditional Arabic', serif;
  font-size: 1.2em;
  line-height: 1.8;
  direction: rtl;
}

.bengali-text {
  font-family: 'Kalpurush', 'SolaimanLipi', sans-serif;
  font-size: 1em;
  line-height: 1.6;
}

.english-text {
  font-family: 'Inter', 'Roboto', sans-serif;
  font-size: 1em;
  line-height: 1.5;
}
```

### আইকন গাইডলাইন

- **স্টাইল**: Outline স্টাইল প্রাধান্য
- **সাইজ**: 16px, 24px, 32px, 48px
- **ফরম্যাট**: SVG (স্কেলেবল)
- **নামকরণ**: `icon-name-size.svg`

## 🏆 স্বীকৃতি

আপনার অবদানের জন্য আমরা নিম্নলিখিত উপায়ে স্বীকৃতি প্রদান করি:

- **Contributors.md**: সব অবদানকারীর তালিকা
- **Release Notes**: বড় অবদানের উল্লেখ
- **GitHub Profile**: Contributor badge
- **Social Media**: বিশেষ অবদানের প্রচার

## 📞 যোগাযোগ

অবদান সংক্রান্ত কোনো প্রশ্ন থাকলে:

- **GitHub Discussions**: [প্রকল্পের আলোচনা](https://github.com/yourusername/islamic-ai-chatbot/discussions)
- **Discord**: [আমাদের Discord সার্ভার](https://discord.gg/islamic-ai-chatbot)
- **ইমেইল**: contributors@islamic-ai-chatbot.com

---

**জাজাকাল্লাহু খাইরান** আপনার অবদানের জন্য! আল্লাহ তাআলা আমাদের এই প্রচেষ্টা কবুল করুন। 🤲

