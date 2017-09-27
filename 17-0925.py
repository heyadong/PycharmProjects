from pyecharts import Geo, Page, Grid, Line
import random
data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
geo = Geo('全国空气质量', 'PM2.5', title_color="#fff", title_pos='center',background_color='red',
          width=1200, height=600)
attr, value = geo.cast(data)
geo.add("", attr, value, type='effectScatter',  effect_scale=5)
"""# page.add(geo)
data_1 = [('成都', 9), ('绵阳', 10)]
geo2 = Geo('成都市地图DEMO', title_color='#fff', background_color="")"""
grid = Grid()
#  折线图
line = Line()
attr_1 = ['a', 'b', 'c', 'd', 'e', 'f']
val = [random.randint(1,40) for _ in range(6)]
va2 = [random.randint(2,40) for _ in range(6)]
print(val)
line.add("A",attr_1, val, is_fill=True, line_opacity=0.2, area_opacity=0.4, is_smooth=True,symbol=None)
line.add('B',attr_1,va2, is_fill=True, line_opacity=0.2, area_opacity=0.4, is_smooth=True, )
line.render()

#grid.add(line,)
#grid.add(geo,)
#grid.render()

