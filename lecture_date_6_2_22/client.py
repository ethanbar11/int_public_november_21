import requests

response = requests.get('http://127.0.0.1:5000/hello')
response2 = requests.post('http://127.0.0.1:5000/validate_snake', json={'snake': 50})
print(response.text)
print(response2.text)
