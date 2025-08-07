# 后台管理系统

一个基于 Vue 3 + Flask 的前后端分离后台管理系统，实现了完整的登录功能。

## 技术栈

### 后端
- Flask 2.3.3
- Flask-CORS (跨域支持)
- Flask-JWT-Extended (JWT认证)
- Flask-SQLAlchemy (数据库ORM)
- SQLite (数据库)
- bcrypt (密码加密)

### 前端
- Vue 3 (Composition API)
- Vue Router 4 (路由管理)
- Pinia (状态管理)
- Element Plus (UI组件库)
- Axios (HTTP客户端)
- Vite (构建工具)

## 项目结构

```
├── backend/                 # 后端Flask应用
│   ├── app.py              # 主应用文件
│   └── requirements.txt    # Python依赖
├── frontend/               # 前端Vue应用
│   ├── src/
│   │   ├── views/          # 页面组件
│   │   │   ├── Login.vue   # 登录页面
│   │   │   └── Dashboard.vue # 仪表板页面
│   │   ├── stores/         # Pinia状态管理
│   │   │   └── auth.js     # 认证状态管理
│   │   ├── router/         # 路由配置
│   │   │   └── index.js    # 路由定义
│   │   ├── App.vue         # 根组件
│   │   └── main.js         # 应用入口
│   ├── index.html          # HTML模板
│   ├── package.json        # 前端依赖
│   └── vite.config.js      # Vite配置
└── README.md               # 项目说明
```

## 功能特性

- ✅ 用户登录/登出
- ✅ JWT Token认证
- ✅ 路由守卫
- ✅ 响应式仪表板
- ✅ 用户信息显示
- ✅ 现代化UI设计

## 快速开始

### 1. 启动后端服务

```bash
# 进入后端目录
cd backend

# 安装Python依赖
pip install -r requirements.txt

# 启动Flask服务
python app.py
```

后端服务将在 `http://localhost:5000` 启动

### 2. 启动前端服务

```bash
# 进入前端目录
cd frontend

# 安装Node.js依赖
npm install

# 启动开发服务器
npm run dev
```

前端服务将在 `http://localhost:3000` 启动

### 3. 访问系统

打开浏览器访问 `http://localhost:3000`

## 默认账户

- 用户名：`admin`
- 密码：`admin123`

## API接口

### 认证相关

- `POST /api/login` - 用户登录
- `GET /api/profile` - 获取用户信息
- `GET /api/health` - 健康检查

### 请求示例

```bash
# 登录
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# 获取用户信息 (需要JWT Token)
curl -X GET http://localhost:5000/api/profile \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## 开发说明

### 后端开发

- 数据库使用SQLite，数据文件位于 `backend/admin_system.db`
- JWT Token有效期为24小时
- 密码使用bcrypt加密存储

### 前端开发

- 使用Vue 3 Composition API
- 状态管理使用Pinia
- UI组件使用Element Plus
- 路由使用Vue Router 4

### 跨域配置

前端已配置代理，API请求会自动转发到后端：
- 开发环境：`/api/*` → `http://localhost:5000/api/*`

## 部署说明

### 后端部署

```bash
# 生产环境启动
export FLASK_ENV=production
python app.py
```

### 前端部署

```bash
# 构建生产版本
npm run build

# 部署dist目录到Web服务器
```

## 许可证

MIT License 