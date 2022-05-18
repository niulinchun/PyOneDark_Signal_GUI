import torch
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import cv2
from sklearn.metrics import confusion_matrix
from app.config import *

from app.dataProcess import split_test_and_train
import os

# modName = [b'8PSK', b'AM-DSB', b'AM-SSB', b'BPSK', b'CPFSK', b'GFSK', b'PAM4', b'QAM16', b'QAM64', b'QPSK', b'WBFM']
from app.model import getSignalModel
from app.myNetwork import Network
from app.evaluate import EvalThread

def showDataset(test_percent, snr, random_seed, img_num, dataset="RML2016.04c"):
    split_test_and_train(test_percent=test_percent, snr=snr, random_seed=random_seed)
    # 数据集路径及调制类型获取
    root = "E:/workspace/Pycharm_workspace/PyOneDark_Signal_GUI/app/data/"
    # x_train = np.load(root + "train/data_{}db.npy".format(snr))
    # y_train = np.load(root + "train/label_{}db.npy".format(snr))

    x_train = np.load("./app/data/train/data_{}db.npy".format(snr))
    y_train = np.load("./app/data/train/label_{}db.npy".format(snr))

    # 测试区间获取
    # start_idx = int(idx_range[0])-1
    # end_idx = int(idx_range[1])-1
    start_idx = 0
    end_idx = len(x_train)
    # 随机取N个样本绘制并返回
    raw_images = []
    show_idx = random.sample(range(start_idx, end_idx), img_num)
    for idx in show_idx:
        raw_image = showOriSignal(x_train[idx], modName[y_train[idx]], idx)
        raw_images.append(raw_image)

    # cv2::Mat
    return raw_images


def showDataset_(snr, old_class, new_class, dataset="RML2016.04c"):
    # split_test_and_train(test_percent=test_percent, snr=snr, random_seed=random_seed)
    # 数据集路径及调制类型获取
    # x_train = np.load(root + "train/data_{}db.npy".format(snr))
    # y_train = np.load(root + "train/label_{}db.npy".format(snr))

    x_train = np.load("./app/data/train/data_{}db.npy".format(snr))
    y_train = np.load("./app/data/train/label_{}db.npy".format(snr))
    # x_train = np.load("./data/train/data_{}db.npy".format(snr))
    # y_train = np.load("./data/train/label_{}db.npy".format(snr))
    old_data = []
    new_data = []
    for i in range(len(old_class)):
        label = modName_map.get(old_class[i])
        ith_data = x_train[y_train == label]
        show_idx = random.sample(range(0, len(ith_data)), 1)
        old_data.append(ith_data[show_idx[0]])

    for i in range(len(new_class)):
        label = modName_map.get(new_class[i])
        ith_data = x_train[y_train == label]
        show_idx = random.sample(range(0, len(ith_data)), 1)
        new_data.append(ith_data[show_idx[0]])
    image_old = showOriSignal_(old_data, old_class, "old")
    image_new = showOriSignal_(new_data, new_class, "new")

    # cv2::Mat
    return image_old, image_new


def showOriSignal(sample, mod_name, idx):
    ''' 绘制并展示一个样本信号的图像 '''

    signal_data = sample[0]

    figure = plt.figure(figsize=(9, 6))
    plt.title(str(idx) + " " + str(mod_name), fontsize=30)
    plt.xlabel('N', fontsize=20)
    plt.ylabel("Value", fontsize=20)

    plt.plot(signal_data[:, 0], label='I', linewidth=2.0)
    plt.plot(signal_data[:, 1], color='red', label='Q', linewidth=2.0)
    plt.legend(loc="upper right", fontsize=30)
    plt.savefig("./gui/images/app_images/signal_sample.jpg", dpi=300)
    plt.close()
    # image = fig2data(figure)
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # return image

def showOriSignal_(data_list, label_list, flag="old"):

    fig, subs = plt.subplots(1, len(data_list), figsize=(4*len(data_list), 2))

    for i in range(len(data_list)):
        signal_data = data_list[i][0]
        title = label_list[i]
        subs[i].set_title(str(title), fontsize=20)
        # subs[i].set_xlabel('N', fontsize=10)
        # subs[i].set_ylabel("Value", fontsize=10)

        subs[i].plot(signal_data[:, 0], label='I', linewidth=2.0)
        subs[i].plot(signal_data[:, 1], color='red', label='Q', linewidth=2.0)
        subs[i].legend(loc="upper right", fontsize=15)

    plt.show()
    # plt.close()
    fig.savefig('./gui/images/app_images/image_{}.png'.format(flag), bbox_inches='tight', pad_inches=0, dpi=200)
    # fig.savefig('./image_{}.png'.format(flag), bbox_inches='tight', pad_inches=0, dpi=500)
    plt.close()
    image = fig2data(fig)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image


def fig2data(fig):
    """
    fig = plt.figure()
    image = fig2data(fig)
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    import PIL.Image as Image
    # draw the renderer
    fig.canvas.draw()

    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)

    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll(buf, 3, axis=2)
    image = Image.frombytes("RGBA", (w, h), buf.tostring())
    image = np.asarray(image)
    return image


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

def next_sample(snr, task_size, pick_method, class_type, old_class, dataset="RML2016.04c"):
    for i in range(len(old_class)):
        old_class[i] = str(old_class[i], "utf-8")
    model_name = "_".join(old_class)
    # 8PSK_AM-DSB_AM-SSB_BPSK_CPFSK_GFSK_PAM4_QAM16_QAM64.pkl
    model_path = "./app/checkpoint/task_{}/{}/{}.pkl".format(task_size, pick_method, model_name)

    feature_extractor = getSignalModel(dataset=dataset, numclass=len(old_class))
    model = Network(len(old_class), feature_extractor)
    old_data = np.load(root_path + "data/test/old/data_{}db.npy".format(snr), allow_pickle=True)
    old_label = np.load(root_path + "data/test/old/label_{}db.npy".format(snr), allow_pickle=True)
    new_data = np.load(root_path + "data/test/new/data_{}db.npy".format(snr), allow_pickle=True)
    new_label = np.load(root_path + "data/test/new/label_{}db.npy".format(snr), allow_pickle=True)
    data = np.concatenate([old_data, new_data])
    label = np.concatenate([old_label, new_label])

    feature_extractor = getSignalModel(dataset, len(old_class))
    model = Network(all_class, feature_extractor)
    res = torch.load(model_path)
    model.load_state_dict(res['model'])
    # model.to(device)
    if class_type == "随机":
        show_idx = random.sample(range(0, len(data)), 1)
        show_idx = show_idx[0]
        showOriSignal(data[show_idx], modName[label[show_idx]], show_idx)
        start = time.time()
        pred = model(torch.Tensor(data[show_idx:show_idx+1]))
        # pred = pred.cpu().numpy()
        pred = pred.detach().numpy()
        pred = np.argmax(pred)
        end = time.time()
        return modName_map_[label[show_idx]], modName_map_[pred], (end-start)
        # raw_image = showOriSignal(data[show_idx], modName[label[show_idx]], show_idx)
    elif class_type in old_class:
        ith_data = old_data[old_label == modName_map.get(bytes(class_type, "utf-8"))]
        ith_label = old_label[old_label == modName_map.get(bytes(class_type, "utf-8"))]
        show_idx = random.sample(range(0, len(ith_data)), 1)
        show_idx = show_idx[0]
        showOriSignal(ith_data[show_idx], modName[ith_label[show_idx]], show_idx)
        start = time.time()
        pred = model(torch.Tensor(ith_data[show_idx:show_idx+1]))
        # pred = pred.cpu().numpy()
        pred = pred.detach().numpy()
        pred = np.argmax(pred)
        end = time.time()
        return modName_map_[ith_label[show_idx]], modName_map_[pred], (end-start)
    else:
        ith_data = new_data[new_label == modName_map.get(bytes(class_type, "utf-8"))]
        ith_label = new_label[new_label == modName_map.get(bytes(class_type, "utf-8"))]
        show_idx = random.sample(range(0, len(ith_data)), 1)
        show_idx = show_idx[0]
        showOriSignal(ith_data[show_idx], modName[ith_label[show_idx]], show_idx)
        start = time.time()
        pred = model(torch.Tensor(ith_data[show_idx:show_idx+1]))
        # pred = pred.cpu().numpy()
        pred = pred.detach().numpy()
        pred = np.argmax(pred)
        end = time.time()
        return modName_map_[ith_label[show_idx]], modName_map_[pred], (end-start)

def inference(snr, pick_method, task_size, old_class, dataset="RML2016.04c"):
    for i in range(len(old_class)):
        old_class[i] = str(old_class[i], "utf-8")
    model_name = "_".join(old_class)
    # 8PSK_AM-DSB_AM-SSB_BPSK_CPFSK_GFSK_PAM4_QAM16_QAM64.pkl
    print(model_name)
    model_path = "./app/checkpoint/task_{}/{}/{}.pkl".format(task_size, pick_method, model_name)

    # feature_extractor = getSignalModel(dataset, len(old_class))
    # model = Network(all_class, feature_extractor)
    # res = torch.load(model_path)
    # model.load_state_dict(res['model'])
    # model.to(device)

    # snr, new_class, dataset = "RML2016.04c"

    eval = EvalThread(model_path, snr, all_class-len(old_class), dataset="RML2016.04c")
    eval.run()
    return eval.result



if __name__ == '__main__':
    snr = 12
    old_class = [b'AM-DSB', b'AM-SSB', b'BPSK', b'CPFSK', b'GFSK', b'PAM4']
    new_class = [b'8PSK', b'QAM16', b'QAM64', b'QPSK', b'WBFM']
    showDataset_(snr, old_class, new_class, dataset="RML2016.04c")