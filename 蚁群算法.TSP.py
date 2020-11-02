# author： zongwei
# description：ACO.TSP

import math
import random
import numpy as np
import matplotlib.pyplot as plt
import copy


alpha = 1  # 信息素重要程度因子
beta = 5  # 启发函数重要程度因子
vol = 0.5  # 信息素挥发因子
Q = 10000  # 信息素常数
city_num = 31  # 城市数量
ant_num = 31  # 蚂蚁数量
city_xy = [[1304, 2312], [3639, 1315], [4177, 2244], [3712, 1399], [3488, 1535], [3326, 1556], [3238, 1229], [4196, 1044],
     [4312, 790], [4386, 570], [3007, 1970], [2562, 1756], [2788, 1491], [2381, 1676], [1332, 695], [3715, 1678],
     [3918, 2179], [4061, 2370], [3780, 2212], [3676, 2578], [4029, 2838], [4263, 2931], [3429, 1908], [3507, 2376],
     [3394, 2643], [3439, 3201], [2935, 3240], [3140, 3550], [2545, 2357], [2778, 2826], [2370, 2975]]
city_list = list(range(0, city_num))  # 总城市的列表集合
information_ij = np.ones((city_num, city_num))   # 信息素浓度矩阵

# 城市之间的路径距离
length_ij = np.zeros((city_num, city_num))
for i in range(0, city_num):
    for j in range(0, city_num):
        length_ij[i][j] = math.sqrt((city_xy[i][0] - city_xy[j][0])**2 + (city_xy[i][1] - city_xy[j][1])**2)
        pass
    pass


# 产生蚂蚁的初始城市
def initial_ant_path_random():
    initial_ant_path = []  # 所有蚂蚁的路径列表
    for index in range(0, ant_num):
        initial_ant_path.append([random.randint(0, city_num-1)])
        pass
    return initial_ant_path


ant_path = initial_ant_path_random().copy()


# 计算允许访问的城市集合
def allow_city(arrived_city):
    not_arrived_city = list(set(city_list) - set(arrived_city))
    return not_arrived_city


# 输出转移概率归一化后并累加的函数
def normalize_sum(transport_probability_list):
    normalize_list = []
    for probability in transport_probability_list:
        normalize_list.append(probability/sum(transport_probability_list))
        pass
    normalize_array = np.array(normalize_list)
    sum_list = list(normalize_array.cumsum())
    return sum_list


# 计算城市之间的转移概率,输入参数为某一只蚂蚁的当前路径，计算出剩余可选城市和选择的概率
def calculate_transport_probability(ant_path_list):
    not_arrived_city_list = allow_city(ant_path_list)
    city_i = ant_path_list[-1]
    sum_ = 0
    transport_probability = []
    for city_j in not_arrived_city_list:
        sum_ = sum_ + information_ij[city_i][city_j]**alpha * (1/length_ij[city_i][city_j])**beta
        pass
    for city_j in not_arrived_city_list:
        transport_probability.append((information_ij[city_i][city_j]**alpha * (1/length_ij[city_i][city_j])**beta)/sum_)
        pass
    normalize_sum_list = normalize_sum(transport_probability)
    return not_arrived_city_list, normalize_sum_list


# 计算路径长度,输入参数为所有蚂蚁的不闭环的路径
def calculate_path_length(all_ant_path):
    all_ant_path_length = []
    for every_ant_path in all_ant_path:
        length = 0
        for i in range(0, city_num - 1):
            length = length + math.sqrt((city_xy[every_ant_path[i]][0]-city_xy[every_ant_path[i+1]][0])**2 + (city_xy[every_ant_path[i]][1]-city_xy[every_ant_path[i+1]][1])**2)
            pass
        length = length + math.sqrt((city_xy[every_ant_path[30]][0]-city_xy[every_ant_path[0]][0])**2 + (city_xy[every_ant_path[30]][1]-city_xy[every_ant_path[0]][1])**2)
        all_ant_path_length.append(length)
        pass
    return all_ant_path_length


# 轮盘赌选择下一个城市
def choose_next_city(all_ant_path):
    # new_all_ant_path = all_ant_path.copy()
    new_all_ant_path = copy.deepcopy(all_ant_path)
    for every_ant_path in new_all_ant_path:
        not_arrived_city_list, normalize_sum_list = calculate_transport_probability(every_ant_path)
        temp = random.random()
        for i in range(0, len(normalize_sum_list)):
            if normalize_sum_list[i] > temp:
                every_ant_path.append(not_arrived_city_list[i])
                break
                pass
            pass
        pass
    return new_all_ant_path
    pass


generation = 0
generation_max = 100
if __name__ == '__main__':
    x_list = []
    y_list = []
    y1_list = []
    result_list = []
    while generation < generation_max:
        # ant_now_path = ant_path.copy()
        ant_now_path = copy.deepcopy(ant_path)
        for i in range(0, city_num):
            ant_next_path = choose_next_city(ant_now_path)
            ant_now_path = ant_next_path
            pass
        all_ant_path_length = calculate_path_length(ant_now_path)
        information_ij_delta = np.zeros((city_num, city_num))
        # information_ij_delta = information_ij_delta_.copy()
        for ant_index, every_ant_path in enumerate(ant_now_path):
            for i in range(0, city_num - 1):
                information_ij_delta[every_ant_path[i]][every_ant_path[i+1]], information_ij_delta[every_ant_path[i+1]][every_ant_path[i]] = Q/all_ant_path_length[ant_index], Q/all_ant_path_length[ant_index]
                pass
            information_ij_delta[every_ant_path[30]][every_ant_path[0]], information_ij_delta[every_ant_path[0]][every_ant_path[30]] = Q/all_ant_path_length[ant_index], Q/all_ant_path_length[ant_index]
            pass
        information_ij = (1 - vol) * information_ij + information_ij_delta
        generation += 1
        print(generation)
        x_list.append(generation)
        # y_list.append(sum(all_ant_path_length)/31)
        y1_list.append(min(all_ant_path_length))
        pass
    print(min(all_ant_path_length), ant_now_path[all_ant_path_length.index(min(all_ant_path_length))])
    # print(all_ant_path_length.means())
    # print(sum(all_ant_path_length)/31)
    pass
    plt.plot(x_list, y1_list, linewidth=0.5)
    plt.show()
