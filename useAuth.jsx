import { createContext, useContext, useState, useEffect } from 'react'

const AuthContext = createContext()

const API_BASE_URL = 'http://localhost:5000/api/v1'

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Check for stored token on app load
    const token = localStorage.getItem('access_token')
    if (token) {
      // Verify token with server
      fetchUserProfile(token)
    } else {
      setLoading(false)
    }
  }, [])

  const fetchUserProfile = async (token) => {
    try {
      const response = await fetch(`${API_BASE_URL}/auth/profile`, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      })

      if (response.ok) {
        const data = await response.json()
        if (data.success) {
          setUser(data.data)
        } else {
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
        }
      } else {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
      }
    } catch (error) {
      console.error('Failed to fetch user profile:', error)
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
    } finally {
      setLoading(false)
    }
  }

  const login = async (email, password) => {
    try {
      const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      })

      const data = await response.json()

      if (response.ok && data.success) {
        localStorage.setItem('access_token', data.data.access_token)
        localStorage.setItem('refresh_token', data.data.refresh_token)
        
        setUser({
          id: data.data.user_id,
          username: data.data.username,
          email: data.data.email
        })

        return { success: true }
      } else {
        return { 
          success: false, 
          error: data.error?.message || 'Login failed' 
        }
      }
    } catch (error) {
      console.error('Login error:', error)
      return { 
        success: false, 
        error: 'Network error. Please try again.' 
      }
    }
  }

  const register = async (username, email, password, fullName = '') => {
    try {
      const response = await fetch(`${API_BASE_URL}/auth/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
          username, 
          email, 
          password, 
          full_name: fullName,
          preferred_language: 'bn'
        })
      })

      const data = await response.json()

      if (response.ok && data.success) {
        localStorage.setItem('access_token', data.data.access_token)
        localStorage.setItem('refresh_token', data.data.refresh_token)
        
        setUser({
          id: data.data.user_id,
          username: data.data.username,
          email: data.data.email
        })

        return { success: true }
      } else {
        return { 
          success: false, 
          error: data.error?.message || 'Registration failed' 
        }
      }
    } catch (error) {
      console.error('Registration error:', error)
      return { 
        success: false, 
        error: 'Network error. Please try again.' 
      }
    }
  }

  const logout = async () => {
    try {
      const token = localStorage.getItem('access_token')
      if (token) {
        await fetch(`${API_BASE_URL}/auth/logout`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        })
      }
    } catch (error) {
      console.error('Logout error:', error)
    } finally {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      setUser(null)
    }
  }

  const updateProfile = async (profileData) => {
    try {
      const token = localStorage.getItem('access_token')
      if (!token) return { success: false, error: 'Not authenticated' }

      const response = await fetch(`${API_BASE_URL}/auth/profile`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(profileData)
      })

      const data = await response.json()

      if (response.ok && data.success) {
        setUser(data.data)
        return { success: true }
      } else {
        return { 
          success: false, 
          error: data.error?.message || 'Profile update failed' 
        }
      }
    } catch (error) {
      console.error('Profile update error:', error)
      return { 
        success: false, 
        error: 'Network error. Please try again.' 
      }
    }
  }

  const getAuthHeaders = () => {
    const token = localStorage.getItem('access_token')
    return token ? { 'Authorization': `Bearer ${token}` } : {}
  }

  const value = {
    user,
    loading,
    login,
    register,
    logout,
    updateProfile,
    getAuthHeaders,
    API_BASE_URL
  }

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}

