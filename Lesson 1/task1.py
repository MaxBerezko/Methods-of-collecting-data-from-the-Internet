import requests
import json

user = 'MaxBerezko'
url = f'https://api.github.com/users/{user}/repos'

user_repos = requests.get(url).json()

with open('repos_names.json', 'w') as file:
    json.dump(user_repos, file)

for repo_name in user_repos:
    print(repo_name['name'])