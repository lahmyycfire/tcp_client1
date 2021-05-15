import math

# 计算标准正态分布中的累计概率分布函数(CDF） P(x<=a)
def f1(a):
    p = 0.2316419
    b1 = 0.31938153
    b2 = -0.356563782
    b3 = 1.781477937
    b4 = -1.821255978
    b5 = 1.330274429

    x = math.fabs(a)
    t = 1 / (1 + p * x)

    val = 1 - (1 / (math.sqrt(2 * math.pi)) * math.exp(-1 * math.pow(a, 2) / 2)) * (
            b1 * t + b2 * math.pow(t, 2) + b3 * math.pow(t, 3) + b4 * math.pow(t, 4) + b5 * math.pow(t, 5))

    if (a < 0):
        val = 1 - val


    return val


print(f1(4.163064941733942059483))
print(f1(1))
# print((1-0.94)/(1-0.94^5))
# print(3^2)