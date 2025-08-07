import { defineStore } from 'pinia'
import axios from 'axios'

// 配置axios默认设置
axios.defaults.headers.common['Content-Type'] = 'application/json'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
    loading: false
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
    userRole: (state) => state.user?.role || null
  },

  actions: {
    async login(credentials) {
      this.loading = true
      try {
        const response = await axios.post('/api/login', credentials)
        const { access_token, user } = response.data
        
        this.token = access_token
        this.user = user
        localStorage.setItem('token', access_token)
        
        // 设置axios默认headers
        axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`
        
        return { success: true }
      } catch (error) {
        return { 
          success: false, 
          error: error.response?.data?.error || '登录失败' 
        }
      } finally {
        this.loading = false
      }
    },

    async getProfile() {
      try {
        const response = await axios.get('/api/profile')
        this.user = response.data
        return { success: true }
      } catch (error) {
        return { 
          success: false, 
          error: error.response?.data?.error || '获取用户信息失败' 
        }
      }
    },

    logout() {
      this.user = null
      this.token = null
      localStorage.removeItem('token')
      delete axios.defaults.headers.common['Authorization']
    },

    initializeAuth() {
      const token = localStorage.getItem('token')
      if (token) {
        this.token = token
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
        this.getProfile()
      }
    }
  }
}) 