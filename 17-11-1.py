import requests
from bs4 import BeautifulSoup
import re
import pymysql
url = 'https://chongqing.anjuke.com/sale/jiulongpo/p3/#filtersort'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
req = requests.get(url=url, headers=headers)
print(req.status_code)
html = req.text
#print(html)
soup = BeautifulSoup(html, 'html5lib')
house_details = soup.find_all('div', class_='house-details')
print(house_details)
prices = soup.find_all('div', class_="pro-price")
house_info = {}
house_infos = []
connect = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='mytest',charset='utf8')
cursor = connect.cursor()
'''
for house_detail in house_details:
    house_detail = str(house_detail)
    house_name = re.findall(r'target="_blank"\s+title="(.*?)">', house_detail)
    house_address = re.findall(r'<span class="comm-address" title="(.*?)">', house_detail)
    house_items = re.findall(r'<span>(.*?)</span><em class="spe-lines">\|</em><span>(.*?)</span>', house_detail)
    print(house_items)
    if len(house_items) == 2:
        cursor.execute('insert into house_info(name, address, house_room,house_area,house_floor,house_time) values(%s, %s, %s, %s, %s,%s)',
                       [house_name[0],
                        house_address[0],
                        house_items[0][0],
                        house_items[0][1],
                        house_items[1][0],
                        house_items[1][1]])
    else:
         cursor.execute('insert into house_info(name, address, house_room,house_area) values(%s, %s, %s, %s)',
                       [house_name[0],
                        house_address[0],
                        house_items[0][0],
                        hose_items[0][1]])

'''
print(house_infos)
house_id = 164
for price in prices:
    price = str(price)
    #  匹配价格信息
    house_prices = re.findall(r'<span class="price-det"><strong>(\d+)</strong>万</span><span class="unit-price">(.*?)</span>', price)
    print(house_prices)
    cursor.execute('update house_info set single_price=%s,house_price=%s where idhouse_info=%s',
                   (house_prices[0][1],
                    house_prices[0][0],
                    house_id))
    house_id += 1


connect.commit()
cursor.close()
connect.close()
"""
 house_info['name'] = house_name[0]
        house_info['address'] = house_address[0]
        house_info['house_room'] = house_items[0][0]
        house_info['house_area'] = house_items[0][1]
        house_info['house_floor'] = house_items[1][0]
        house_info['house_time'] = house_items[1][1]
        house_infos.append(house_info)"""





