
import numpy as np

list1 = [1, 2, 3, 'a']
print(list1)

a = np.array([1, 2, 3, 4, 5]) # tuple是元组，python内置的数据类型，不可变
b = np.array([[1, 2, 3], [4, 5, 6]])
c = list(a)  # array到list的转换
print(a, np.shape(a))

print(b, np.shape(b))

print(c, np.shape(c))
