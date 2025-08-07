@echo off
echo ========================================
echo 后台管理系统启动脚本
echo ========================================
echo.

echo 1. 检查Python环境...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python未安装或未添加到PATH
    pause
    exit /b 1
)

echo.
echo 2. 启动Flask后端服务...
cd backend
start "Flask Backend" cmd /k "echo 正在启动后端服务... && pip install -r requirements.txt && python app.py"

echo 等待后端服务启动...
timeout /t 8 /nobreak > nul

echo.
echo 3. 测试后端连接...
cd ..
python test_connection.py

echo.
echo 4. 启动Vue前端服务...
cd frontend
start "Vue Frontend" cmd /k "echo 正在启动前端服务... && npm install && npm run dev"

echo.
echo ========================================
echo 服务启动完成！
echo ========================================
echo 前端地址: http://localhost:3000
echo 后端地址: http://localhost:5000
echo 默认账户: admin / admin123
echo.
echo 如果遇到问题，请检查：
echo 1. 端口5000和3000是否被占用
echo 2. 防火墙是否阻止了连接
echo 3. 浏览器控制台是否有错误信息
echo.
pause 