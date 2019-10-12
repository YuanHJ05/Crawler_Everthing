import requests
# from .setting import TEST_URL
from ProxyPool.proxypool.setting import TEST_URL

proxy = 'http://localhost:5555/random'

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}

print(TEST_URL)
response = requests.get(TEST_URL, proxies=proxies, verify=False)
if response.status_code == 200:
    print('Successfully')
    print(response.text)