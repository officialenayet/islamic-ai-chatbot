import { createContext, useContext, useState, useEffect } from 'react'
import { useAuth } from './useAuth'

const ChatContext = createContext()

export function ChatProvider({ children }) {
  const { getAuthHeaders, API_BASE_URL } = useAuth()
  const [currentSession, setCurrentSession] = useState(null)
  const [messages, setMessages] = useState([])
  const [sessions, setSessions] = useState([])
  const [loading, setLoading] = useState(false)
  const [typing, setTyping] = useState(false)

  const startNewSession = async (title = 'নতুন চ্যাট') => {
    try {
      setLoading(true)
      const response = await fetch(`${API_BASE_URL}/chat/start`, {
        method: 'POST',
        headers: {
          ...getAuthHeaders(),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title })
      })

      const data = await response.json()

      if (response.ok && data.success) {
        const newSession = data.data
        setCurrentSession(newSession)
        setMessages([])
        setSessions(prev => [newSession, ...prev])
        return { success: true, session: newSession }
      } else {
        return { 
          success: false, 
          error: data.error?.message || 'Failed to start chat session' 
        }
      }
    } catch (error) {
      console.error('Start session error:', error)
      return { 
        success: false, 
        error: 'Network error. Please try again.' 
      }
    } finally {
      setLoading(false)
    }
  }

  const sendMessage = async (messageText, language = 'bn') => {
    if (!currentSession) {
      const sessionResult = await startNewSession()
      if (!sessionResult.success) {
        return sessionResult
      }
    }

    try {
      setTyping(true)
      
      // Add user message to UI immediately
      const userMessage = {
        id: Date.now().toString(),
        user_message: messageText,
        bot_response: '',
        sources: [],
        created_at: new Date().toISOString(),
        isLoading: true
      }
      
      setMessages(prev => [...prev, userMessage])

      const response = await fetch(`${API_BASE_URL}/chat/message`, {
        method: 'POST',
        headers: {
          ...getAuthHeaders(),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          session_id: currentSession.session_id || currentSession.id,
          message: messageText,
          language
        })
      })

      const data = await response.json()

      if (response.ok && data.success) {
        // Update the message with bot response
        setMessages(prev => 
          prev.map(msg => 
            msg.id === userMessage.id 
              ? { ...data.data, isLoading: false }
              : msg
          )
        )
        return { success: true, data: data.data }
      } else {
        // Remove the loading message on error
        setMessages(prev => prev.filter(msg => msg.id !== userMessage.id))
        return { 
          success: false, 
          error: data.error?.message || 'Failed to send message' 
        }
      }
    } catch (error) {
      console.error('Send message error:', error)
      // Remove the loading message on error
      setMessages(prev => prev.filter(msg => msg.id === userMessage.id ? false : true))
      return { 
        success: false, 
        error: 'Network error. Please try again.' 
      }
    } finally {
      setTyping(false)
    }
  }

  const loadChatHistory = async (sessionId = null) => {
    try {
      setLoading(true)
      const url = sessionId 
        ? `${API_BASE_URL}/chat/history?session_id=${sessionId}`
        : `${API_BASE_URL}/chat/history`

      const response = await fetch(url, {
        headers: getAuthHeaders()
      })

      const data = await response.json()

      if (response.ok && data.success) {
        if (sessionId) {
          // Load specific session
          setCurrentSession(data.data.session)
          setMessages(data.data.messages.reverse()) // Reverse to show oldest first
        } else {
          // Load all sessions
          setSessions(data.data.sessions || [])
        }
        return { success: true, data: data.data }
      } else {
        return { 
          success: false, 
          error: data.error?.message || 'Failed to load chat history' 
        }
      }
    } catch (error) {
      console.error('Load chat history error:', error)
      return { 
        success: false, 
        error: 'Network error. Please try again.' 
      }
    } finally {
      setLoading(false)
    }
  }

  const deleteSession = async (sessionId) => {
    try {
      const response = await fetch(`${API_BASE_URL}/chat/session/${sessionId}`, {
        method: 'DELETE',
        headers: getAuthHeaders()
      })

      const data = await response.json()

      if (response.ok && data.success) {
        setSessions(prev => prev.filter(s => s.id !== sessionId))
        
        // If current session is deleted, clear it
        if (currentSession && currentSession.id === sessionId) {
          setCurrentSession(null)
          setMessages([])
        }
        
        return { success: true }
      } else {
        return { 
          success: false, 
          error: data.error?.message || 'Failed to delete session' 
        }
      }
    } catch (error) {
      console.error('Delete session error:', error)
      return { 
        success: false, 
        error: 'Network error. Please try again.' 
      }
    }
  }

  const updateSessionTitle = async (sessionId, title) => {
    try {
      const response = await fetch(`${API_BASE_URL}/chat/session/${sessionId}/title`, {
        method: 'PUT',
        headers: {
          ...getAuthHeaders(),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title })
      })

      const data = await response.json()

      if (response.ok && data.success) {
        setSessions(prev => 
          prev.map(s => s.id === sessionId ? { ...s, title } : s)
        )
        
        if (currentSession && currentSession.id === sessionId) {
          setCurrentSession(prev => ({ ...prev, title }))
        }
        
        return { success: true }
      } else {
        return { 
          success: false, 
          error: data.error?.message || 'Failed to update session title' 
        }
      }
    } catch (error) {
      console.error('Update session title error:', error)
      return { 
        success: false, 
        error: 'Network error. Please try again.' 
      }
    }
  }

  const submitFeedback = async (messageId, rating, comment = '') => {
    try {
      const response = await fetch(`${API_BASE_URL}/feedback/message/${messageId}`, {
        method: 'POST',
        headers: {
          ...getAuthHeaders(),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rating, comment })
      })

      const data = await response.json()

      if (response.ok && data.success) {
        // Update message with feedback
        setMessages(prev => 
          prev.map(msg => 
            msg.id === messageId 
              ? { ...msg, feedback_rating: rating, feedback_comment: comment }
              : msg
          )
        )
        return { success: true }
      } else {
        return { 
          success: false, 
          error: data.error?.message || 'Failed to submit feedback' 
        }
      }
    } catch (error) {
      console.error('Submit feedback error:', error)
      return { 
        success: false, 
        error: 'Network error. Please try again.' 
      }
    }
  }

  const value = {
    currentSession,
    messages,
    sessions,
    loading,
    typing,
    startNewSession,
    sendMessage,
    loadChatHistory,
    deleteSession,
    updateSessionTitle,
    submitFeedback,
    setCurrentSession,
    setMessages
  }

  return (
    <ChatContext.Provider value={value}>
      {children}
    </ChatContext.Provider>
  )
}

export function useChat() {
  const context = useContext(ChatContext)
  if (!context) {
    throw new Error('useChat must be used within a ChatProvider')
  }
  return context
}

