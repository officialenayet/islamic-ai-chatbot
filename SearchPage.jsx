import { useState, useEffect } from 'react'
import { useSearchParams } from 'react-router-dom'
import { Search, Filter, Book, FileText, HelpCircle, Copy, Bookmark } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Card, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { useAuth } from '@/hooks/useAuth'

export default function SearchPage() {
  const { API_BASE_URL, getAuthHeaders } = useAuth()
  const [searchParams, setSearchParams] = useSearchParams()
  const [searchQuery, setSearchQuery] = useState(searchParams.get('q') || '')
  const [activeTab, setActiveTab] = useState('all')
  const [loading, setLoading] = useState(false)
  const [results, setResults] = useState({
    verses: [],
    hadith: [],
    fatwa: []
  })

  useEffect(() => {
    const query = searchParams.get('q')
    if (query) {
      setSearchQuery(query)
      performSearch(query)
    }
  }, [searchParams])

  const performSearch = async (query) => {
    if (!query.trim()) return

    setLoading(true)
    try {
      // Search in parallel
      const [versesRes, hadithRes, fatwaRes] = await Promise.all([
        fetch(`${API_BASE_URL}/quran/search?q=${encodeURIComponent(query)}&language=bn`),
        fetch(`${API_BASE_URL}/hadith/search?q=${encodeURIComponent(query)}&language=bn`),
        fetch(`${API_BASE_URL}/fatwa/search?q=${encodeURIComponent(query)}&language=bn`)
      ])

      const [versesData, hadithData, fatwaData] = await Promise.all([
        versesRes.json(),
        hadithRes.json(),
        fatwaRes.json()
      ])

      setResults({
        verses: versesData.success ? versesData.data.results : [],
        hadith: hadithData.success ? hadithData.data.results : [],
        fatwa: fatwaData.success ? fatwaData.data.results : []
      })
    } catch (error) {
      console.error('Search error:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleSearch = (e) => {
    e.preventDefault()
    if (searchQuery.trim()) {
      setSearchParams({ q: searchQuery.trim() })
    }
  }

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text)
  }

  const addBookmark = async (contentType, contentId) => {
    try {
      const response = await fetch(`${API_BASE_URL}/user/bookmarks`, {
        method: 'POST',
        headers: {
          ...getAuthHeaders(),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          content_type: contentType,
          content_id: contentId
        })
      })

      if (response.ok) {
        // Could show success message
      }
    } catch (error) {
      console.error('Failed to add bookmark:', error)
    }
  }

  const renderVerseResult = (verse) => (
    <Card key={verse.id} className="border-emerald-200 hover:shadow-md transition-shadow">
      <CardContent className="p-6">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center space-x-2">
            <Badge className="bg-blue-100 text-blue-700">আয়াত</Badge>
            <span className="text-sm text-emerald-600">
              {verse.surah_name} - {verse.surah_number}:{verse.verse_number}
            </span>
          </div>
          <div className="flex items-center space-x-1">
            <Button
              variant="ghost"
              size="sm"
              onClick={() => copyToClipboard(verse.bengali_translation)}
              className="text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
            >
              <Copy className="h-4 w-4" />
            </Button>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => addBookmark('verse', verse.id)}
              className="text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
            >
              <Bookmark className="h-4 w-4" />
            </Button>
          </div>
        </div>
        
        {verse.arabic_text && (
          <p className="text-right text-lg text-emerald-900 font-arabic leading-relaxed mb-3">
            {verse.arabic_text}
          </p>
        )}
        
        <p className="text-gray-700 mb-2">{verse.bengali_translation}</p>
        
        {verse.transliteration && (
          <p className="text-sm text-emerald-600 italic">{verse.transliteration}</p>
        )}
      </CardContent>
    </Card>
  )

  const renderHadithResult = (hadith) => (
    <Card key={hadith.id} className="border-emerald-200 hover:shadow-md transition-shadow">
      <CardContent className="p-6">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center space-x-2">
            <Badge className="bg-green-100 text-green-700">হাদিস</Badge>
            <span className="text-sm text-emerald-600">
              {hadith.book_name} - {hadith.hadith_number}
            </span>
          </div>
          <div className="flex items-center space-x-1">
            <Button
              variant="ghost"
              size="sm"
              onClick={() => copyToClipboard(hadith.bengali_translation)}
              className="text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
            >
              <Copy className="h-4 w-4" />
            </Button>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => addBookmark('hadith', hadith.id)}
              className="text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
            >
              <Bookmark className="h-4 w-4" />
            </Button>
          </div>
        </div>
        
        {hadith.arabic_text && (
          <p className="text-right text-lg text-emerald-900 font-arabic leading-relaxed mb-3">
            {hadith.arabic_text}
          </p>
        )}
        
        <p className="text-gray-700 mb-3">{hadith.bengali_translation}</p>
        
        <div className="flex items-center space-x-4 text-sm text-emerald-600">
          {hadith.narrator && <span>বর্ণনাকারী: {hadith.narrator}</span>}
          {hadith.grade && <span>গ্রেড: {hadith.grade}</span>}
        </div>
      </CardContent>
    </Card>
  )

  const renderFatwaResult = (fatwa) => (
    <Card key={fatwa.id} className="border-emerald-200 hover:shadow-md transition-shadow">
      <CardContent className="p-6">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center space-x-2">
            <Badge className="bg-purple-100 text-purple-700">ফতোয়া</Badge>
            <span className="text-sm text-emerald-600">
              {fatwa.scholar_name}
            </span>
          </div>
          <div className="flex items-center space-x-1">
            <Button
              variant="ghost"
              size="sm"
              onClick={() => copyToClipboard(`প্রশ্ন: ${fatwa.question}\n\nউত্তর: ${fatwa.answer}`)}
              className="text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
            >
              <Copy className="h-4 w-4" />
            </Button>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => addBookmark('fatwa', fatwa.id)}
              className="text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
            >
              <Bookmark className="h-4 w-4" />
            </Button>
          </div>
        </div>
        
        <div className="space-y-3">
          <div>
            <h4 className="text-sm font-medium text-emerald-700 mb-1">প্রশ্ন:</h4>
            <p className="text-gray-700 text-sm">{fatwa.question}</p>
          </div>
          <div>
            <h4 className="text-sm font-medium text-emerald-700 mb-1">উত্তর:</h4>
            <p className="text-gray-700 text-sm">
              {fatwa.answer.length > 300 
                ? fatwa.answer.substring(0, 300) + '...' 
                : fatwa.answer}
            </p>
          </div>
        </div>
      </CardContent>
    </Card>
  )

  const getTotalResults = () => {
    return results.verses.length + results.hadith.length + results.fatwa.length
  }

  const getAllResults = () => {
    return [
      ...results.verses.map(v => ({ ...v, type: 'verse' })),
      ...results.hadith.map(h => ({ ...h, type: 'hadith' })),
      ...results.fatwa.map(f => ({ ...f, type: 'fatwa' }))
    ]
  }

  return (
    <div className="max-w-6xl mx-auto p-6">
      {/* Header */}
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-emerald-800 mb-2">ইসলামিক অনুসন্ধান</h1>
        <p className="text-emerald-600">কোরআন, হাদিস ও ফতোয়া খুঁজুন</p>
      </div>

      {/* Search Form */}
      <form onSubmit={handleSearch} className="mb-6">
        <div className="flex space-x-2">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-emerald-500" />
            <Input
              placeholder="আপনার অনুসন্ধান লিখুন..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-10 border-emerald-200 focus:border-emerald-500"
            />
          </div>
          <Button
            type="submit"
            disabled={loading}
            className="bg-emerald-600 hover:bg-emerald-700"
          >
            {loading ? 'খুঁজছি...' : 'খুঁজুন'}
          </Button>
        </div>
      </form>

      {/* Results */}
      {searchQuery && (
        <div>
          <div className="mb-4">
            <p className="text-emerald-600">
              "{searchQuery}" এর জন্য {getTotalResults()} টি ফলাফল পাওয়া গেছে
            </p>
          </div>

          <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
            <TabsList className="grid w-full grid-cols-4 mb-6">
              <TabsTrigger value="all" className="data-[state=active]:bg-emerald-100 data-[state=active]:text-emerald-800">
                সব ({getTotalResults()})
              </TabsTrigger>
              <TabsTrigger value="verses" className="data-[state=active]:bg-emerald-100 data-[state=active]:text-emerald-800">
                <Book className="h-4 w-4 mr-1" />
                আয়াত ({results.verses.length})
              </TabsTrigger>
              <TabsTrigger value="hadith" className="data-[state=active]:bg-emerald-100 data-[state=active]:text-emerald-800">
                <FileText className="h-4 w-4 mr-1" />
                হাদিস ({results.hadith.length})
              </TabsTrigger>
              <TabsTrigger value="fatwa" className="data-[state=active]:bg-emerald-100 data-[state=active]:text-emerald-800">
                <HelpCircle className="h-4 w-4 mr-1" />
                ফতোয়া ({results.fatwa.length})
              </TabsTrigger>
            </TabsList>

            <TabsContent value="all" className="space-y-4">
              {loading ? (
                <div className="text-center py-12">
                  <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-emerald-600 mx-auto mb-4"></div>
                  <p className="text-emerald-600">অনুসন্ধান করা হচ্ছে...</p>
                </div>
              ) : getTotalResults() === 0 ? (
                <div className="text-center py-12">
                  <Search className="h-16 w-16 text-emerald-300 mx-auto mb-4" />
                  <h3 className="text-lg font-medium text-emerald-800 mb-2">কোন ফলাফল পাওয়া যায়নি</h3>
                  <p className="text-emerald-600">অন্য কিছু খুঁজে দেখুন</p>
                </div>
              ) : (
                <div className="space-y-4">
                  {getAllResults().map((result) => {
                    if (result.type === 'verse') return renderVerseResult(result)
                    if (result.type === 'hadith') return renderHadithResult(result)
                    if (result.type === 'fatwa') return renderFatwaResult(result)
                    return null
                  })}
                </div>
              )}
            </TabsContent>

            <TabsContent value="verses" className="space-y-4">
              {results.verses.length === 0 ? (
                <div className="text-center py-12">
                  <Book className="h-16 w-16 text-emerald-300 mx-auto mb-4" />
                  <h3 className="text-lg font-medium text-emerald-800 mb-2">কোন আয়াত পাওয়া যায়নি</h3>
                  <p className="text-emerald-600">অন্য কিছু খুঁজে দেখুন</p>
                </div>
              ) : (
                results.verses.map(renderVerseResult)
              )}
            </TabsContent>

            <TabsContent value="hadith" className="space-y-4">
              {results.hadith.length === 0 ? (
                <div className="text-center py-12">
                  <FileText className="h-16 w-16 text-emerald-300 mx-auto mb-4" />
                  <h3 className="text-lg font-medium text-emerald-800 mb-2">কোন হাদিস পাওয়া যায়নি</h3>
                  <p className="text-emerald-600">অন্য কিছু খুঁজে দেখুন</p>
                </div>
              ) : (
                results.hadith.map(renderHadithResult)
              )}
            </TabsContent>

            <TabsContent value="fatwa" className="space-y-4">
              {results.fatwa.length === 0 ? (
                <div className="text-center py-12">
                  <HelpCircle className="h-16 w-16 text-emerald-300 mx-auto mb-4" />
                  <h3 className="text-lg font-medium text-emerald-800 mb-2">কোন ফতোয়া পাওয়া যায়নি</h3>
                  <p className="text-emerald-600">অন্য কিছু খুঁজে দেখুন</p>
                </div>
              ) : (
                results.fatwa.map(renderFatwaResult)
              )}
            </TabsContent>
          </Tabs>
        </div>
      )}

      {/* Popular Searches */}
      {!searchQuery && (
        <div className="mt-12">
          <h2 className="text-lg font-semibold text-emerald-800 mb-4">জনপ্রিয় অনুসন্ধান</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {[
              'নামাজের নিয়ম',
              'রমজানের ফজিলত',
              'যাকাতের নিসাব',
              'হজের নিয়ম',
              'দোয়া কবুলের সময়',
              'তাওবার নিয়ম'
            ].map((query) => (
              <Card
                key={query}
                className="border-emerald-200 hover:border-emerald-300 cursor-pointer transition-colors"
                onClick={() => {
                  setSearchQuery(query)
                  setSearchParams({ q: query })
                }}
              >
                <CardContent className="p-4">
                  <p className="text-emerald-700 font-medium">{query}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

