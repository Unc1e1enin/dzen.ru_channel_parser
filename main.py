import requests
from bs4 import BeautifulSoup

for i in range(1, 251):
    url = f'https://dzen.ru/media/zen/channels?page={i}'
    headers = {
        'Accept': 
        'Accept-Encoding': 
        'Accept-Language': 
        'Cache-Control':,
        'Connection': 
        'Cookie': 
        'Host': 'dzen.ru',
        'Referer': 'https://sso.dzen.ru/',
        'Sec-Fetch-Dest':
        'Sec-Fetch-Mode': 
        'Sec-Fetch-Site': 
        'Sec-Fetch-User': 
        'Upgrade-Insecure-Requests': 
        'User-Agent': 
        'sec-ch-ua': 
        'sec-ch-ua-mobile': 
        'sec-ch-ua-platform': 
    }

    re = requests.get(url=url, headers=headers)
    # print(re.text)

    soup = BeautifulSoup(re.text, 'lxml')
    links = soup.find_all('a', 'channel-item__link')
    # print(links)

    for items in links:
        # print('https://dzen.ru' + items.get('href'))
        with open('links.txt', 'a+') as file:
            file.write('https://dzen.ru' + items.get('href') + '\n')
