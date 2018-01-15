def func1(n=5,m=3):
    none_list = []
    for i in range(1, m+1):
        none_list.append(i*n)
        n +=1
    return n, none_list
print(func1(10))
print(func1(m=4))
print(func1(n=3))
print(func1(7,5))
print(func1(m=3))
import cmath
# cmath支持复数运算，运算结果显示为复数
import math
# 复数
a = complex(1,2)
# print(a)
# 三角函数
# cmath复数
print(cmath.sin(60))
import math
print(math.sin(60))
# round四舍五入，保留小数，接受两个参数，round（float,位数)
# print(round(1.23,1))
# 数字化格式输出
# 'string {空格数,.2f}'.format(x)
x = 1235.6789
y = 'the number is {:0.2f}'.format(x)
print(y)
print(format(x,'40.2f'))
# 分数运算
# 用法
# Fraction(分子，分母）
from fractions import Fraction
a = Fraction(4,5)
b = Fraction(7,16)
print(a+b)
c = a*b
print(c.numerator)
print(c.denominator)
# 转化成浮点数
d = float(c)
print(float(c))
# 列表和数组的区别
m1 = [1,2,3]
m2 = [4,5,6]
print(m1+m2)
# print(m1*m2)
# print(m1+10) 语法错误
import numpy as np
m3 = np.array(m1)
m4 = np.array(m2)
print(m3,m4)
print(m3+m4)
print(m3*m4)
print(m3+10)
# 矩阵和线性代数运算
m5 = np.matrix([m1,
               m2,
               [7,8,9]])
print(m5)
