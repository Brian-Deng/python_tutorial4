

# score = int(input('请输入一个成绩：'))
# if score >= 90 and score <= 100:
#     print('A')
# elif score >= 80 and score <= 89:
#     print('B')

# 斐波拉契数列求通项
# 是不是在更新呀
def fibo(n):
    if n == 1 or n == 2:
        res = 1
    else:
        res = fibo(n-2) + fibo(n-1)
    return res

nb = fibo(6)
print(nb)