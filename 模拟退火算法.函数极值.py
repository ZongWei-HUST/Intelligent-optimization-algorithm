import math
import random


T0 = 100
alpha = 0.99
Tf = 0.01
T = T0
Markov_len = 500
s = 0.02
min_x = -4
max_x = 4
min_y = -4
max_y = 4


# 其实转移函数的设计是关键,保证波动的范围不大不小刚刚好
def neighbor(pre_x, pre_y):
    while True:
        new_x = pre_x + s*(min_x + random.random()*(max_x-min_x))
        new_y = pre_y + s*(min_y + random.random()*(max_y-min_y))
        if min_x < new_x < max_x and min_y < new_y < max_y:
            return new_x, new_y


def func(x, y):
    return 3*math.cos(x*y)+x+y**2
    # return 5*math.cos(x*y)+x*y+math.pow(y, 3)


if __name__ == '__main__':
    x0 = min_x + random.random()*(max_x-min_x)
    y0 = min_y + random.random()*(max_x-min_x)
    while T > Tf:
        i = 0
        unaccepted_num = 0
        while i < Markov_len and unaccepted_num < 10:
            value = func(x0, y0)
            next_x, next_y = neighbor(x0, y0)
            new_value = func(next_x, next_y)
            delta = new_value - value
            if delta < 0:
                x0, y0 = next_x, next_y
                unaccepted_num = 0
                pass
            if delta >= 0:
                a = random.random()
                if a < math.exp(-delta/T):
                    x0, y0 = next_x, next_y
                    unaccepted_num = 0
                    pass
                else:
                    x0, y0 = x0, y0
                    unaccepted_num = unaccepted_num + 1
                    pass
                pass
            i = i+1
            print('i的值为%d' % i)
            pass
        T = T * alpha
        print('T的值为%f' % T)
        pass
    print(x0, y0)
    print(value)


