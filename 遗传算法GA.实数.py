# y=x+10sin(5x)+7cos(4x),x∈[0,10]
# 求解函数最大值
# 绘制函数图像
# 实数编码

import math
import random
import numpy as np
import matplotlib.pyplot as plt

pop_len = 200
gen_len = 1
cross_pro = 0.4
mut_pro = 0.01


def encode():
    """
    编码函数
    :return: 返回200*1的实数种群矩阵
    """
    population_initial = np.random.uniform(0,10, (pop_len, gen_len))
    np.round(population_initial, 4, out=population_initial)
    return population_initial
    pass


def fitness(population):
    """
    适应度计算函数
    :param population: 输入参数为十进制种群
    :return: 返回每条染色体对应的适应度值，存在负适应度值
    """
    fitness_list = []
    for index, item in enumerate(population):
        fitness_result = item[0]+10*math.sin(5*item[0])+7*math.cos(4*item[0])
        fitness_list.append(fitness_result)
        pass
    return fitness_list
    pass


# def deal_fitness_list(fitness_list):
#     """
#     适应度处理函数
#     :param fitness_list: 输入参数为适应度函数求解得到的适应度列表
#     :return: 讲适应度列表中的正数取倒数，求最小值
#     """
#     fitness_list_reverse = []
#     for i in range(0, len(fitness_list)):
#         fitness_list_reverse.append(1/fitness_list[i])
#         pass
#     return fitness_list_reverse
#     pass


def deal_fitness_list(fitness_list):
    """
    适应度处理函数
    :param fitness_list: 输入参数为适应度函数求解得到的适应度列表
    :return: 讲适应度列表中的负值替换成0
    """
    for i in range(0, len(fitness_list)):
        if fitness_list[i] < 0:
            fitness_list[i] = 0
            pass
        pass
    return fitness_list
    pass


def normalize(fitness_list):
    """
    归一化函数
    :param fitness_list:  输入参数为处理后的适应度列表
    :return: 返回适应度归一化并累加之后的列表
    """
    normalize_list = []  # 存放累加后的适应度值
    # 适应度归一化处理
    for item in fitness_list:
        normalize_list.append(item/sum(fitness_list))
        pass
    # print(sum(fitness_list))
    # 适应度归一化后累加
    for i in range(1, len(normalize_list)):
        normalize_list[i] = normalize_list[i]+normalize_list[i-1]
        pass
    return normalize_list
    pass


def select(normalize_list, population):
    """
    选择函数
    :param normalize_list: 输入参数为适应度归一化并累加之后的列表
    :param population: 输入参数为初始迭代前的种群
    :return: 返回选择函数得到的下一代种群
    """
    index_list = []
    i = 0
    while i < len(normalize_list):
        random_01 = random.random()
        for j in range(0, len(normalize_list)):
            if normalize_list[j] > random_01:
                index_list.append(j)
                break
                pass
            pass
        i = i+1
        pass
    return population[index_list]  # 返回下一代种群population_next
    pass


def crossover(population):
    """
    交叉函数
    :param population: 输入参数为种群
    :return: 返回交叉后的种群
    """
    order_list = list(range(0, pop_len))
    index_list = random.sample(order_list, int(pop_len*cross_pro))
    for i in range(0, len(index_list), 2):
        arithmetic = random.random()
        population[i], population[i+1] = np.dot(np.array([arithmetic, 1-arithmetic]), population[[i, i+1]]), np.dot(np.array([1-arithmetic, arithmetic]), population[[i, i+1]])
        pass
    return population
    pass


def mutation(population):
    """
    变异函数
    :param population: 输入为迭代之前的种群
    :return: 返回值为变异后的种群
    """
    order_list = list(range(0, pop_len*gen_len))
    index_list = random.sample(order_list, int(pop_len*gen_len*mut_pro))
    for i in range(0, len(index_list)):
        row = index_list[i] // gen_len
        col = index_list[i] % gen_len
        # population[row-1][col-1] = np.random.normal(0, 0.05)
        # population[row - 1][col - 1] = 0
        # population[row-1][col-1] = random.uniform(-32, 32)
        population[row - 1][col - 1] = random.uniform(0, 10)
        pass
    return population
    pass


# 遗传算法流程
generation = 0  # 迭代参数
generation_max = 1000  # 最大迭代次数
pop = encode()  # 初始化种群，记为pop
fitness_max_list = []
while generation < generation_max:
    a = fitness(pop)
    fitness_max_list.append(sum(a)/pop_len)
    # fitness_max_list.append(max(a))
    b = deal_fitness_list(a)
    c = select(normalize(b), pop)
    d = crossover(c)
    pop = mutation(d)
    print(generation, sum(a)/pop_len)
    generation += 1
    pass
print(pop[a.index(max(a))], max(a))

# 绘制平均适应度收敛迭代图像
generation_list = list(range(0, generation_max))
x = generation_list
y = fitness_max_list
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y, linewidth=0.5)
plt.show()
