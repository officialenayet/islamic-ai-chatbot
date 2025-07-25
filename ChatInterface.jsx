import { useState, useRef, useEffect } from 'react'
import { Send, Loader2, ThumbsUp, ThumbsDown, Copy, Bookmark, ExternalLink } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { Card, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Separator } from '@/components/ui/separator'
import { useChat } from '@/hooks/useChat'
import { useAuth } from '@/hooks/useAuth'

export default function ChatInterface() {
  const { user } = useAuth()
  const { 
    currentSession, 
    messages, 
    typing, 
    sendMessage, 
    submitFeedback,
    loadChatHistory 
  } = useChat()
  
  const [inputMessage, setInputMessage] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const messagesEndRef = useRef(null)
  const textareaRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages, typing])

  useEffect(() => {
    // Load chat history on component mount
    if (user && !currentSession) {
      loadChatHistory()
    }
  }, [user])

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!inputMessage.trim() || isSubmitting) return

    const message = inputMessage.trim()
    setInputMessage('')
    setIsSubmitting(true)

    const result = await sendMessage(message)
    
    if (!result.success) {
      // Handle error - maybe show a toast
      console.error('Failed to send message:', result.error)
    }
    
    setIsSubmitting(false)
    textareaRef.current?.focus()
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSubmit(e)
    }
  }

  const handleFeedback = async (messageId, rating) => {
    const result = await submitFeedback(messageId, rating)
    if (!result.success) {
      console.error('Failed to submit feedback:', result.error)
    }
  }

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text)
    // Could show a toast here
  }

  const formatSource = (source) => {
    if (source.type === 'verse') {
      return {
        title: `কোরআন - ${source.reference}`,
        content: source.text,
        arabic: source.arabic,
        type: 'আয়াত'
      }
    } else if (source.type === 'hadith') {
      return {
        title: `হাদিস - ${source.reference}`,
        content: source.text,
        arabic: source.arabic,
        narrator: source.narrator,
        grade: source.grade,
        type: 'হাদিস'
      }
    } else if (source.type === 'fatwa') {
      return {
        title: `ফতোয়া - ${source.reference}`,
        content: source.answer,
        scholar: source.scholar,
        type: 'ফতোয়া'
      }
    }
    return null
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
    <div className="flex flex-col h-[calc(100vh-4rem)]">
      {/* Welcome Message */}
      {messages.length === 0 && !typing && (
        <div className="flex-1 flex items-center justify-center p-8">
          <div className="text-center max-w-2xl">
            <div className="w-20 h-20 bg-gradient-to-br from-emerald-600 to-teal-600 rounded-full flex items-center justify-center mx-auto mb-6">
              <span className="text-2xl text-white">السلام</span>
            </div>
            <h2 className="text-2xl font-bold text-emerald-800 mb-4">
              আসসালামু আলাইকুম, {user.full_name || user.username}!
            </h2>
            <p className="text-emerald-600 mb-6">
              আমি আপনার ইসলামিক AI সহায়ক। কোরআন, হাদিস, ফতোয়া এবং ইসলামিক বিষয়ে যেকোনো প্রশ্ন করুন।
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-left">
              <Card className="border-emerald-200 hover:border-emerald-300 transition-colors cursor-pointer"
                    onClick={() => setInputMessage('নামাজের নিয়ম কি?')}>
                <CardContent className="p-4">
                  <h3 className="font-medium text-emerald-800 mb-2">নামাজ সম্পর্কে</h3>
                  <p className="text-sm text-emerald-600">নামাজের নিয়ম, সময় ও গুরুত্ব</p>
                </CardContent>
              </Card>
              <Card className="border-emerald-200 hover:border-emerald-300 transition-colors cursor-pointer"
                    onClick={() => setInputMessage('রমজানের ফজিলত কি?')}>
                <CardContent className="p-4">
                  <h3 className="font-medium text-emerald-800 mb-2">রমজান ও রোজা</h3>
                  <p className="text-sm text-emerald-600">রমজানের ফজিলত ও রোজার বিধান</p>
                </CardContent>
              </Card>
              <Card className="border-emerald-200 hover:border-emerald-300 transition-colors cursor-pointer"
                    onClick={() => setInputMessage('যাকাতের নিসাব কত?')}>
                <CardContent className="p-4">
                  <h3 className="font-medium text-emerald-800 mb-2">যাকাত</h3>
                  <p className="text-sm text-emerald-600">যাকাতের নিসাব ও হিসাব</p>
                </CardContent>
              </Card>
              <Card className="border-emerald-200 hover:border-emerald-300 transition-colors cursor-pointer"
                    onClick={() => setInputMessage('হজের নিয়ম কি?')}>
                <CardContent className="p-4">
                  <h3 className="font-medium text-emerald-800 mb-2">হজ ও উমরা</h3>
                  <p className="text-sm text-emerald-600">হজের নিয়ম ও গুরুত্ব</p>
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      )}

      {/* Messages */}
      <ScrollArea className="flex-1 p-4">
        <div className="max-w-4xl mx-auto space-y-6">
          {messages.map((message, index) => (
            <div key={message.id || index} className="space-y-4">
              {/* User Message */}
              <div className="flex justify-end">
                <div className="max-w-[80%] bg-emerald-600 text-white rounded-2xl rounded-br-md px-4 py-3">
                  <p className="whitespace-pre-wrap">{message.user_message}</p>
                </div>
              </div>

              {/* Bot Response */}
              <div className="flex justify-start">
                <div className="max-w-[90%] space-y-4">
                  <Card className="border-emerald-200">
                    <CardContent className="p-4">
                      {message.isLoading ? (
                        <div className="flex items-center space-x-2 text-emerald-600">
                          <Loader2 className="h-4 w-4 animate-spin" />
                          <span>উত্তর তৈরি হচ্ছে...</span>
                        </div>
                      ) : (
                        <>
                          <div className="prose prose-emerald max-w-none">
                            <div className="whitespace-pre-wrap text-gray-800">
                              {message.bot_response}
                            </div>
                          </div>

                          {/* Sources */}
                          {message.sources && message.sources.length > 0 && (
                            <div className="mt-4 pt-4 border-t border-emerald-100">
                              <h4 className="text-sm font-medium text-emerald-800 mb-3">তথ্যসূত্র:</h4>
                              <div className="space-y-3">
                                {message.sources.map((source, sourceIndex) => {
                                  const formattedSource = formatSource(source)
                                  if (!formattedSource) return null

                                  return (
                                    <Card key={sourceIndex} className="border-emerald-100 bg-emerald-50">
                                      <CardContent className="p-3">
                                        <div className="flex items-start justify-between mb-2">
                                          <Badge variant="secondary" className="bg-emerald-100 text-emerald-700">
                                            {formattedSource.type}
                                          </Badge>
                                          <Button
                                            variant="ghost"
                                            size="sm"
                                            onClick={() => copyToClipboard(formattedSource.content)}
                                            className="h-6 w-6 p-0"
                                          >
                                            <Copy className="h-3 w-3" />
                                          </Button>
                                        </div>
                                        <h5 className="text-sm font-medium text-emerald-800 mb-1">
                                          {formattedSource.title}
                                        </h5>
                                        {formattedSource.arabic && (
                                          <p className="text-right text-lg mb-2 text-emerald-900 font-arabic">
                                            {formattedSource.arabic}
                                          </p>
                                        )}
                                        <p className="text-sm text-gray-700">
                                          {formattedSource.content}
                                        </p>
                                        {formattedSource.narrator && (
                                          <p className="text-xs text-emerald-600 mt-1">
                                            বর্ণনাকারী: {formattedSource.narrator}
                                          </p>
                                        )}
                                        {formattedSource.grade && (
                                          <p className="text-xs text-emerald-600">
                                            গ্রেড: {formattedSource.grade}
                                          </p>
                                        )}
                                      </CardContent>
                                    </Card>
                                  )
                                })}
                              </div>
                            </div>
                          )}

                          {/* Actions */}
                          <div className="flex items-center justify-between mt-4 pt-3 border-t border-emerald-100">
                            <div className="flex items-center space-x-2">
                              <Button
                                variant="ghost"
                                size="sm"
                                onClick={() => handleFeedback(message.id, 5)}
                                className="text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
                              >
                                <ThumbsUp className="h-4 w-4" />
                              </Button>
                              <Button
                                variant="ghost"
                                size="sm"
                                onClick={() => handleFeedback(message.id, 1)}
                                className="text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
                              >
                                <ThumbsDown className="h-4 w-4" />
                              </Button>
                              <Button
                                variant="ghost"
                                size="sm"
                                onClick={() => copyToClipboard(message.bot_response)}
                                className="text-emerald-600 hover:text-emerald-700 hover:bg-emerald-50"
                              >
                                <Copy className="h-4 w-4" />
                              </Button>
                            </div>
                            <div className="text-xs text-emerald-500">
                              {message.created_at && new Date(message.created_at).toLocaleTimeString('bn-BD')}
                            </div>
                          </div>
                        </>
                      )}
                    </CardContent>
                  </Card>
                </div>
              </div>
            </div>
          ))}

          {/* Typing Indicator */}
          {typing && (
            <div className="flex justify-start">
              <Card className="border-emerald-200">
                <CardContent className="p-4">
                  <div className="flex items-center space-x-2 text-emerald-600">
                    <Loader2 className="h-4 w-4 animate-spin" />
                    <span>টাইপ করছি...</span>
                  </div>
                </CardContent>
              </Card>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </ScrollArea>

      {/* Input Area */}
      <div className="border-t border-emerald-200 bg-white p-4">
        <div className="max-w-4xl mx-auto">
          <form onSubmit={handleSubmit} className="flex space-x-2">
            <div className="flex-1 relative">
              <Textarea
                ref={textareaRef}
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="আপনার প্রশ্ন লিখুন..."
                className="min-h-[50px] max-h-32 resize-none border-emerald-200 focus:border-emerald-500 pr-12"
                disabled={isSubmitting}
              />
            </div>
            <Button
              type="submit"
              disabled={!inputMessage.trim() || isSubmitting}
              className="bg-emerald-600 hover:bg-emerald-700 px-4"
            >
              {isSubmitting ? (
                <Loader2 className="h-4 w-4 animate-spin" />
              ) : (
                <Send className="h-4 w-4" />
              )}
            </Button>
          </form>
          <div className="text-xs text-emerald-500 mt-2 text-center">
            Enter চেপে পাঠান, Shift+Enter দিয়ে নতুন লাইন
          </div>
        </div>
      </div>
    </div>
  )
}

