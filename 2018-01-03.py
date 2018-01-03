'''
命名元祖collections.namedtuple的用法
from collections import Chainmap/
一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。然后，这些字典并
不是真的合并在一起了，ChainMap 类只是在内部创建了一个容纳这些字典的列表并重
新定义了一些常见的字典操作来遍历这个列表。大部分字典操作都是可以正常使用的

'''

from collections import ChainMap
from collections import namedtuple
# 命名元祖 namedtuple
name_tuple = namedtuple('name_tuple',['x', 'y', 'z'])
# 赋值
p = name_tuple('a', 'b', 'c')
q = name_tuple('A', 'B', 'C')
print(p,'\n',q)
print(p.x, p.y, p.z)
#  namedtuple和普通元组的数据结构是一样的，可以进行解压赋值，迭代，索引等操作支持所有普通元祖的操作。
print(p[0])
# 修改namedtuple值
p = p._replace(x='A')
print(p)
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = ChainMap(a,b)
print(c)
# ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})
# 如果出现重复键，那么第一次出现的映射值会被返回。因此，例子程序中的 c['z']
# 总是会返回字典 a 中对应的值，而不是 b 中对应的值。
# 对于字典的更新或删除操作总是影响的是列表中第一个字典。比如
del c['z']
print(c)
# ChainMap({'x': 1}, {'y': 2, 'z': 4})
# 特别注意的是ChainMap不会更新字典需要使用update的方法，
b.update(a)
print(a)
print(b)

