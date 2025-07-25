import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { Toaster } from '@/components/ui/sonner'
import { AuthProvider, useAuth } from '@/hooks/useAuth'
import { ChatProvider } from '@/hooks/useChat'
import Header from '@/components/Header'
import Sidebar from '@/components/Sidebar'
import ChatInterface from '@/components/ChatInterface'
import AuthPage from '@/components/AuthPage'
import ProfilePage from '@/components/ProfilePage'
import BookmarksPage from '@/components/BookmarksPage'
import SearchPage from '@/components/SearchPage'
import './App.css'

function AppContent() {
  const { user, loading } = useAuth()
  const [sidebarOpen, setSidebarOpen] = useState(false)

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-teal-100 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600 mx-auto mb-4"></div>
          <p className="text-emerald-700 font-medium">লোড হচ্ছে...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-teal-100">
      <Header onMenuClick={() => setSidebarOpen(!sidebarOpen)} />
      
      <div className="flex">
        <Sidebar isOpen={sidebarOpen} onClose={() => setSidebarOpen(false)} />
        
        <main className={`flex-1 transition-all duration-300 ${sidebarOpen ? 'ml-64' : 'ml-0'} pt-16`}>
          <Routes>
            <Route 
              path="/auth" 
              element={user ? <Navigate to="/" replace /> : <AuthPage />} 
            />
            <Route 
              path="/" 
              element={user ? <ChatInterface /> : <Navigate to="/auth" replace />} 
            />
            <Route 
              path="/profile" 
              element={user ? <ProfilePage /> : <Navigate to="/auth" replace />} 
            />
            <Route 
              path="/bookmarks" 
              element={user ? <BookmarksPage /> : <Navigate to="/auth" replace />} 
            />
            <Route 
              path="/search" 
              element={<SearchPage />} 
            />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
      </div>
      
      <Toaster />
    </div>
  )
}

function App() {
  return (
    <Router>
      <AuthProvider>
        <ChatProvider>
          <AppContent />
        </ChatProvider>
      </AuthProvider>
    </Router>
  )
}

export default App

