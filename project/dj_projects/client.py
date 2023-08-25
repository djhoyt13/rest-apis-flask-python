import requests
url = 'http://127.0.0.1:5000/store'


payload = {}

headers = {"Content-Type": "application/json"}

response = requests.request("GET", url, json=payload, headers=headers)

print(response.text)

#with open("./seerist_response.json", "w") as file:
#    file.write(response.text)

print("All Done...")