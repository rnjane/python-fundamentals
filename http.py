import requests

response = requests.get('https://api.github.com', auth=('user', 'pass'))

print(response.status_code)
print(response.headers['content-type'])