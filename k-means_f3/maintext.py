import numpy as np
from sklearn.cluster import KMeans

from data_processing import get_data
from data_story import input_data


def main():
    all_data = get_data()
    X = np.array(all_data)

    '''for i in range(90, 100):
        kmeans = KMeans(n_clusters=i)
        # 根据数据data进行聚类，结果存放于result_list中
        result_list = kmeans.fit_predict(X)
        # 将原始的数据data和聚类结果result_list
        # 传入对应的函数计算出该结果下的轮廓系数
        print("轮廓系数" , metrics.silhouette_score(X, result_list))'''

    '''estimator = KMeans(n_clusters=100, random_state=100)  # 构造聚类器,设定随机种子
    estimator.fit(X)
    r1 = pd.Series(estimator.labels_).value_counts()  # 统计各个类别的数目
    r2 = pd.DataFrame(estimator.cluster_centers_)  # 找出聚类中心
    r = pd.concat([r2, r1], axis=1)  # 横向连接（0是纵向），得到聚类中心对应的类别下的数目


    print("轮廓系数：", metrics.silhouette_score(X, estimator.labels_, metric='euclidean'))
    '''

    kmeans = KMeans(n_clusters=10, max_iter=200, n_init=10, init="k-means++", random_state=0)
    kmeans.fit(X)
    x = kmeans.labels_
    input_data(x)
    '''wcss.append(kmeans.inertia_)
       result_list = kmeans.fit_predict(X)
       print("轮廓系数", metrics.silhouette_score(X, result_list))
       plt.plot(range(100, 110), wcss)
       plt.title("The Elbow Method")
       plt.xlabel("Number of Clusters")
       plt.ylabel("WCSS")
       plt.show()'''


if __name__ == '__main__':
    main()
