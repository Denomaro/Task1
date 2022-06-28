#Лекция 1

#Задание 2

def int32_to_ip(int32):
    return '.'.join([str((int32 >> 8 * i) % 256) for i in [3, 2, 1, 0]])
