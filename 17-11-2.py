import pymysql
from pyecharts import Bar, Line, Pie
from pyecharts import Page
connnect = pymysql.connect(host='localhost', port=3306, user='root', password='password', db='mytest',charset='utf8')
cursor = connnect.cursor()
cursor.execute('select * from house_info')
house_infos = cursor.fetchall()
connnect.commit()
cursor.close()
connnect.close()
print(house_infos)
house_area = dict()
house_price = dict()

'''初始化字典 '''
house_area['<60m²'] = 0
house_area['60m²-80m²'] = 0
house_area['80m²-100m²'] = 0
house_area['100m²-120m²'] = 0
house_area['>120m²'] = 0
house_price['<8500元'] = 0
house_price['8500-9500元'] = 0
house_price['9500-10000'] = 0
house_price['10000']
for house_info in house_infos:
    #  面积数据
    house_areas = house_info[-5].split('m²')[0]
    #  房价数据
    house_prices = house_info[-2].split('元')[0]

    if int(house_areas) < 60:
        house_area['<60m²'] += 1
    elif 60 <= int(house_areas) < 80:
        house_area['60m²-80m²'] += 1
    elif 80 <= int(house_areas) < 100:
        house_area['80m²-100m²'] += 1
    elif 100 <= int(house_areas) < 120:
        house_area['100m²-120m²'] += 1
    elif int(house_areas) >= 120:
        house_area['>120m²'] += 1

page = Page()
bar = Bar('九龙坡区二手房信息')
bar.add('房屋面积', list(house_area.keys()), list(house_area.values()), is_stack=True)
page.add(bar)
line = Line('九龙坡区二手房信息')
line.add('房屋面积', list(house_area.keys()), list(house_area.values()),line_opacity=1,
             mark_point=['max', 'min'], label_color='red'
         )
page.add(line)
pie= Pie('九龙坡区二手房信息')
pie.add('房屋面积', list(house_area.keys()), list(house_area.values()),is_label_show=True, legend_pos='left')
page.add(pie)
page.render()









