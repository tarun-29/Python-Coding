import requests 
url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url, headers={"Accept" : "application/json"}, params={"term":"cat"})

data = response.json()
print(data['setup'])
print(data['punchline'])