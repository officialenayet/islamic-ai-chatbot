import { useState, useEffect } from 'react'
import { User, Mail, Calendar, Globe, Edit3, Save, X } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Avatar, AvatarFallback } from '@/components/ui/avatar'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { useAuth } from '@/hooks/useAuth'

export default function ProfilePage() {
  const { user, updateProfile, API_BASE_URL, getAuthHeaders } = useAuth()
  const [isEditing, setIsEditing] = useState(false)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [success, setSuccess] = useState('')
  const [stats, setStats] = useState(null)
  
  const [profileData, setProfileData] = useState({
    full_name: user?.full_name || '',
    preferred_language: user?.preferred_language || 'bn',
    timezone: user?.timezone || 'Asia/Dhaka'
  })

  useEffect(() => {
    if (user) {
      setProfileData({
        full_name: user.full_name || '',
        preferred_language: user.preferred_language || 'bn',
        timezone: user.timezone || 'Asia/Dhaka'
      })
      fetchUserStats()
    }
  }, [user])

  const fetchUserStats = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/user/stats`, {
        headers: getAuthHeaders()
      })
      
      if (response.ok) {
        const data = await response.json()
        if (data.success) {
          setStats(data.data)
        }
      }
    } catch (error) {
      console.error('Failed to fetch user stats:', error)
    }
  }

  const handleSave = async () => {
    setLoading(true)
    setError('')
    setSuccess('')

    const result = await updateProfile(profileData)
    
    if (result.success) {
      setSuccess('প্রোফাইল সফলভাবে আপডেট হয়েছে')
      setIsEditing(false)
    } else {
      setError(result.error)
    }
    
    setLoading(false)
  }

  const handleCancel = () => {
    setProfileData({
      full_name: user?.full_name || '',
      preferred_language: user?.preferred_language || 'bn',
      timezone: user?.timezone || 'Asia/Dhaka'
    })
    setIsEditing(false)
    setError('')
    setSuccess('')
  }

  const getUserInitials = () => {
    if (user?.full_name) {
      return user.full_name.split(' ').map(n => n[0]).join('').toUpperCase()
    }
    return user?.username?.charAt(0).toUpperCase() || 'U'
  }

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A'
    return new Date(dateString).toLocaleDateString('bn-BD', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    })
  }

  if (!user) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center text-emerald-600">
          <p>অনুগ্রহ করে লগইন করুন</p>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-emerald-800">প্রোফাইল</h1>
          <p className="text-emerald-600">আপনার অ্যাকাউন্ট তথ্য ও পরিসংখ্যান</p>
        </div>
        
        {!isEditing ? (
          <Button
            onClick={() => setIsEditing(true)}
            className="bg-emerald-600 hover:bg-emerald-700"
          >
            <Edit3 className="h-4 w-4 mr-2" />
            সম্পাদনা
          </Button>
        ) : (
          <div className="flex space-x-2">
            <Button
              onClick={handleSave}
              disabled={loading}
              className="bg-emerald-600 hover:bg-emerald-700"
            >
              <Save className="h-4 w-4 mr-2" />
              সংরক্ষণ
            </Button>
            <Button
              onClick={handleCancel}
              variant="outline"
              className="border-emerald-200 text-emerald-700 hover:bg-emerald-50"
            >
              <X className="h-4 w-4 mr-2" />
              বাতিল
            </Button>
          </div>
        )}
      </div>

      {/* Alerts */}
      {error && (
        <Alert className="border-red-200 bg-red-50">
          <AlertDescription className="text-red-700">
            {error}
          </AlertDescription>
        </Alert>
      )}

      {success && (
        <Alert className="border-emerald-200 bg-emerald-50">
          <AlertDescription className="text-emerald-700">
            {success}
          </AlertDescription>
        </Alert>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Profile Information */}
        <div className="lg:col-span-2 space-y-6">
          <Card className="border-emerald-200">
            <CardHeader>
              <CardTitle className="text-emerald-800">ব্যক্তিগত তথ্য</CardTitle>
              <CardDescription>
                আপনার অ্যাকাউন্ট তথ্য আপডেট করুন
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex items-center space-x-4 mb-6">
                <Avatar className="h-20 w-20">
                  <AvatarFallback className="bg-emerald-100 text-emerald-700 text-xl font-bold">
                    {getUserInitials()}
                  </AvatarFallback>
                </Avatar>
                <div>
                  <h3 className="text-lg font-medium text-emerald-800">
                    {user.full_name || user.username}
                  </h3>
                  <p className="text-emerald-600">{user.email}</p>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="username">ব্যবহারকারী নাম</Label>
                  <Input
                    id="username"
                    value={user.username}
                    disabled
                    className="bg-gray-50 border-gray-200"
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="email">ইমেইল</Label>
                  <Input
                    id="email"
                    value={user.email}
                    disabled
                    className="bg-gray-50 border-gray-200"
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="full_name">পূর্ণ নাম</Label>
                  <Input
                    id="full_name"
                    value={profileData.full_name}
                    onChange={(e) => setProfileData(prev => ({ ...prev, full_name: e.target.value }))}
                    disabled={!isEditing}
                    className={isEditing ? "border-emerald-200 focus:border-emerald-500" : "bg-gray-50 border-gray-200"}
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="language">পছন্দের ভাষা</Label>
                  <Select
                    value={profileData.preferred_language}
                    onValueChange={(value) => setProfileData(prev => ({ ...prev, preferred_language: value }))}
                    disabled={!isEditing}
                  >
                    <SelectTrigger className={isEditing ? "border-emerald-200 focus:border-emerald-500" : "bg-gray-50 border-gray-200"}>
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="bn">বাংলা</SelectItem>
                      <SelectItem value="en">English</SelectItem>
                      <SelectItem value="ar">العربية</SelectItem>
                      <SelectItem value="ur">اردو</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-2 md:col-span-2">
                  <Label htmlFor="timezone">টাইমজোন</Label>
                  <Select
                    value={profileData.timezone}
                    onValueChange={(value) => setProfileData(prev => ({ ...prev, timezone: value }))}
                    disabled={!isEditing}
                  >
                    <SelectTrigger className={isEditing ? "border-emerald-200 focus:border-emerald-500" : "bg-gray-50 border-gray-200"}>
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="Asia/Dhaka">Asia/Dhaka (GMT+6)</SelectItem>
                      <SelectItem value="Asia/Karachi">Asia/Karachi (GMT+5)</SelectItem>
                      <SelectItem value="Asia/Dubai">Asia/Dubai (GMT+4)</SelectItem>
                      <SelectItem value="Asia/Riyadh">Asia/Riyadh (GMT+3)</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Statistics */}
        <div className="space-y-6">
          <Card className="border-emerald-200">
            <CardHeader>
              <CardTitle className="text-emerald-800">পরিসংখ্যান</CardTitle>
              <CardDescription>
                আপনার ব্যবহারের তথ্য
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              {stats ? (
                <>
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-emerald-600">মোট চ্যাট সেশন</span>
                    <span className="font-medium text-emerald-800">{stats.total_sessions}</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-emerald-600">মোট বার্তা</span>
                    <span className="font-medium text-emerald-800">{stats.total_messages}</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-emerald-600">বুকমার্ক</span>
                    <span className="font-medium text-emerald-800">{stats.total_bookmarks}</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-emerald-600">অনুসন্ধান</span>
                    <span className="font-medium text-emerald-800">{stats.total_searches}</span>
                  </div>
                  
                  <div className="pt-4 border-t border-emerald-100">
                    <h4 className="text-sm font-medium text-emerald-800 mb-2">বুকমার্ক বিভাগ</h4>
                    <div className="space-y-2">
                      <div className="flex items-center justify-between">
                        <span className="text-xs text-emerald-600">আয়াত</span>
                        <span className="text-xs font-medium text-emerald-800">{stats.bookmark_breakdown?.verse || 0}</span>
                      </div>
                      <div className="flex items-center justify-between">
                        <span className="text-xs text-emerald-600">হাদিস</span>
                        <span className="text-xs font-medium text-emerald-800">{stats.bookmark_breakdown?.hadith || 0}</span>
                      </div>
                      <div className="flex items-center justify-between">
                        <span className="text-xs text-emerald-600">ফতোয়া</span>
                        <span className="text-xs font-medium text-emerald-800">{stats.bookmark_breakdown?.fatwa || 0}</span>
                      </div>
                    </div>
                  </div>
                </>
              ) : (
                <div className="text-center py-4">
                  <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-emerald-600 mx-auto mb-2"></div>
                  <p className="text-sm text-emerald-600">লোড হচ্ছে...</p>
                </div>
              )}
            </CardContent>
          </Card>

          <Card className="border-emerald-200">
            <CardHeader>
              <CardTitle className="text-emerald-800">অ্যাকাউন্ট তথ্য</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              <div className="flex items-center space-x-2">
                <Calendar className="h-4 w-4 text-emerald-600" />
                <div>
                  <p className="text-xs text-emerald-600">সদস্য হয়েছেন</p>
                  <p className="text-sm font-medium text-emerald-800">
                    {formatDate(stats?.member_since)}
                  </p>
                </div>
              </div>
              <div className="flex items-center space-x-2">
                <Globe className="h-4 w-4 text-emerald-600" />
                <div>
                  <p className="text-xs text-emerald-600">শেষ সক্রিয়</p>
                  <p className="text-sm font-medium text-emerald-800">
                    {formatDate(stats?.last_active)}
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}

