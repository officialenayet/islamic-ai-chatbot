import { useState, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { 
  MessageCircle, 
  Plus, 
  Search, 
  Bookmark, 
  History, 
  Settings,
  X,
  MoreHorizontal,
  Trash2,
  Edit3
} from 'lucide-react'
import { Button } from '@/components/ui/button'
import { ScrollArea } from '@/components/ui/scroll-area'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { useChat } from '@/hooks/useChat'
import { useAuth } from '@/hooks/useAuth'
import { cn } from '@/lib/utils'

export default function Sidebar({ isOpen, onClose }) {
  const { user } = useAuth()
  const { 
    sessions, 
    currentSession, 
    startNewSession, 
    loadChatHistory, 
    deleteSession,
    setCurrentSession,
    setMessages 
  } = useChat()
  const navigate = useNavigate()
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (user && isOpen) {
      loadChatHistory()
    }
  }, [user, isOpen])

  const handleNewChat = async () => {
    setLoading(true)
    const result = await startNewSession()
    if (result.success) {
      navigate('/')
      onClose()
    }
    setLoading(false)
  }

  const handleSessionClick = async (session) => {
    setCurrentSession(session)
    const result = await loadChatHistory(session.id)
    if (result.success) {
      navigate('/')
      onClose()
    }
  }

  const handleDeleteSession = async (sessionId, e) => {
    e.stopPropagation()
    if (confirm('এই চ্যাট সেশনটি মুছে ফেলতে চান?')) {
      await deleteSession(sessionId)
    }
  }

  const formatDate = (dateString) => {
    const date = new Date(dateString)
    const now = new Date()
    const diffTime = Math.abs(now - date)
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))

    if (diffDays === 1) return 'আজ'
    if (diffDays === 2) return 'গতকাল'
    if (diffDays <= 7) return `${diffDays} দিন আগে`
    return date.toLocaleDateString('bn-BD')
  }

  const truncateTitle = (title, maxLength = 30) => {
    if (title.length <= maxLength) return title
    return title.substring(0, maxLength) + '...'
  }

  return (
    <>
      {/* Overlay */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-black/20 z-40 lg:hidden"
          onClick={onClose}
        />
      )}

      {/* Sidebar */}
      <div className={cn(
        "fixed left-0 top-16 h-[calc(100vh-4rem)] w-64 bg-white border-r border-emerald-200 shadow-lg z-50 transform transition-transform duration-300 ease-in-out",
        isOpen ? "translate-x-0" : "-translate-x-full"
      )}>
        <div className="flex flex-col h-full">
          {/* Header */}
          <div className="p-4 border-b border-emerald-100">
            <div className="flex items-center justify-between mb-3">
              <h2 className="text-lg font-semibold text-emerald-800">চ্যাট হিস্টরি</h2>
              <Button
                variant="ghost"
                size="sm"
                onClick={onClose}
                className="lg:hidden text-emerald-600 hover:text-emerald-700"
              >
                <X className="h-4 w-4" />
              </Button>
            </div>
            
            <Button
              onClick={handleNewChat}
              disabled={loading}
              className="w-full bg-emerald-600 hover:bg-emerald-700 text-white"
            >
              <Plus className="h-4 w-4 mr-2" />
              নতুন চ্যাট
            </Button>
          </div>

          {/* Navigation */}
          <div className="px-4 py-2 border-b border-emerald-100">
            <nav className="space-y-1">
              <Link
                to="/search"
                onClick={onClose}
                className="flex items-center px-3 py-2 text-sm text-emerald-700 hover:text-emerald-800 hover:bg-emerald-50 rounded-md transition-colors"
              >
                <Search className="h-4 w-4 mr-3" />
                অনুসন্ধান
              </Link>
              <Link
                to="/bookmarks"
                onClick={onClose}
                className="flex items-center px-3 py-2 text-sm text-emerald-700 hover:text-emerald-800 hover:bg-emerald-50 rounded-md transition-colors"
              >
                <Bookmark className="h-4 w-4 mr-3" />
                বুকমার্ক
              </Link>
            </nav>
          </div>

          {/* Chat Sessions */}
          <ScrollArea className="flex-1 px-4 py-2">
            <div className="space-y-1">
              {sessions.length === 0 ? (
                <div className="text-center py-8 text-emerald-600">
                  <MessageCircle className="h-8 w-8 mx-auto mb-2 opacity-50" />
                  <p className="text-sm">কোন চ্যাট নেই</p>
                  <p className="text-xs opacity-75">নতুন চ্যাট শুরু করুন</p>
                </div>
              ) : (
                sessions.map((session) => (
                  <div
                    key={session.id}
                    className={cn(
                      "group flex items-center justify-between p-2 rounded-md cursor-pointer transition-colors",
                      currentSession?.id === session.id
                        ? "bg-emerald-100 text-emerald-800"
                        : "hover:bg-emerald-50 text-emerald-700"
                    )}
                    onClick={() => handleSessionClick(session)}
                  >
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-medium truncate">
                        {truncateTitle(session.title || 'নতুন চ্যাট')}
                      </p>
                      <p className="text-xs opacity-75">
                        {formatDate(session.updated_at || session.created_at)}
                      </p>
                    </div>
                    
                    <DropdownMenu>
                      <DropdownMenuTrigger asChild>
                        <Button
                          variant="ghost"
                          size="sm"
                          className="opacity-0 group-hover:opacity-100 h-6 w-6 p-0 text-emerald-600 hover:text-emerald-700"
                          onClick={(e) => e.stopPropagation()}
                        >
                          <MoreHorizontal className="h-3 w-3" />
                        </Button>
                      </DropdownMenuTrigger>
                      <DropdownMenuContent align="end">
                        <DropdownMenuItem>
                          <Edit3 className="mr-2 h-3 w-3" />
                          নাম পরিবর্তন
                        </DropdownMenuItem>
                        <DropdownMenuItem
                          onClick={(e) => handleDeleteSession(session.id, e)}
                          className="text-red-600 hover:text-red-700"
                        >
                          <Trash2 className="mr-2 h-3 w-3" />
                          মুছে ফেলুন
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </div>
                ))
              )}
            </div>
          </ScrollArea>

          {/* Footer */}
          <div className="p-4 border-t border-emerald-100">
            <Button
              variant="ghost"
              className="w-full justify-start text-emerald-700 hover:text-emerald-800 hover:bg-emerald-50"
            >
              <Settings className="h-4 w-4 mr-3" />
              সেটিংস
            </Button>
          </div>
        </div>
      </div>
    </>
  )
}

