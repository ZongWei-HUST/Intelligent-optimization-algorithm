import numpy as np
volume = [95, 75, 23, 73, 50, 22, 6, 57, 89, 98]
value = [89, 59, 19, 43, 100, 72, 44, 16, 7, 64]
volume_np = np.array(volume)
value_np = np.array(value)
contain_max = 300


def str_num(str_list):
    num_list = []
    for str_ in str_list:
        num_list.append(int(str_))
        pass
    return num_list


value_list = 0
x_np_best = np.zeros(10)
for i in range(0, 1024):
    a = '{:010b}'.format(i)
    b = str_num(a)
    x_np = np.array(b)
    print('i的值为%d' % i, x_np)
    while sum(x_np*volume_np) < contain_max:
        if sum(x_np*value_np) > value_list:
            value_list = sum(x_np*value_np)
            x_np_best = x_np.copy()
        break
        pass
    pass
print(value_list, x_np_best, sum(x_np_best*volume_np))





