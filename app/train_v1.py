from PyQt6.QtCore import pyqtSignal
from torch.utils.data import DataLoader
import torch.nn.functional as F
import threading
# from PySide6.QtCore import QThread
from app.model import getSignalModel
from app.myNetwork import Network
from app.signalDataset import PretrainSignalDataset, IncrementSignalDataset, EvalDataset
from app.dataProcess import prepare_pretrain_data, prepare_increment_data
from app.config import *
import numpy as np
import copy
from app.utils import mutualInfo_ori, get_weight_by_linearProgram


# def get_one_hot(target, num_class):
#     one_hot = torch.zeros(target.shape[0], num_class).to(device)
#     one_hot = one_hot.scatter(dim=1, index=target.long().view(-1, 1), value=1.)
#     return one_hot
#
#
#
#
#
# def compute_loss(model, imgs, target, numclass):
#     output = model(imgs)  # ( , 20)
#     target = get_one_hot(target, numclass)  # ( , 20)
#     target = target.long()
#     output, target = output.to(device), target.to(device)
#     # class_loss = F.cross_entropy(output, target)
#     log_prob = torch.nn.functional.log_softmax(output, dim=1)
#     class_loss = -torch.sum(log_prob * target) / imgs.size(0)
#     return class_loss
#
#
# def test(model, testloader):
#     model.eval()  # 切换推理模式
#     correct, total = 0, 0
#     preds = []
#     for setp, (imgs, labels) in enumerate(testloader):
#         imgs = imgs.type(torch.FloatTensor)
#         imgs, labels = imgs.to(device), labels.to(device)
#         with torch.no_grad():
#             outputs = model(imgs)
#         outputs = outputs.cpu()
#         preds.append(outputs)
#         predicts = torch.max(outputs, dim=1)[1]
#         correct += (predicts == labels.cpu()).sum()
#         total += len(labels)
#     accuracy = 100. * correct / total
#     model.train()
#     return accuracy, preds
#
#
# # 旧类数据训练旧模型
# def pretrain(snr, old_class_num, memory_size, dataset="RML2016.04c"):
#     prepare_pretrain_data(snr, old_class_num, dataset)
#     feature_extractor = getSignalModel(dataset, old_class_num)
#     model = Network(old_class_num, feature_extractor)
#
#     train_dataset = PretrainSignalDataset(snr=snr, data_type="train")
#     test_dataset = PretrainSignalDataset(snr=snr, data_type="test")
#     train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=batch_size, num_workers=num_worker)
#     test_dataloader = DataLoader(test_dataset, shuffle=False, batch_size=batch_size, num_workers=num_worker)
#
#     if pretrain_epoch == 0:
#         res = torch.load(pretrain_model_path + "/pretrain_" + str(old_class_num) + ".pkl")
#         model.load_state_dict(res['model'])
#         test_accuracy, _ = test(model, test_dataloader)
#         print("old model old data test accuracy: {}%".format(test_accuracy))
#         return test_accuracy
#
#     model.to(device)
#     model.train()
#     best_acc = 0
#     optimizer = optim.Adam(params=model.parameters(), lr=learning_rate, weight_decay=0.001)
#     for i in range(pretrain_epoch):
#         loss = []
#         if i == 20:
#             for p in optimizer.param_groups:
#                 p['lr'] = learning_rate / 2.
#         if i == 40:
#             for p in optimizer.param_groups:
#                 p['lr'] = learning_rate / 4.
#         if i == 60:
#             for p in optimizer.param_groups:
#                 p['lr'] = learning_rate / 8.
#         if i == 80:
#             for p in optimizer.param_groups:
#                 p['lr'] = learning_rate / 16.
#         for step, (data, label) in enumerate(train_dataloader):
#             data = data.type(torch.FloatTensor)
#             data, label = data.to(device), label.to(device)
#             optimizer.zero_grad()
#             loss_value = compute_loss(model, data, label, old_class_num)
#             loss_value.backward()
#             loss.append(loss_value.item())
#             optimizer.step()
#         loss = np.mean(loss)
#         print("epoch:{}, loss_value: {}. The best accuray is {}".format(i + 1, loss, best_acc))
#         if (i + 1) % 1 == 0:
#             test_accuracy, _ = test(model=model, testloader=test_dataloader)
#             if test_accuracy > best_acc:
#                 best_acc = test_accuracy
#                 state = {'model': model.state_dict()}
#                 # best_model = '{}_{}_model.pkl'.format(i + 1, '%.3f' % best_acc)
#                 torch.save(state, pretrain_model_path + "/pretrain_" + str(old_class_num) + ".pkl")
#             print('epoch: {} is finished. accuracy is: {}'.format(i + 1, test_accuracy))
#
#     # res = torch.load(pretrain_model_path + "/pretrain_" + str(old_class_num) + ".pkl")
#     # model.load_state_dict(res['model'])
#     save_memory(model, train_dataset, old_class_num, memory_size, snr)
#
#     return best_acc
#
#
# def save_memory(model, train_dataset, old_class_num, memory_size, snr):
#     model.eval()  # 首先将模型转到推理模式
#     m = int(memory_size / old_class_num)  # 内存大小/类别总数 = 每个类别的样本个数
#     exampler_data = []
#     exampler_label = []
#     data, label = train_dataset.data, train_dataset.targets
#     for i in range(old_class_num):
#         ith_data = data[label == i]
#         ith_label = label[label == i]
#         exampler_data.append(ith_data)
#         exampler_label.append(ith_label)
#
#     # self.exemplar_set, _ = MinMaxUncertainty(self.model, exampler_data, exampler_label, self.memory_size)  # 创建该类的样本集
#     # self.exemplar_set, _ = RandomPicking(exampler_data, exampler_label, self.memory_size, random_seed=self.random_seed)  # 创建该类的样本集
#     exemplar_set_data, exemplar_set_label = mutualInfo_ori(model, exampler_data, exampler_label, memory_size)  # 创建该类的样本集
#     exemplar_set_data = np.concatenate(exemplar_set_data)
#     exemplar_set_label = np.concatenate(exemplar_set_label)
#     np.save("./app/data/train/memory/data_{}db.npy".format(snr), exemplar_set_data)
#     np.save("./app/data/train/memory/label_{}db.npy".format(snr), exemplar_set_label)
#

class Pretrain():

    def __init__(self, snr, old_class_num, memory_size, dataset="RML2016.04c"):
        super().__init__()
        self.snr = snr
        self.old_class_num = old_class_num
        self.memory_size = memory_size
        self.dataset = dataset
        self.result = None

    def get_one_hot(self, target, num_class):
        one_hot = torch.zeros(target.shape[0], num_class).to(device)
        one_hot = one_hot.scatter(dim=1, index=target.long().view(-1, 1), value=1.)
        return one_hot

    def compute_loss(self, imgs, target, numclass):
        output = self.model(imgs)  # ( , 20)
        target = self.get_one_hot(target, numclass)  # ( , 20)
        target = target.long()
        output, target = output.to(device), target.to(device)
        # class_loss = F.cross_entropy(output, target)
        log_prob = torch.nn.functional.log_softmax(output, dim=1)
        class_loss = -torch.sum(log_prob * target) / imgs.size(0)
        return class_loss

    def test(self, testloader):
        self.model.eval()  # 切换推理模式
        correct, total = 0, 0
        preds = []
        for setp, (imgs, labels) in enumerate(testloader):
            imgs = imgs.type(torch.FloatTensor)
            imgs, labels = imgs.to(device), labels.to(device)
            with torch.no_grad():
                outputs = self.model(imgs)
            outputs = outputs.cpu()
            preds.append(outputs)
            predicts = torch.max(outputs, dim=1)[1]
            correct += (predicts == labels.cpu()).sum()
            total += len(labels)
        accuracy = 100. * correct / total
        self.model.train()
        return accuracy, preds

    # 旧类数据训练旧模型
    def run(self):
        prepare_pretrain_data(self.snr, self.old_class_num, self.dataset)
        feature_extractor = getSignalModel(self.dataset, self.old_class_num)
        self.model = Network(self.old_class_num, feature_extractor)

        train_dataset = PretrainSignalDataset(snr=self.snr, data_type="train")
        test_dataset = PretrainSignalDataset(snr=self.snr, data_type="test")
        train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=batch_size, num_workers=num_worker)
        test_dataloader = DataLoader(test_dataset, shuffle=False, batch_size=batch_size, num_workers=num_worker)

        if pretrain_epoch == 0:
            res = torch.load(pretrain_model_path + "/pretrain_" + str(self.old_class_num) + ".pkl")
            self.model.load_state_dict(res['model'])
            test_accuracy, _ = self.test(test_dataloader)
            print("old model old data test accuracy: {}%".format(test_accuracy))
            return test_accuracy

        self.model.to(device)
        self.model.train()
        best_acc = 0
        optimizer = optim.Adam(params=self.model.parameters(), lr=learning_rate, weight_decay=0.001)
        for i in range(pretrain_epoch):
            loss = []
            if i == 20:
                for p in optimizer.param_groups:
                    p['lr'] = learning_rate / 2.
            if i == 40:
                for p in optimizer.param_groups:
                    p['lr'] = learning_rate / 4.
            if i == 60:
                for p in optimizer.param_groups:
                    p['lr'] = learning_rate / 8.
            if i == 80:
                for p in optimizer.param_groups:
                    p['lr'] = learning_rate / 16.
            for step, (data, label) in enumerate(train_dataloader):
                data = data.type(torch.FloatTensor)
                data, label = data.to(device), label.to(device)
                optimizer.zero_grad()
                loss_value = self.compute_loss(data, label, self.old_class_num)
                loss_value.backward()
                loss.append(loss_value.item())
                optimizer.step()
            loss = np.mean(loss)
            print("epoch:{}, loss_value: {}. The best accuray is {}".format(i + 1, loss, best_acc))
            if (i + 1) % 1 == 0:
                test_accuracy, _ = self.test(testloader=test_dataloader)
                if test_accuracy > best_acc:
                    best_acc = test_accuracy
                    state = {'model': self.model.state_dict()}
                    # best_model = '{}_{}_model.pkl'.format(i + 1, '%.3f' % best_acc)
                    torch.save(state, pretrain_model_path + "/pretrain_" + str(self.old_class_num) + ".pkl")
                print('epoch: {} is finished. accuracy is: {}'.format(i + 1, test_accuracy))

        # res = torch.load(pretrain_model_path + "/pretrain_" + str(old_class_num) + ".pkl")
        # model.load_state_dict(res['model'])
        self.save_memory(train_dataset, self.old_class_num, self.memory_size, self.snr)
        self.result = best_acc

        # return best_acc

    def save_memory(self, train_dataset, old_class_num, memory_size, snr):
        self.model.eval()  # 首先将模型转到推理模式
        m = int(memory_size / old_class_num)  # 内存大小/类别总数 = 每个类别的样本个数
        exampler_data = []
        exampler_label = []
        data, label = train_dataset.data, train_dataset.targets
        for i in range(old_class_num):
            ith_data = data[label == i]
            ith_label = label[label == i]
            exampler_data.append(ith_data)
            exampler_label.append(ith_label)

        # self.exemplar_set, _ = MinMaxUncertainty(self.model, exampler_data, exampler_label, self.memory_size)  # 创建该类的样本集
        # self.exemplar_set, _ = RandomPicking(exampler_data, exampler_label, self.memory_size, random_seed=self.random_seed)  # 创建该类的样本集
        exemplar_set_data, exemplar_set_label = mutualInfo_ori(self.model, exampler_data, exampler_label,
                                                               memory_size)  # 创建该类的样本集
        exemplar_set_data = np.concatenate(exemplar_set_data)
        exemplar_set_label = np.concatenate(exemplar_set_label)
        np.save("./data/train/memory/data_{}db.npy".format(snr), exemplar_set_data)
        np.save("./data/train/memory/label_{}db.npy".format(snr), exemplar_set_label)

class IncrementTrain():
    def __init__(self, snr, memory_size, new_class, task_size, dataset="RML2016.04c"):
        super().__init__()
        self.snr = snr
        self.memory_size = memory_size
        self.new_class = new_class
        self.task_size = task_size
        self.dataset = dataset
        self.result = 0.0
        self.all_class = 11
        self.old_model = None
        self.model = None
        # feature_extractor = getSignalModel(self.dataset, self.all_class-self.new_class)
        # self.old_model = Network(self.all_class-self.new_class, feature_extractor)
        # res = torch.load(pretrain_model_path + "/pretrain_" + str(self.all_class-self.new_class) + ".pkl")
        # self.old_model.load_state_dict(res['model'])

    def get_one_hot(self, target, num_class):
        one_hot = torch.zeros(target.shape[0], num_class).to(device)
        one_hot = one_hot.scatter(dim=1, index=target.long().view(-1, 1), value=1.)
        return one_hot

    def compute_loss(self, model, imgs, target, numclass):
        output = model(imgs)  # ( , 20)
        target = self.get_one_hot(target, numclass)  # ( , 20)
        target = target.long()
        output, target = output.to(device), target.to(device)
        # class_loss = F.cross_entropy(output, target)
        log_prob = torch.nn.functional.log_softmax(output, dim=1)
        class_loss = -torch.sum(log_prob * target) / imgs.size(0)
        return class_loss

    def compute_distill_and_class_loss(self, imgs, target, task):
        numclass = task[-1] + 1
        # aug_loss = self.ISDALoss(self.model, imgs, torch.tensor(target, dtype=torch.int64), 0.5)
        output = self.model(imgs)  # ( , 20)
        target = self.get_one_hot(target, numclass)  # ( , 20)
        target = target.long()
        output, target = output.to(device), target.to(device)
        # class_loss = F.cross_entropy(output, target)
        log_prob = torch.nn.functional.log_softmax(output, dim=1)
        class_loss = -torch.sum(log_prob * target) / imgs.size(0)

        old_output = self.old_model(imgs)
        old_output = F.softmax(old_output, dim=1)
        # print("old_output:", old_output.shape)
        old_label = torch.zeros(size=(imgs.size(0), numclass))
        old_label[:, :numclass - len(task)] = old_output
        old_label = old_label.to(device)
        # log_prob = torch.nn.functional.log_softmax(output, dim=1)
        distill_loss = -torch.sum(log_prob * old_label) / imgs.size(0)
        lam = (numclass - len(task)) / numclass
        return 0.61*class_loss + 0.39*distill_loss
        # return lam * class_loss + (1 - lam) * distill_loss

    def test(self, testloader):
        self.model.eval()  # 切换推理模式
        correct, total = 0, 0
        preds = []
        for setp, (imgs, labels) in enumerate(testloader):
            imgs = imgs.type(torch.FloatTensor)
            imgs, labels = imgs.to(device), labels.to(device)
            with torch.no_grad():
                outputs = self.model(imgs)
            outputs = outputs.cpu()
            preds.append(outputs)
            predicts = torch.max(outputs, dim=1)[1]
            correct += (predicts == labels.cpu()).sum()
            total += len(labels)
        accuracy = 100. * correct / total
        self.model.train()
        return accuracy, preds

    def increment_linearProgram(self, old_class, task, train_dataset):
        numclass = task[-1] + 1
        print("old_class:", old_class, numclass)
        self.model.eval()
        oldfeature = []
        for i in range(old_class):
            data, _ = train_dataset.get_image_class(i)
            data = torch.Tensor(data).to(device)
            features = self.model.get_feature(data)
            feature_center = torch.mean(features, dim=0, keepdim=True)
            oldfeature.append(feature_center)
        # oldfeature = torch.stack(oldfeature)
        oldfeature = torch.cat(oldfeature, dim=0)
        newfeature = []
        for i in range(old_class, numclass):
            data, _ = train_dataset.get_image_class(i)
            data = torch.Tensor(data).to(device)
            features = self.model.get_feature(data)
            print("features.shape:", features.shape)
            feature_center = torch.mean(features, dim=0, keepdim=True)
            newfeature.append(feature_center)
        # newfeature = torch.stack(newfeature)
        newfeature = torch.cat(newfeature, dim=0)
        weight = self.model.fc.weight.data
        print("oldfeature:", oldfeature.shape, newfeature.shape, weight.shape)
        oldfeature = oldfeature.cpu().detach().numpy()
        newfeature = newfeature.cpu().detach().numpy()
        weight = weight.t().cpu().numpy()
        res = get_weight_by_linearProgram(oldfeature, newfeature, weight, bound, len(task), feature_dim=512)
        print("new_weight:", np.array(res.x).shape)
        new_weight = res.x
        new_weight = new_weight.reshape((512, len(task)))
        # 这里将计算的新类权重传进去
        self.model.Incremental_learning(numclass, new_weight)  # 修改全连接层输出类别数，并且对模型初始化,

    def get_all_task_new_class(self, old_class):
        classes = []
        if self.new_class % self.task_size == 0:
            for cls in range(old_class, self.all_class, self.task_size):  # (9, 11, 2)
                task_cls = []
                for t in range(self.task_size):
                    task_cls.append(cls + t)
                classes.append(task_cls)
        else:
            rest = self.new_class % self.task_size
            for cls in range(old_class, self.all_class - rest, self.task_size):
                task_cls = []
                for t in range(self.task_size):
                    task_cls.append(cls + t)
                classes.append(task_cls)
            task_cls = []
            for t in range(rest):
                task_cls.append(self.all_class - rest + t)
            classes.append(task_cls)
        return classes

    def run(self):
        # [[7, 8], [9, 10]]
        old_class = self.all_class - self.new_class
        classes = self.get_all_task_new_class(old_class)

        print("classes:", classes)
        feature_extractor = getSignalModel(self.dataset, old_class)
        self.model = Network(old_class, feature_extractor)
        res = torch.load(pretrain_model_path + "pretrain_" + str(old_class) + ".pkl")
        self.model.load_state_dict(res['model'])
        self.model.to(device)

        # 共需增量len(classes)次
        for task in classes:
            num_class = task[-1] + 1
            old_class = num_class - len(task)
            self.old_model = copy.deepcopy(self.model)

            prepare_increment_data(task, self.snr)

            train_dataset = IncrementSignalDataset(snr=self.snr, data_type="train", dataset=self.dataset)
            # test_dataset = IncrementSignalDataset(snr=self.snr, data_type="test", dataset=self.dataset)
            test_dataset = EvalDataset(snr=self.snr, data_type="observed", dataset=self.dataset)
            train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=batch_size, num_workers=num_worker)
            test_dataloader = DataLoader(test_dataset, shuffle=False, batch_size=batch_size, num_workers=num_worker)

            self.increment_linearProgram(old_class, task, train_dataset)

            self.model.to(device)
            self.model.train()
            best_acc = 0
            optimizer = optim.Adam(params=self.model.parameters(), lr=learning_rate, weight_decay=0.001)
            for i in range(train_epoch):
                loss = []
                if i == 20:
                    for p in optimizer.param_groups:
                        p['lr'] = learning_rate / 2.
                if i == 40:
                    for p in optimizer.param_groups:
                        p['lr'] = learning_rate / 4.
                if i == 60:
                    for p in optimizer.param_groups:
                        p['lr'] = learning_rate / 8.
                if i == 80:
                    for p in optimizer.param_groups:
                        p['lr'] = learning_rate / 16.
                for step, (data, label) in enumerate(train_dataloader):
                    data = data.type(torch.FloatTensor)
                    data, label = data.to(device), label.to(device)
                    optimizer.zero_grad()
                    loss_value = self.compute_distill_and_class_loss(data, label, task)
                    loss_value.backward()
                    loss.append(loss_value.item())
                    optimizer.step()
                loss = np.mean(loss)
                print("epoch:{}, loss_value: {}. The best accuray is {}".format(i + 1, loss, best_acc))
                if (i + 1) % 1 == 0:
                    test_accuracy, _ = self.test(test_dataloader)
                    if test_accuracy > best_acc:
                        best_acc = test_accuracy
                        state = {'model': self.model.state_dict()}
                        # best_model = '{}_{}_model.pkl'.format(i + 1, '%.3f' % best_acc)
                        torch.save(state, pretrain_model_path + "/increment_" + str(num_class) + ".pkl")
                    print('epoch: {} is finished. accuracy is: {}'.format(i + 1, test_accuracy))

            # res = torch.load(pretrain_model_path + "/pretrain_" + str(old_class_num) + ".pkl")
            # model.load_state_dict(res['model'])
            self.save_memory(train_dataset, num_class, self.memory_size, self.snr)
            self.result = best_acc

    def save_memory(self, train_dataset, num_class, memory_size, snr):
        self.model.eval()  # 首先将模型转到推理模式
        m = int(memory_size / num_class)  # 内存大小/类别总数 = 每个类别的样本个数
        exampler_data = []
        exampler_label = []
        for i in range(num_class):
            data, label = train_dataset.get_image_class(i)
            exampler_data.append(data)
            exampler_label.append(label)

        # self.exemplar_set, _ = MinMaxUncertainty(self.model, exampler_data, exampler_label, self.memory_size)  # 创建该类的样本集
        # self.exemplar_set, _ = RandomPicking(exampler_data, exampler_label, self.memory_size, random_seed=self.random_seed)  # 创建该类的样本集
        exemplar_set_data, exemplar_set_label = mutualInfo_ori(self.model, exampler_data, exampler_label, memory_size)  # 创建该类的样本集
        exemplar_set_data = np.concatenate(exemplar_set_data)
        exemplar_set_label = np.concatenate(exemplar_set_label)
        np.save(root_path+"data/train/memory/data_{}db.npy".format(snr), exemplar_set_data)
        np.save(root_path+"data/train/memory/label_{}db.npy".format(snr), exemplar_set_label)

# 增量学习新类别数据
# class IncrementTrain(threading.Thread):
#     def __init__(self, snr, memory_size, new_class, task_size, dataset="RML2016.04c"):
#         super().__init__()
#         self.is_finished = False
#         self.snr = snr
#         self.memory_size = memory_size
#         self.new_class = new_class
#         self.task_size = task_size
#         self.dataset = dataset
#         self.result = 0.0
#         self.all_class = 11
#         self.old_model = None
#         self.model = None
#         # feature_extractor = getSignalModel(self.dataset, self.all_class-self.new_class)
#         # self.old_model = Network(self.all_class-self.new_class, feature_extractor)
#         # res = torch.load(pretrain_model_path + "/pretrain_" + str(self.all_class-self.new_class) + ".pkl")
#         # self.old_model.load_state_dict(res['model'])
#
#     def get_one_hot(self, target, num_class):
#         one_hot = torch.zeros(target.shape[0], num_class).to(device)
#         one_hot = one_hot.scatter(dim=1, index=target.long().view(-1, 1), value=1.)
#         return one_hot
#
#     def compute_loss(self, model, imgs, target, numclass):
#         output = model(imgs)  # ( , 20)
#         target = self.get_one_hot(target, numclass)  # ( , 20)
#         target = target.long()
#         output, target = output.to(device), target.to(device)
#         # class_loss = F.cross_entropy(output, target)
#         log_prob = torch.nn.functional.log_softmax(output, dim=1)
#         class_loss = -torch.sum(log_prob * target) / imgs.size(0)
#         return class_loss
#
#     def compute_distill_and_class_loss(self, imgs, target, task):
#         numclass = task[-1] + 1
#         # aug_loss = self.ISDALoss(self.model, imgs, torch.tensor(target, dtype=torch.int64), 0.5)
#         output = self.model(imgs)  # ( , 20)
#         target = self.get_one_hot(target, numclass)  # ( , 20)
#         target = target.long()
#         output, target = output.to(device), target.to(device)
#         # class_loss = F.cross_entropy(output, target)
#         log_prob = torch.nn.functional.log_softmax(output, dim=1)
#         class_loss = -torch.sum(log_prob * target) / imgs.size(0)
#
#         old_output = self.old_model(imgs)
#         old_output = F.softmax(old_output, dim=1)
#         print("old_output:", old_output.shape)
#         old_label = torch.zeros(size=(imgs.size(0), numclass))
#         old_label[:, :numclass - len(task)] = old_output
#         old_label = old_label.to(device)
#         # log_prob = torch.nn.functional.log_softmax(output, dim=1)
#         distill_loss = -torch.sum(log_prob * old_label) / imgs.size(0)
#         lam = (numclass - len(task)) / numclass
#         # return 0.61*class_loss + 0.39*distill_loss
#         return lam * class_loss + (1 - lam) * distill_loss
#
#     def test(self, testloader):
#         self.model.eval()  # 切换推理模式
#         correct, total = 0, 0
#         preds = []
#         for setp, (imgs, labels) in enumerate(testloader):
#             imgs = imgs.type(torch.FloatTensor)
#             imgs, labels = imgs.to(device), labels.to(device)
#             with torch.no_grad():
#                 outputs = self.model(imgs)
#             outputs = outputs.cpu()
#             preds.append(outputs)
#             predicts = torch.max(outputs, dim=1)[1]
#             correct += (predicts == labels.cpu()).sum()
#             total += len(labels)
#         accuracy = 100. * correct / total
#         self.model.train()
#         return accuracy, preds
#
#     def increment_linearProgram(self, old_class, task, train_dataset):
#         numclass = task[-1] + 1
#         print("old_class:", old_class, numclass)
#         self.model.eval()
#         oldfeature = []
#         for i in range(old_class):
#             data, _ = train_dataset.get_image_class(i)
#             data = torch.Tensor(data).to(device)
#             features = self.model.get_feature(data)
#             feature_center = torch.mean(features, dim=0, keepdim=True)
#             oldfeature.append(feature_center)
#         # oldfeature = torch.stack(oldfeature)
#         oldfeature = torch.cat(oldfeature, dim=0)
#         newfeature = []
#         for i in range(old_class, numclass):
#             data, _ = train_dataset.get_image_class(i)
#             data = torch.Tensor(data).to(device)
#             features = self.model.get_feature(data)
#             print("features.shape:", features.shape)
#             feature_center = torch.mean(features, dim=0, keepdim=True)
#             newfeature.append(feature_center)
#         # newfeature = torch.stack(newfeature)
#         newfeature = torch.cat(newfeature, dim=0)
#         weight = self.model.fc.weight.data
#         print("oldfeature:", oldfeature.shape, newfeature.shape, weight.shape)
#         oldfeature = oldfeature.cpu().detach().numpy()
#         newfeature = newfeature.cpu().detach().numpy()
#         weight = weight.t().cpu().numpy()
#         res = get_weight_by_linearProgram(oldfeature, newfeature, weight, bound, len(task), feature_dim=512)
#         print("new_weight:", np.array(res.x).shape)
#         new_weight = res.x
#         new_weight = new_weight.reshape((512, len(task)))
#         # 这里将计算的新类权重传进去
#         self.model.Incremental_learning(numclass, new_weight)  # 修改全连接层输出类别数，并且对模型初始化,
#
#     def get_all_task_new_class(self, old_class):
#         classes = []
#         if self.new_class % self.task_size == 0:
#             for cls in range(old_class, self.all_class, self.task_size):  # (9, 11, 2)
#                 task_cls = []
#                 for t in range(self.task_size):
#                     task_cls.append(cls + t)
#                 classes.append(task_cls)
#         else:
#             rest = self.new_class % self.task_size
#             for cls in range(old_class, self.all_class - rest, self.task_size):
#                 task_cls = []
#                 for t in range(self.task_size):
#                     task_cls.append(cls + t)
#                 classes.append(task_cls)
#             task_cls = []
#             for t in range(rest):
#                 task_cls.append(self.all_class - rest + t)
#             classes.append(task_cls)
#         return classes
#
#     def run(self):
#         self.is_finished = False
#         # [[7, 8], [9, 10]]
#         old_class = self.all_class - self.new_class
#         classes = self.get_all_task_new_class(old_class)
#
#         print("classes:", classes)
#         feature_extractor = getSignalModel(self.dataset, old_class)
#         self.model = Network(old_class, feature_extractor)
#         res = torch.load(pretrain_model_path + "/pretrain_" + str(old_class) + ".pkl")
#         self.model.load_state_dict(res['model'])
#         self.model.to(device)
#
#         # 共需增量len(classes)次
#         for task in classes:
#             num_class = task[-1] + 1
#             old_class = num_class - len(task)
#             self.old_model = copy.deepcopy(self.model)
#
#             prepare_increment_data(task, self.snr)
#
#             train_dataset = IncrementSignalDataset(snr=self.snr, data_type="train", dataset=self.dataset)
#             test_dataset = IncrementSignalDataset(snr=self.snr, data_type="test", dataset=self.dataset)
#             train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=batch_size, num_workers=num_worker)
#             test_dataloader = DataLoader(test_dataset, shuffle=False, batch_size=batch_size, num_workers=num_worker)
#
#             self.increment_linearProgram(old_class, task, train_dataset)
#
#             self.model.to(device)
#             self.model.train()
#             best_acc = 0
#             optimizer = optim.Adam(params=self.model.parameters(), lr=learning_rate, weight_decay=0.001)
#             for i in range(train_epoch):
#                 loss = []
#                 if i == 20:
#                     for p in optimizer.param_groups:
#                         p['lr'] = learning_rate / 2.
#                 if i == 40:
#                     for p in optimizer.param_groups:
#                         p['lr'] = learning_rate / 4.
#                 if i == 60:
#                     for p in optimizer.param_groups:
#                         p['lr'] = learning_rate / 8.
#                 if i == 80:
#                     for p in optimizer.param_groups:
#                         p['lr'] = learning_rate / 16.
#                 for step, (data, label) in enumerate(train_dataloader):
#                     data = data.type(torch.FloatTensor)
#                     data, label = data.to(device), label.to(device)
#                     optimizer.zero_grad()
#                     loss_value = self.compute_distill_and_class_loss(data, label, task)
#                     loss_value.backward()
#                     loss.append(loss_value.item())
#                     optimizer.step()
#                 loss = np.mean(loss)
#                 print("epoch:{}, loss_value: {}. The best accuray is {}".format(i + 1, loss, best_acc))
#                 if (i + 1) % 1 == 0:
#                     test_accuracy, _ = self.test(test_dataloader)
#                     if test_accuracy > best_acc:
#                         best_acc = test_accuracy
#                         state = {'model': self.model.state_dict()}
#                         # best_model = '{}_{}_model.pkl'.format(i + 1, '%.3f' % best_acc)
#                         torch.save(state, pretrain_model_path + "/pretrain_" + str(num_class) + ".pkl")
#                     print('epoch: {} is finished. accuracy is: {}'.format(i + 1, test_accuracy))
#
#             # res = torch.load(pretrain_model_path + "/pretrain_" + str(old_class_num) + ".pkl")
#             # model.load_state_dict(res['model'])
#             self.save_memory(train_dataset, num_class, self.memory_size, self.snr)
#             self.result = best_acc
#
#         self.is_finished = True
#
#     def save_memory(self, train_dataset, num_class, memory_size, snr):
#         self.model.eval()  # 首先将模型转到推理模式
#         m = int(memory_size / num_class)  # 内存大小/类别总数 = 每个类别的样本个数
#         exampler_data = []
#         exampler_label = []
#         for i in range(num_class):
#             data, label = train_dataset.get_image_class(i)
#             exampler_data.append(data)
#             exampler_label.append(label)
#
#         # self.exemplar_set, _ = MinMaxUncertainty(self.model, exampler_data, exampler_label, self.memory_size)  # 创建该类的样本集
#         # self.exemplar_set, _ = RandomPicking(exampler_data, exampler_label, self.memory_size, random_seed=self.random_seed)  # 创建该类的样本集
#         exemplar_set_data, exemplar_set_label = mutualInfo_ori(self.model, exampler_data, exampler_label, memory_size)  # 创建该类的样本集
#         exemplar_set_data = np.concatenate(exemplar_set_data)
#         exemplar_set_label = np.concatenate(exemplar_set_label)
#         np.save("./app/data/train/memory/data_{}db.npy".format(snr), exemplar_set_data)
#         np.save("./app/data/train/memory/label_{}db.npy".format(snr), exemplar_set_label)


if __name__ == '__main__':
    snr = 12
    old_class_num = 9
    memory_size = 200
    # preTrain = Pretrain(snr, old_class_num, memory_size, dataset="RML2016.04c")
    # preTrain.run()

    new_class = 2
    task_size = 2
    incrementTrain = IncrementTrain(snr, memory_size, new_class, task_size, dataset="RML2016.04c")
    incrementTrain.run()
