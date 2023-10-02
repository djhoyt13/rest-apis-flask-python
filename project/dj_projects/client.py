import requests
url = 'http://127.0.0.1:5000/store'


'''
Create GET Request
'''
# payload = {
#     "name": "My Store"
# }

# headers = {"Content-Type": "application/json"}

# response = requests.request("GET", url, json=payload, headers=headers)

# print(response.text)

# with open("./seerist_response.json", "w") as file:
#    file.write(response.text)

# print("All Done...")

'''
Create POST Request
'''

# payload = {
#     "name": "My Store"
# }

# headers = {"Content-Type": "application/json"}

# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)

'''
Creat Items in each store
'''

# url = 'http://127.0.0.1:5000/store/My Store/item'
url = 'https://workspaces/rest-apis-flask-python/project/dj_projects/client.py/store/My Store/item'

payload = {
    "name": "Table",
    "price": 17.99
}

headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

print("All Done...")