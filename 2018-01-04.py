'''
1.deque 生成固定大小的队列，先进先出
from colleections import deque
用法:
q = deque(maxlen = n)
更一般的，deque 类可以被用在任何你只需要一个简单队列数据结构的场合。如果
你不设置最大队列大小，那么就会得到一个无限大小队列，你可以在队列的两端执行添
加和弹出元素的操作。
使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并
且这个队列已满的时候，最老的元素会自动被移除掉。
在队列两端插入或删除元素时间复杂度都是 O(1) ，而在列表的开头插入或删除元
素的时间复杂度为 O(N)

2.
字符串的操作
2.1
re.split(分割字符串）
2.2 字符串开头或结尾匹配
str.startwith()
str.endwith()
'''
from collections import deque
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.appendleft(1)
print(q)

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
import os
result = re.split(r'[;,\s]\s*', line)
print(result)
main_c = os.listdir(path='C:')
print(any(name.endswith(('.py', '.h')) for name in os.listdir()))

# '''字符串忽略大小写'''
# re,findall查找时传入参数flags=re.IGNORECASE
text = 'UPPER python, lower python, Mixed python'
list_re = re.findall('python', text, flags=re.IGNORECASE)
print(list_re)
# 正则匹配默认贪婪匹配，正则表达式以？符号结尾将以最短字符匹配。
# （.*?)
# .不会匹配空格 传入re.DOTALL
#
text_1 = 'UPPER python\n '\
         'lower python, ' \
         'Mixed python'
print(re.findall(r'(.*?)python', text_1, re.DOTALL))


# 字符串替换replace
text_2 = 'hello    world'
print(re.sub('\s+',' ',text_2))
# print(text_2.replace(' ',''))
# 格式化字符串，
text_3 = 'hello'
print(format(text_3,'>20'))
print(format(text_3,'^20'))
print(format(text_3,'=<20'))
f_num = 1.234
print(format(f_num,'.1f'))
print('{:.1f}{:.2f}'.format(f_num,f_num))









