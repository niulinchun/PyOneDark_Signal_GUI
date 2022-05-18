import threading
import numpy as np
from torch.utils.data import DataLoader
from app.config import *
from app.model import getSignalModel
from app.myNetwork import Network
from app.signalDataset import EvalDataset
# from app.inference_UI import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def plot_confusion_matrix(y_true, y_pred, labels, title='Normalized confusion matrix', intFlag=0):
    ''' 绘制混淆矩阵 '''
    cmap = plt.cm.Blues
    ''' 颜色参考http://blog.csdn.net/haoji007/article/details/52063168'''
    cm = confusion_matrix(y_true, y_pred)
    tick_marks = np.array(range(len(labels))) + 0.5
    np.set_printoptions(precision=2)
    if cm.sum(axis=1)[:, np.newaxis].all() != 0:
        cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    else:
        intFlag = 1
    figure = plt.figure(figsize=(10, 9), dpi=360)
    ind_array = np.arange(len(labels))
    x, y = np.meshgrid(ind_array, ind_array)
    # intFlag = 0 # 标记在图片中对文字是整数型还是浮点型
    for x_val, y_val in zip(x.flatten(), y.flatten()):
        if (intFlag):
            c = cm[y_val][x_val]
            plt.text(x_val, y_val, "%d" % (c,), color='red', fontsize=12, va='center', ha='center')

        else:
            c = cm_normalized[y_val][x_val]
            if (c > 0.0001):
                # 这里是绘制数字，可以对数字大小和颜色进行修改
                plt.text(x_val, y_val, "%0.2f" % (c * 100,) + "%", color='red', fontsize=10, va='center', ha='center')
            else:
                plt.text(x_val, y_val, "%d" % (0,), color='red', fontsize=10, va='center', ha='center')
    if (intFlag):
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
    else:
        plt.imshow(cm_normalized, interpolation='nearest', cmap=cmap)
    plt.gca().set_xticks(tick_marks, minor=True)
    plt.gca().set_yticks(tick_marks, minor=True)
    plt.gca().xaxis.set_ticks_position('none')
    plt.gca().yaxis.set_ticks_position('none')
    plt.grid(True, which='minor', linestyle='-')
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.title('Confusion Matrix', fontsize=18)
    plt.colorbar()
    xlocations = np.array(range(len(labels)))
    plt.xticks(xlocations, labels, rotation=90)
    plt.yticks(xlocations, labels)
    plt.ylabel('Index of True Classes')
    plt.xlabel('Index of Predict Classes')
    plt.savefig('./gui/images/app_images/confusion_matrix.jpg', dpi=300)

    # image = fig2data(figure)
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # return image
    # plt.title(title)
    # plt.show()

class EvalThread():

    def __init__(self, model_path, snr, new_class, dataset="RML2016.04c"):
        super().__init__()
        self.model_path = model_path
        self.snr = snr
        self.new_class = new_class
        self.dataset = dataset
        self.result = None
        self.model = None

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
        old_dataset = EvalDataset(snr=self.snr, data_type="old", dataset=self.dataset)
        new_dataset = EvalDataset(snr=self.snr, data_type="new", dataset=self.dataset)
        observed_dataset = EvalDataset(snr=self.snr, data_type="observed", dataset=self.dataset)

        old_dataloader = DataLoader(old_dataset, shuffle=False, batch_size=batch_size, num_workers=num_worker)
        new_dataloader = DataLoader(new_dataset, shuffle=False, batch_size=batch_size, num_workers=num_worker)
        observed_dataloader = DataLoader(observed_dataset, shuffle=False, batch_size=batch_size, num_workers=num_worker)

        feature_extractor = getSignalModel(self.dataset, all_class)
        self.model = Network(all_class, feature_extractor)
        res = torch.load(self.model_path)
        self.model.load_state_dict(res['model'])
        self.model.to(device)

        old_oa, _ = self.test(old_dataloader)
        new_oa, _ = self.test(new_dataloader)
        all_oa, pred = self.test(observed_dataloader)

        pred = np.concatenate(pred)

        y_pred = np.argmax(pred, axis=1)
        y_true = observed_dataset.targets
        print(y_pred.shape, y_true.shape)

        confusion_matrix = plot_confusion_matrix(y_true, y_pred, modName, title='Normalized confusion matrix', intFlag=0)

        # self.result = [old_oa, new_oa, all_oa], confusion_matrix
        self.result = old_oa, new_oa, all_oa

# class EvalThread(threading.Thread):
#
#     def __init__(self, snr, new_class, dataset="RML2016.04c"):
#         super().__init__()
#         self.is_finished = False
#         self.snr = snr
#         self.new_class = new_class
#         self.dataset = dataset
#         self.result = None
#         self.model = None
#
#     def get_one_hot(self, target, num_class):
#         one_hot = torch.zeros(target.shape[0], num_class).to(device)
#         one_hot = one_hot.scatter(dim=1, index=target.long().view(-1, 1), value=1.)
#         return one_hot
#
#     def compute_loss(self, imgs, target, numclass):
#         output = self.model(imgs)  # ( , 20)
#         target = self.get_one_hot(target, numclass)  # ( , 20)
#         target = target.long()
#         output, target = output.to(device), target.to(device)
#         # class_loss = F.cross_entropy(output, target)
#         log_prob = torch.nn.functional.log_softmax(output, dim=1)
#         class_loss = -torch.sum(log_prob * target) / imgs.size(0)
#         return class_loss
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
#     # 旧类数据训练旧模型
#     def run(self):
#         self.is_finished = False
#
#         old_dataset = EvalDataset(snr=self.snr, data_type="old", dataset=self.dataset)
#         new_dataset = EvalDataset(snr=self.snr, data_type="new", dataset=self.dataset)
#         observed_dataset = EvalDataset(snr=self.snr, data_type="observed", dataset=self.dataset)
#
#         old_dataloader = DataLoader(old_dataset, shuffle=False, batch_size=batch_size, num_workers=num_worker)
#         new_dataloader = DataLoader(new_dataset, shuffle=False, batch_size=batch_size, num_workers=num_worker)
#         observed_dataloader = DataLoader(observed_dataset, shuffle=False, batch_size=batch_size, num_workers=num_worker)
#
#         feature_extractor = getSignalModel(self.dataset, all_class)
#         self.model = Network(all_class, feature_extractor)
#         res = torch.load(pretrain_model_path + "/pretrain_" + str(all_class) + ".pkl")
#         self.model.load_state_dict(res['model'])
#         self.model.to(device)
#
#         old_oa, _ = self.test(old_dataloader)
#         new_oa, _ = self.test(new_dataloader)
#         all_oa, pred = self.test(observed_dataloader)
#
#         pred = np.concatenate(pred)
#
#         y_pred = np.argmax(pred, axis=1)
#         y_true = observed_dataset.targets
#         print(y_pred.shape, y_true.shape)
#
#         confusion_matrix = plot_confusion_matrix(y_true, y_pred, modName, title='Normalized confusion matrix', intFlag=0)
#
#         self.is_finished = True
#
#         self.result = [old_oa, new_oa, all_oa], confusion_matrix


if __name__ == '__main__':
    t = EvalThread(snr=12, new_class=2, dataset="RML2016.04c")
    t.start()
