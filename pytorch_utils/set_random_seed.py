import random

import numpy as np
import torch


def set_seed(seed: int) -> None:
    """
    设置随机种子，使得结果可以复现
    :param seed:
    :return:
    """
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
