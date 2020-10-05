
# Chapter 2

# 反正最后的程序跑出来还是在这个里面
# 不管是什么，可能一些重要成果就是通过python直接跑出来了

# import keyword
# print(keyword.kwlist)

#
# name = '玛丽亚'
# print(name)
# print(id(name)) # 标识
# print(type(name)) # 类型

# 浮点类型
# n1 = 1.1
# n2 = 2.2
# print(n1+n2)
# from decimal import Decimal
# print(Decimal ('1.1')+Decimal ('2.2'))

# 布尔类型
# f1 = True
# f2 = False

# 字符串类型
# ''  ""  """ """   ''' '''都可以
# str1 = '''干'''
# str2 = """干"""
# print(str1, type(str1))

# 数据类型转换
# 为什么需要这个转换？需要拼接
# 包括int(), str(), float()等函数

# 中文编码声明注释
# coding: utf-8


# Chapter 3

# 输入函数input()
# present = input('要什么礼物')
# print(present)
# i1 = input('intg 1')
# i2 = input('intg 2')
# print((int(i1)+int(i2)))
# sum([10,20])
# print(sum([0,1,2]))

# 各种运算符
# **是幂运算， %是取余 //是整除
# 整除注意正负数

# 运算符
# 链式赋值a=b=c=20
# a = 20
# b = 10
# print(a, id(a), b, id(b))
# 系列解包赋值：
# a,b,c=20,30,40
# print(a,b,c)
# 交换
# a,b = b,a
# 比较运算符的结果为bool类型
# 一个变量由三部分组成：标识、类型、值
# ==比较的是值，is/is not比较的是标识
# a = 10
# b = 10
# print(a is b) # True
# list1 = [11,22,33]
# list2 = [11,22,33]
# print(list1 is list2) # False，id不一样
# 布尔运算符：and, or, not, in, not in;
# s = 'helloworld'
# print('w' in s) # True
# 位运算符&, |, >>, <<
# print(4&8) # 按二进制与
# 运算符优先级
# 算术运算符--位运算--比较运算（得出true/false）--布尔运算（拿true/false进行运算）--赋值运算


# chapter 4


# 程序的组织结构
# 顺序--选择--循环
# python一切皆对象，所有对象都有一个bool值，用bool()函数查看
# 测试对象的布尔值
# print(bool(False))
# print(bool([])) # 空列表
# print(bool(list())) # 空列表
# print(bool(tuple())) # 空元组
# print(bool({})) # 空字典
# print(bool(dict())) # 空字典
# print(bool(set())) # 空集合

# 选择结构：银行取款
# money = 1000 # 余额
# s = int(input('请输入取款金额')) # 取款金额
# 判断余额是否充足
# if money >= s:
#     money = money - s
#     print('取款成功，余额为：', money)

# 双分支结构，判断奇偶数
# num = int(input(('请输入一个整数')))
# if num%2 == 0:
#     print(num, '是偶数')
# else:
#     print(num, '是奇数')

# 多分支结构
# score = int(input('请输入一个成绩：'))
# score = input('请输入一个成绩：') # input得到的是string类型
# print(score, type(score))
# if score >= 90 and score <= 100: # 或者可以写成，90<=score<=100
#     print('A')
# elif score >=80 and score <= 89:
#     print('B')
# else:
#     print('error')

# 嵌套if
# 会员打折
# answer = input('您是会员吗？y/n')
# money = float(input('请输入您的购物金额：'))
# if answer == 'y':
#     if money >= 200:
#         print('打8折，付款金额为：', money * 0.8)
#     elif money >= 100:
#         print('打8折，付款金额为：', money * 0.9)
#     else:
#         print('不打折，付款金额为：', money)
# else:
#     if money >= 200:
#         print('打9.5折，付款金额为：', money * 0.95)
#     else:
#         print('不打折，付款金额为：', money)

# 条件表达式：将多行写成一行
# a = 10
# b = 20
# print(a) if a >= b else print(b)

# pass语句，只是占位符，还没想好程序怎么写
# if a >= b:
#     pass
# else:
#     pass

# 对象的布尔值：可以直接把对象放到条件表达式！
# age = int(input('请输入您的年龄'))
# if age:
#     print(age)
# else:
#     print('年龄为：', age)


# Chapter 5

# 内置函数range()：直接使用
# 三种创建方式
# 1
# r = range(10) # 默认从0开始，步长为1
# print(r)
# print(list(r)) # 用于查看range对象中的整数序列
# 2
# r = range(1, 10) # 指定了从1开始
# print(list(r))
# 3
# r = range(1, 10, 3)
# print(list(r))
# 判断指定的整数在序列中是否存在
# print(10 in r)
# print(10 not in r)

# 循环结构
# a = 0
# sum1 = 0
# while a <= 4:
#     # print(a)
#     sum1 = sum1 + a
#     a = a + 1
# print(sum1)
# 计算1-100之间的偶数和
# a = 0
# sum1 = 0
# while (a%2 == 0 and a <= 100): # & 是位运bai算；and 是逻辑运算
#     sum1 = sum1 + a
#     a = a + 2
# print(a, sum1)
# for-in循环
# in表达从（字符串、序列等）中依次取值，又称为遍历
# for item in 'Python': # 第一次取出来的是P
#     print(item)
# for item in range(1, 10):
#     print(item)
# 可以用下划线_表示不需要用到的变量
# for _ in range(1, 5):
#     print('gan')
# sum1 = 0
# for i in range(1, 101, 1):
#     if i%2 == 0:
#         sum1 = sum1 + i
# print(sum1)

# 流程控制语句break，输密码
# for item in range(3):
#     pwd = input('请输入密码')
#     if pwd == '8888:
#         break
#     else:
#         print('密码不正确')
# continue
# 输出1-50之间的所有5的倍数
# for item in range(1,51):
#     if item%5 != 0:
#         continue
#     print(item)

# else 语句，可以与for/while搭配使用
# for item in range(3):
#     pwd = input('请输入密码')
#     if pwd == '8888':
#         break
#     else:
#         print('密码不正确')
# else:
#     print('三次密码均错误')

# 嵌套循环
# 打印三行四列的矩形
# for i in range(1, 4): # 行数
#     for j in range(1, 5):
#         print('*', end = '\t') # 不换行输出
#     print()
# 打印99乘法表。先打一个直角三角形，9行，每行1-9个*
# for i in range(1, 10): # 行数
#     for j in range(1, i+1):
#         # print('*', end = '\t')
#         print(i, '*', j, '=', i*j, end = '\t')
#     print()
# 二重循环中的break和continue



# Chapter 6

# 一次排开

# 列表
# 列表相当于书包
# 列表相当于其他语言中的数组
# 可以存储不同类型的对象：int, float, string
# a = 10 # 变量存储的是一个对象的引用。id, type, value
# lst = ['hello', 'world', 98]
# print(id(lst))
# print(type(lst))
# print(lst)
# list存储的是一个id，这个id指向三个对象的id，然后就会输出三个对象的值

# 列表创建：使用中括号，或者调用内置函数list()
# lst1 = ['hello', 'world', 98]
# print(lst1[0]) # 列表的调用，索引从0开始
# print(lst1[-3]) # 也可以从负数开始
# lst2 = list(['hello', 'world', 98])

# 列表的查询操作，类似于matlab的find函数了
# lst = ['hello', 'world', 98, 'hello']
# print(lst.index('hello')) # 只返回第一个相同元素的索引
# print(lst.index('python'))
# 在指定的范围内查找索引
# print(lst.index('hello', 1, 3)) # 左闭右开，从1开始，1，2.但是索引从0开始，所以找不到

# 获取列表的单个元素：给我索引，0-(N-1)
# lst = ['hello', 'world', 98, 'hello', 'world', 234]
# print(lst[2])
# 获取列表的多个元素：切片
# 列表名[start:stop:step]
# lst = [10, 20, 30, 40 ,50 ,60, 70, 80]
# print(lst[1:6:1])
# lst2 = lst[1:6:1]
# print('原列表的id', id(lst))
# print('新列表的id', id(lst2))
# step为负数的话，则第一个元素是列表的最后一个元素

# 判断指定的元素在列表中是否存在
# lst = ['hello', 'world', 98, 'hello']
# print(10 in lst)
# 列表元素的遍历
# lst = ['hello', 'world', 98, 'hello']
# for item in lst:
#     print(item)

# 列表元素的增删改
# 向列表的末尾添加一个元素
# lst = [10, 20, 30]
# print('添加元素之前', lst, id(lst))
# lst.append(100)
# print('添加元素之后', lst, id(lst))
# extend
# lst2 = ['hello', 'world']
# lst.append(lst2) # [10, 20, 30, 100, ['hello', 'world']]
# lst.extend(lst2) # [10, 20, 30, 100, 'hello', 'world']
# print(lst)
# insert 在任意位置添加
# lst.insert(1, 90)
# print(lst)
# 在任意的位置上添加N多元素，切片
# lst3 = [True, False, 'hello']
# lst[1:] = lst3
# print(lst) # 把list[1]后面的全都切掉了，算覆盖

# 列表元素的删除操作
# remove
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30) # 从列表中移除一个元素，如果有重复元素，只移除第一个
print(lst)
# pop()根据索引移除元素
lst.pop(1)
print(lst)
# lst.pop(5) # 如果索引位置不存在，将报错
lst.pop() # 如果不指定参数，将删除列表中的最后一个元素
print(lst)
# 切片：一次至少删除一个元素，将产生新的列表对象
new_lst = lst[1:3]
print('原列表', lst)
print('切片后的列表', new_lst)
# 不产生新的列表对象，而删除原列表的元素
lst[1:3] = []
print(lst)
# clear：清除列表
lst.clear()
print(lst)
# del语句删除列表对象
# del lst
# print(lst)

# 列表元素的修改操作
# lst = [10, 20, 30, 40]
# # 一次修改一个值
# lst[2] = 100
# print(lst)
# lst[1:3] = [300, 400, 500, 600]
# print(lst)

# 列表的排序操作
# sort()
# reverse = True
# lst = [20, 40, 10, 98, 54]
# print('排序前的列表', lst, id(lst))
# lst.sort()
# print('排序后的列表', lst, id(lst))

# 降序排列
# lst.sort(reverse = True)
# print(lst)
# 内置函数sorted()，将产生新的列表对象
# lst = [20, 40, 10, 98, 54]
# print('原列表', lst)
# new_lst = sorted(lst)
# print(lst)
# print(new_lst)
# 指定关键字参数
# dese_lst = sorted(lst, reverse = True)
# print(dese_lst)

# 列表生成式
# lst = [i*i for i in range(1, 10)]
# print(lst)
# lst2 = [i*2 for i in range(1, 6)]
# print(lst2)
# r = range(1, 5)
# print(list(range(1, 5))) # 生成1, 2, 3, 4


# Chapter 夫妻站：字典

# 什么是字典
# 列表是有序序列
# python内置的数据结构之一，与列表一样是一个可变序列（可以增删改）
# 以键值对的方式存储数据，字典是一个无序的序列
# {}定义
# score = {'张三': 100, '李四': 98 } # 键值对
# hash(key)
# key必须是不可变序列
# str/整数序列就是不可变序列，不可以增删改
# 根据key查找value查找所在的位置
# 创建方式：2种
# 花括号
scores = {'张三': 100, '李四': 98, '王五': 95}
print(scores, type(scores))
# dict()
student = dict(name = 'jack', age = 20) # 2个键值对
print(student)
# 空字典
d = {}
print(d)

# 字典元素的获取
# 2种：[],
scores = {'张三': 100, '李四': 98, '王五': 95}
print(scores['张三'])
# print(scores['陈六'])
print(scores.get('张三'))
print(scores.get('陈六')) # 输出None
print(scores.get('马奇', 99)) # 99是查找马奇不存在时对应的默认值

# key的判断
scores = {'张三': 100, '李四': 98, '王五': 95}
print('张三' in scores) # True
del scores['张三'] # 删除指定的键值对
scores.clear()
print(scores)
# scores.del(['张三'])

# 字典元素的新增
scores['陈六'] = 98
print(scores)
# 修改
scores['陈六'] = 100
print(scores)

# 字典的视图
# keys(), values(), item()
scores = {'张三': 100, '李四': 98, '王五': 95}
keys = scores.keys()
print(keys, type(keys))
print(list(keys)) # 将所有的键转换为列表
values = scores.values()
print(values, type(values))
print(list(values)) # 将所有的值转换为列表
items = scores.items()
print(items, type(items))
print(list(items)) # 列表元素时元组！！ # 将所有的键值对转换为列表

# 字典元素的遍历
scores = {'张三': 100, '李四': 98, '王五': 95}
for item in scores: # 遍历的是键，要遍历值或者键值对的话还要加上其他函数
    print(item) # key
    print(scores[item]) # value
    # print() # 能不能输出键值对呢？

# 总结
# key不能重复，否则会覆盖
# value可以重复
# 为什么不能用列表作键？因为列表是可变对象
# lst = [10, 20]
# d = {lst: 10} # unhashable type: 'list'
# 空间换时间

# 字典生成式
# 内置函数zip()
items = ['fruits', 'books', 'others']
prices = [96, 78, 85]
d = {item:price for item, price in zip(items, prices)}
print(d)
e = {item.upper():price for item, price in zip(items, prices)} # zip以元素少的列表为准
print(e)


# Chapter 8：是棑还是散
# 两种数据结构：元组和集合

# 元组是不可变序列，没有增删改操作；字符串也是，如果强行加个东西上去，那么相当于造了一个新的字符串，则地址会改变
t = ('python', 'hello', 90) #与列表十分相似
t = 'python', 'hello', 90 # 省略()
# 使用内置函数tuple()
t = tuple(('python', 'hello', 90))
# 如果只有一个元素，须加逗号
t = ('ppp',)
print(type(t))
# 创建空元组
t = ()
t = tuple()

# 为什么将元组设计成不可变序列
# 元组中是可变对象，则可变对象的引用不允许改变，但是数据允许改变
# 元组中是不可变对象，则不能再引用其他对象
t = (10, [20, 30], 9)
print(t[1])
# t[1] = 90 # 报错：TypeError: 'tuple' object does not support item assignment（元组中是可变对象，则可变对象的引用不允许改变，但是数据允许改变）
t[1].append(100) # 向列表中添加元素，添加后id是不变的
t[1].insert(2, 50) # 向列表任意位置插入元素
print(t[1], id(t[1]))
# print(t[1][0]) # 还真可以这么玩：先具体到列表，再提取列表的元素
# sub_list = t[1]
# print(sub_list[0], type(sub_list[0]))
# t[2] =

# 元组的遍历，for in
t = ['Python', 'world', 98]
print(t[0])
# 遍历元组
for item in t:
    print(item)

# 什么是集合
# 可变类型序列
# 没有value，只有key，也用了hash函数
# 集合是没有value的字典
# 创建，2种
s = {2, 3, 4, 5, 5, 6, 7, 7} # 不允许重复，会去重
# 内置函数set()
s = set(range(6))
lst = list(range(6))
print(s, lst)
s = set([1, 2, 3, 3, 4])
s = set((1, 2, 3, 3, 4))
s4 = set('python')
s5 = set({12, 4, 34, 55, 66, 44, 4}) # 去重且无序
# 定义一个空集合
s7 = set()

# 集合的相关操作
# 判断操作
s = {10, 20, 30, 40, 50}
print(10 in s)
# 新增操作，2种
# add()
s.add(80)
print(s)
s.update({200, 400, 300})
print(s)
s.update([200, 400, 300])
s.update((200, 400, 300))
print(s)
# 删除操作
# remove
s.remove(10)
s.discard(500) # 不会报错
s.pop() # 删除任意一个元素，删除谁不知道
s.pop()
# s.pop(400) # 不能指定参数
s.clear() # 清空集合的元素

# 集合之间的关系
# 是否相等
s = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s == s2)
# 上述两个集合相等
# 是否为子集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1)) # s2是否是s1的子集
print(s3.issubset(s1))
# 超集
print(s1.issuperset(s2)) # s1是否是s2的超集
print(s1.issuperset(s3))
# 是否有交集
print(s2.isdisjoint(s3))
print(s1.isdisjoint(s3))

# 集合的数学操作
# 交、并、差、对称差集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s1.intersection(s2))
print(s1 & s2)
# 并集
print(s1.union(s2)) # 去掉重复元素
print(s1 | s2)
# 差集
print(s1.difference(s2))
print(s1 - s2)
# 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

# 集合生成式 P75
# 列表、字典都有生成式，但是元组没有，因为元组是不可变序列





