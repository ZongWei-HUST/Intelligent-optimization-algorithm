import numpy as np
import math
import random
import matplotlib.pyplot as plt


w = 0.5  # 惯性因子
c1 = 2  # 每个粒子的个体学习因子
c2 = 2  # 每个粒子的群体学习因子
N = 30  # 粒子数
var_num = 2  # 变量个数
v_max = 1.2  # 最大飞翔速度
v_min = -1.2  # 最小飞翔速度
v_pre = np.random.random((N, var_num))  # 初始粒子速度
p_best = np.zeros((N, var_num))  # 单个粒子最优位置
g_best = []  # 所有粒子最优位置
iteration_max = 5  # 最大迭代次数


def pre_pso():
    pos = np.random.uniform(-4, 4, (N, var_num))
    np.round(pos, 2, out=pos)
    return pos
    pass


def func(x, y):
    return 3*math.cos(x*y)+x+y**2


def p_value(pso):
    pso_value = []
    for p in pso:
        pso_value.append(func(p[0], p[1]))
        pass
    return pso_value


def update(pso, v):
    v_next = v.copy()
    pso_next = np.zeros((N, var_num))
    for index in range(0, N):
        temp1 = w*v[index][0]+c1*random.random()*(p_best[index][0]-pso[index][0])+c2*random.random()*(g_best[0]-pso[index][0])
        if temp1 > v_max:
            temp1 = v_max
            pass
        if temp1 < v_min:
            temp1 = v_min
            pass
        temp2 = w*v[index][1]+c1*random.random()*(p_best[index][1]-pso[index][1])+c2*random.random()*(g_best[1]-pso[index][1])
        if temp2 > v_max:
            temp2 = v_max
            pass
        if temp2 < v_min:
            temp2 = v_min
            pass
        pso_next[index][0] = pso[index][0] + temp1
        if pso_next[index][0] > 4:
            pso_next[index][0] = 4
            pass
        elif pso_next[index][0] < -4:
            pso_next[index][0] = -4
            pass
        pso_next[index][1] = pso[index][1] + temp2
        if pso_next[index][1] > 4:
            pso_next[index][1] = 4
            pass
        elif pso_next[index][1] < -4:
            pso_next[index][1] = -4
            pass
        v_next[index][0] = temp1
        v_next[index][1] = temp2
        pass
    return pso_next, v_next
    pass


pso = pre_pso()
pso_value = p_value(pso)
p_best = pso.copy()
g_best.extend(list(pso[pso_value.index(min(pso_value))]))
iteration = 0
while iteration < iteration_max:
    pso_next, v_next = update(pso, v_pre)
    pso_next_value = p_value(pso_next)
    for i in range(0, N):
        if pso_next_value[i] < pso_value[i]:
            p_best[i] = pso_next[pso_next_value.index(pso_next_value[i])]
        pass
    g_best.clear()
    g_best.extend(list(pso_next[pso_next_value.index(min(pso_next_value))]))
    pso = pso_next
    v_pre = v_next.copy()
    iteration += 1
    pass
print(g_best, func(g_best[0], g_best[1]))
