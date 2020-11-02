# import random
import matplotlib.pyplot as plt
# order_list = list(range(0, 100))
# print(order_list)
# index_list = random.sample(order_list, int(40))
# print(index_list)
# list1 = [1, 3, 4]
# print(id(list1))
# for i, j in enumerate(list1):
#     print(j)


# def reverse(list_):
#     for index, item in enumerate(list_):
#         list_[index] = 1/item
#         print(item)
#     return list_
#
#
# a = reverse(list1)
# print(a)
# print(id(a))
# print(list1)

import random
import time
import numpy as np
import math
# print(random.randint(0, 1))
# print(random.random())
# a = 1 + 2j
# print(a.real)
# print(a.imag)


# 交叉方法
###################################################################
# order_list = [0, 1, 2, 3, 4, 5, 6, 7]
# a = np.array([[7, 5, 4, 2, 1, 3, 6, 0], [1, 2, 3, 4, 5, 6, 7, 0]])
# # print(type(a[0]))
# list1 = a[0]
# list2 = a[1]
# # cross_index = random.randint(0, 7)
# cross_index = 3
# list1_left = list1[0:cross_index]
# list1_right = list1[cross_index:]
# list2_left = list2[0:cross_index]
# list2_right = list2[cross_index:]
# print(list1_left, list1_right)
# print(list2_left, list2_right)
# dict1 = dict(zip(list1_right, list2_right))
# dict2 = dict(zip(list2_right, list1_right))
# print(dict1)
# print(dict2)
# # print(dict1[3])
# # list1_left_new = list1_left  #这里=赋值操作之后，两个列表的地址是一样的!
# # list1_right_new = list1_right  #这里=赋值操作之后，两个列表的地址是一样的!
# list1_left_new = []
# list2_left_new = []
# list1_left_new.extend(list1_left)
# list2_left_new.extend(list2_left)
# for index in range(0, len(list1_left)):
#     while True:
#         if list1_left_new[index] in list2_right:
#             list1_left_new[index] = dict2[list1_left_new[index]]
#             pass
#         if list1_left_new[index] not in list2_right:
#             break
#             pass
#         pass
# print(list1_left, list1_left_new)
# list1_new = list1_left_new + list(list2_right)
# print(list1_new)
# for index in range(0, len(list2_left)):
#     while True:
#         if list2_left_new[index] in list1_right:
#             list2_left_new[index] = dict1[list2_left_new[index]]
#             pass
#         if list2_left_new[index] not in list1_right:
#             break
#             pass
#     pass
# print(list2_left, list2_left_new)
# list2_new = list2_left_new + list(list1_right)
# print(list2_new)
# print(list2_new)
#################################################################

# encode_pop = np.empty([2, 7], dtype=int)
# for i in range(0, 2):
#     encode_pop[i] = np.array([random.sample(order_list, 7)])
#     pass
# print(encode_pop)
# 顺序编码交叉方式
#################################################################
# a ="5 15 20 21 17 2 16 7 8 9 14 0 28 30 25 27 26 10 29 24 19 23 18 22 11 13 12 6 1 3 4"
# list1 = a.split(' ')
# index_list = []
# for i in list1:
#     index_list.append(int(i))
#     pass
# print(index_list)
# c = [[1304, 2312], [3639, 1315], [4177, 2244], [3712, 1399], [3488, 1535], [3326, 1556], [3238, 1229], [4196, 1044],
#      [4312, 790], [4386, 570], [3007, 1970], [2562, 1756], [2788, 1491], [2381, 1676], [1332, 695], [3715, 1678],
#      [3918, 2179], [4061, 2370], [3780, 2212], [3676, 2578], [4029, 2838], [4263, 2931], [3429, 1908], [3507, 2376],
#      [3394, 2643], [3439, 3201], [2935, 3240], [3140, 3550], [2545, 2357], [2778, 2826], [2370, 2975]]
# list_x = []
# for i in index_list:
#     list_x.append(c[i][0])
#     pass
# list_x.append(c[index_list[0]][0])
# print(list_x)
# list_y = []
# for i in index_list:
#     list_y.append(c[i][1])
#     pass
# list_y.append(c[index_list[0]][1])
# print(list_y)
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(list_x, list_y,'ob', linewidth=0.5)
# plt.plot(list_x, list_y, linewidth=0.5)
# plt.show()
#################################################################

# import queue
# list1 = [[1, 2], [2, 3]]
# q = queue.Queue(maxsize=2)
# for i in list1:
#     q.put(i)

# while not q.empty():
#     print(q.get())
#     pass
# q.get()
# q.get()
# print(q.full())
# print(q.queue, type(q.queue))
# print([2, 1][::-1])
# if [2, 1][::-1] in q.queue:
#     print('Ture')

# a=[1,2]
# b = []
# b.extend(a)
# print(b,id(a),id(b))
# city_num = 31
# c = [[1304, 2312], [3639, 1315], [4177, 2244], [3712, 1399], [3488, 1535], [3326, 1556], [3238, 1229], [4196, 1044],
#      [4312, 790], [4386, 570], [3007, 1970], [2562, 1756], [2788, 1491], [2381, 1676], [1332, 695], [3715, 1678],
#      [3918, 2179], [4061, 2370], [3780, 2212], [3676, 2578], [4029, 2838], [4263, 2931], [3429, 1908], [3507, 2376],
#      [3394, 2643], [3439, 3201], [2935, 3240], [3140, 3550], [2545, 2357], [2778, 2826], [2370, 2975]]
# def path_length(solution):
#     length = 0
#     for i in range(0, city_num-1):
#         length = length + math.sqrt((c[solution[i]][0]-c[solution[i+1]][0]) ** 2 + (c[solution[i]][1]-c[solution[i+1]][1]) ** 2)
#     pass
#     length = length + math.sqrt((c[solution[30]][0]-c[solution[0]][0]) ** 2 + (c[solution[30]][1]-c[solution[0]][1]) ** 2)
#     return length
#
#
# solution = [0, 15, 7, 14, 29, 9, 4, 11, 20, 27, 24, 30, 22, 6, 17, 21, 2, 5, 10, 13, 25, 18, 12, 19, 23, 1, 16, 3, 28, 26, 8]
# print(path_length(solution))
# a, b = 1, 2
# a, b = b, a
# print(a, b)

# pso_next = np.zeros((30, 2))
# print(pso_next)
# li = [1, 2]
# li.clear()
# li.extend([2, 3])
# print(li, len(li))
import numpy as np
import random
import random
# a = np.random.random((30, 2))
# b = np.zeros((30, 2))
# c = np.array([[1, 2], [3, 4]])
# print(c)
# a = b.copy()
# print(a)
# x_np = np.zeros(10)
# print(x_np)
# print(random.randint(0, 10))
# order_list = list(range(0, 10))
# print(order_list)
# index_list = random.sample(order_list, 2)
# print(index_list)
# x_np = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# x_np = np.zeros(10)
# print(x_np)
# print(x_np)
# value = [89, 59, 19, 43, 100, 72, 44, 16, 7, 64]
# value_np = np.array(value)
# sum_ = sum(x_np*value_np)
# print(sum_)
# a = random.random()
# print(a)
# order_list = list(range(0, 9))
# index_list = random.sample(order_list, 1)
# print(order_list, index_list)
# li1 = [1, 2]
# li2 = li1.copy()
# print(li2)
# import queue
# q = queue.Queue()
# q.put(1)
# q.put(2)
# q.get()
# print(q)
# print(random.randint(0, 1))
import numpy as np
# city_list = list(range(0, 31))
# # arrived_city = [1]
# # not_arrived_city = list(set(city_list) - set(arrived_city))
# # print(not_arrived_city, not_arrived_city[-1])
# a = np.array([0, 1, 2, 3, 4])
# print(list(a.cumsum()))
# print(random.random())
# city_num =31
# information_ij_delta = np.ones((city_num, city_num))
# # print(information_ij_delta)
# information_ij_delta[0][0] = 1
# print(information_ij_delta*3)
# ant_path = np.array(1)
# ant_now_path = ant_path.copy()
# print(id(ant_path), id(ant_now_path))
# import copy
# a = [[1, 2, 3], [4, 5, 6]]
# b = copy.copy(a)
# # print(id(a), id(b))
# # print(id(a[0]), id(b[0]))
# for i in range(0, len(b)):
#     # print(id(i))
#     a[0] = [2, 3, 4]
#     pass
# print(a, b)
a, b, c = 1, 2, 3
a, b, c = c, a, b
print(a, b, c)
import numpy
import cv2