import requests as rq 
from bs4 import BeautifulSoup as bs
import configs
from tqdm import tqdm
url = configs.SITE_URL
save_address = configs.FILE_ADDRESS
tags = configs.ICONS_TAG_ADDR

# this for loop go through all pages from 1 to 179 in arzdigital website
for page in range(1, 179):
    res = rq.get(url + str(page))
    if res.status_code == 200:
        print('web site is good')
        
    soup = bs(res.text, 'html.parser')
    all_tags = soup.find_all('td', class_= tags)
    print(f'Page:{page}, {len(all_tags)} coins,')
    
    # getting name and image src of coins
    coin_names, coin_icon = [], []
    for name in all_tags:
        coin_names.append(name.a.span.text)
    for imgs in all_tags:
        coin_icon.append(imgs.a.i.img.get('data-src'))
    
    # concatinating names with sources
    concatinate = list(zip(coin_names, coin_icon))

    # this for loop is for getting icons src and downloading,,
    for coin in concatinate:
        contents = rq.get(coin[1], stream=True)
        with open(save_address + coin[0] + '.png', 'wb') as f:
            f.write(contents.content)
