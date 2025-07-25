import { useState } from 'react'
import { MessageCircle, Eye, EyeOff, Loader2 } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { useAuth } from '@/hooks/useAuth'

export default function AuthPage() {
  const { login, register } = useAuth()
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  
  // Login form state
  const [loginData, setLoginData] = useState({
    email: '',
    password: ''
  })
  
  // Register form state
  const [registerData, setRegisterData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
    fullName: ''
  })

  const handleLogin = async (e) => {
    e.preventDefault()
    setIsLoading(true)
    setError('')

    if (!loginData.email || !loginData.password) {
      setError('ইমেইল এবং পাসওয়ার্ড প্রয়োজন')
      setIsLoading(false)
      return
    }

    const result = await login(loginData.email, loginData.password)
    
    if (!result.success) {
      setError(result.error)
    }
    
    setIsLoading(false)
  }

  const handleRegister = async (e) => {
    e.preventDefault()
    setIsLoading(true)
    setError('')

    // Validation
    if (!registerData.username || !registerData.email || !registerData.password) {
      setError('সব ক্ষেত্র পূরণ করুন')
      setIsLoading(false)
      return
    }

    if (registerData.password !== registerData.confirmPassword) {
      setError('পাসওয়ার্ড মিলছে না')
      setIsLoading(false)
      return
    }

    if (registerData.password.length < 8) {
      setError('পাসওয়ার্ড কমপক্ষে ৮ অক্ষরের হতে হবে')
      setIsLoading(false)
      return
    }

    const result = await register(
      registerData.username,
      registerData.email,
      registerData.password,
      registerData.fullName
    )
    
    if (!result.success) {
      setError(result.error)
    }
    
    setIsLoading(false)
  }

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        {/* Logo and Title */}
        <div className="text-center mb-8">
          <div className="w-16 h-16 bg-gradient-to-br from-emerald-600 to-teal-600 rounded-2xl flex items-center justify-center mx-auto mb-4">
            <MessageCircle className="h-8 w-8 text-white" />
          </div>
          <h1 className="text-2xl font-bold text-emerald-800 mb-2">ইসলামিক AI চ্যাটবট</h1>
          <p className="text-emerald-600">কোরআন, হাদিস ও ইসলামিক জ্ঞানের AI সহায়ক</p>
        </div>

        <Card className="border-emerald-200 shadow-lg">
          <Tabs defaultValue="login" className="w-full">
            <TabsList className="grid w-full grid-cols-2 mb-4">
              <TabsTrigger value="login" className="data-[state=active]:bg-emerald-100 data-[state=active]:text-emerald-800">
                লগইন
              </TabsTrigger>
              <TabsTrigger value="register" className="data-[state=active]:bg-emerald-100 data-[state=active]:text-emerald-800">
                নিবন্ধন
              </TabsTrigger>
            </TabsList>

            {error && (
              <Alert className="mb-4 border-red-200 bg-red-50">
                <AlertDescription className="text-red-700">
                  {error}
                </AlertDescription>
              </Alert>
            )}

            {/* Login Tab */}
            <TabsContent value="login">
              <CardHeader className="pb-4">
                <CardTitle className="text-emerald-800">লগইন করুন</CardTitle>
                <CardDescription>
                  আপনার অ্যাকাউন্টে প্রবেশ করুন
                </CardDescription>
              </CardHeader>
              <CardContent>
                <form onSubmit={handleLogin} className="space-y-4">
                  <div className="space-y-2">
                    <Label htmlFor="login-email">ইমেইল</Label>
                    <Input
                      id="login-email"
                      type="email"
                      placeholder="your@email.com"
                      value={loginData.email}
                      onChange={(e) => setLoginData(prev => ({ ...prev, email: e.target.value }))}
                      className="border-emerald-200 focus:border-emerald-500"
                      disabled={isLoading}
                    />
                  </div>
                  
                  <div className="space-y-2">
                    <Label htmlFor="login-password">পাসওয়ার্ড</Label>
                    <div className="relative">
                      <Input
                        id="login-password"
                        type={showPassword ? "text" : "password"}
                        placeholder="আপনার পাসওয়ার্ড"
                        value={loginData.password}
                        onChange={(e) => setLoginData(prev => ({ ...prev, password: e.target.value }))}
                        className="border-emerald-200 focus:border-emerald-500 pr-10"
                        disabled={isLoading}
                      />
                      <Button
                        type="button"
                        variant="ghost"
                        size="sm"
                        className="absolute right-0 top-0 h-full px-3 py-2 hover:bg-transparent"
                        onClick={() => setShowPassword(!showPassword)}
                        disabled={isLoading}
                      >
                        {showPassword ? (
                          <EyeOff className="h-4 w-4 text-emerald-500" />
                        ) : (
                          <Eye className="h-4 w-4 text-emerald-500" />
                        )}
                      </Button>
                    </div>
                  </div>

                  <Button 
                    type="submit" 
                    className="w-full bg-emerald-600 hover:bg-emerald-700"
                    disabled={isLoading}
                  >
                    {isLoading ? (
                      <>
                        <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                        লগইন হচ্ছে...
                      </>
                    ) : (
                      'লগইন করুন'
                    )}
                  </Button>
                </form>
              </CardContent>
            </TabsContent>

            {/* Register Tab */}
            <TabsContent value="register">
              <CardHeader className="pb-4">
                <CardTitle className="text-emerald-800">নিবন্ধন করুন</CardTitle>
                <CardDescription>
                  নতুন অ্যাকাউন্ট তৈরি করুন
                </CardDescription>
              </CardHeader>
              <CardContent>
                <form onSubmit={handleRegister} className="space-y-4">
                  <div className="space-y-2">
                    <Label htmlFor="register-fullname">পূর্ণ নাম (ঐচ্ছিক)</Label>
                    <Input
                      id="register-fullname"
                      type="text"
                      placeholder="আপনার পূর্ণ নাম"
                      value={registerData.fullName}
                      onChange={(e) => setRegisterData(prev => ({ ...prev, fullName: e.target.value }))}
                      className="border-emerald-200 focus:border-emerald-500"
                      disabled={isLoading}
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="register-username">ব্যবহারকারী নাম</Label>
                    <Input
                      id="register-username"
                      type="text"
                      placeholder="username"
                      value={registerData.username}
                      onChange={(e) => setRegisterData(prev => ({ ...prev, username: e.target.value }))}
                      className="border-emerald-200 focus:border-emerald-500"
                      disabled={isLoading}
                    />
                  </div>
                  
                  <div className="space-y-2">
                    <Label htmlFor="register-email">ইমেইল</Label>
                    <Input
                      id="register-email"
                      type="email"
                      placeholder="your@email.com"
                      value={registerData.email}
                      onChange={(e) => setRegisterData(prev => ({ ...prev, email: e.target.value }))}
                      className="border-emerald-200 focus:border-emerald-500"
                      disabled={isLoading}
                    />
                  </div>
                  
                  <div className="space-y-2">
                    <Label htmlFor="register-password">পাসওয়ার্ড</Label>
                    <div className="relative">
                      <Input
                        id="register-password"
                        type={showPassword ? "text" : "password"}
                        placeholder="কমপক্ষে ৮ অক্ষর"
                        value={registerData.password}
                        onChange={(e) => setRegisterData(prev => ({ ...prev, password: e.target.value }))}
                        className="border-emerald-200 focus:border-emerald-500 pr-10"
                        disabled={isLoading}
                      />
                      <Button
                        type="button"
                        variant="ghost"
                        size="sm"
                        className="absolute right-0 top-0 h-full px-3 py-2 hover:bg-transparent"
                        onClick={() => setShowPassword(!showPassword)}
                        disabled={isLoading}
                      >
                        {showPassword ? (
                          <EyeOff className="h-4 w-4 text-emerald-500" />
                        ) : (
                          <Eye className="h-4 w-4 text-emerald-500" />
                        )}
                      </Button>
                    </div>
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="register-confirm-password">পাসওয়ার্ড নিশ্চিত করুন</Label>
                    <Input
                      id="register-confirm-password"
                      type="password"
                      placeholder="পাসওয়ার্ড পুনরায় লিখুন"
                      value={registerData.confirmPassword}
                      onChange={(e) => setRegisterData(prev => ({ ...prev, confirmPassword: e.target.value }))}
                      className="border-emerald-200 focus:border-emerald-500"
                      disabled={isLoading}
                    />
                  </div>

                  <Button 
                    type="submit" 
                    className="w-full bg-emerald-600 hover:bg-emerald-700"
                    disabled={isLoading}
                  >
                    {isLoading ? (
                      <>
                        <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                        নিবন্ধন হচ্ছে...
                      </>
                    ) : (
                      'নিবন্ধন করুন'
                    )}
                  </Button>
                </form>
              </CardContent>
            </TabsContent>
          </Tabs>
        </Card>

        {/* Footer */}
        <div className="text-center mt-6 text-sm text-emerald-600">
          <p>ইসলামিক AI চ্যাটবট ব্যবহার করে আপনি</p>
          <p>কোরআন, হাদিস ও ইসলামিক জ্ঞান অর্জন করতে পারবেন</p>
        </div>
      </div>
    </div>
  )
}

