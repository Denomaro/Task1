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

