import requests

response = requests.get("http://api.github.com")

response.raise_for_status
print("status Code", response.status_code)
data=response.json()
print(data["current_user_url"])


#post--call

payload ={"prompt": "HELLO","max_token": "50","temp": "2"}
headers = {"Authentication":"Bearer Fake_Key"}


post = requests.post(
    "http://httpbin.org/post",
    json=payload,
    headers=headers,
    timeout=20

)

post.raise_for_status()
enchoed_data = post.json()
print(enchoed_data)
