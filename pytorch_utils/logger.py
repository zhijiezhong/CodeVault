# -*- coding: utf-8 -*-
# @Time    : 2023/11/21
# @Author  : Zhong Zhijie

import logging
import os
import sys
import numpy as np
from utils import print_config_summary


class Logger:
    def __init__(self, save_dir, file_name='5.train.log', name='train'):
        """
        :param name: logger名称
        :param save_dir: 日志保存的目录
        :param file_name: 日志保存的文件名
        """
        self.name = name
        self.save_dir = save_dir
        self.file_name = file_name

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)

        ch = logging.StreamHandler(stream=sys.stdout)
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s", datefmt='%Y/%m/%d %I:%M:%S')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        if self.save_dir:
            fh = logging.FileHandler(os.path.join(self.save_dir, self.file_name))
            fh.setLevel(logging.INFO)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        return logger

    def save_model_structure(self, model):
        # 保存模型的结构，方便以后查看对应使用的模型
        model_log_path = os.path.join(self.save_dir, '1.model.log')
        with open(model_log_path, 'w', encoding='utf8') as f:
            f.write(str(model))
        f.close()

    def save_param_setting(self, args):
        parameter_log_path = os.path.join(self.save_dir, '2.parameter.log')
        args_draw = print_config_summary(args)
        with open(parameter_log_path, 'w', encoding='utf8') as f:
            f.write(args_draw)
        f.close()

    def save_metric(self, metric: dict):
        metric_log_path = os.path.join(self.save_dir, '3.metric.log')
        best_metric_log_path = os.path.join(self.save_dir, '4.best_metric.log')
        # 将字典中的值列表转换为 NumPy 数组
        array_metric = np.array([v for v in metric.values()])
        # 保存 NumPy 数组到文本文件
        np.savetxt(metric_log_path, array_metric, delimiter=',', fmt='%f')

        index_values = {}
        for key, values in metric.items():
            if 'loss' in key.lower():
                min_index = values.index(min(values)) + 1
                index_values[key] = 'At the {}th epoch, the minimum {} is {}.'.format(min_index, key.lower(),
                                                                                      min(values))
            else:
                max_index = values.index(max(values)) + 1
                index_values[key] = max_index
                index_values[key] = 'At the {}th epoch, the maximum {} is {}.'.format(max_index, key.lower(),
                                                                                      max(values))

        # 找到最长的键的长度
        max_key_length = max(len(k) for k in index_values.keys())
        with open(best_metric_log_path, 'w') as f:
            for k, v in index_values.items():
                # 将 k 右对齐并占用最长键的长度
                formatted_key = f"{k:>{max_key_length}}"
                f.write(f"{formatted_key}: {v}\n")
        f.close()
