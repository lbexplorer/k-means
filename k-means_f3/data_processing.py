import os
import numpy as np


def data_make(i):
    i = i.strip('\n').split(' ')
    i = i[0].split()
    return i


def get_data():
    path1 = os.getcwd()
    path2 = os.path.join(path1, 'text2.txt')
    tiket_id2_data_map = {}
    with open(path2, 'r') as f1:
        data = f1.readlines()
        for i in data:
            result = data_make(i)
            build_data(result, tiket_id2_data_map)

        data_result = get_array(tiket_id2_data_map)
        return data_result


def get_array(tiket_id2_data_map):
    data_result = []
    for list_item in tiket_id2_data_map.keys():
        aim_list = get_list(tiket_id2_data_map[list_item])
        data_result.append(aim_list)
    return data_result


def get_list(tiket):
    b = [0] * 1943
    for j in tiket:
        print(j)
        b[int(j) - 1] = 1
    print(b)
    b = np.array(b)
    return b


def build_data(result, tiket_id2_data_map):
    if result[0] not in tiket_id2_data_map:
        tiket_id2_data_map[result[0]] = []
        tiket_id2_data_map[result[0]].append(result[1])
    else:
        tiket_id2_data_map[result[0]].append(result[1])
