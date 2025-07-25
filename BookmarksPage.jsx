import { useState, useEffect } from 'react'
import { Bookmark, Copy, Trash2, Search, Filter } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { ScrollArea } from '@/components/ui/scroll-area'
import { useAuth } from '@/hooks/useAuth'

export default function BookmarksPage() {
  const { API_BASE_URL, getAuthHeaders } = useAuth()
  const [bookmarks, setBookmarks] = useState([])
  const [loading, setLoading] = useState(true)
  const [searchQuery, setSearchQuery] = useState('')
  const [filterType, setFilterType] = useState('all')

  useEffect(() => {
    fetchBookmarks()
  }, [])

  const fetchBookmarks = async () => {
    try {
      setLoading(true)
      const response = await fetch(`${API_BASE_URL}/user/bookmarks`, {
        headers: getAuthHeaders()
      })

      if (response.ok) {
        const data = await response.json()
        if (data.success) {
          setBookmarks(data.data.bookmarks)
        }
      }
    } catch (error) {
      console.error('Failed to fetch bookmarks:', error)
    } finally {
      setLoading(false)
    }
  }

  const removeBookmark = async (bookmarkId) => {
    try {
      const response = await fetch(`${API_BASE_URL}/user/bookmarks/${bookmarkId}`, {
        method: 'DELETE',
        headers: getAuthHeaders()
      })

      if (response.ok) {
        setBookmarks(prev => prev.filter(b => b.id !== bookmarkId))
      }
    } catch (error) {
      console.error('Failed to remove bookmark:', error)
    }
  }

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text)
  }

  const getTypeLabel = (type) => {
    switch (type) {
      case 'verse': return 'আয়াত'
      case 'hadith': return 'হাদিস'
      case 'fatwa': return 'ফতোয়া'
      default: return type
    }
  }

  const getTypeBadgeColor = (type) => {
    switch (type) {
      case 'verse': return 'bg-blue-100 text-blue-700'
      case 'hadith': return 'bg-green-100 text-green-700'
      case 'fatwa': return 'bg-purple-100 text-purple-700'
      default: return 'bg-gray-100 text-gray-700'
    }
  }

  const filteredBookmarks = bookmarks.filter(bookmark => {
    const matchesSearch = !searchQuery || 
      (bookmark.content && JSON.stringify(bookmark.content).toLowerCase().includes(searchQuery.toLowerCase())) ||
      (bookmark.notes && bookmark.notes.toLowerCase().includes(searchQuery.toLowerCase()))
    
    const matchesFilter = filterType === 'all' || bookmark.content_type === filterType

    return matchesSearch && matchesFilter
  })

  const renderBookmarkContent = (bookmark) => {
    const content = bookmark.content
    if (!content) return null

    switch (bookmark.content_type) {
      case 'verse':
        return (
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <h3 className="font-medium text-emerald-800">
                সূরা {content.surah_number}, আয়াত {content.verse_number}
              </h3>
              <Badge className={getTypeBadgeColor(bookmark.content_type)}>
                {getTypeLabel(bookmark.content_type)}
              </Badge>
            </div>
            {content.arabic_text && (
              <p className="text-right text-lg text-emerald-900 font-arabic leading-relaxed">
                {content.arabic_text}
              </p>
            )}
            <p className="text-gray-700">
              {content.bengali_translation || content.english_translation}
            </p>
            {content.transliteration && (
              <p className="text-sm text-emerald-600 italic">
                {content.transliteration}
              </p>
            )}
          </div>
        )

      case 'hadith':
        return (
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <h3 className="font-medium text-emerald-800">
                {content.book_name} - {content.hadith_number}
              </h3>
              <Badge className={getTypeBadgeColor(bookmark.content_type)}>
                {getTypeLabel(bookmark.content_type)}
              </Badge>
            </div>
            {content.arabic_text && (
              <p className="text-right text-lg text-emerald-900 font-arabic leading-relaxed">
                {content.arabic_text}
              </p>
            )}
            <p className="text-gray-700">
              {content.bengali_translation || content.english_translation}
            </p>
            <div className="flex items-center space-x-4 text-sm text-emerald-600">
              {content.narrator && <span>বর্ণনাকারী: {content.narrator}</span>}
              {content.grade && <span>গ্রেড: {content.grade}</span>}
            </div>
          </div>
        )

      case 'fatwa':
        return (
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <h3 className="font-medium text-emerald-800">
                ফতোয়া - {content.scholar_name}
              </h3>
              <Badge className={getTypeBadgeColor(bookmark.content_type)}>
                {getTypeLabel(bookmark.content_type)}
              </Badge>
            </div>
            <div className="space-y-2">
              <div>
                <h4 className="text-sm font-medium text-emerald-700 mb-1">প্রশ্ন:</h4>
                <p className="text-gray-700 text-sm">{content.question}</p>
              </div>
              <div>
                <h4 className="text-sm font-medium text-emerald-700 mb-1">উত্তর:</h4>
                <p className="text-gray-700 text-sm">
                  {content.answer?.length > 200 
                    ? content.answer.substring(0, 200) + '...' 
                    : content.answer}
                </p>
              </div>
            </div>
          </div>
        )

      default:
        return null
    }
  }

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('bn-BD', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    })
  }

  return (
    <div className="max-w-6xl mx-auto p-6">
      {/* Header */}
      <div className="mb-6">
        <h1 className="text-2xl font-bold text-emerald-800 mb-2">বুকমার্ক</h1>
        <p className="text-emerald-600">আপনার সংরক্ষিত ইসলামিক কন্টেন্ট</p>
      </div>

      {/* Search and Filter */}
      <div className="flex flex-col sm:flex-row gap-4 mb-6">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-emerald-500" />
          <Input
            placeholder="বুকমার্ক খুঁজুন..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="pl-10 border-emerald-200 focus:border-emerald-500"
          />
        </div>
        <Select value={filterType} onValueChange={setFilterType}>
          <SelectTrigger className="w-full sm:w-48 border-emerald-200">
            <Filter className="h-4 w-4 mr-2" />
            <SelectValue />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">সব ধরনের</SelectItem>
            <SelectItem value="verse">আয়াত</SelectItem>
            <SelectItem value="hadith">হাদিস</SelectItem>
            <SelectItem value="fatwa">ফতোয়া</SelectItem>
          </SelectContent>
        </Select>
      </div>

      {/* Bookmarks List */}
      {loading ? (
        <div className="text-center py-12">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-emerald-600 mx-auto mb-4"></div>
          <p className="text-emerald-600">বুকমার্ক লোড হচ্ছে...</p>
        </div>
      ) : filteredBookmarks.length === 0 ? (
        <div className="text-center py-12">
          <Bookmark className="h-16 w-16 text-emerald-300 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-emerald-800 mb-2">
            {searchQuery || filterType !== 'all' ? 'কোন বুকমার্ক পাওয়া যায়নি' : 'কোন বুকমার্ক নেই'}
          </h3>
          <p className="text-emerald-600">
            {searchQuery || filterType !== 'all' 
              ? 'অন্য কিছু খুঁজে দেখুন বা ফিল্টার পরিবর্তন করুন'
              : 'চ্যাট করার সময় গুরুত্বপূর্ণ তথ্য বুকমার্ক করুন'
            }
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {filteredBookmarks.map((bookmark) => (
            <Card key={bookmark.id} className="border-emerald-200 hover:shadow-md transition-shadow">
              <CardContent className="p-6">
                {renderBookmarkContent(bookmark)}
                
                {bookmark.notes && (
                  <div className="mt-4 p-3 bg-emerald-50 rounded-lg">
                    <h4 className="text-sm font-medium text-emerald-700 mb-1">নোট:</h4>
                    <p className="text-sm text-emerald-800">{bookmark.notes}</p>
                  </div>
                )}

                <div className="flex items-center justify-between mt-4 pt-4 border-t border-emerald-100">
                  <div className="flex items-center space-x-2">
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => copyToClipboard(
                        bookmark.content_type === 'verse' 
                          ? bookmark.content?.bengali_translation || bookmark.content?.english_translation || ''
                          : bookmark.content_type === 'hadith'
                          ? bookmark.content?.bengali_translation || bookmark.content?.english_translation || ''
                          : bookmark.content?.answer || ''
                      )}
                      className="text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
                    >
                      <Copy className="h-4 w-4" />
                    </Button>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => removeBookmark(bookmark.id)}
                      className="text-red-600 hover:text-red-700 hover:bg-red-50"
                    >
                      <Trash2 className="h-4 w-4" />
                    </Button>
                  </div>
                  <span className="text-xs text-emerald-500">
                    {formatDate(bookmark.created_at)}
                  </span>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  )
}

