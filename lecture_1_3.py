#Лекция 1

#Задание 3

def zeros(n):
    x = n // 5
    y = x
    while x > 0:
        x /= 5
        y += int(x)
    return y

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7