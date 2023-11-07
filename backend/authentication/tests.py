from django.test import TestCase
import requests as rq

# Create your tests here.
payload = {
    "email": "test@gmail.com",
    "password": "MyPassword"
}
response = rq.post("http://127.0.0.1:8000/api/user/login/", data=payload)
print(response.status_code, response.json())
