import requests

response = requests.get('http://127.0.0.1:5000/bla')
response2 = requests.post('http://127.0.0.1:5000/dog', json={'my_name': 50})
print(type(response2))
print(response2.text)
