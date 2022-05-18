import torch
import torch.nn as nn
import torch.nn.functional as F
import torchsummary
import torchstat
import ptflops
import numpy as np

# acars模型
class AcarsModel(nn.Module):
    def __init__(self, numclass):
        super(AcarsModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 150, kernel_size=(15, 2), stride=(1, 1))
        self.conv2 = nn.Conv2d(150, 150, kernel_size=(7, 1), stride=(1, 1))
        self.conv3 = nn.Conv2d(150, 150, kernel_size=(5, 1), stride=(1, 1))
        self.conv4 = nn.Conv2d(150, 150, kernel_size=(5, 1), stride=(1, 1))
        self.conv5 = nn.Conv2d(150, 150, kernel_size=(3, 1), stride=(1, 1))
        self.conv6 = nn.Conv2d(150, 150, kernel_size=(5, 1), stride=(1, 1))
        self.conv7 = nn.Conv2d(150, 150, kernel_size=(5, 1), stride=(1, 1))

        self.bnconv1 = nn.BatchNorm2d(150)
        self.bnconv2 = nn.BatchNorm2d(150)
        self.bnconv3 = nn.BatchNorm2d(150)
        self.bnconv4 = nn.BatchNorm2d(150)
        self.bnconv5 = nn.BatchNorm2d(150)
        self.bnconv6 = nn.BatchNorm2d(150)
        self.bnconv7 = nn.BatchNorm2d(150)

        self.dropout = nn.Dropout()

        self.maxPool = nn.MaxPool2d((2, 1), stride=(2, 1), return_indices=True)

        self.fc = nn.Linear(150 * 28, 512)

        # self.fc = nn.Linear(512, numclass)

    def forward(self, x):
        x, _ = self.maxPool(F.relu(self.bnconv1(self.conv1(x))))
        x, _ = self.maxPool(F.relu(self.bnconv2(self.conv2(x))))
        x, _ = self.maxPool(F.relu(self.bnconv3(self.conv3(x))))
        x, _ = self.maxPool(F.relu(self.bnconv4(self.conv4(x))))
        x, _ = self.maxPool(F.relu(self.bnconv5(self.conv5(x))))
        x, _ = self.maxPool(F.relu(self.bnconv6(self.conv6(x))))
        x, _ = self.maxPool(F.relu(self.bnconv7(self.conv7(x))))
        # print(x.shape)
        x = x.view(-1, 150 * 28)
        x = self.dropout(F.relu(self.fc(x)))
        # x = self.fc(x)
        return x

    # def get_feature(self, x):
    #     x, _ = self.maxPool(F.relu(self.bnconv1(self.conv1(x))))
    #     x, _ = self.maxPool(F.relu(self.bnconv2(self.conv2(x))))
    #     x, _ = self.maxPool(F.relu(self.bnconv3(self.conv3(x))))
    #     x, _ = self.maxPool(F.relu(self.bnconv4(self.conv4(x))))
    #     x, _ = self.maxPool(F.relu(self.bnconv5(self.conv5(x))))
    #     x, _ = self.maxPool(F.relu(self.bnconv6(self.conv6(x))))
    #     x, _ = self.maxPool(F.relu(self.bnconv7(self.conv7(x))))
    #     # print(x.shape)
    #     x = x.view(-1, 150 * 28)
    #     feature = self.dropout(F.relu(self.dense1(x)))
    #     return feature


# RML2016.04c模型
class ModulationModel(nn.Module):
    def __init__(self, numclass):
        super(ModulationModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 128, kernel_size=(3, 2), stride=(1, 1))
        self.conv2 = nn.Conv2d(128, 256, kernel_size=(3, 1), stride=(1, 1))
        self.conv3 = nn.Conv2d(256, 512, kernel_size=(3, 1), stride=(1, 1))

        self.bnconv1 = nn.BatchNorm2d(128)
        self.bnconv2 = nn.BatchNorm2d(256)
        self.bnconv3 = nn.BatchNorm2d(512)

        self.dropout = nn.Dropout(0.5)

        self.maxpool = nn.MaxPool2d((3, 1), return_indices=True)

        self.fc = nn.Linear(512 * 3, 512)

        # self.cls = nn.Linear(512, numclass)

    def forward(self, x):
        x, _ = self.maxpool(F.relu(self.bnconv1(self.conv1(x))))
        x, _ = self.maxpool(F.relu(self.bnconv2(self.conv2(x))))
        x, _ = self.maxpool(F.relu(self.bnconv3(self.conv3(x))))
        # print(x.shape)
        x = x.view(-1, 512 * 3)
        x = self.dropout(F.relu(self.fc(x)))
        # x = self.cls(x)
        return x


def getSignalModel(dataset, numclass):
    feature_extractor = None
    if dataset == "acars":
        feature_extractor = AcarsModel(numclass)
    if dataset == "RML2016.04c":
        feature_extractor = ModulationModel(numclass)
    return feature_extractor


if __name__ == '__main__':
    # model = AcarsModel(20)
    # x = torch.Tensor(np.Random.randn(2, 1, 4096, 2))
    # out = model(x)

    model = ModulationModel(11)
    x = torch.Tensor(np.random.randn(2, 1, 128, 2))
    out = model(x)
    print(out.shape)

    # torchsummary.summary(model.cuda(), (1, 128, 2))

    # torchstat.stat(model, [1, 128, 2])

    # flops, params = ptflops.get_model_complexity_info(model, (1, 4096, 2), as_strings=True)

    # print(flops)
    # print(params)
