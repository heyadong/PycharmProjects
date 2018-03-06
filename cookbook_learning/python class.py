# 1、创建大量对象时节省内存的方法
_formats = dict(ymd='{d.year}-{d.month}-{d.day}', mdy='{d.month}/{d.day}/{d.year}',
                dmy='{d.day}/{d.month}/{d.year}')


class Date(object):
    '''
    给类添加属性__slot__可以节省实例化所需要内存
    但使用__slots__方法后不能再给类添加新的属性，只能通过__slots__添加
    '''
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        # __format__方法可以格式化类的显示方式
        # 改变format方法
        if not format_spec:
            format_spec = 'ymd'
        fmt = _formats[format_spec]
        return fmt.format(d=self)

    # 使对象支持上下文管理。

    def __enter__(self):
        return format(self, 'ymd')

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


now_date = Date('2018', '03', '05')
print(format(now_date, 'mdy'))
# 2、让对象支持上下文管理方法
"""
原理：编写上下文管理器的主要原理是你的代码会放到 with 语句块中执行。当出现 with
语句的时候，对象的 __enter__() 方法被触发，它返回的值 (如果有的话) 会被赋值给
as 声明的变量。然后，with 语句块里面的代码开始执行。最后，__exit__() 方法被触
发进行清理工作。
 __enter__ 方法 使用with语句时调用 并将返回值传给as后的参数 date"""
with now_date as date:
    print(date)


# 3 Python 中类中的属性和方法的访问控制
# 在类名和方法名上添加下划线 _name,或者__name.
# 类中以单下划线开头的属性和方法，是内部方法，不能限制外部访问。子类可以继承和修改属性和方法
# 以双下划线开头的变量名和方法。子类将不能继承,访问名称变成其他形式 _Classname__function_name
class A:
    def __init__(self):
        self.__private = 0
        self._inprivate = '内部私有变量可以继承'
        self.public = 1

    def public_method(self):
        try:
            print("打印对象的私有变量：{}".format(self.__private))
        except:
            print("不能访问")

    def __private_method(self):
        print('我是A类的独有方法！并且不能被继承')

    def _inprivate_method(self):
        print("我是内部的方法")


class B(A):
    def __init__(self):
        super().__init__()
        self.__private = "更改后的私有变量"

    def _inprivate_method(self):
        print('更改后的内部方法')

    def __private_method(self):
        super().public_method()
        print("我是B类的独有方法,访问方式_B__private_method")


c = B()
# d = A()
# print(c._inprivate)
# c._B__private_method()
c._inprivate_method()

# 3、子类调用父类方法:
# 使用super(）方法:
# super().father_function()
# 4、python 的继承原理
# 每一个类，Python 会计算出一个所谓的方法解析顺序 (MRO) 列表。这个 MRO
# 列表就是一个简单的所有基类的线性顺序表。继承是按照从左到右的方式查找对应的方法
print(B.__mro__)


# out：(<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


# 4、类中的@property创建可以管理的属性
class Students:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = value

    # 禁止删除属性操作
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete a attribute")


a1 = Students('niaho')
a1.name = "nihao"
# 4.1、property 还有一种创建动态属性的方法
# 如下定义圆的面积，只有在访问该属性时才会计算出来。

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def print_radius(self):
        print(self.radius)

    @property
    def area(self):
        '''
        计算圆面积
        :return:
        '''
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        '''
        计算圆的直径
        :return:
        '''
        return self.radius * 2

    @property
    def perimeter(self):
        """
        计算圆周长
        """
        return 2 * math.pi * self.radius


my_circle = Circle(2)
print(my_circle.area, my_circle.diameter)
# 类常用方法hasattr, getattr() setattr()
# hasattr() 判断类中是否有这个方法和属性,返回True和False
print(hasattr(Circle, 'perimeter'))
# getattr() 获取到类中的属性和方法，获取方法后可以运行(getattr()())
getattr(my_circle, 'print_radius')
getattr(my_circle, 'radius')
# setattr() 为类属性赋值,如果类中没有属性，添加属性后赋值。

# 5、不使用__init__实例化一个对象：
my_student = Students.__new__(Students)
# in：print(my_student.name)
# out:AttributeError: 'Students' object has no attribute '_name'
setattr(my_student, 'name', 'heyadong')
print(my_student.name)


# 6、通过字符串调用对象的方法：
# 1、使用getattr()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x1, y1):
        return math.hypot(self.x - x1, self.y - y1)

    def __repr__(self):
        return 'Point(%r,%r)' % (self.x ,self.y)


points = [Point(1, 2),Point(3, 0),Point(10, -3),Point(-5, -7), Point(-1, 8),Point(3, 2)]
points1 = points[:]
points2 = points.copy()
points1.sort(key=lambda r: r.distance(0,0),reverse=True)
print('排序后')
print(points1)


