import requests
import json

response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    if 'Python' in data['title']:
        print(data['title'])
        print(data['link'])
        print(data['answer_count'])