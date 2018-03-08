#  1、装饰器
import time
from functools import wraps, partial

# 装饰器(函数闭包的应用)
# 通常使用functools.wraps来注解一个装饰器
# 使用@wraps(func)能够保留原始函数的元数据


def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@time_this
def count_time(n):
    while n > 0:
        n -= 1
        print('1')

# count_time(10000)


#  2、装饰器作用在某个函数上，保留函数的重要的元信息比如名字、文档字符串、注解和参数签名
def loging(func):
    def log(*args ,**kwargs):
        print(func.__name__ + " is running")
        return func
    return log
@loging
def countdown(n):
    while n>0:
        n -= 1
countdown(100000)
# count_time(100000)
print(countdown.__name__)
# out:log
# 使用@wraps包装后的函数是名称还是count_time,
print(count_time.__name__)
# out:count_time
# @wraps另外一个重要的属性就是可以访问装饰之前的函数
# 访问方法 count_time.__wrapped__
count_time.__wrapped__(10)
