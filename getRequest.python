import requests
import json
result = (requests.get("https://jsonplaceholder.typicode.com/todos").text)

print(type(result)) #str

result = json.loads(result)
print(type(result)) #list
print(result[0])
print(result[0]["userId"])
