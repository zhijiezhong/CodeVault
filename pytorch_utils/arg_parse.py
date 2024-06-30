import argparse


def get_argparse():
    # 获取解析器
    parser = argparse.ArgumentParser()

    # 训练前的准备
    parser.add_argument('--data_dir', default='data', type=str, help='Path to data')
    parser.add_argument('--output_dir', default='outputs', type=str,
                        help='Save path for models, logs, and other files')
    parser.add_argument('--load_model_state_dir', default='outputs/model', type=str, help='Path to the loaded model')
    parser.add_argument('--retraining', action="store_true", help='Loading the model for retraining')
    parser.add_argument('--seed', default=42, type=int, help='Setting the random seed')

    # 训练过程
    parser.add_argument('--device', default='cuda:0', type=str, choices=['cuda:0', 'cuda:1', 'cpu'], help='Device used')
    parser.add_argument('--epochs', default=20, type=int, help='Number of training epochs')
    parser.add_argument('--batch_size', default=32, type=int, help='Batch size')
    parser.add_argument('--optimizer', default='Adam', type=str, choices=['Adam', 'SGD'], help='Name of optimizer')
    parser.add_argument('--lr', default=0.001, type=float, help='Learning rate')
    parser.add_argument('--weight_decay', default=1e-5, type=float, help='Weight decay')
    parser.add_argument('--dropout', default=0.5, type=float, help='Dropout rate')
    parser.add_argument('--patience', default=100, type=int, help='Early stop')
    parser.add_argument('--use_tensorboard', action="store_true", help='Whether to use tensorboard')

    return parser
