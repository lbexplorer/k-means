import os


def comnination_data(raw_data, result_data):
    with open(path_batch, 'r') as file_batch:
        data_batch = file_batch.readlines()
        for i in range(len(data_batch)):
            merge = raw_data[i] + data_batch[i]
            result_data.append(merge)
        with open(path_result, 'w') as file_result:
            file_result.writelines(result_data)


def get_result_data(raw_data, result_data):
    # with open(path_order, 'r') as file_order:
    #   data_order = file_order.readlines()
    for temp in range(len(raw_data)):
        temp_data = raw_data[temp].strip('\n')
        temp_data = temp_data + ','
        raw_data[temp] = temp_data

    comnination_data(raw_data, result_data)


def input_data(aim):
    global path_batch, path_order, path_result

    raw_data = aim.tolist()
    raw_data = list(map(str, raw_data))

    path1 = os.getcwd()
    path_batch = os.path.join(path1, 'batch_number.txt')
    path_order = os.path.join(path1, 'order_number.txt')
    path_result = os.path.join(path1, 'data_result.txt')
    result_data = []
    #批次数据
    with open(path_batch, 'r') as file_batch:
        data_batch = file_batch.readlines()
    with open(path_order, 'r') as file_batch:
        data_batch = file_batch.readlines()

    get_result_data(raw_data, result_data)


if __name__ == '__main__':
    pass
