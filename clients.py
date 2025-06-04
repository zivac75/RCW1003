import requests

url = 'rcw-test-first-evgmhsdsh4hgcwgt.canadaeast-01.azurewebsites.net/api/hello'

response = requests.get(url)
response =response.json()
print(response['message'])