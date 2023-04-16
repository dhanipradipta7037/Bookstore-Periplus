from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
import time

data =[]
s = HTMLSession()

for x in range(1, 6):
    url = f'https://www.periplus.com/product/Search?filter_name=python&filter_category_id=0&author=&format=all&availability=In%20Stock&page={x}'
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    products = soup.find_all('div', class_='product-content product-contents')
    time.sleep(10)

    for item in products:
        try:
            nama = item.find('h3').text.strip()
        except:
            nama = 'None'
        
        try:
            format = item.find('div', class_='product-binding').text.strip()
        except:
            format = 'None'
        
        try:
            penulis = item.find('div', class_='product-author author-category').text.strip()
        except:
            penulis = 'None'
        
        try:
            Harga = item.find('div', class_='specials2').text.strip()
        except:
            Harga = 'None'
        
        lists = {'Nama Buku':nama,
                'Format Buku':format,
                'Penulis Buku':penulis,
                'Harga Buku':Harga
                }
        data.append(lists)

df = pd.DataFrame(data)
print(df)


