import requests


api_url = 'http://127.0.0.1:8000/authorization/'


login_data = {
    'username': 'sayf',
    'password': 'sayf'
}


response = requests.post(api_url, json=login_data)


if response.status_code == 200:
    print("Login successful!")
    token = response.json().get('token')
    print(f"Authentication Token: {token}")
else:
    print("Login failed. Status code:", response.status_code)
