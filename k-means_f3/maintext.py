import os

import numpy as np
from sklearn.cluster import KMeans

from data_processing import get_data


def main():
    all_data = get_data()
    X = np.array(all_data)
    kmeans = KMeans(n_clusters=98, random_state=0).fit(X)
    aim = kmeans.labels_  # 输出原始数据的聚类后的标签值
    path1 = os.getcwd()
    path2 = os.path.join(path1, 'data.txt')
    with open(path2, 'w') as f1:
        f1.writelines(aim)


if __name__ == '__main__':
    main()
