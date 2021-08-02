#   Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, 
#   пройдя авторизацию. Ответ сервера записать в файл.

import requests
import json

url = 'https://postman-echo.com/basic-auth'
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.3.757 Yowser/2.5 Safari/537.36',
    'Authorization': 'Basic cG9zdG1hbjpwYXNzd29yZA=='
}
    
answer = requests.get(url, headers=headers)

with open('answer.json', 'w') as file:
    json.dump(answer.json(), file)









