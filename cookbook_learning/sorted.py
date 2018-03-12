a = [1,2,3,11,5,6,8,23,3]
def sort_func(b):
    for i in range(len(b)):
        for k in range(len(b)-1):
            if b[k]>b[k+1]:
                b[k],b[k+1] = b[k+1],b[k]
    return b
def sort_func1(list1):
    for i in range(len(list1)-1):
        for k in range(i+1,len(list1)):
            if list1[i]>list1[k]:
                list1[k],list1[i] = list1[i],list1[k]
    return list1
print(sort_func(a))
print(sort_func1(a))