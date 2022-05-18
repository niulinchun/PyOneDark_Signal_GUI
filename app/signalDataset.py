import torch
import numpy as np
from torch.utils.data import Dataset
from app.config import *


class PretrainSignalDataset(Dataset):

    def __init__(self, snr=12, data_type="train", dataset="RML2016.04c"):
        super(PretrainSignalDataset, self).__init__()
        # self.root_path = "./app/data/"
        self.root_path = root_path+"data/"
        self.data, self.targets = [], []
        if dataset == "acars":
            pass
        if dataset == "RML2016.04c":
            self.data = np.load(self.root_path + data_type + "/old/data_{}db.npy".format(snr), allow_pickle=True)
            self.targets = np.load(self.root_path + data_type + "/old/label_{}db.npy".format(snr), allow_pickle=True)

    def __getitem__(self, index):
        return self.data[index], self.targets[index]

    def __len__(self):
        return len(self.data)


class IncrementSignalDataset(Dataset):

    def __init__(self, snr=12, data_type="train", dataset="RML2016.04c"):
        super(IncrementSignalDataset, self).__init__()
        # self.root_path = "./app/data/"
        self.root_path = root_path+"data/"
        self.data, self.targets = [], []

        if dataset == "acars":
            pass
        if dataset == "RML2016.04c" and data_type == "train":
            memory_data = np.load(self.root_path + data_type + "/memory/data_{}db.npy".format(snr), allow_pickle=True)
            memory_label = np.load(self.root_path + data_type + "/memory/label_{}db.npy".format(snr), allow_pickle=True)
            current_data = np.load(self.root_path + data_type + "/current/data_{}db.npy".format(snr), allow_pickle=True)
            current_label = np.load(self.root_path + data_type + "/current/label_{}db.npy".format(snr), allow_pickle=True)
            self.data = np.concatenate((memory_data, current_data))
            self.targets = np.concatenate((memory_label, current_label))
        if dataset == "RML2016.04c" and data_type == "test":
            self.data = np.load(self.root_path + data_type + "/current/data_{}db.npy".format(snr), allow_pickle=True)
            self.targets = np.load(self.root_path + data_type + "/current/label_{}db.npy".format(snr), allow_pickle=True)

    def __getitem__(self, index):
        return self.data[index], self.targets[index]

    def __len__(self):
        return len(self.data)

    def get_image_class(self, cls):
        return self.data[self.targets == cls], self.targets[self.targets == cls]

class EvalDataset(Dataset):
    def __init__(self, snr=12, data_type="old", dataset="RML2016.04c"):
        super(EvalDataset, self).__init__()
        self.root_path = root_path+"data/"
        # self.root_path = "./app/data/"
        self.data, self.targets = [], []
        if dataset == "acars":
            pass
        if dataset == "RML2016.04c":
            self.data = np.load(self.root_path + "test/" + data_type + "/data_{}db.npy".format(snr), allow_pickle=True)
            self.targets = np.load(self.root_path + "test/" + data_type + "/label_{}db.npy".format(snr), allow_pickle=True)
            print("EvalDataset:", np.unique(self.targets))

    def __getitem__(self, index):
        return self.data[index], self.targets[index]

    def __len__(self):
        return len(self.data)

if __name__ == '__main__':
    train_dataset = PretrainSignalDataset(snr=12, data_type="train", dataset="RML2016.04c")
    test_dataset = PretrainSignalDataset(snr=12, data_type="test", dataset="RML2016.04c")
