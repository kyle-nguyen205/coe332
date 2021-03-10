import requests

def print_content(response):
    print(response.status_code)
    print(response.json())
    print(response.headers)

response1 = requests.get(url='http://localhost:5025/animals')
response2 = requests.get(url='http://localhost:5025/animals/body/oyster')
response3 = requests.get(url='http://localhost:5025/animals/head/bunny')

print_content(response1)
print_content(response2)
print_content(response3)
