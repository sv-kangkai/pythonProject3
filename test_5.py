import requests

url = 'https://link-target.net/416534/50-facts-in-breaking-bad'
username = 'sp31157243'
password = '1234567'

proxy = f'https://user-{username}:{password}@china-gate.visitxiangtan.com:8000'

response = requests.get(url, proxies={'http': proxy, 'https': proxy})

print(response.text)