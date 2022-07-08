import requests

result = requests.get('http://127.0.0.1:8000/job/?name=Job1')

print(result.text)

print(result.status_code)
print(result.headers['content-type'])
print(result.encoding)
print(result.text)
print(result.json())
