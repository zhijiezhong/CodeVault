# -*- coding: utf-8 -*-
# @Time    : 2023/12/21
# @Author  : Zhong Zhijie

import numpy as np
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE


def plot_embeddings(embeddings, features, labels):
    # norm = Normalized(embeddings)
    # embeddings = norm.MinMax()

    emb_list = []
    for k in range(features.shape[0]):
        emb_list.append(embeddings[k])
    emb_list = np.array(emb_list)

    model = TSNE(n_components=2, init="pca")
    # model = TSNE(n_components=2)
    node_pos = model.fit_transform(emb_list)

    color_idx = {}
    for i in range(features.shape[0]):
        color_idx.setdefault(labels[i][0], [])
        color_idx[labels[i][0]].append(i)

    for c, idx in color_idx.items():
        plt.scatter(node_pos[idx, 0], node_pos[idx, 1], label=c, s=5)  # c=node_colors)
    plt.axis('off')
    # plt.legend()
    plt.gca.legend_ = None
    plt.show()
