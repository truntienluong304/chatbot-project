import requests

url = 'http://localhost:5000/chatbot'
question = "Nhiễm trùng sơ sinh là gì?"
response = requests.post(url, json={'question': question})

print(response.json()['answer'])
