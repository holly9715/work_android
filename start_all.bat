@echo off
echo 启动后台管理系统...
echo.

echo 1. 启动Flask后端服务...
start "Flask Backend" cmd /k "cd backend && pip install -r requirements.txt && python app.py"

echo 等待后端服务启动...
timeout /t 5 /nobreak > nul

echo 2. 启动Vue前端服务...
start "Vue Frontend" cmd /k "cd frontend && npm install && npm run dev"

echo.
echo 服务启动完成！
echo 前端地址: http://localhost:3000
echo 后端地址: http://localhost:5000
echo.
echo 按任意键退出...
pause > nul 