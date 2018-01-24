#  基本日期和时间的操作
from datetime import datetime,timedelta
print(datetime(2018,1,19))
# datetime.now()返回当前时间
print(str(datetime.now()).split('.')[0])
#  创建一个生成器，生成指定日期内的所有时段


def date_range(start_date, end_date, step):
    while start_date<=end_date:
        yield start_date
        start_date += step

print([i for i in date_range(datetime(2018,1,19),datetime(2018,1,31),timedelta(days=1))])
# 3.字符串转化成日期：datetime.strptime(,'%Y-%m-%d)注意y是大写
text_time = '2017-09-18'
print(datetime.strptime(text_time,'%Y-%m-%d'))
# output:  2017-09-18 00:00:00

'''
    迭代器和生成器：
'''
# 代理迭代
class Node:
    def __init__(self,value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({})'.format(self._value)

    def add_children(self,node):
        self._children.append(node)

    def __iter__(self):
        '''__iter__方法返回一个迭代器'''
        return iter(self._children)
    def deep_iter(self):
        '''
            实现一个以深度优先方式遍历树形节点的生成器。
        '''
        yield self
        for c in self:
            # yield from 实现深度优先遍历树节点生成器：
            # 构建subgenerator
            yield from c.deep_iter()

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_children(child1)
root.add_children(child2)
child1.add_children(Node('a'))
child1.add_children(Node('b'))
child2.add_children(Node('A'))
for i in root.deep_iter():
    print(i)
# output:Node(0)
# Node(1)
# Node(a)
# Node(b)
# Node(2)
# Node(A)