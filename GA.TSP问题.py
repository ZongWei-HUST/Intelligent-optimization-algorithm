# 求解TSP问题
# 顺序编码

import math
import random
import numpy as np
import matplotlib.pyplot as plt

pop_len = 100
gen_len = 31
cross_pro = 0.4
mut_pro = 0.05
c = [[1304, 2312], [3639, 1315], [4177, 2244], [3712, 1399], [3488, 1535], [3326, 1556], [3238, 1229], [4196, 1044],
     [4312, 790], [4386, 570], [3007, 1970], [2562, 1756], [2788, 1491], [2381, 1676], [1332, 695], [3715, 1678],
     [3918, 2179], [4061, 2370], [3780, 2212], [3676, 2578], [4029, 2838], [4263, 2931], [3429, 1908], [3507, 2376],
     [3394, 2643], [3439, 3201], [2935, 3240], [3140, 3550], [2545, 2357], [2778, 2826], [2370, 2975]]


def encode():
    order_list = list(range(0, gen_len))
    encode_pop = np.empty([pop_len, gen_len], dtype=int)
    for i in range(0, pop_len):
        encode_pop[i] = np.array([random.sample(order_list, int(gen_len))])
        pass
    return encode_pop
    pass


def fitness(encode_pop):
    fitness_list = []
    global c
    for i in range(0, pop_len):
        length = 0
        for j in range(0, gen_len-1):
            # c[encode_pop[i][j]][0] = x1, c[encode_pop[i][j]][1] = y1
            # c[encode_pop[i][j+1]][0] = x2, c[encode_pop[i][j+1]][1] = y2
            length = length+math.sqrt((c[encode_pop[i][j]][0]-c[encode_pop[i][j+1]][0])**2+(c[encode_pop[i][j]][1]-c[encode_pop[i][j+1]][1])**2)
            pass
        length = length + math.sqrt((c[encode_pop[i][30]][0]-c[encode_pop[i][0]][0])**2+(c[encode_pop[i][30]][1]-c[encode_pop[i][0]][1])**2)
        fitness_list.append(length)
        pass
    return fitness_list
    pass


def deal_fitness_list(fitness_list):
    fitness_list_reverse = []
    for i in range(0, len(fitness_list)):
        fitness_list_reverse.append(1/fitness_list[i])
        pass
    return fitness_list_reverse
    pass


def normalize(fitness_list):
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


def select(normalize_list, population, fitness_list_reverse):
    index_list = []
    i = 0
    index_max = fitness_list_reverse.index(max(fitness_list_reverse))
    while i < len(normalize_list)-10:
        random_01 = random.random()
        for j in range(0, len(normalize_list)):
            if normalize_list[j] > random_01:
                index_list.append(j)
                break
                pass
            pass
        i = i+1
        pass
    for i in range(0, 10):
        index_list.append(index_max)
        pass
    return population[index_list]  # 返回下一代种群population_next
    pass


def crossover(population):
    order_list = list(range(0, pop_len))
    index_list = random.sample(order_list, int(pop_len * cross_pro))
    for i in range(0, len(index_list), 2):
        list1 = population[i]
        list2 = population[i+1]
        cross_index = random.randint(0, gen_len)
        list1_left = list1[0:cross_index]
        list1_right = list1[cross_index:]
        list2_left = list2[0:cross_index]
        list2_right = list2[cross_index:]
        dict1 = dict(zip(list1_right, list2_right))
        dict2 = dict(zip(list2_right, list1_right))
        list1_left_new = []
        list2_left_new = []
        list1_left_new.extend(list1_left)
        list2_left_new.extend(list2_left)
        for index in range(0, len(list1_left)):
            while True:
                if list1_left_new[index] in list2_right:
                    list1_left_new[index] = dict2[list1_left_new[index]]
                    pass
                if list1_left_new[index] not in list2_right:
                    break
                    pass
                pass
        list1_new = list1_left_new + list(list2_right)
        for index in range(0, len(list2_left)):
            while True:
                if list2_left_new[index] in list1_right:
                    list2_left_new[index] = dict1[list2_left_new[index]]
                    pass
                if list2_left_new[index] not in list1_right:
                    break
                    pass
            pass
        list2_new = list2_left_new + list(list1_right)
        population[i] = list1_new
        population[i+1] = list2_new
        pass
    return population
    pass


def mutation(population):
    order_list = list(range(0, pop_len))
    index_list = random.sample(order_list, int(pop_len*mut_pro))
    for index in index_list:
        order_list2 = list(range(0, gen_len))
        index_list2 = random.sample(order_list2, 2)
        population[index][index_list2[0]], population[index][index_list2[1]] = population[index][index_list2[1]], population[index][index_list2[0]]
        pass
    return population
    pass


# 遗传过程
generation = 0  # 迭代参数
generation_max = 10000 # 最大迭代次数
pop = encode()  # 初始化种群，记为pop
fitness_mean_list = []
while generation < generation_max:
    a = fitness(pop)
    if min(a) < 18500:
        print(pop[a.index(min(a))], min(a))
        break
        pass
    fitness_mean_list.append(sum(a)/pop_len)
    # fitness_max_list.append(max(a))
    b = deal_fitness_list(a)
    c1 = select(normalize(b), pop, b)
    d = crossover(c1)
    pop = mutation(d)
    print(generation, sum(a)/pop_len)
    generation += 1
    pass
print(pop[a.index(min(a))], min(a))

# 绘制路径图
index_list_order = list(pop[a.index(min(a))])
list_x = []
for i in index_list_order:
    list_x.append(c[i][0])
    pass
list_x.append(c[index_list_order[0]][0])
list_y = []
for i in index_list_order:
    list_y.append(c[i][1])
    pass
list_y.append(c[index_list_order[0]][1])
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(list_x, list_y, 'ob', linewidth=0.5)
plt.plot(list_x, list_y, linewidth=0.5)
plt.show()
