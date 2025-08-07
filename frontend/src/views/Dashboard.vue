<template>
  <div class="admin-layout">
    <header class="admin-header">
      <div class="logo">后台管理系统</div>
      <div class="user-info">
        <img class="avatar" src="https://i.pravatar.cc/40" alt="用户头像" />
        <span class="username">Admin</span>
      </div>
    </header>
    <div class="admin-main">
      <aside class="admin-sidebar">
        <ul>
          <li :class="{active: activeMenu === 'dashboard'}" @click="activeMenu = 'dashboard'">仪表盘</li>
          <li :class="{active: activeMenu === 'users'}" @click="activeMenu = 'users'">用户管理</li>
          <li :class="{active: activeMenu === 'orders'}" @click="activeMenu = 'orders'">订单管理</li>
          <li :class="{active: activeMenu === 'settings'}" @click="activeMenu = 'settings'">系统设置</li>
        </ul>
      </aside>
      <section class="admin-content">
        <div v-if="activeMenu === 'dashboard'">
          <h2>仪表盘</h2>
          <p>欢迎来到后台管理系统！</p>
        </div>
        <div v-else-if="activeMenu === 'users'">
          <h2>用户管理</h2>
          <p>这里是用户管理页面。</p>
        </div>
        <div v-else-if="activeMenu === 'orders'">
          <h2>订单管理</h2><el-button @click="test">测试</el-button>
          <p>这里是订单管理页面。</p>
        </div>
        <div v-else-if="activeMenu === 'settings'">
          <h2>系统设置</h2>
          <p>这里是系统设置页面。</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
const activeMenu = ref('dashboard');
const test = () => {
  // 点击按钮后，页面会跳转到指定地址
  console.log("test")
//   axios.get('http://192.168.0.100:2375/version').then(res => {
//     console.log(res)
//   })
  axios.get('http://127.0.0.1:5000/host_api/v1/reboot_host/192.168.0.100').then(res => {
    console.log(res)
  })
}
</script>

<style scoped>
.admin-layout {
  min-height: 100vh;
  background: #f5f6fa;
}
.admin-header {
  height: 56px;
  background: #222e3c;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
}
.logo {
  font-size: 20px;
  font-weight: bold;
}
.user-info {
  display: flex;
  align-items: center;
}
.avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  margin-right: 10px;
  border: 2px solid #fff;
}
.username {
  font-size: 16px;
}
.admin-main {
  display: flex;
  min-height: calc(100vh - 56px);
}
.admin-sidebar {
  width: 200px;
  background: #fff;
  box-shadow: 2px 0 8px rgba(0,0,0,0.03);
  padding-top: 24px;
}
.admin-sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.admin-sidebar li {
  padding: 14px 32px;
  cursor: pointer;
  color: #222e3c;
  font-size: 16px;
  transition: background 0.2s, color 0.2s;
}
.admin-sidebar li.active,
.admin-sidebar li:hover {
  background: #007bff;
  color: #fff;
}
.admin-content {
  flex: 1;
  padding: 32px;
}
</style>
