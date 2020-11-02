import math
import random
import numpy as np
import matplotlib.pyplot as plt

volume = [95, 75, 23, 73, 50, 22, 6, 57, 89, 98]
value = [89, 59, 19, 43, 100, 72, 44, 16, 7, 64]
volume_np = np.array(volume)
value_np = np.array(value)
contain_max = 300
T0 = 100
alpha = 0.99
Tf = 0.01
T = T0
Markov_len = 10


# 其实转移函数的设计是关键,保证波动的范围不大不小刚刚好,不然很容易陷入局部最优
# 在得到局部最优后就无法产生更好的邻居了,后面的都不接受
def neighbor(x):
    y = x.copy()
    while True:
        order_list = list(range(0, 10))
        index_list = random.sample(order_list, 2)
        temp1 = -x[index_list[0]] + 1
        temp2 = -x[index_list[1]] + 1
        if sum(x*volume_np) - x[index_list[0]] * volume_np[index_list[0]] + temp1 * volume_np[index_list[0]] - x[index_list[1]] * volume_np[index_list[1]] + temp2 * volume_np[index_list[1]] <= contain_max:
            y[index_list[0]] = temp1
            y[index_list[1]] = temp2
            break
            pass
        pass
    return y


# 测试领域函数
# def neighbor(x):
#     y = x.copy()
#     while True:
#         order_list = list(range(0, 10))
#         index_list = random.sample(order_list, 1)
#         temp1 = -x[index_list[0]] + 1
#         # temp2 = -x[index_list[1]] + 1
#         if sum(x*volume_np) - x[index_list[0]] * volume_np[index_list[0]] + temp1 * volume_np[index_list[0]] <= contain_max:
#             y[index_list[0]] = temp1
#             # y[index_list[1]] = temp2
#             break
#             pass
#         pass
#     return y


def func(x):
    return sum(x*value_np)


if __name__ == '__main__':
    x_np = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    y_list = []
    # x_np = np.zeros(10)
    while T > Tf:
        i = 0
        while i < Markov_len:
            x_value = func(x_np)
            x_np_next = neighbor(x_np)
            new_value = func(x_np_next)
            delta = x_value - new_value
            if delta < 0:
                x_np = x_np_next
                pass
            if delta >= 0:
                a = random.random()
                b = math.exp(-delta / T)
                print('b的值为{}'.format(b))
                if a < math.exp(-delta/T):
                    x_np = x_np_next
                    pass
                else:
                    x_np = x_np
                    pass
                pass
            i = i+1
            print('i的值为%d' % i)
            pass
        T = T * alpha
        print('T的值为%f' % T)
        y_list.append(func(x_np))
        pass
    print(x_np, func(x_np))
    x_list = range(0, len(y_list))
    plt.plot(x_list, y_list, linewidth=0.8)
    plt.show()


