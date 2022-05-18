import torch
from torch import optim

acars_data_path = "E:/课题相关/信号相关/信号增量代码/sig_increase_mulclass/data/"
modulation_data_path = "E:/课题相关/信号相关/信号增量代码/sig_increase/"

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

modName = [b'8PSK', b'AM-DSB', b'AM-SSB', b'BPSK', b'CPFSK', b'GFSK', b'PAM4', b'QAM16', b'QAM64', b'QPSK', b'WBFM']


modName_map = {b'8PSK': 0, b'AM-DSB': 1, b'AM-SSB': 2, b'BPSK': 3, b'CPFSK': 4, b'GFSK': 5, b'PAM4': 6, b'QAM16': 7, b'QAM64': 8, b'QPSK': 9, b'WBFM': 10}

modName_map_ = {0: b'8PSK', 1: b'AM-DSB', 2: b'AM-SSB', 3:b'BPSK', 4:b'CPFSK', 5:b'GFSK', 6:b'PAM4', 7:b'QAM16', 8:b'QAM64', 9:b'QPSK', 10:b'WBFM'}
# modName = ["8PSK", "AM-DSB", "AM-SSB", "BPSK", "CPFSK", "GFSK", "PAM4", "QAM16", "QAM64", "QPSK", "WBFM"]

test_ratio = 0.5

batch_size = 32

learning_rate = 0.001

num_worker = 1

pretrain_epoch = 100

train_epoch = 100

pretrain_model_path = "./app/checkpoint/"
# pretrain_model_path = "./checkpoint/"

bound = 0.3

all_class = 11

root_path = "./app/"
# root_path = "./"