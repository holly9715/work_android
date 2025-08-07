import requests
import time

def test_connection():
    print("测试后端连接...")
    
    # 等待后端启动
    time.sleep(2)
    
    try:
        # 测试健康检查
        response = requests.get('http://localhost:5000/api/health')
        print(f"✅ 后端连接成功: {response.status_code}")
        print(f"响应内容: {response.json()}")
        
        # 测试登录
        login_data = {
            "username": "admin",
            "password": "admin123"
        }
        
        response = requests.post(
            'http://localhost:5000/api/login',
            json=login_data,
            headers={'Content-Type': 'application/json'}
        )
        
        print(f"✅ 登录测试: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"登录成功: {data.get('message')}")
            print(f"Token: {data.get('access_token')[:20]}...")
        else:
            print(f"登录失败: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ 无法连接到后端服务，请确保后端正在运行")
    except Exception as e:
        print(f"❌ 测试失败: {e}")

if __name__ == "__main__":
    test_connection() 