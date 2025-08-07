import requests
import json

# 测试后端API
def test_backend():
    base_url = "http://localhost:5000"
    
    # 测试健康检查
    try:
        response = requests.get(f"{base_url}/api/health")
        print(f"健康检查: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"健康检查失败: {e}")
        return
    
    # 测试登录
    try:
        login_data = {
            "username": "admin",
            "password": "admin123"
        }
        response = requests.post(
            f"{base_url}/api/login",
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"登录测试: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"登录成功: {data.get('message')}")
            token = data.get('access_token')
            
            # 测试获取用户信息
            if token:
                headers = {"Authorization": f"Bearer {token}"}
                profile_response = requests.get(f"{base_url}/api/profile", headers=headers)
                print(f"获取用户信息: {profile_response.status_code}")
                if profile_response.status_code == 200:
                    print(f"用户信息: {profile_response.json()}")
        else:
            print(f"登录失败: {response.json()}")
    except Exception as e:
        print(f"登录测试失败: {e}")

if __name__ == "__main__":
    test_backend() 