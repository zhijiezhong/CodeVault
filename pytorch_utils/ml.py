# -*- coding: utf-8 -*-
# @Time    : 2023/12/21
# @Author  : Zhong Zhijie

from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split


def svm4cls(embedding, labels, label_ratio=0.3):
    """
    使用svm做分类
    :param embedding: 节点的嵌入
    :param labels: 节点的标签
    :param label_ratio: 测试的比例
    :return: F1分数
    """
    X_train, X_test, Y_train, Y_test = train_test_split(embedding, labels, test_size=label_ratio, random_state=42)
    clf = svm.SVC(probability=True)
    clf.fit(X_train, Y_train)

    Pred_Y = clf.predict(X_test)
    score = f1_score(Pred_Y, Y_test, average='weighted')
    return score


def pca2embedding(matrix, pca_dim=128):
    pca = PCA(n_components=pca_dim)
    pca_matrix = pca.fit_transform(matrix)
    return pca_matrix


