a = -1
c = 5000
b = c - a
rate1 = 1.1
rate2 = 0.6

result = pre = result1 = result2 = -999999999999
while a < c:

    pre = result
    a += 1
    b = c - a
    result1 = (0.8 * a) + a - c
    result2 = (0.8 * b) + b - c

    result = min(result1, result2)
    print(a, b, result1, result2)