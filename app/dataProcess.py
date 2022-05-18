# -*- coding: utf-8 -*-
import os, random
import numpy as np
import random, sys
import _pickle as cPickle
from app.config import *


# def getdata(root=modulation_data_path, test_percent=0.5, random_seed=1, train=True, valid=False, test=False):
#     np.Random.seed(random_seed)
#
#     Xd = cPickle.load(open(root+"2016.04C.multisnr.pkl", 'rb'), encoding='bytes')
#     snrs, mods = map(lambda j: sorted(list(set(map(lambda x: x[j], Xd.keys())))), [1, 0])
#     print("snrs", snrs, mods)
#     lbl = []
#     X_mods = []
#     Y_mods = []
#     define_class = [b'8PSK', b'AM-DSB', b'AM-SSB', b'BPSK', b'CPFSK', b'GFSK', b'PAM4', b'QAM16', b'QAM64', b'QPSK',
#                     b'WBFM']
#     labels_dic = {k: v for v, k in enumerate(define_class)}
#
#     # 11 kinds of mods, e.g. b'8PSK'
#     for mod in mods:
#         Xmod = []
#         Ymod = []
#         # 20 kinds of snrs: e.g. -20
#         # for snr in snrs[17:18]:
#         for snr in snrs[16:17]:
#             # print("snr:", snr) # 12db
#             Xmod.append(Xd[(mod, snr)])
#             # lbl is label,220 kinds of label: e.g. (b'8PSK',-20)
#             for i in range(Xd[(mod, snr)].shape[0]):
#                 lbl.append((mod, snr))
#                 Ymod.append(labels_dic[mod])
#         Xmod = np.vstack(Xmod)
#         X_mods.append(Xmod)
#         Y_mods.append(Ymod)
#     X_train = []
#     Y_train = []
#     X_test = []
#     Y_test = []
#     X_val = []
#     Y_val = []
#     for l in range(len(X_mods)):
#         n_examples = len(X_mods[l])
#         n_train = int(n_examples * test_percent)
#
#         train_idx = np.Random.choice(range(0, n_examples), size=n_train, replace=False)
#         test_idx = list(set(range(0, n_examples)) - set(train_idx))
#         if valid:
#             n_val = int(n_train * 0.1)
#             val_idx = np.Random.choice(range(0, n_train), size=n_val, replace=False)
#             new_train_idx = list(set(range(0, n_train)) - set(val_idx))
#
#             X_train.append(X_mods[l][train_idx][new_train_idx])
#             Y_train.append(np.array((n_train-n_val) * [l]))
#             X_val.append(X_mods[l][train_idx][val_idx])
#             Y_val.append(np.array(n_val * [l]))
#         else:
#             X_train.append(X_mods[l][train_idx])
#             Y_train.append(np.array(n_train * [l]))
#         X_test.append(X_mods[l][test_idx])
#         Y_test.append(np.array((n_examples - n_train) * [l]))
#         #print(len(X_test[l]))
#         #print(len(Y_test[l]))
#         #print(Y_test[l])
#     X_train = np.vstack(X_train)
#     X_test = np.vstack(X_test)
#     X_train = np.transpose(X_train,(0,2,1))
#     X_test = np.transpose(X_test,(0,2,1))
#     Y_train = np.concatenate(Y_train[:])
#     Y_test = np.concatenate(Y_test[:])
#     random_train_idx = np.Random.choice(range(0, X_train.shape[0]), size=X_train.shape[0], replace=False)
#     random_test_idx = np.Random.choice(range(0, X_test.shape[0]), size=X_test.shape[0], replace=False)
#     # print("len(X_train):", len(X_train))
#     X_train = X_train[:,np.newaxis,:,:]
#     X_test = X_test[:,np.newaxis,:,:]
#     if train:
#         # print("train_shape:", X_train.shape, Y_train.shape)
#         return X_train[random_train_idx], Y_train[random_train_idx]
#     if test:
#         # print("test_shape:", X_test.shape, Y_test.shape)
#         return X_test[random_test_idx], Y_test[random_test_idx]
#     else:
#         X_val = np.vstack(X_val)
#         X_val = np.transpose(X_val, (0, 2, 1))
#         Y_val = np.concatenate(Y_val[:])
#         random_val_idx = np.Random.choice(range(0, X_val.shape[0]), size=X_val.shape[0], replace=False)
#         X_val = X_val[:, np.newaxis, :, :]
#         # print("val_shape:", X_val.shape, Y_val.shape)
#         return X_val[random_val_idx], Y_val[random_val_idx]


def read_data(root=modulation_data_path, snr=12, test_percent=0.5, random_seed=1):
    np.random.seed(random_seed)

    Xd = cPickle.load(open(root + "2016.04C.multisnr.pkl", 'rb'), encoding='bytes')
    # print(Xd)
    # [-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    # [b'8PSK', b'AM-DSB', b'AM-SSB', b'BPSK', b'CPFSK', b'GFSK', b'PAM4', b'QAM16', b'QAM64', b'QPSK', b'WBFM']
    snrs, mods = map(lambda j: sorted(list(set(map(lambda x: x[j], Xd.keys())))), [1, 0])
    print("snrs", snrs, mods)
    lbl = []
    X_mods = []
    Y_mods = []
    define_class = [b'8PSK', b'AM-DSB', b'AM-SSB', b'BPSK', b'CPFSK', b'GFSK', b'PAM4', b'QAM16', b'QAM64', b'QPSK',
                    b'WBFM']
    labels_dic = {k: v for v, k in enumerate(define_class)}

    # 11 kinds of mods, e.g. b'8PSK'
    for mod in mods:
        Xmod = []
        Ymod = []
        # 20 kinds of snrs: e.g. -20
        # for snr in snrs[17:18]:
        # print("snr:", snr) # 12db
        Xmod.append(Xd[(mod, snr)])
        # lbl is label,220 kinds of label: e.g. (b'8PSK',-20)
        for i in range(Xd[(mod, snr)].shape[0]):
            lbl.append((mod, snr))
            Ymod.append(labels_dic[mod])
        Xmod = np.vstack(Xmod)
        X_mods.append(Xmod)
        Y_mods.append(Ymod)

    # data = []
    # label = []

    # for l in range(len(X_mods)):
    #     data.append(X_mods[l])
    #     label.append(Y_mods[l])

    # data = np.concatenate(data)
    # label = np.concatenate(label)

    # return data, label
    return X_mods, Y_mods


# "D:/课题相关/信号相关/信号增量代码/sig_increase_mulclass/data/"
def get_acars(root=acars_data_path):
    train_data_path = root + "x_train_100persample.npy"
    train_label_path = root + "y_train_100persample.npy"
    test_data_path = root + "x_test_8000samples.npy"
    test_label_path = root + "y_test_8000samples.npy"

    train_data = np.load(train_data_path)
    train_label = np.load(train_label_path)
    test_data = np.load(test_data_path)
    test_label = np.load(test_label_path)
    print(train_data.shape, train_label.shape, test_data.shape, test_label.shape)

    train_data = np.transpose(train_data, (3, 0, 1, 2))
    test_data = np.transpose(test_data, (3, 0, 1, 2))

    print(train_data.shape, train_label.shape, test_data.shape, test_label.shape)

    return train_data, train_label, test_data, test_label


def get_acars_mix(root=acars_data_path, test_percent=0.5, random_seed=1, train=True, valid=False, test=False):
    np.random.seed(random_seed)
    train_data_path = root + "x_train_100persample.npy"
    train_label_path = root + "y_train_100persample.npy"
    test_data_path = root + "x_test_8000samples.npy"
    test_label_path = root + "y_test_8000samples.npy"

    train_data = np.load(train_data_path)
    train_label = np.load(train_label_path)
    test_data = np.load(test_data_path)
    test_label = np.load(test_label_path)
    print(train_data.shape, train_label.shape, test_data.shape, test_label.shape)
    train_data = np.transpose(train_data, (3, 2, 0, 1))
    test_data = np.transpose(test_data, (3, 2, 0, 1))
    all_data = np.concatenate([train_data, test_data], axis=0)
    all_label = np.concatenate([train_label, test_label], axis=0)

    indices = np.arange(0, len(all_data))
    np.random.shuffle(indices)
    test_data = all_data[indices][:int(len(all_data) * test_percent)]
    test_label = all_label[indices][:int(len(all_data) * test_percent)]
    train_data = all_data[indices][-int(len(all_data) * test_percent):]
    train_label = all_label[indices][-int(len(all_data) * test_percent):]
    print(train_data.shape, train_label.shape, test_data.shape, test_label.shape)
    if train:
        return train_data, train_label
    else:
        return test_data, test_label


# 分割测试集和训练集
def split_test_and_train(test_percent=0.5, snr=12, random_seed=1):
    np.random.seed(random_seed)
    # (11, ) (11, )
    data = np.load(root_path+"data/data_{}db.npy".format(snr), allow_pickle=True)
    label = np.load(root_path+"data/label_{}db.npy".format(snr), allow_pickle=True)

    train_data = []
    train_label = []
    test_data = []
    test_label = []

    for i in range(len(data)):
        data_len_ith_class = len(data[i])
        indices = np.arange(0, data_len_ith_class)
        np.random.shuffle(indices)
        data_shuffle = data[i][indices]
        data_len_ith_class_test = int(data_len_ith_class * test_percent)
        test_data.append(data_shuffle[:data_len_ith_class_test])
        test_label.append(label[i][:data_len_ith_class_test])
        train_data.append(data_shuffle[data_len_ith_class_test:])
        train_label.append(label[i][data_len_ith_class_test:])

    train_data = np.concatenate(train_data)
    train_label = np.concatenate(train_label)
    test_data = np.concatenate(test_data)
    test_label = np.concatenate(test_label)

    train_data = np.transpose(train_data, (0, 2, 1))
    test_data = np.transpose(test_data, (0, 2, 1))

    train_data = train_data[:, np.newaxis, :, :]
    test_data = test_data[:, np.newaxis, :, :]

    np.save(root_path+"data/train/data_{}db.npy".format(snr), train_data)
    np.save(root_path+"data/train/label_{}db.npy".format(snr), train_label)
    np.save(root_path+"data/test/data_{}db.npy".format(snr), test_data)
    np.save(root_path+"data/test/label_{}db.npy".format(snr), test_label)


# 保存所有snr为npy文件
def save_npy():
    for snr in [-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]:
        data, label = read_data(root=modulation_data_path, snr=snr)
        data = np.array(data)
        label = np.array(label)
        print(np.array(data).shape, np.array(label).shape)
        np.save(root_path+"data/data_{}db.npy".format(snr), data)
        np.save(root_path+"data/label_{}db.npy".format(snr), label)


def get_number_of_each_class(snr=12):
    train_data = np.load("./data/train/data_{}db.npy".format(snr), allow_pickle=True)
    print(train_data.shape)
    train_label = np.load(root_path+"data/train/label_{}db.npy".format(snr), allow_pickle=True)
    test_data = np.load(root_path+"data/test/data_{}db.npy".format(snr), allow_pickle=True)
    test_label = np.load(root_path+"data/test/label_{}db.npy".format(snr), allow_pickle=True)
    data = np.load(root_path+"data/data_{}db.npy".format(snr), allow_pickle=True)
    label = np.load(root_path+"data/label_{}db.npy".format(snr), allow_pickle=True)
    data = np.concatenate(data)
    label = np.concatenate(label)
    train_num_list = []
    test_num_list = []
    num_list = []
    for i in range(11):
        train_label_i = train_label[train_label == i]
        test_label_i = test_label[test_label == i]
        label_i = label[label == i]
        train_num_list.append(len(train_label_i))
        test_num_list.append(len(test_label_i))
        num_list.append(len(label_i))
    sum_test = 0
    sum_train = 0
    for i in test_num_list:
        sum_test = sum_test + i
    for i in train_num_list:
        sum_train = sum_train + i
    print("each_class_of_train_data:", train_num_list, sum_train)
    print("each_class_of_test_data:", test_num_list, sum_test)
    print("each_class_of_all_data:", num_list)

def prepare_pretrain_data(snr=12, old_class=5, dataset="RML2016.04c"):
    train_data = np.load(root_path+"data/train/data_{}db.npy".format(snr), allow_pickle=True)
    train_label = np.load(root_path+"data/train/label_{}db.npy".format(snr), allow_pickle=True)
    test_data = np.load(root_path+"data/test/data_{}db.npy".format(snr), allow_pickle=True)
    test_label = np.load(root_path+"data/test/label_{}db.npy".format(snr), allow_pickle=True)
    old_train_data = []
    old_train_label = []
    old_test_data = []
    old_test_label = []
    new_train_data = []
    new_train_label = []
    new_test_data = []
    new_test_label = []
    for i in range(old_class):
        old_train_data.append(train_data[train_label == i])
        old_train_label.append(train_label[train_label == i])
        old_test_data.append(test_data[test_label == i])
        old_test_label.append(test_label[test_label == i])
    for i in range(old_class, 11):
        new_train_data.append(train_data[train_label == i])
        new_train_label.append(train_label[train_label == i])
        new_test_data.append(test_data[test_label == i])
        new_test_label.append(test_label[test_label == i])
    old_train_data = np.concatenate(old_train_data)
    old_train_label = np.concatenate(old_train_label)
    old_test_data = np.concatenate(old_test_data)
    old_test_label = np.concatenate(old_test_label)
    new_train_data = np.concatenate(new_train_data)
    new_train_label = np.concatenate(new_train_label)
    new_test_data = np.concatenate(new_test_data)
    new_test_label = np.concatenate(new_test_label)
    np.save(root_path+"data/train/old/data_{}db.npy".format(snr), old_train_data)
    np.save(root_path+"data/train/old/label_{}db.npy".format(snr), old_train_label)
    np.save(root_path+"data/test/old/data_{}db.npy".format(snr), old_test_data)
    np.save(root_path+"data/test/old/label_{}db.npy".format(snr), old_test_label)
    np.save(root_path+"data/train/new/data_{}db.npy".format(snr), new_train_data)
    np.save(root_path+"data/train/new/label_{}db.npy".format(snr), new_train_label)
    np.save(root_path+"data/test/new/data_{}db.npy".format(snr), new_test_data)
    np.save(root_path+"data/test/new/label_{}db.npy".format(snr), new_test_label)
    np.save(root_path+"data/test/observed/data_{}db.npy".format(snr), old_test_data)
    np.save(root_path+"data/test/observed/label_{}db.npy".format(snr), old_test_label)


def prepare_increment_data(task_class, snr=12):
    observed_test_data = np.load(root_path+"data/test/observed/data_{}db.npy".format(snr))
    observed_test_label = np.load(root_path+"data/test/observed/label_{}db.npy".format(snr))
    new_train_data = np.load(root_path+"data/train/new/data_{}db.npy".format(snr))
    new_train_label = np.load(root_path+"data/train/new/label_{}db.npy".format(snr))
    new_test_data = np.load(root_path+"data/test/new/data_{}db.npy".format(snr))
    new_test_label = np.load(root_path+"data/test/new/label_{}db.npy".format(snr))
    current_task_data_train = []
    current_task_label_train = []
    current_task_data_test = []
    current_task_label_test = []
    for cls in task_class:
        current_task_data_train.append(new_train_data[new_train_label == cls])
        current_task_label_train.append(new_train_label[new_train_label == cls])
        current_task_data_test.append(new_test_data[new_test_label == cls])
        current_task_label_test.append(new_test_label[new_test_label == cls])
    current_task_data_train = np.concatenate(current_task_data_train)
    current_task_label_train = np.concatenate(current_task_label_train)
    current_task_data_test = np.concatenate(current_task_data_test)
    current_task_label_test = np.concatenate(current_task_label_test)
    observed_test_data = np.concatenate((current_task_data_test, observed_test_data))
    observed_test_label = np.concatenate((current_task_label_test, observed_test_label))
    np.save(root_path+"data/train/current/data_{}db.npy".format(snr), current_task_data_train)
    np.save(root_path+"data/train/current/label_{}db.npy".format(snr), current_task_label_train)
    np.save(root_path+"data/test/current/data_{}db.npy".format(snr), current_task_data_test)
    np.save(root_path+"data/test/current/label_{}db.npy".format(snr), current_task_label_test)
    np.save(root_path+"data/test/observed/data_{}db.npy".format(snr), observed_test_data)
    np.save(root_path+"data/test/observed/label_{}db.npy".format(snr), observed_test_label)



if __name__ == '__main__':
    # save_npy()

    # split_test_and_train(test_percent=0.5, snr=12)

    get_number_of_each_class(snr=12)
