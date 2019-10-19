# 阶乘
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


# 最大公约数
def gcd(x,y):
    # 辗转相除法
    if max(x,y) % min(x,y) == 0:
        return min(x,y)
    else:
        x,y= min(x,y),max(x,y) % min(x,y)
        return gcd(x,y)
