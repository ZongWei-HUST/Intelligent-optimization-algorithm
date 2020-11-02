# author： zongwei
# description：TS.TSP

import math
import random
import matplotlib.pyplot as plt
import queue
import time


city_num = 31
neighbor_num = 200
table_length = 10
k_opt = 2
c = [[1304, 2312], [3639, 1315], [4177, 2244], [3712, 1399], [3488, 1535], [3326, 1556], [3238, 1229], [4196, 1044],
     [4312, 790], [4386, 570], [3007, 1970], [2562, 1756], [2788, 1491], [2381, 1676], [1332, 695], [3715, 1678],
     [3918, 2179], [4061, 2370], [3780, 2212], [3676, 2578], [4029, 2838], [4263, 2931], [3429, 1908], [3507, 2376],
     [3394, 2643], [3439, 3201], [2935, 3240], [3140, 3550], [2545, 2357], [2778, 2826], [2370, 2975]]
# 采用队列结构实现禁忌表
taboo_Table = queue.Queue(maxsize=table_length)


def initial_solution():
    """
    生成初始解
    :return: 初始解城市序列
    """
    return list(range(0, 31))
    # 蚁群算法求解初始解
    # return [30, 29, 26, 27, 25, 19, 24, 23, 18, 16, 17, 2, 20, 21, 5, 4, 22, 3, 1, 15, 7, 8, 9, 6, 12, 10, 28, 11, 13, 0, 14]


def path_length(solution):
    """
    计算城市解序列对应的路径长度
    :param solution: 城市解序列
    :return: 路径长度
    """
    length = 0
    for i in range(0, city_num-1):
        length = length + math.sqrt((c[solution[i]][0]-c[solution[i+1]][0]) ** 2 + (c[solution[i]][1]-c[solution[i+1]][1]) ** 2)
    pass
    length = length + math.sqrt((c[solution[30]][0]-c[solution[0]][0]) ** 2 + (c[solution[30]][1]-c[solution[0]][1]) ** 2)
    return length


def swap(solution):
    """
    对当前解产生neighbor_num个候选解
    :param solution: 当前解
    :return: 返回三个参数，一是交换后的城市序列列表，二是对应的路径长度，三是交换规则列表，放置在禁忌表中
    """
    swap_list = []
    value_list = []
    finally_list = []
    while len(finally_list) < neighbor_num:
        new_solution = []
        new_solution.extend(solution)
        index_list = random.sample(list(range(1, city_num)), int(k_opt))
        while index_list not in finally_list:
            finally_list.append(index_list)
            if k_opt == 2:
                new_solution[index_list[0]], new_solution[index_list[1]] = solution[index_list[1]], solution[index_list[0]]
            if k_opt == 3:
                new_solution[index_list[0]], new_solution[index_list[1]], new_solution[index_list[2]] = new_solution[index_list[2]], solution[index_list[0]], solution[index_list[1]]
            swap_list.append(new_solution)
            new_length = path_length(new_solution)
            value_list.append(new_length)
            pass
        pass
    return swap_list, value_list, finally_list


def choose(swap_list, value_list, finally_list):
    """
    根据swap函数的输出，从候选解中选择一个邻域解作为下一次迭代的初始解
    :param swap_list: 交换后的城市序列列表
    :param value_list: 对应的路径长度
    :param finally_list: 交换规则列表，放置在禁忌表中
    :return:
    """
    min_index = value_list.index(min(value_list))
    while True:
        if finally_list[min_index] in taboo_Table.queue or finally_list[min_index][::-1] in taboo_Table.queue:
            # value_list.remove(value_list[min_index])
            value_list[min_index] = 1000000
            min_index = value_list.index(min(value_list))
            pass
        if finally_list[min_index] not in taboo_Table.queue and finally_list[min_index][::-1] not in taboo_Table.queue:
            break
            pass
        pass
    if taboo_Table.full() is False:
        taboo_Table.put(finally_list[min_index])
        pass
    if taboo_Table.full() is True:
        taboo_Table.get()
        taboo_Table.put(finally_list[min_index])
        pass
    return swap_list[min_index]


if __name__ == '__main__':
    start = time.time()
    generation = 0
    pre_solution = initial_solution()
    p = path_length(pre_solution)
    p_list = []
    while generation < 10000:
        # 禁忌表长度动态变化
        # if generation > 25:
        #     table_length = 9
        # if generation > 50:
        #     table_length = 8
        # if generation > 75:
        #     table_length = 7
        # k_opt动态变化
        # if generation > 25:
        #     k_opt = 2
        solution = pre_solution
        p = path_length(pre_solution)
        p_list.append(p)
        if p < 15700:
            break
        a, b, m = swap(solution)
        pre_solution = choose(a, b, m)
        print(generation)
        generation += 1
        pass
    print(pre_solution, path_length(pre_solution))
    end = time.time()
    print(end-start)
    # 绘制路径图
    list_x = []
    for i in pre_solution:
        list_x.append(c[i][0])
        pass
    list_x.append(c[pre_solution[0]][0])
    list_y = []
    for i in pre_solution:
        list_y.append(c[i][1])
        pass
    list_y.append(c[pre_solution[0]][1])
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(list_x, list_y, 'ob', linewidth=0.5)
    plt.plot(list_x, list_y, linewidth=0.5)
    plt.show()
    plt.figure()
    plt.plot(list(range(0, generation+1)), p_list)
    plt.show()
