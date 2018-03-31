#coding:utf-8

#数组元素去重

list = ['1.2','2.2','3.4','1.2.4']  # 具有重复元素的数组
list1= []                         #创建一个新的数组来存储无重复元素的数组
listArray = set(list)
print listArray
for element in list :
    if(element not in list1):
        list1.append(element)

print list1
