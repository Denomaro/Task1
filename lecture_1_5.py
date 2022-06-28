#Лекция 1

#Задание 5

def count_find_num(primesL, limit):
    k = 1
    res = {}
    for i in primesL:
        k *= i
    res[k] = primesL[:]

    while True:
        flag = True
        for d in primesL:
            for k in list(res):
                if k*d < limit+1 and k*d not in res:
                    res[k*d] = res.get(k) + [d]
                    flag = False
        if flag:
            break
    if max(res) > limit:
        return []
    else:
        return [len(res), max(res)]

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []