# from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout, QLabel
# from PyQt6.QtCore import QTimer, QDateTime
# import sys
#
#
# class ShowTime(QWidget):
#     def __init__(self, parent=None):
#         super(ShowTime, self).__init__(parent)
#         self.setWindowTitle("动态显示当前时间")
#         self.label = QLabel('显示当前时间')
#         self.startBtn = QPushButton('开始')
#         self.endBtn = QPushButton('结束')
#         layout = QGridLayout()
#         self.timer = QTimer()
#         self.timer.timeout.connect(lambda: self.showTime(2))
#         layout.addWidget(self.label, 0, 0, 1, 2)
#         layout.addWidget(self.startBtn, 1, 0)
#         layout.addWidget(self.endBtn, 1, 1)
#         self.startBtn.clicked.connect(self.startTimer)
#         self.endBtn.clicked.connect(self.endTimer)
#         self.setLayout(layout)
#
#     def showTime(self, i):
#         print("开始计时", i)
#         time = QDateTime.currentDateTime()
#
#         timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
#         self.label.setText(timeDisplay)
#
#     def startTimer(self):
#         self.timer.start(1000)
#         self.startBtn.setEnabled(False)
#         self.endBtn.setEnabled(True)
#
#     def endTimer(self):
#         self.timer.stop()
#         self.startBtn.setEnabled(True)
#         self.endBtn.setEnabled(False)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     form = ShowTime()
#     form.show()
#     sys.exit(app.exec())
# ---------------------------------
# import sys
# from PyQt6 import QtWidgets
#
#
# class Demo(QtWidgets.QWidget):
#     """
#     setGeometry()方法中是个参数的函数是：
#     setGeometry(左右， 上下， 宽， 高)
#     基于二维平面四个参数可以这样理解。
#     """
#
#     def __init__(self):
#         super().__init__()
#         # 设置窗口大小
#         size = 200, 400
#         # self.resize(*size)
#         offset = 0
#         size2 = size[0], size[1] + offset
#         self.resize(*size2)
#         # self.setMaximumSize(*size2)
#         self.setMinimumSize(*size2)
#
#         self.button = QtWidgets.QPushButton(self)
#         self.button.setText('button')
#         self.button.setGeometry(0, 0, 50, 20)
#
#         self.line = QtWidgets.QLineEdit(self)
#         self.line.setGeometry(53, 0, 140, 20)
#
#         # 默认是隐藏的，需要使用show()方法显示对话框
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     ex = Demo()
#     sys.exit(app.exec())

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# author: chenqionghe

# fig, subs = plt.subplots(2, 2)
#
# # 画第1个图：折线图
# x = np.arange(1, 100)
# subs[0][0].plot(x, x * x)
#
# # 画第2个图：散点图
# subs[0][1].scatter(np.arange(0, 10), np.Random.rand(10))
# subs[0][1].set_title("title")
#
# # 画第3个图：饼图
# subs[1][0].pie(x=[15, 30, 45, 10], labels=list('ABCD'), autopct='%.0f', explode=[0, 0.05, 0, 0])
#
# # 画第4个图：条形图
# subs[1][1].bar([20, 10, 30, 25, 15], [25, 15, 35, 30, 20], color='b')
# plt.show()
# plt.close()

# fig, subs = plt.subplots(nrows=1, ncols=3, figsize=(24, 8))
# ax_list = []
#
# for j in range(1):
#     for i in range(3):
#         ax_list.append(subs[i])
#
# for i in ax_list:
#     i.bar([20, 10, 30, 25, 15], [25, 15, 35, 30, 20], color='b')
#
# plt.show()
# plt.close()

a = ['BPSK', 'SAS', '9PSO']
b = "_".join(a)
print(b)
