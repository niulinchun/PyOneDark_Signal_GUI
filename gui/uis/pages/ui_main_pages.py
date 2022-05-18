# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from app.config import modName
from qt_core import *


class Ui_MainPages(object):
    # 这里把空的content_area_Frame传过来, 设置一些参数，比如大小
    # 这里的MainPages参数呢是真正的主内容的Frame，往该Frame中添加一些下拉框，展示控件之类的东西

    def setup_main(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        # 首先设置一下默认的内容区域大小
        MainPages.resize(860, 600)
        # 这里开始时创建page1 设置一下布局
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        # 堆载窗口控件，就是多个页面来回切换，可以往该空间中添加多个页面，每个页面都是一个QWidget
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")

    def setup_page_1(self):
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        # 第一页的布局，可以往布局里添加控件
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        # 这里QFrame穿page_1指的是该Frame的父组件是page_1,但是并没有把该组件放到父组件，最后还得addWidget
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)

        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)

    def setup_page_2(self):
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        # 首先定义了page2的整体布局为垂直布局
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        # page2中的滚动区域是。。。
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        # 这里的content是。。。
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 580))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        # 水平布局
        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        # 垂直布局中添加水平布局
        self.verticalLayout.addLayout(self.row_1_layout)

        # 水平布局
        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)
        # 水平布局
        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)
        # 垂直布局
        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)
        # 垂直布局
        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        # 这里是滚动区域中添加了内容
        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)

    def setup_page_IL(self):
        self.page_IL = QWidget()
        self.page_IL.setObjectName(u"page_IL")
        self.page_IL.setStyleSheet(u"QFrame {\n""font-size: 16pt;\n""}")
        self.page_IL_layout = QVBoxLayout(self.page_IL)
        self.page_IL_layout.setObjectName(u"page_IL_layout")

        self.page_IL_top_layout = QVBoxLayout(self.page_IL)

        self.title_label_IL = QLabel(self.page_IL)
        self.title_label_IL.setText("Incremental Learning System")
        self.title_label_IL.setObjectName(u"title_label_IL")
        self.title_label_IL.setMaximumSize(QSize(16777215, 80))
        font_IL = QFont()
        font_IL.setPointSize(26)
        font_IL.setBold(False)
        font_IL.setItalic(False)
        self.title_label_IL.setFont(font_IL)
        self.title_label_IL.setStyleSheet(u"font: 26pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.title_label_IL.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        # self.title_label_IL.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.page_IL_top_layout.addWidget(self.title_label_IL)
        self.page_IL_layout.addLayout(self.page_IL_top_layout)

        self.empty_label = QLabel(self.page_IL)
        self.empty_label.setText(" ")
        self.empty_label.setObjectName(u"label_27")
        self.empty_label.setMaximumSize(QSize(16777215, 10))
        # self.page_IL_layout.addWidget()

        # 下拉框之前的label
        self.label_IL_data = QLabel(self.page_IL)
        self.label_IL_data.setText("Choose Dataset")
        self.label_IL_data.setObjectName(u"label_IL_data")
        self.label_IL_data.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        # 下拉框
        self.comboBox_IL_data = QComboBox(self.page_IL)
        self.comboBox_IL_data.addItem("")
        self.comboBox_IL_data.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data.setMinimumSize(QSize(150, 40))
        self.comboBox_IL_data.setMaximumSize(QSize(100, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data.setFont(font_comboBox)
        self.comboBox_IL_data.setAutoFillBackground(False)
        self.comboBox_IL_data.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                            "border-radius: 5px;\n"
                                            "border: 2px solid rgb(33, 37, 43);\n"
                                            "padding: 5px;\n"
                                            "padding-left: 10px;\n"
                                            "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data.setIconSize(QSize(16, 16))
        self.comboBox_IL_data.setFrame(True)
        # 下拉框之前的label1
        self.label_IL_data1 = QLabel(self.page_IL)
        self.label_IL_data1.setText("Choose Dataset")
        self.label_IL_data1.setObjectName(u"label_IL_data")
        self.label_IL_data1.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data1.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data1.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        # 下拉框
        self.comboBox_IL_data1 = QComboBox(self.page_IL)
        self.comboBox_IL_data1.addItem("")
        self.comboBox_IL_data1.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data1.setMinimumSize(QSize(150, 40))
        self.comboBox_IL_data1.setMaximumSize(QSize(100, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data1.setFont(font_comboBox)
        self.comboBox_IL_data1.setAutoFillBackground(False)
        self.comboBox_IL_data1.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                             "border-radius: 5px;\n"
                                             "border: 2px solid rgb(33, 37, 43);\n"
                                             "padding: 5px;\n"
                                             "padding-left: 10px;\n"
                                             "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data.setIconSize(QSize(16, 16))
        self.comboBox_IL_data.setFrame(True)
        # 下拉框之前的label2
        self.label_IL_data2 = QLabel(self.page_IL)
        self.label_IL_data2.setText("Choose Dataset")
        self.label_IL_data2.setObjectName(u"label_IL_data")
        self.label_IL_data2.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data2.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.label_IL_data2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        # 下拉框
        self.comboBox_IL_data2 = QComboBox(self.page_IL)
        for i in range(5):
            self.comboBox_IL_data2.addItem("")
        self.comboBox_IL_data2.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data2.setMinimumSize(QSize(150, 40))
        self.comboBox_IL_data2.setMaximumSize(QSize(100, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data2.setFont(font_comboBox)
        self.comboBox_IL_data2.setAutoFillBackground(False)
        self.comboBox_IL_data2.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                             "border-radius: 5px;\n"
                                             "border: 2px solid rgb(33, 37, 43);\n"
                                             "padding: 5px;\n"
                                             "padding-left: 10px;\n"
                                             "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data.setIconSize(QSize(16, 16))
        self.comboBox_IL_data.setFrame(True)
        # 下拉框之前的label3
        self.label_IL_data3 = QLabel(self.page_IL)
        self.label_IL_data3.setText("Choose Dataset")
        self.label_IL_data3.setObjectName(u"label_IL_data")
        self.label_IL_data3.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data3.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data2.setAlignment(Qt.AlignRight)

        # 下拉框
        self.comboBox_IL_data3 = QComboBox(self.page_IL)
        self.comboBox_IL_data3.addItem("")
        self.comboBox_IL_data3.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data3.setMinimumSize(QSize(150, 40))
        self.comboBox_IL_data3.setMaximumSize(QSize(100, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data3.setFont(font_comboBox)
        self.comboBox_IL_data3.setAutoFillBackground(False)
        self.comboBox_IL_data3.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                             "border-radius: 5px;\n"
                                             "border: 2px solid rgb(33, 37, 43);\n"
                                             "padding: 5px;\n"
                                             "padding-left: 10px;\n"
                                             "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data.setIconSize(QSize(16, 16))
        self.comboBox_IL_data.setFrame(True)

        self.page_IL_layout1 = QHBoxLayout(self.page_IL)
        self.page_IL_layout1.addWidget(self.label_IL_data)
        self.page_IL_layout1.addWidget(self.comboBox_IL_data)
        self.page_IL_layout1.addWidget(self.label_IL_data3)
        self.page_IL_layout1.addWidget(self.comboBox_IL_data3)

        self.page_IL_layout2 = QHBoxLayout(self.page_IL)
        self.page_IL_layout2.addWidget(self.label_IL_data1)
        self.page_IL_layout2.addWidget(self.comboBox_IL_data1)

        self.page_IL_layout3 = QHBoxLayout(self.page_IL)
        self.page_IL_layout3.addWidget(self.label_IL_data2)
        self.page_IL_layout3.addWidget(self.comboBox_IL_data2)

        self.page_IL_layout.addLayout(self.page_IL_layout1)
        self.page_IL_layout.addLayout(self.page_IL_layout2)
        self.page_IL_layout.addLayout(self.page_IL_layout3)

        self.page_IL_layout.setStretchFactor(self.page_IL_layout1, 2)
        self.page_IL_layout.setStretchFactor(self.page_IL_layout2, 4)
        self.page_IL_layout.setStretchFactor(self.page_IL_layout3, 4)

        self.pages.addWidget(self.page_IL)

    def setup_page_OP(self):
        self.page_OP = QWidget()
        self.page_OP.setObjectName(u"page_OP")
        # 以下4行不知道 QSizePolicy
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page_OP.sizePolicy().hasHeightForWidth())
        self.page_OP.setSizePolicy(sizePolicy1)
        # 设置字体大小
        self.page_OP.setStyleSheet(u"QFrame {\n"
                                   "	font-size: 16pt;\n"
                                   "}")
        # 这个页面定义了一个垂直布局
        self.page_3_layout = QVBoxLayout(self.page_OP)
        # 布局起名
        self.page_3_layout.setObjectName(u"page_3_layout")
        # 定义页面顶部标题 电磁信号增量分类系统
        self.title_label_op = QLabel(self.page_OP)
        self.title_label_op.setObjectName(u"title_label_op")
        self.title_label_op.setMaximumSize(QSize(16777215, 40))
        # 定义一个字体样式
        font3 = QFont()
        font3.setPointSize(26)
        font3.setBold(False)
        font3.setItalic(False)
        # 顶部标题的字体设置
        self.title_label_op.setFont(font3)
        # 微软雅黑
        self.title_label_op.setStyleSheet(u"font: 26pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # 标题居中
        self.title_label_op.setAlignment(Qt.AlignCenter)

        # 将上述定义的标题放到垂直布局中
        self.page_3_layout.addWidget(self.title_label_op)

        self.label_27 = QLabel(self.page_OP)  # 就是个空的占位符吧相当于，setText("")
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 10))

        self.page_3_layout.addWidget(self.label_27)  # 放到垂直布局中

        # 定义两个水平布局
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        # 数据集
        self.label_op_data = QLabel(self.page_OP)
        self.label_op_data.setObjectName(u"label_op_data")
        self.label_op_data.setMaximumSize(QSize(16777215, 20))
        self.label_op_data.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_op_data.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_op_data)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        # 数据集下拉框
        self.comboBox_op_data = QComboBox(self.page_OP)
        self.comboBox_op_data.addItem("")
        self.comboBox_op_data.setObjectName(u"comboBox_op_data")
        self.comboBox_op_data.setMinimumSize(QSize(150, 40))
        self.comboBox_op_data.setMaximumSize(QSize(100, 16777215))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        self.comboBox_op_data.setFont(font4)
        self.comboBox_op_data.setAutoFillBackground(False)
        self.comboBox_op_data.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                            "border-radius: 5px;\n"
                                            "border: 2px solid rgb(33, 37, 43);\n"
                                            "padding: 5px;\n"
                                            "padding-left: 10px;\n"
                                            "font: 14pt \"Segoe UI\";")
        self.comboBox_op_data.setIconSize(QSize(16, 16))
        self.comboBox_op_data.setFrame(True)

        self.horizontalLayout_8.addWidget(self.comboBox_op_data)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.page_OP)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_op_snr = QLabel(self.page_OP)
        self.label_op_snr.setObjectName(u"label_op_snr")
        self.label_op_snr.setMinimumSize(QSize(20, 0))
        self.label_op_snr.setMaximumSize(QSize(16777215, 20))
        self.label_op_snr.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_op_snr.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_op_snr)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.comboBox_op_snr = QComboBox(self.page_OP)
        self.comboBox_op_snr.addItem("")
        self.comboBox_op_snr.setObjectName(u"comboBox_op_snr")
        self.comboBox_op_snr.setMinimumSize(QSize(0, 40))
        self.comboBox_op_snr.setMaximumSize(QSize(100, 16777215))
        self.comboBox_op_snr.setFont(font4)
        self.comboBox_op_snr.setAutoFillBackground(False)
        self.comboBox_op_snr.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                           "border-radius: 5px;\n"
                                           "border: 2px solid rgb(33, 37, 43);\n"
                                           "padding: 5px;\n"
                                           "padding-left: 10px;\n"
                                           "font: 14pt \"Segoe UI\";")
        self.comboBox_op_snr.setIconSize(QSize(16, 16))
        self.comboBox_op_snr.setFrame(True)

        self.horizontalLayout_13.addWidget(self.comboBox_op_snr)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_3 = QLabel(self.page_OP)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_11.addWidget(self.label_3)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_op_sample = QLabel(self.page_OP)
        self.label_op_sample.setObjectName(u"label_op_sample")
        self.label_op_sample.setMinimumSize(QSize(20, 0))
        self.label_op_sample.setMaximumSize(QSize(16777215, 20))
        self.label_op_sample.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_op_sample.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_op_sample)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.comboBox_op_sample = QComboBox(self.page_OP)
        self.comboBox_op_sample.addItem("")
        self.comboBox_op_sample.addItem("")
        self.comboBox_op_sample.addItem("")
        self.comboBox_op_sample.addItem("")
        self.comboBox_op_sample.addItem("")
        self.comboBox_op_sample.addItem("")
        self.comboBox_op_sample.addItem("")
        self.comboBox_op_sample.addItem("")
        self.comboBox_op_sample.addItem("")
        self.comboBox_op_sample.addItem("")
        self.comboBox_op_sample.setObjectName(u"comboBox_op_sample")
        self.comboBox_op_sample.setMinimumSize(QSize(120, 40))
        self.comboBox_op_sample.setMaximumSize(QSize(100, 16777215))
        self.comboBox_op_sample.setFont(font4)
        self.comboBox_op_sample.setAutoFillBackground(False)
        self.comboBox_op_sample.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                              "border-radius: 5px;\n"
                                              "border: 2px solid rgb(33, 37, 43);\n"
                                              "padding: 5px;\n"
                                              "padding-left: 10px;\n"
                                              "font: 14pt \"Segoe UI\";")
        self.comboBox_op_sample.setIconSize(QSize(16, 16))
        self.comboBox_op_sample.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox_op_sample)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.page_OP)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)

        self.layout_op_data_open = QHBoxLayout()
        self.layout_op_data_open.setObjectName(u"layout_op_data_open")

        self.horizontalLayout_2.addLayout(self.layout_op_data_open)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_5 = QLabel(self.page_OP)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_15.addWidget(self.label_5)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_15)

        self.page_3_layout.addLayout(self.horizontalLayout_2)

        self.label_59 = QLabel(self.page_OP)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(16777215, 10))
        self.label_59.setStyleSheet(u"")
        self.label_59.setFrameShape(QFrame.HLine)
        self.label_59.setFrameShadow(QFrame.Plain)

        self.page_3_layout.addWidget(self.label_59)

        self.scroll_area_op = QScrollArea(self.page_OP)
        self.scroll_area_op.setObjectName(u"scroll_area_op")
        self.scroll_area_op.setStyleSheet(u"background: transparent;")
        self.scroll_area_op.setFrameShape(QFrame.NoFrame)
        self.scroll_area_op.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_op.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_op.setWidgetResizable(True)
        self.contents_op = QWidget()
        self.contents_op.setObjectName(u"contents_op")
        self.contents_op.setGeometry(QRect(0, 0, 1254, 910))
        self.contents_op.setLayoutDirection(Qt.LeftToRight)
        self.contents_op.setStyleSheet(u"background: transparent;")
        self.verticalLayout_2 = QVBoxLayout(self.contents_op)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(2)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.pic_op_data_1 = QLabel(self.contents_op)
        self.pic_op_data_1.setObjectName(u"pic_op_data_1")
        self.pic_op_data_1.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_op_data_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.pic_op_data_1)

        self.horizontalLayout_29.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.pic_op_data_2 = QLabel(self.contents_op)
        self.pic_op_data_2.setObjectName(u"pic_op_data_2")
        self.pic_op_data_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_op_data_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.pic_op_data_2)

        self.horizontalLayout_29.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.pic_op_data_3 = QLabel(self.contents_op)
        self.pic_op_data_3.setObjectName(u"pic_op_data_3")
        self.pic_op_data_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_op_data_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_73.addWidget(self.pic_op_data_3)

        self.horizontalLayout_29.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pic_op_data_4 = QLabel(self.contents_op)
        self.pic_op_data_4.setObjectName(u"pic_op_data_4")
        self.pic_op_data_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_op_data_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.pic_op_data_4)

        self.horizontalLayout_29.addLayout(self.horizontalLayout_31)

        self.verticalLayout_2.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(2)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.pic_op_data_5 = QLabel(self.contents_op)
        self.pic_op_data_5.setObjectName(u"pic_op_data_5")
        self.pic_op_data_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_op_data_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.pic_op_data_5)

        self.horizontalLayout_34.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.pic_op_data_6 = QLabel(self.contents_op)
        self.pic_op_data_6.setObjectName(u"pic_op_data_6")
        self.pic_op_data_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_op_data_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.pic_op_data_6)

        self.horizontalLayout_34.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.pic_op_data_7 = QLabel(self.contents_op)
        self.pic_op_data_7.setObjectName(u"pic_op_data_7")
        self.pic_op_data_7.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_op_data_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.pic_op_data_7)

        self.horizontalLayout_34.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.pic_op_data_8 = QLabel(self.contents_op)
        self.pic_op_data_8.setObjectName(u"pic_op_data_8")
        self.pic_op_data_8.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_op_data_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.pic_op_data_8)

        self.horizontalLayout_34.addLayout(self.horizontalLayout_37)

        self.verticalLayout_2.addLayout(self.horizontalLayout_34)

        self.label_6 = QLabel(self.contents_op)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 10))
        self.label_6.setStyleSheet(u"color: rgb(27, 30, 35);")
        self.label_6.setFrameShape(QFrame.HLine)
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setLineWidth(1)

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_op_base_model = QLabel(self.contents_op)
        self.label_op_base_model.setObjectName(u"label_op_base_model")
        self.label_op_base_model.setMaximumSize(QSize(170, 16777215))
        self.label_op_base_model.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_op_base_model.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_op_base_model)

        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_7 = QLabel(self.contents_op)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_22.addWidget(self.label_7)

        self.horizontalLayout_17.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_op_shot_base = QLabel(self.contents_op)
        self.label_op_shot_base.setObjectName(u"label_op_shot_base")
        self.label_op_shot_base.setMaximumSize(QSize(150, 16777215))
        self.label_op_shot_base.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_op_shot_base.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_op_shot_base)

        self.horizontalLayout_17.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.comboBox_op_shot_base = QComboBox(self.contents_op)
        self.comboBox_op_shot_base.addItem("")
        self.comboBox_op_shot_base.addItem("")
        self.comboBox_op_shot_base.addItem("")
        self.comboBox_op_shot_base.addItem("")
        self.comboBox_op_shot_base.addItem("")
        self.comboBox_op_shot_base.addItem("")
        self.comboBox_op_shot_base.addItem("")
        self.comboBox_op_shot_base.addItem("")
        self.comboBox_op_shot_base.addItem("")
        self.comboBox_op_shot_base.addItem("")
        self.comboBox_op_shot_base.setObjectName(u"comboBox_op_shot_base")
        self.comboBox_op_shot_base.setMinimumSize(QSize(0, 40))
        self.comboBox_op_shot_base.setMaximumSize(QSize(100, 16777215))
        self.comboBox_op_shot_base.setFont(font4)
        self.comboBox_op_shot_base.setAutoFillBackground(False)
        self.comboBox_op_shot_base.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                                 "border-radius: 5px;\n"
                                                 "border: 2px solid rgb(33, 37, 43);\n"
                                                 "padding: 5px;\n"
                                                 "padding-left: 10px;\n"
                                                 "font: 14pt \"Segoe UI\";")
        self.comboBox_op_shot_base.setIconSize(QSize(16, 16))
        self.comboBox_op_shot_base.setFrame(True)

        self.horizontalLayout_20.addWidget(self.comboBox_op_shot_base)

        self.horizontalLayout_17.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_10 = QLabel(self.contents_op)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_19.addWidget(self.label_10)

        self.horizontalLayout_17.addLayout(self.horizontalLayout_19)

        self.layout_op_test_base = QVBoxLayout()
        self.layout_op_test_base.setObjectName(u"layout_op_test_base")

        self.horizontalLayout_17.addLayout(self.layout_op_test_base)

        self.horizontalLayout_9.addLayout(self.horizontalLayout_17)

        self.label_9 = QLabel(self.contents_op)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(5, 16777215))
        self.label_9.setStyleSheet(u"color: rgb(27, 30, 35);")
        self.label_9.setFrameShape(QFrame.VLine)
        self.label_9.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_op_adv_model = QLabel(self.contents_op)
        self.label_op_adv_model.setObjectName(u"label_op_adv_model")
        self.label_op_adv_model.setMinimumSize(QSize(0, 0))
        self.label_op_adv_model.setMaximumSize(QSize(100, 16777215))
        self.label_op_adv_model.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_op_adv_model.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_op_adv_model)

        self.horizontalLayout_16.addLayout(self.verticalLayout_4)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_op_choice_method = QLabel(self.contents_op)
        self.label_op_choice_method.setObjectName(u"label_op_choice_method")
        self.label_op_choice_method.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_op_choice_method.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_op_choice_method)

        self.horizontalLayout_16.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.comboBox_op_method = QComboBox(self.contents_op)
        self.comboBox_op_method.addItem("")
        self.comboBox_op_method.addItem("")
        self.comboBox_op_method.addItem("")
        self.comboBox_op_method.setObjectName(u"comboBox_op_method")
        self.comboBox_op_method.setMinimumSize(QSize(130, 40))
        self.comboBox_op_method.setMaximumSize(QSize(100, 16777215))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.comboBox_op_method.setFont(font5)
        self.comboBox_op_method.setAutoFillBackground(False)
        self.comboBox_op_method.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                              "border-radius: 5px;\n"
                                              "border: 2px solid rgb(33, 37, 43);\n"
                                              "padding: 5px;\n"
                                              "padding-left: 10px;\n"
                                              "font: 12pt \"Segoe UI\";")
        self.comboBox_op_method.setIconSize(QSize(16, 16))
        self.comboBox_op_method.setFrame(True)

        self.horizontalLayout_26.addWidget(self.comboBox_op_method)

        self.horizontalLayout_16.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_op_shot_adv = QLabel(self.contents_op)
        self.label_op_shot_adv.setObjectName(u"label_op_shot_adv")
        self.label_op_shot_adv.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_op_shot_adv.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_op_shot_adv)

        self.horizontalLayout_16.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.comboBox_op_shot_adv = QComboBox(self.contents_op)

        for i in range(10):
            self.comboBox_op_shot_adv.addItem("")

        # self.comboBox_op_shot_adv.addItem("")
        # self.comboBox_op_shot_adv.addItem("")
        # self.comboBox_op_shot_adv.addItem("")
        # self.comboBox_op_shot_adv.addItem("")
        # self.comboBox_op_shot_adv.addItem("")
        # self.comboBox_op_shot_adv.addItem("")
        # self.comboBox_op_shot_adv.addItem("")
        # self.comboBox_op_shot_adv.addItem("")
        # self.comboBox_op_shot_adv.addItem("")
        # self.comboBox_op_shot_adv.addItem("")
        self.comboBox_op_shot_adv.setObjectName(u"comboBox_op_shot_adv")
        self.comboBox_op_shot_adv.setMinimumSize(QSize(0, 40))
        self.comboBox_op_shot_adv.setMaximumSize(QSize(100, 16777215))
        self.comboBox_op_shot_adv.setFont(font4)
        self.comboBox_op_shot_adv.setAutoFillBackground(False)
        self.comboBox_op_shot_adv.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                                "border-radius: 5px;\n"
                                                "border: 2px solid rgb(33, 37, 43);\n"
                                                "padding: 5px;\n"
                                                "padding-left: 10px;\n"
                                                "font: 14pt \"Segoe UI\";")
        self.comboBox_op_shot_adv.setIconSize(QSize(16, 16))
        self.comboBox_op_shot_adv.setFrame(True)

        self.horizontalLayout_24.addWidget(self.comboBox_op_shot_adv)

        self.horizontalLayout_16.addLayout(self.horizontalLayout_24)

        self.layout_op_test_adv = QHBoxLayout()
        self.layout_op_test_adv.setObjectName(u"layout_op_test_adv")

        self.horizontalLayout_16.addLayout(self.layout_op_test_adv)

        self.horizontalLayout_9.addLayout(self.horizontalLayout_16)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.layout_op_acc_base = QHBoxLayout()
        self.layout_op_acc_base.setObjectName(u"layout_op_acc_base")

        self.horizontalLayout_30.addLayout(self.layout_op_acc_base)

        self.label_8 = QLabel(self.contents_op)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(5, 16777215))
        self.label_8.setStyleSheet(u"color: rgb(27, 30, 35);")
        self.label_8.setFrameShape(QFrame.VLine)
        self.label_8.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_30.addWidget(self.label_8)

        self.layout_op_acc_adv = QHBoxLayout()
        self.layout_op_acc_adv.setObjectName(u"layout_op_acc_adv")

        self.horizontalLayout_30.addLayout(self.layout_op_acc_adv)

        self.verticalLayout_2.addLayout(self.horizontalLayout_30)

        self.layout_op_imageShow = QWidget(self.contents_op)
        self.layout_op_imageShow.setObjectName(u"layout_op_imageShow")
        self.horizontalLayout = QHBoxLayout(self.layout_op_imageShow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout_op_imageShow_1 = QHBoxLayout()
        self.layout_op_imageShow_1.setObjectName(u"layout_op_imageShow_1")
        self.pic_op_matrix1 = QLabel(self.layout_op_imageShow)
        self.pic_op_matrix1.setObjectName(u"pic_op_matrix1")
        self.pic_op_matrix1.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_op_matrix1.setAlignment(Qt.AlignCenter)

        self.layout_op_imageShow_1.addWidget(self.pic_op_matrix1)

        self.horizontalLayout.addLayout(self.layout_op_imageShow_1)

        self.layout_op_imageShow_2 = QHBoxLayout()
        self.layout_op_imageShow_2.setObjectName(u"layout_op_imageShow_2")
        self.pic_op_matrix2 = QLabel(self.layout_op_imageShow)
        self.pic_op_matrix2.setObjectName(u"pic_op_matrix2")
        self.pic_op_matrix2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_op_matrix2.setAlignment(Qt.AlignCenter)

        self.layout_op_imageShow_2.addWidget(self.pic_op_matrix2)

        self.horizontalLayout.addLayout(self.layout_op_imageShow_2)

        self.verticalLayout_2.addWidget(self.layout_op_imageShow)

        self.scroll_area_op.setWidget(self.contents_op)

        self.page_3_layout.addWidget(self.scroll_area_op)

        self.pages.addWidget(self.page_OP)

    # 数据选择下拉框
    def setup_row_1_layout(self):
        page_IL_row_1_layout = QHBoxLayout()
        page_IL_row_1_layout.setObjectName(u"page_IL_row_1_layout")

        # 定义四组下拉框layout
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()
        layout_3 = QHBoxLayout()
        layout_4 = QHBoxLayout()
        layout_5 = QHBoxLayout()

        # 第一组下拉框
        self.label_IL_data = QLabel(self.page_IL)
        self.label_IL_data.setText("Choose Dataset")
        self.label_IL_data.setObjectName(u"label_IL_data")
        self.label_IL_data.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_IL_data = QComboBox(self.page_IL)
        for i in range(1):
            self.comboBox_IL_data.addItem("")
        self.comboBox_IL_data.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data.setMinimumSize(QSize(150, 40))
        self.comboBox_IL_data.setMaximumSize(QSize(200, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data.setFont(font_comboBox)
        self.comboBox_IL_data.setAutoFillBackground(False)
        self.comboBox_IL_data.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                            "border-radius: 5px;\n"
                                            "border: 2px solid rgb(33, 37, 43);\n"
                                            "padding: 5px;\n"
                                            "padding-left: 10px;\n"
                                            "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data.setIconSize(QSize(16, 16))
        self.comboBox_IL_data.setFrame(True)

        # 第二组下拉框
        self.label_IL_data1 = QLabel(self.page_IL)
        self.label_IL_data1.setText("Choose Dataset")
        self.label_IL_data1.setObjectName(u"label_IL_data")
        self.label_IL_data1.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data1.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data1.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_IL_data1 = QComboBox(self.page_IL)
        for i in range(1):
            self.comboBox_IL_data1.addItem("")
        self.comboBox_IL_data1.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data1.setMinimumSize(QSize(100, 40))
        self.comboBox_IL_data1.setMaximumSize(QSize(200, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data1.setFont(font_comboBox)
        self.comboBox_IL_data1.setAutoFillBackground(False)
        self.comboBox_IL_data1.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                             "border-radius: 5px;\n"
                                             "border: 2px solid rgb(33, 37, 43);\n"
                                             "padding: 5px;\n"
                                             "padding-left: 10px;\n"
                                             "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data1.setIconSize(QSize(16, 16))
        self.comboBox_IL_data1.setFrame(True)

        # 第三组下拉框
        self.label_IL_data2 = QLabel(self.page_IL)
        self.label_IL_data2.setText("Choose Dataset")
        self.label_IL_data2.setObjectName(u"label_IL_data")
        self.label_IL_data2.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data2.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_IL_data2 = QComboBox(self.page_IL)
        for i in range(5):
            self.comboBox_IL_data2.addItem("")
        self.comboBox_IL_data2.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data2.setMinimumSize(QSize(100, 40))
        self.comboBox_IL_data2.setMaximumSize(QSize(200, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data2.setFont(font_comboBox)
        self.comboBox_IL_data2.setAutoFillBackground(False)
        self.comboBox_IL_data2.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                             "border-radius: 5px;\n"
                                             "border: 2px solid rgb(33, 37, 43);\n"
                                             "padding: 5px;\n"
                                             "padding-left: 10px;\n"
                                             "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data2.setIconSize(QSize(16, 16))
        self.comboBox_IL_data2.setFrame(True)

        # 第四组下拉框
        self.label_IL_data3 = QLabel(self.page_IL)
        self.label_IL_data3.setText("Choose Dataset")
        self.label_IL_data3.setObjectName(u"label_IL_data")
        self.label_IL_data3.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data3.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_IL_data3 = QComboBox(self.page_IL)
        for i in range(4):
            self.comboBox_IL_data3.addItem("")
        self.comboBox_IL_data3.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data3.setMinimumSize(QSize(100, 40))
        self.comboBox_IL_data3.setMaximumSize(QSize(200, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data3.setFont(font_comboBox)
        self.comboBox_IL_data3.setAutoFillBackground(False)
        self.comboBox_IL_data3.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                             "border-radius: 5px;\n"
                                             "border: 2px solid rgb(33, 37, 43);\n"
                                             "padding: 5px;\n"
                                             "padding-left: 10px;\n"
                                             "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data3.setIconSize(QSize(16, 16))
        self.comboBox_IL_data3.setFrame(True)

        # 第五组下拉框
        # self.label_IL_data4 = QLabel(self.page_IL)
        # self.label_IL_data4.setText("Choose Dataset")
        # self.label_IL_data4.setObjectName(u"label_IL_data")
        # self.label_IL_data4.setMaximumSize(QSize(16777215, 20))
        # self.label_IL_data4.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.label_IL_data4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        #
        # self.comboBox_IL_data4 = QComboBox(self.page_IL)
        # for i in range(5, 11, 1):
        #     self.comboBox_IL_data4.addItem("")
        # self.comboBox_IL_data4.setObjectName(u"comboBox_op_data")
        # self.comboBox_IL_data4.setMinimumSize(QSize(100, 40))
        # self.comboBox_IL_data4.setMaximumSize(QSize(200, 16777215))
        # font_comboBox = QFont()
        # font_comboBox.setPointSize(14)
        # font_comboBox.setBold(False)
        # font_comboBox.setItalic(False)
        # self.comboBox_IL_data4.setFont(font_comboBox)
        # self.comboBox_IL_data4.setAutoFillBackground(False)
        # self.comboBox_IL_data4.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
        #                                      "border-radius: 5px;\n"
        #                                      "border: 2px solid rgb(33, 37, 43);\n"
        #                                      "padding: 5px;\n"
        #                                      "padding-left: 10px;\n"
        #                                      "font: 14pt \"Segoe UI\";")
        # self.comboBox_IL_data4.setIconSize(QSize(16, 16))
        # self.comboBox_IL_data4.setFrame(True)

        hspace0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # hspace1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # hspace2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # hspace3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # hspace4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hspace5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        layout_1.addWidget(self.label_IL_data)
        layout_1.addWidget(self.comboBox_IL_data)
        # layout_1.addItem(hspace1)
        layout_2.addWidget(self.label_IL_data1)
        layout_2.addWidget(self.comboBox_IL_data1)
        # layout_1.addItem(hspace2)
        layout_3.addWidget(self.label_IL_data2)
        layout_3.addWidget(self.comboBox_IL_data2)
        # layout_1.addItem(hspace3)
        layout_4.addWidget(self.label_IL_data3)
        layout_4.addWidget(self.comboBox_IL_data3)
        # layout_1.addItem(hspace4)
        # layout_5.addWidget(self.label_IL_data4)
        # layout_5.addWidget(self.comboBox_IL_data4)

        self.page_IL_layout_loadData = QHBoxLayout()
        self.page_IL_layout_loadData.setObjectName(u"page_IL_layout_loadData")
        # self.page_IL_layout_train.addItem(hspace5)

        page_IL_row_1_layout.addItem(hspace0)
        page_IL_row_1_layout.addLayout(layout_1)
        page_IL_row_1_layout.addLayout(layout_2)
        page_IL_row_1_layout.addLayout(layout_3)
        page_IL_row_1_layout.addLayout(layout_4)
        # page_IL_row_1_layout.addLayout(layout_5)
        page_IL_row_1_layout.addLayout(self.page_IL_layout_loadData)
        page_IL_row_1_layout.addItem(hspace5)

        # page_IL_row_1_layout.setStretchFactor(layout_1, 1)
        # page_IL_row_1_layout.setStretchFactor(layout_2, 2)
        # page_IL_row_1_layout.setStretchFactor(layout_3, 2)
        # page_IL_row_1_layout.setStretchFactor(layout_4, 2)
        # page_IL_row_1_layout.setStretchFactor(self.page_IL_layout_train, 3)

        return page_IL_row_1_layout

    # 数据集展示
    def setup_row_2_layout(self):
        # layout = QVBoxLayout()
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        # sizePolicy1.setHeightForWidth(self.page_OP.sizePolicy().hasHeightForWidth())
        # self.page_OP.setSizePolicy(sizePolicy1)
        widget = QWidget()
        # widget.setMaximumSize(QSize(2000, 600))
        widget.setMinimumSize(QSize(800, 400))
        widget.setSizePolicy(sizePolicy1)
        layout = QVBoxLayout(widget)
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        layout.addLayout(h_layout1)
        layout.addLayout(h_layout2)

        self.pic_IL_data_1 = QLabel(self.page_IL_contents)
        self.pic_IL_data_1.setObjectName(u"pic_op_data_1")
        self.pic_IL_data_1.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_IL_data_1.setAlignment(Qt.AlignCenter)

        h_layout1.addWidget(self.pic_IL_data_1)

        self.pic_IL_data_2 = QLabel(self.page_IL_contents)
        self.pic_IL_data_2.setObjectName(u"pic_op_data_1")
        self.pic_IL_data_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_IL_data_2.setAlignment(Qt.AlignCenter)
        h_layout1.addWidget(self.pic_IL_data_2)

        self.pic_IL_data_3 = QLabel(self.page_IL_contents)
        self.pic_IL_data_3.setObjectName(u"pic_op_data_1")
        self.pic_IL_data_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_IL_data_3.setAlignment(Qt.AlignCenter)
        h_layout1.addWidget(self.pic_IL_data_3)

        self.pic_IL_data_4 = QLabel(self.page_IL_contents)
        self.pic_IL_data_4.setObjectName(u"pic_op_data_1")
        self.pic_IL_data_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_IL_data_4.setAlignment(Qt.AlignCenter)
        h_layout1.addWidget(self.pic_IL_data_4)

        self.pic_IL_data_5 = QLabel(self.page_IL_contents)
        self.pic_IL_data_5.setObjectName(u"pic_op_data_1")
        self.pic_IL_data_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_IL_data_5.setAlignment(Qt.AlignCenter)
        h_layout2.addWidget(self.pic_IL_data_5)

        self.pic_IL_data_6 = QLabel(self.page_IL_contents)
        self.pic_IL_data_6.setObjectName(u"pic_op_data_1")
        self.pic_IL_data_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_IL_data_6.setAlignment(Qt.AlignCenter)
        h_layout2.addWidget(self.pic_IL_data_6)

        self.pic_IL_data_7 = QLabel(self.page_IL_contents)
        self.pic_IL_data_7.setObjectName(u"pic_op_data_1")
        self.pic_IL_data_7.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_IL_data_7.setAlignment(Qt.AlignCenter)
        h_layout2.addWidget(self.pic_IL_data_7)

        self.pic_IL_data_8 = QLabel(self.page_IL_contents)
        self.pic_IL_data_8.setObjectName(u"pic_op_data_1")
        self.pic_IL_data_8.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_IL_data_8.setAlignment(Qt.AlignCenter)
        h_layout2.addWidget(self.pic_IL_data_8)

        # self.pic_IL_data_1.setMaximumSize(QSize(400, 300))
        self.pic_IL_data_1.setMinimumSize(QSize(200, 150))
        # self.pic_IL_data_2.setMaximumSize(QSize(400, 300))
        self.pic_IL_data_2.setMinimumSize(QSize(200, 150))
        # self.pic_IL_data_3.setMaximumSize(QSize(400, 300))
        self.pic_IL_data_3.setMinimumSize(QSize(200, 150))
        # self.pic_IL_data_4.setMaximumSize(QSize(400, 300))
        self.pic_IL_data_4.setMinimumSize(QSize(200, 150))
        # self.pic_IL_data_5.setMaximumSize(QSize(400, 300))
        self.pic_IL_data_5.setMinimumSize(QSize(200, 150))
        # self.pic_IL_data_6.setMaximumSize(QSize(400, 300))
        self.pic_IL_data_6.setMinimumSize(QSize(200, 150))
        # self.pic_IL_data_7.setMaximumSize(QSize(400, 300))
        self.pic_IL_data_7.setMinimumSize(QSize(200, 150))
        # self.pic_IL_data_8.setMaximumSize(QSize(400, 300))
        self.pic_IL_data_8.setMinimumSize(QSize(200, 150))

        self.pic_IL_data_1.setScaledContents(True)
        self.pic_IL_data_2.setScaledContents(True)
        self.pic_IL_data_3.setScaledContents(True)
        self.pic_IL_data_4.setScaledContents(True)
        self.pic_IL_data_5.setScaledContents(True)
        self.pic_IL_data_6.setScaledContents(True)
        self.pic_IL_data_7.setScaledContents(True)
        self.pic_IL_data_8.setScaledContents(True)

        return widget

    def setup_row_3_left_layout(self):
        layout = QVBoxLayout()
        page_IL_row_3_layout = QHBoxLayout()
        page_IL_row_3_layout.setContentsMargins(0, 0, 0, 0)
        page_IL_row_3_layout.setObjectName(u"page_IL_row_3_layout")

        # 定义四组下拉框layout
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()
        layout_3 = QHBoxLayout()
        layout_4 = QHBoxLayout()
        layout_5 = QHBoxLayout()

        # 第一组下拉框
        self.label_IL_data5 = QLabel(self.page_IL)
        self.label_IL_data5.setText("Choose Dataset")
        self.label_IL_data5.setObjectName(u"label_IL_data")
        self.label_IL_data5.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data5.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_IL_data5 = QComboBox(self.page_IL)
        for i in range(7):
            self.comboBox_IL_data5.addItem("")
        self.comboBox_IL_data5.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data5.setMinimumSize(QSize(100, 40))
        self.comboBox_IL_data5.setMaximumSize(QSize(200, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data5.setFont(font_comboBox)
        self.comboBox_IL_data5.setAutoFillBackground(False)
        self.comboBox_IL_data5.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                            "border-radius: 5px;\n"
                                            "border: 2px solid rgb(33, 37, 43);\n"
                                            "padding: 5px;\n"
                                            "padding-left: 10px;\n"
                                            "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data5.setIconSize(QSize(16, 16))
        self.comboBox_IL_data5.setFrame(True)


        # 第二组下拉框
        self.label_IL_data6 = QLabel(self.page_IL)
        self.label_IL_data6.setText("Choose Dataset")
        self.label_IL_data6.setObjectName(u"label_IL_data")
        self.label_IL_data6.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data6.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data6.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_IL_data6 = QComboBox(self.page_IL)
        for i in range(6):
            self.comboBox_IL_data6.addItem("")
        self.comboBox_IL_data6.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data6.setMinimumSize(QSize(100, 40))
        self.comboBox_IL_data6.setMaximumSize(QSize(200, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data6.setFont(font_comboBox)
        self.comboBox_IL_data6.setAutoFillBackground(False)
        self.comboBox_IL_data6.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                             "border-radius: 5px;\n"
                                             "border: 2px solid rgb(33, 37, 43);\n"
                                             "padding: 5px;\n"
                                             "padding-left: 10px;\n"
                                             "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data6.setIconSize(QSize(16, 16))
        self.comboBox_IL_data6.setFrame(True)

        hspace0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hspace5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        layout_1.addWidget(self.label_IL_data5)
        layout_1.addWidget(self.comboBox_IL_data5)
        layout_2.addWidget(self.label_IL_data6)
        layout_2.addWidget(self.comboBox_IL_data6)

        self.page_IL_layout_pretrain = QHBoxLayout()
        self.page_IL_layout_pretrain.setObjectName(u"page_IL_layout_pretrain")

        # page_IL_row_3_layout.addItem(hspace0)
        page_IL_row_3_layout.addLayout(layout_1)
        page_IL_row_3_layout.addLayout(layout_2)
        page_IL_row_3_layout.addLayout(self.page_IL_layout_pretrain)
        page_IL_row_3_layout.addItem(hspace5)

        # acc显示
        page_IL_row_4_left_layout = QHBoxLayout()
        page_IL_row_4_left_layout.setObjectName(u"page_IL_row_3_layout")
        page_IL_row_4_left_layout.setContentsMargins(0, 0, 0, 0)
        # acc_widget = QWidget()
        # acc_widget.setMinimumSize(QSize(300, 300))
        # page_IL_row_4_left_layout.addWidget(acc_widget)

        self.pretrain_acc_layout = QHBoxLayout()
        page_IL_row_4_left_layout.addLayout(self.pretrain_acc_layout)

        # 增量下拉框和显示
        page_IL_row_4_layout = QHBoxLayout()
        page_IL_row_4_layout.setContentsMargins(0, 0, 0, 0)
        page_IL_row_4_layout.setObjectName(u"page_IL_row_3_layout")

        # 定义四组下拉框layout
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()

        # 第一组下拉框
        self.label_IL_data8 = QLabel(self.page_IL)
        self.label_IL_data8.setText("Choose Dataset")
        self.label_IL_data8.setObjectName(u"label_IL_data")
        self.label_IL_data8.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data8.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data8.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        # 第二组下拉框
        self.label_IL_data9 = QLabel(self.page_IL)
        self.label_IL_data9.setText("Choose Dataset")
        self.label_IL_data9.setObjectName(u"label_IL_data")
        self.label_IL_data9.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data9.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data9.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_IL_data9 = QComboBox(self.page_IL)
        for i in range(3):
            self.comboBox_IL_data9.addItem("")
        self.comboBox_IL_data9.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data9.setMinimumSize(QSize(100, 40))
        self.comboBox_IL_data9.setMaximumSize(QSize(200, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data9.setFont(font_comboBox)
        self.comboBox_IL_data9.setAutoFillBackground(False)
        self.comboBox_IL_data9.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                             "border-radius: 5px;\n"
                                             "border: 2px solid rgb(33, 37, 43);\n"
                                             "padding: 5px;\n"
                                             "padding-left: 10px;\n"
                                             "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data9.setIconSize(QSize(16, 16))
        self.comboBox_IL_data9.setFrame(True)

        hspace0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hspace5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        layout_1.addWidget(self.label_IL_data8)
        # layout_1.addWidget(self.comboBox_IL_data8)
        layout_2.addWidget(self.label_IL_data9)
        layout_2.addWidget(self.comboBox_IL_data9)

        self.page_IL_layout_increment_train = QHBoxLayout()
        self.page_IL_layout_increment_train.setObjectName(u"page_IL_layout_increment_train")

        self.page_IL_layout_new_class = QHBoxLayout()
        self.page_IL_layout_new_class.setObjectName(u"page_IL_layout_new_class")

        # page_IL_row_4_layout.addItem(hspace0)
        page_IL_row_4_layout.addLayout(layout_1)
        page_IL_row_4_layout.addLayout(self.page_IL_layout_new_class)
        page_IL_row_4_layout.addLayout(layout_2)
        page_IL_row_4_layout.addLayout(self.page_IL_layout_increment_train)
        page_IL_row_4_layout.addItem(hspace5)

        # increment acc显示
        page_IL_row_4_right_layout = QHBoxLayout()
        page_IL_row_4_right_layout.setObjectName(u"page_IL_row_3_layout")
        page_IL_row_4_right_layout.setContentsMargins(0, 0, 0, 0)
        # acc_widget = QWidget()
        # acc_widget.setMinimumSize(QSize(300, 300))
        # page_IL_row_4_right_layout.addWidget(acc_widget)
        self.increment_train_acc_layout = QHBoxLayout()
        page_IL_row_4_right_layout.addLayout(self.increment_train_acc_layout)

        layout.addLayout(page_IL_row_3_layout)
        layout.addLayout(page_IL_row_4_left_layout)
        layout.addLayout(page_IL_row_4_layout)
        layout.addLayout(page_IL_row_4_right_layout)

        return layout

    def setup_row_3_right_layout(self):
        page_IL_row_3_layout = QHBoxLayout()
        page_IL_row_3_layout.setContentsMargins(0, 0, 0, 0)
        page_IL_row_3_layout.setObjectName(u"page_IL_row_3_layout")

        # 定义四组下拉框layout
        # layout_1 = QHBoxLayout()
        # layout_2 = QHBoxLayout()
        #
        # # 第一组下拉框
        # self.label_IL_data8 = QLabel(self.page_IL)
        # self.label_IL_data8.setText("Choose Dataset")
        # self.label_IL_data8.setObjectName(u"label_IL_data")
        # self.label_IL_data8.setMaximumSize(QSize(16777215, 20))
        # self.label_IL_data8.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.label_IL_data8.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        #
        # # 第二组下拉框
        # self.label_IL_data9 = QLabel(self.page_IL)
        # self.label_IL_data9.setText("Choose Dataset")
        # self.label_IL_data9.setObjectName(u"label_IL_data")
        # self.label_IL_data9.setMaximumSize(QSize(16777215, 20))
        # self.label_IL_data9.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.label_IL_data9.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        #
        # self.comboBox_IL_data9 = QComboBox(self.page_IL)
        # for i in range(3):
        #     self.comboBox_IL_data9.addItem("")
        # self.comboBox_IL_data9.setObjectName(u"comboBox_op_data")
        # self.comboBox_IL_data9.setMinimumSize(QSize(100, 40))
        # self.comboBox_IL_data9.setMaximumSize(QSize(200, 16777215))
        # font_comboBox = QFont()
        # font_comboBox.setPointSize(14)
        # font_comboBox.setBold(False)
        # font_comboBox.setItalic(False)
        # self.comboBox_IL_data9.setFont(font_comboBox)
        # self.comboBox_IL_data9.setAutoFillBackground(False)
        # self.comboBox_IL_data9.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
        #                                      "border-radius: 5px;\n"
        #                                      "border: 2px solid rgb(33, 37, 43);\n"
        #                                      "padding: 5px;\n"
        #                                      "padding-left: 10px;\n"
        #                                      "font: 14pt \"Segoe UI\";")
        # self.comboBox_IL_data9.setIconSize(QSize(16, 16))
        # self.comboBox_IL_data9.setFrame(True)
        #
        # hspace0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # hspace5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        #
        # layout_1.addWidget(self.label_IL_data8)
        # # layout_1.addWidget(self.comboBox_IL_data8)
        # layout_2.addWidget(self.label_IL_data9)
        # layout_2.addWidget(self.comboBox_IL_data9)
        #
        # self.page_IL_layout_increment_train = QHBoxLayout()
        # self.page_IL_layout_increment_train.setObjectName(u"page_IL_layout_increment_train")
        #
        # self.page_IL_layout_new_class = QHBoxLayout()
        # self.page_IL_layout_new_class.setObjectName(u"page_IL_layout_new_class")
        #
        # page_IL_row_3_layout.addItem(hspace0)
        # page_IL_row_3_layout.addLayout(layout_1)
        # page_IL_row_3_layout.addLayout(self.page_IL_layout_new_class)
        # page_IL_row_3_layout.addLayout(layout_2)
        # page_IL_row_3_layout.addLayout(self.page_IL_layout_increment_train)
        # page_IL_row_3_layout.addItem(hspace5)

        return page_IL_row_3_layout

    def setup_row_4_left_layout(self):
        page_IL_row_4_left_layout = QHBoxLayout()
        page_IL_row_4_left_layout.setObjectName(u"page_IL_row_3_layout")
        page_IL_row_4_left_layout.setContentsMargins(0, 0, 0, 0)
        # acc_widget = QWidget()
        # acc_widget.setMinimumSize(QSize(300, 300))
        # page_IL_row_4_left_layout.addWidget(acc_widget)

        self.pretrain_acc_layout = QHBoxLayout()
        page_IL_row_4_left_layout.addLayout(self.pretrain_acc_layout)

        return page_IL_row_4_left_layout

    def setup_row_4_right_layout(self):
        page_IL_row_4_right_layout = QHBoxLayout()
        page_IL_row_4_right_layout.setObjectName(u"page_IL_row_3_layout")
        page_IL_row_4_right_layout.setContentsMargins(0, 0, 0, 0)
        # acc_widget = QWidget()
        # acc_widget.setMinimumSize(QSize(300, 300))
        # page_IL_row_4_right_layout.addWidget(acc_widget)
        self.increment_train_acc_layout = QHBoxLayout()
        page_IL_row_4_right_layout.addLayout(self.increment_train_acc_layout)

        return page_IL_row_4_right_layout

    def setup_row_5_layout(self):
        page_IL_row_5_layout = QHBoxLayout()
        page_IL_row_5_layout.setContentsMargins(0, 0, 0, 0)
        page_IL_row_5_layout.setObjectName(u"page_IL_row_5_layout")

        hspace0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hspace5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.page_IL_layout_test = QHBoxLayout()
        self.page_IL_layout_test.setObjectName(u"page_IL_layout_test")

        # page_IL_row_5_layout.addItem(hspace0)
        page_IL_row_5_layout.addLayout(self.page_IL_layout_test)
        page_IL_row_5_layout.addItem(hspace5)

        return page_IL_row_5_layout

    def setup_row_6_layout(self):
        page_IL_row_6_layout = QHBoxLayout()
        page_IL_row_6_layout.setContentsMargins(0, 0, 0, 0)
        page_IL_row_6_layout.setObjectName(u"page_IL_row_6_layout")

        row_6_left_layout = QHBoxLayout()
        row_6_right_layout = QVBoxLayout()
        hspace0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hspace1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        page_IL_row_6_layout.addItem(hspace0)
        page_IL_row_6_layout.addLayout(row_6_left_layout)
        page_IL_row_6_layout.addLayout(row_6_right_layout)
        page_IL_row_6_layout.addItem(hspace1)
        # page_IL_row_6_layout.setStretchFactor(row_6_left_layout, 1)
        # page_IL_row_6_layout.setStretchFactor(row_6_right_layout, 1)

        self.row_6_1_layout = QHBoxLayout()
        self.row_6_2_layout = QHBoxLayout()
        self.row_6_3_layout = QHBoxLayout()

        self.label_old_oa = QLabel(self.page_IL)
        self.label_old_oa.setObjectName(u"label_old_oa")
        self.label_old_oa.setMaximumSize(QSize(16777215, 20))
        self.label_old_oa.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_old_oa.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.label_new_oa = QLabel(self.page_IL)
        self.label_new_oa.setObjectName(u"label_new_oa")
        self.label_new_oa.setMaximumSize(QSize(16777215, 20))
        self.label_new_oa.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_new_oa.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.label_all_oa = QLabel(self.page_IL)
        self.label_all_oa.setObjectName(u"label_all_oa")
        self.label_all_oa.setMaximumSize(QSize(16777215, 20))
        self.label_all_oa.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_all_oa.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.row_6_1_layout.addWidget(self.label_old_oa)
        self.row_6_2_layout.addWidget(self.label_new_oa)
        self.row_6_3_layout.addWidget(self.label_all_oa)

        row_6_right_layout.addLayout(self.row_6_1_layout)
        row_6_right_layout.addLayout(self.row_6_2_layout)
        row_6_right_layout.addLayout(self.row_6_3_layout)

        self.matrix_label = QLabel()
        row_6_left_layout.addWidget(self.matrix_label)
        self.matrix_label.setMaximumSize(QSize(800, 800))
        self.matrix_label.setMinimumSize(QSize(500, 500))

        return page_IL_row_6_layout

    def setup_row_6_layout_(self):
        page_IL_row_6_layout = QVBoxLayout()
        page_IL_row_6_layout.setContentsMargins(0, 0, 0, 0)
        page_IL_row_6_layout.setObjectName(u"page_IL_row_6_layout")

        row_6_layout_1 = QHBoxLayout()
        row_6_layout_2 = QHBoxLayout()
        row_6_layout_3 = QHBoxLayout()
        row_6_layout_4 = QHBoxLayout()

        page_IL_row_6_layout.addLayout(row_6_layout_1)
        page_IL_row_6_layout.addLayout(row_6_layout_2)
        page_IL_row_6_layout.addLayout(row_6_layout_3)
        page_IL_row_6_layout.addLayout(row_6_layout_4)

        hspace0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hspace1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.page_IL_layout_test = QHBoxLayout()
        self.page_IL_layout_test.setObjectName(u"page_IL_layout_test")

        # page_IL_row_5_layout.addItem(hspace0)
        row_6_layout_1.addLayout(self.page_IL_layout_test)
        row_6_layout_1.addItem(hspace0)

        self.row_6_1_layout = QHBoxLayout()
        self.row_6_2_layout = QHBoxLayout()
        self.row_6_3_layout = QHBoxLayout()

        row_6_layout_3.addLayout(self.row_6_1_layout)
        row_6_layout_3.addLayout(self.row_6_2_layout)
        row_6_layout_3.addLayout(self.row_6_3_layout)

        self.label_old_oa = QLabel(self.page_IL)
        self.label_old_oa.setObjectName(u"label_old_oa")
        self.label_old_oa.setMaximumSize(QSize(16777215, 20))
        self.label_old_oa.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_old_oa.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.label_new_oa = QLabel(self.page_IL)
        self.label_new_oa.setObjectName(u"label_new_oa")
        self.label_new_oa.setMaximumSize(QSize(16777215, 20))
        self.label_new_oa.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_new_oa.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.label_all_oa = QLabel(self.page_IL)
        self.label_all_oa.setObjectName(u"label_all_oa")
        self.label_all_oa.setMaximumSize(QSize(16777215, 20))
        self.label_all_oa.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_all_oa.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        row_6_layout_2.addWidget(self.label_old_oa)
        row_6_layout_2.addWidget(self.label_new_oa)
        row_6_layout_2.addWidget(self.label_all_oa)

        self.matrix_label = QLabel()
        row_6_layout_4.addWidget(self.matrix_label)
        self.matrix_label.setMaximumSize(QSize(800, 800))
        self.matrix_label.setMinimumSize(QSize(500, 500))

        return page_IL_row_6_layout

    def setup_row_title(self):
        title_layout = QHBoxLayout()
        hspace0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hspace1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.page_IL_title_label = QLabel(self.page_IL)
        self.page_IL_title_label.setObjectName(u"title_label")
        self.page_IL_title_label.setMaximumSize(QSize(16777215, 40))
        title_layout.setContentsMargins(0, 0, 0, 25)
        font_IL = QFont()
        font_IL.setPointSize(24)
        font_IL.setBold(True)
        font_IL.setItalic(False)
        self.page_IL_title_label.setFont(font_IL)
        self.page_IL_title_label.setStyleSheet(u"font: 24pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.page_IL_title_label.setAlignment(Qt.AlignHCenter)
        title_layout.addItem(hspace0)
        title_layout.addWidget(self.page_IL_title_label)
        title_layout.addItem(hspace1)

        return title_layout

    def setup_page_IL_1(self):
        self.page_IL = QWidget()
        self.page_IL.setObjectName(u"page_IL")

        # sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # sizePolicy1.setHorizontalStretch(0)
        # sizePolicy1.setVerticalStretch(0)
        # sizePolicy1.setHeightForWidth(self.page_IL.sizePolicy().hasHeightForWidth())
        # self.page_IL.setSizePolicy(sizePolicy1)

        # 首先定义了page2的整体布局为垂直布局
        self.page_IL_layout = QVBoxLayout(self.page_IL)
        # self.page_IL_layout.setSpacing(5)
        self.page_IL_layout.setObjectName(u"page_2_layout")
        self.page_IL_layout.setContentsMargins(5, 5, 5, 5)
        # page2中的滚动区域是。。。
        self.page_IL_scroll_area = QScrollArea(self.page_IL)
        self.page_IL_scroll_area.setObjectName(u"scroll_area")
        self.page_IL_scroll_area.setStyleSheet(u"background: transparent;")
        self.page_IL_scroll_area.setFrameShape(QFrame.NoFrame)
        self.page_IL_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.page_IL_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.page_IL_scroll_area.setWidgetResizable(True)
        # 这里的content是。。。
        self.page_IL_contents = QWidget()
        self.page_IL_contents.setObjectName(u"contents")
        self.page_IL_contents.setGeometry(QRect(0, 0, 840, 580))
        self.page_IL_contents.setStyleSheet(u"background: transparent;")
        # 设置该页面总体的layout
        self.page_IL_verticalLayout = QVBoxLayout(self.page_IL_contents)
        self.page_IL_verticalLayout.setSpacing(15)
        self.page_IL_verticalLayout.setObjectName(u"verticalLayout")
        self.page_IL_verticalLayout.setContentsMargins(5, 5, 5, 5)

        # 设置title的layout
        title_layout = self.setup_row_title()
        self.page_IL_verticalLayout.addLayout(title_layout)

        # 设置description的layout
        description_layout = self.setup_row_description()
        self.page_IL_verticalLayout.addLayout(description_layout)

        # self.page_IL_row_1_layout = QHBoxLayout()
        # self.page_IL_row_1_layout.setObjectName(u"page_IL_row_1_layout")

        # 设置第一行下拉框的layout
        self.page_IL_row_1_layout = self.setup_row_1_layout()
        self.page_IL_verticalLayout.addLayout(self.page_IL_row_1_layout)

        # # 水平布局
        # self.row_1_layout = QHBoxLayout()
        # self.row_1_layout.setObjectName(u"row_1_layout")
        #
        # # 垂直布局中添加水平布局
        # self.page_IL_verticalLayout.addLayout(self.row_1_layout)
        #
        # # 水平布局
        # self.row_2_layout = QHBoxLayout()
        # self.row_2_layout.setObjectName(u"row_2_layout")
        #
        # self.page_IL_verticalLayout.addLayout(self.row_2_layout)
        # # 水平布局
        # self.row_3_layout = QHBoxLayout()
        # self.row_3_layout.setObjectName(u"row_3_layout")
        #
        # self.page_IL_verticalLayout.addLayout(self.row_3_layout)
        # # 垂直布局
        # self.row_4_layout = QVBoxLayout()
        # self.row_4_layout.setObjectName(u"row_4_layout")
        #
        # self.page_IL_verticalLayout.addLayout(self.row_4_layout)
        # # 垂直布局
        # self.row_5_layout = QVBoxLayout()
        # self.row_5_layout.setObjectName(u"row_5_layout")
        #
        # self.page_IL_verticalLayout.addLayout(self.row_5_layout)

        # 这里是滚动区域中添加了内容
        self.page_IL_scroll_area.setWidget(self.page_IL_contents)

        self.page_IL_layout.addWidget(self.page_IL_scroll_area)

        self.pages.addWidget(self.page_IL)

    def setup_page_IL_2(self):
        self.page_IL = QWidget()
        self.page_IL.setObjectName(u"page_IL")

        # 首先定义了page2的整体布局为垂直布局
        self.page_IL_layout = QVBoxLayout(self.page_IL)
        self.page_IL_layout.setSpacing(0)
        self.page_IL_layout.setObjectName(u"page_2_layout")
        self.page_IL_layout.setContentsMargins(5, 5, 5, 5)

        self.page_IL_title_layout = self.setup_row_title()
        self.page_IL_layout.addLayout(self.page_IL_title_layout)

        # page2中的滚动区域是。。。
        self.page_IL_scroll_area = QScrollArea(self.page_IL)
        self.page_IL_scroll_area.setObjectName(u"scroll_area")
        self.page_IL_scroll_area.setStyleSheet(u"background: transparent;")
        self.page_IL_scroll_area.setFrameShape(QFrame.Box)
        self.page_IL_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.page_IL_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.page_IL_scroll_area.setWidgetResizable(True)
        # 这里的content是。。。
        self.page_IL_contents = QWidget()
        self.page_IL_contents.setObjectName(u"contents")
        # self.page_IL_contents.setGeometry(QRect(0, 0, 840, 1000))
        self.page_IL_contents.setStyleSheet(u"background: transparent;")
        # 设置该页面总体的layout
        self.page_IL_verticalLayout = QVBoxLayout(self.page_IL_contents)
        self.page_IL_verticalLayout.setSpacing(15)
        self.page_IL_verticalLayout.setObjectName(u"verticalLayout")
        self.page_IL_verticalLayout.setContentsMargins(5, 5, 5, 5)

        # 设置第一行下拉框的layout
        self.page_IL_row_1_layout = self.setup_row_1_layout()
        self.page_IL_verticalLayout.addLayout(self.page_IL_row_1_layout)

        # 设置第二行数据展示layout
        # self.page_IL_row_2_layout = self.setup_row_2_layout()
        # self.page_IL_verticalLayout.addLayout(self.page_IL_row_2_layout)
        self.img_widget = self.setup_row_2_layout()
        self.page_IL_verticalLayout.addWidget(self.img_widget)

        # split_line = QFrame(self.page_IL_contents)
        # split_line.setObjectName(u"split_line")
        # split_line.setFrameShape(QFrame.VLine)
        # split_line.setFrameShadow(QFrame.Sunken)
        self.page_IL_leftright_layout = QHBoxLayout()
        self.page_IL_left_layout = QVBoxLayout()
        # self.page_IL_mid_layout = QVBoxLayout()
        self.page_IL_right_layout = QVBoxLayout()
        # self.page_IL_mid_layout.addWidget(split_line)
        self.page_IL_leftright_layout.addLayout(self.page_IL_left_layout)
        # self.page_IL_leftright_layout.addLayout(self.page_IL_mid_layout)
        self.page_IL_leftright_layout.addLayout(self.page_IL_right_layout)
        self.page_IL_verticalLayout.addLayout(self.page_IL_leftright_layout)

        # self.page_IL_leftright_layout.setStretchFactor(self.page_IL_left_layout, 49)
        # self.page_IL_leftright_layout.setStretchFactor(self.page_IL_mid_layout, 2)
        # self.page_IL_leftright_layout.setStretchFactor(self.page_IL_right_layout, 49)

        self.page_IL_row_3_left_layout = self.setup_row_3_left_layout()
        self.page_IL_left_layout.addLayout(self.page_IL_row_3_left_layout)

        # self.page_IL_row_3_right_layout = self.setup_row_3_right_layout()
        # self.page_IL_right_layout.addLayout(self.page_IL_row_3_right_layout)

        # self.page_IL_row_4_left_layout = self.setup_row_4_left_layout()
        # self.page_IL_left_layout.addLayout(self.page_IL_row_4_left_layout)
        # self.page_IL_row_4_right_layout = self.setup_row_4_right_layout()
        # self.page_IL_right_layout.addLayout(self.page_IL_row_4_right_layout)

        # self.page_IL_row_5_layout = self.setup_row_5_layout()
        # self.page_IL_right_layout.addLayout(self.page_IL_row_5_layout)

        # self.page_IL_row_6_layout = self.setup_row_6_layout()
        # self.page_IL_right_layout.addLayout(self.page_IL_row_6_layout)
        self.page_IL_row_6_layout = self.setup_row_6_layout_()
        self.page_IL_right_layout.addLayout(self.page_IL_row_6_layout)

        self.bottom_space0 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.bottom_space1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.page_IL_verticalLayout.addItem(self.bottom_space1)
        self.page_IL_left_layout.addItem(self.bottom_space0)


        # 水平布局
        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        # 垂直布局中添加水平布局
        self.page_IL_verticalLayout.addLayout(self.row_1_layout)

        # 水平布局
        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.page_IL_verticalLayout.addLayout(self.row_2_layout)
        # 水平布局
        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.page_IL_verticalLayout.addLayout(self.row_3_layout)
        # 垂直布局
        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.page_IL_verticalLayout.addLayout(self.row_4_layout)
        # 垂直布局
        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.page_IL_verticalLayout.addLayout(self.row_5_layout)

        self.page_IL_scroll_area.setWidget(self.page_IL_contents)
        self.page_IL_layout.addWidget(self.page_IL_scroll_area)
        self.pages.addWidget(self.page_IL)

    # new layout
    def setup_row_1_layout_(self):
        page_row_1_layout = QHBoxLayout()
        page_row_1_layout.setContentsMargins(0, 0, 0, 10)

        self.label_IL_data = QLabel(self.page_IL)
        self.label_IL_data.setText("Choose Dataset")
        self.label_IL_data.setObjectName(u"label_IL_data")
        self.label_IL_data.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_IL_data = QComboBox(self.page_IL)
        for i in range(1):
            self.comboBox_IL_data.addItem("")
        self.comboBox_IL_data.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data.setMinimumSize(QSize(150, 40))
        self.comboBox_IL_data.setMaximumSize(QSize(200, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_IL_data.setFont(font_comboBox)
        self.comboBox_IL_data.setAutoFillBackground(False)
        self.comboBox_IL_data.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                            "border-radius: 5px;\n"
                                            "border: 2px solid rgb(33, 37, 43);\n"
                                            "padding: 5px;\n"
                                            "padding-left: 10px;\n"
                                            "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data.setIconSize(QSize(16, 16))
        self.comboBox_IL_data.setFrame(True)

        # 第二组下拉框
        self.label_IL_data1 = QLabel(self.page_IL)
        self.label_IL_data1.setText("Choose Dataset")
        self.label_IL_data1.setObjectName(u"label_IL_data")
        self.label_IL_data1.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data1.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data1.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_IL_data1 = QComboBox(self.page_IL)
        for i in range(1):
            self.comboBox_IL_data1.addItem("")
        self.comboBox_IL_data1.setObjectName(u"comboBox_op_data")
        self.comboBox_IL_data1.setMinimumSize(QSize(100, 40))
        self.comboBox_IL_data1.setMaximumSize(QSize(200, 16777215))

        self.comboBox_IL_data1.setFont(font_comboBox)
        self.comboBox_IL_data1.setAutoFillBackground(False)
        self.comboBox_IL_data1.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                             "border-radius: 5px;\n"
                                             "border: 2px solid rgb(33, 37, 43);\n"
                                             "padding: 5px;\n"
                                             "padding-left: 10px;\n"
                                             "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data1.setIconSize(QSize(16, 16))
        self.comboBox_IL_data1.setFrame(True)

        # 第三组下拉框
        self.label_IL_data2 = QLabel(self.page_IL)
        self.label_IL_data2.setObjectName(u"label_IL_data")
        self.label_IL_data2.setMaximumSize(QSize(16777215, 20))
        self.label_IL_data2.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_IL_data2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_IL_data2 = ComboCheckBox(modName)
        self.comboBox_IL_data2.setMinimumSize(QSize(200, 40))
        self.comboBox_IL_data2.setMaximumSize(QSize(300, 16777215))
        #
        self.comboBox_IL_data2.setFont(font_comboBox)
        # self.comboBox_IL_data2.setAutoFillBackground(False)
        self.comboBox_IL_data2.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                             "border-radius: 5px;\n"
                                             "border: 2px solid rgb(33, 37, 43);\n"
                                             "padding: 1px;\n"
                                             "padding-left: 10px;\n"
                                             "font: 14pt \"Segoe UI\";")
        self.comboBox_IL_data2.setIconSize(QSize(16, 16))
        # self.comboBox_IL_data2.setFrame(True)
        bottom_space0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        bottom_space1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        bottom_space2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout1 = QHBoxLayout()
        layout1.setContentsMargins(50, 0, 50, 0)
        layout2 = QHBoxLayout()
        layout2.setContentsMargins(50, 0, 50, 0)
        layout3 = QHBoxLayout()
        layout3.setContentsMargins(50, 0, 50, 0)
        self.page_IL_layout_loadData = QHBoxLayout()
        self.page_IL_layout_loadData.setContentsMargins(50, 0, 50, 0)
        layout1.addWidget(self.label_IL_data)
        layout1.addWidget(self.comboBox_IL_data)
        layout2.addWidget(self.label_IL_data1)
        layout2.addWidget(self.comboBox_IL_data1)
        layout3.addWidget(self.label_IL_data2)
        layout3.addWidget(self.comboBox_IL_data2)
        # page_row_1_layout.addItem(bottom_space0)
        page_row_1_layout.setAlignment(Qt.AlignCenter)
        page_row_1_layout.addLayout(layout1)
        page_row_1_layout.addItem(bottom_space0)
        page_row_1_layout.addLayout(layout2)
        page_row_1_layout.addItem(bottom_space1)
        page_row_1_layout.addLayout(layout3)
        page_row_1_layout.addItem(bottom_space2)
        page_row_1_layout.addLayout(self.page_IL_layout_loadData)
        # page_row_1_layout.addItem(bottom_space1)
        return page_row_1_layout

    # def setup_row_2_layout_(self):
    #     verticalLayout_5 = QVBoxLayout(self.page_IL_contents)
    #     verticalLayout_5.setObjectName(u"verticalLayout_5")
    #     verticalLayout_5.setContentsMargins(0, 0, 0, 0)
    #     horizontalLayout_43 = QHBoxLayout()
    #     horizontalLayout_43.setObjectName(u"horizontalLayout_43")
    #     verticalLayout_8 = QVBoxLayout()
    #     verticalLayout_8.setObjectName(u"verticalLayout_8")
    #     self.label_old_class = QLabel()
    #     self.label_old_class.setObjectName(u"label_tran4")
    #     self.label_old_class.setMinimumSize(QSize(0, 40))
    #     self.label_old_class.setMaximumSize(QSize(16777215, 50))
    #     self.label_old_class.setFrameShape(QFrame.NoFrame)
    #     self.label_old_class.setFrameShadow(QFrame.Sunken)
    #     self.label_old_class.setAlignment(Qt.AlignCenter)
    #
    #     verticalLayout_8.addWidget(self.label_old_class)
    #
    #     self.pic_old_class = QLabel()
    #     self.pic_old_class.setObjectName(u"pic_tl_source")
    #     self.pic_old_class.setStyleSheet(u"background-color: rgb(33, 37, 43);")
    #     self.pic_old_class.setAlignment(Qt.AlignCenter)
    #     self.pic_old_class.setMaximumSize(QSize(600, 100))
    #
    #     verticalLayout_8.addWidget(self.pic_old_class)
    #
    #     horizontalLayout_43.addLayout(verticalLayout_8)
    #
    #     vline = QLabel()
    #     vline.setObjectName(u"label_31")
    #     vline.setMaximumSize(QSize(1, 16777215))
    #     vline.setStyleSheet(u"color: rgb(27, 30, 35);")
    #     vline.setFrameShape(QFrame.VLine)
    #
    #     horizontalLayout_43.addWidget(vline)
    #
    #     verticalLayout_10 = QVBoxLayout()
    #     verticalLayout_10.setObjectName(u"verticalLayout_10")
    #     self.label_new_class = QLabel()
    #     self.label_new_class.setObjectName(u"label_tran5")
    #     self.label_new_class.setMinimumSize(QSize(0, 40))
    #     self.label_new_class.setMaximumSize(QSize(16777215, 50))
    #     self.label_new_class.setFrameShape(QFrame.NoFrame)
    #     self.label_new_class.setFrameShadow(QFrame.Sunken)
    #     self.label_new_class.setAlignment(Qt.AlignCenter)
    #
    #     verticalLayout_10.addWidget(self.label_new_class)
    #
    #     self.pic_new_class = QLabel()
    #     self.pic_new_class.setObjectName(u"pic_tl_target")
    #     self.pic_new_class.setStyleSheet(u"background-color: rgb(33, 37, 43);")
    #     self.pic_new_class.setAlignment(Qt.AlignCenter)
    #     self.label_new_class.setMaximumSize(QSize(600, 100))
    #
    #     hline = QLabel()
    #     hline.setObjectName(u"label_29")
    #     hline.setMaximumSize(QSize(16777215, 10))
    #     hline.setStyleSheet(u"color: rgb(27, 30, 35);")
    #     hline.setFrameShape(QFrame.HLine)
    #
    #     verticalLayout_10.addWidget(self.pic_new_class)
    #
    #     horizontalLayout_43.addLayout(verticalLayout_10)
    #
    #     horizontalLayout_43.setStretchFactor(verticalLayout_8, 48)
    #     horizontalLayout_43.setStretchFactor(vline, 1)
    #     horizontalLayout_43.setStretchFactor(verticalLayout_10, 48)
    #
    #     verticalLayout_5.addLayout(horizontalLayout_43)
    #     verticalLayout_5.addWidget(hline)
    #
    #     return verticalLayout_5

    def setup_row_2_layout__(self):
        verticalLayout_5 = QVBoxLayout(self.page_IL_contents)
        verticalLayout_5.setObjectName(u"verticalLayout_5")
        verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_43 = QHBoxLayout()
        horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        horizontalLayout_44 = QHBoxLayout()
        horizontalLayout_44.setObjectName(u"horizontalLayout_43")
        # verticalLayout_8 = QVBoxLayout()
        # verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_old_class = QLabel()
        self.label_old_class.setObjectName(u"label_tran4")
        self.label_old_class.setMinimumSize(QSize(0, 40))
        self.label_old_class.setMaximumSize(QSize(16777215, 50))
        self.label_old_class.setFrameShape(QFrame.NoFrame)
        self.label_old_class.setFrameShadow(QFrame.Sunken)
        self.label_old_class.setAlignment(Qt.AlignCenter)

        horizontalLayout_43.addWidget(self.label_old_class)

        self.pic_old_class = QLabel()
        self.pic_old_class.setObjectName(u"pic_tl_source")
        self.pic_old_class.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_old_class.setAlignment(Qt.AlignCenter)
        # self.pic_old_class.setMaximumSize(QSize(700, 100))

        horizontalLayout_44.addWidget(self.pic_old_class)

        vline = QLabel()
        vline.setObjectName(u"label_31")
        vline.setMaximumSize(QSize(1, 16777215))
        vline.setStyleSheet(u"color: rgb(27, 30, 35);")
        vline.setFrameShape(QFrame.VLine)

        horizontalLayout_43.addWidget(vline)

        verticalLayout_10 = QVBoxLayout()
        verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_new_class = QLabel()
        self.label_new_class.setObjectName(u"label_tran5")
        self.label_new_class.setMinimumSize(QSize(0, 40))
        self.label_new_class.setMaximumSize(QSize(16777215, 50))
        self.label_new_class.setFrameShape(QFrame.NoFrame)
        self.label_new_class.setFrameShadow(QFrame.Sunken)
        self.label_new_class.setAlignment(Qt.AlignCenter)

        horizontalLayout_43.addWidget(self.label_new_class)

        self.pic_new_class = QLabel()
        self.pic_new_class.setObjectName(u"pic_tl_target")
        self.pic_new_class.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_new_class.setAlignment(Qt.AlignCenter)

        hline = QLabel()
        hline.setObjectName(u"label_29")
        hline.setMaximumSize(QSize(16777215, 10))
        hline.setStyleSheet(u"color: rgb(27, 30, 35);")
        hline.setFrameShape(QFrame.HLine)
        # horizontalLayout_44.addWidget(vline)
        horizontalLayout_44.addWidget(self.pic_new_class)

        horizontalLayout_44.setStretchFactor(self.pic_old_class, 1)
        horizontalLayout_44.setStretchFactor(self.pic_new_class, 1)

        horizontalLayout_43.addLayout(verticalLayout_10)

        verticalLayout_5.addLayout(horizontalLayout_43)
        verticalLayout_5.addLayout(horizontalLayout_44)
        verticalLayout_5.addWidget(hline)


        return verticalLayout_5

    # def setup_row_3_left_1(self):
    #     layout = QHBoxLayout()
    #
    #     v_layout1 = QVBoxLayout()
    #     v_layout2 = QVBoxLayout()
    #     self.acc_progress_layout = QVBoxLayout()
    #     self.acc_progress_layout.setAlignment(Qt.AlignCenter)
    #     v_layout2.setAlignment(Qt.AlignCenter)
    #
    #     layout.addLayout(v_layout1)
    #     bottom_space1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    #     bottom_space2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    #     layout.addLayout(v_layout2)
    #     # layout.addItem(bottom_space1)
    #     layout.addLayout(self.acc_progress_layout)
    #     # layout.addItem(bottom_space2)
    #
    #     layout.setStretchFactor(v_layout1, 1)
    #     layout.setStretchFactor(v_layout2, 1)
    #     layout.setStretchFactor(self.acc_progress_layout, 1)
    #
    #     self.label_increment_test = QLabel(self.page_IL)
    #     self.label_increment_test.setMinimumSize(QSize(50, 80))
    #     # self.label_increment_test.setMaximumSize(QSize(16777215, 20))
    #     self.label_increment_test.setStyleSheet(u"font: 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
    #     self.label_increment_test.setAlignment(Qt.AlignLeft)
    #
    #     bottom_space0 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    #
    #
    #     v_layout1.addWidget(self.label_increment_test)
    #     v_layout1.addItem(bottom_space0)
    #
    #     # v_layout1.setAlignment(Qt.AlignLeft)
    #     # v_layout2.setAlignment(Qt.AlignLeft | Qt.AlignTop)
    #
    #     h_layout1 = QHBoxLayout()
    #     h_layout2 = QHBoxLayout()
    #     self.test_acc_layout = QHBoxLayout()
    #     v_layout2.addLayout(h_layout1)
    #     bottom_space1 = QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
    #     v_layout2.addItem(bottom_space1)
    #     v_layout2.addLayout(h_layout2)
    #     v_layout2.addLayout(self.test_acc_layout)
    #
    #     v_layout2.setStretchFactor(h_layout1, 1)
    #     v_layout2.setStretchFactor(h_layout2, 1)
    #     v_layout2.setStretchFactor(self.test_acc_layout, 1)
    #
    #
    #     self.label_test_type = QLabel(self.page_IL)
    #     self.label_test_type.setObjectName(u"label_IL_data")
    #     # self.label_test_type.setMaximumSize(QSize(16777215, 20))
    #     self.label_test_type.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
    #     self.label_test_type.setAlignment(Qt.AlignCenter | Qt.AlignTrailing | Qt.AlignVCenter)
    #
    #     self.comboBox_test_type = QComboBox(self.page_IL)
    #     for i in range(3):
    #         self.comboBox_test_type.addItem("")
    #     self.comboBox_test_type.setObjectName(u"comboBox_op_data")
    #     self.comboBox_test_type.setMinimumSize(QSize(150, 40))
    #     # self.comboBox_test_type.setMaximumSize(QSize(200, 16777215))
    #     font_comboBox = QFont()
    #     font_comboBox.setPointSize(14)
    #     font_comboBox.setBold(False)
    #     font_comboBox.setItalic(False)
    #     self.comboBox_test_type.setFont(font_comboBox)
    #     self.comboBox_test_type.setAutoFillBackground(False)
    #     self.comboBox_test_type.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
    #                                         "border-radius: 5px;\n"
    #                                         "border: 2px solid rgb(33, 37, 43);\n"
    #                                         "padding: 5px;\n"
    #                                         "padding-left: 10px;\n"
    #                                         "font: 14pt \"Segoe UI\";")
    #     self.comboBox_test_type.setIconSize(QSize(16, 16))
    #     self.comboBox_test_type.setFrame(True)
    #     h_layout1.addWidget(self.label_test_type)
    #     h_layout1.addWidget(self.comboBox_test_type)
    #
    #     self.label_pick_method = QLabel(self.page_IL)
    #     self.label_pick_method.setObjectName(u"label_IL_data")
    #     # self.label_pick_method.setMaximumSize(QSize(16777215, 20))
    #     self.label_pick_method.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
    #     self.label_pick_method.setAlignment(Qt.AlignCenter | Qt.AlignTrailing | Qt.AlignVCenter)
    #
    #     self.comboBox_pick_method = QComboBox(self.page_IL)
    #     for i in range(3):
    #         self.comboBox_pick_method.addItem("")
    #     self.comboBox_pick_method.setObjectName(u"comboBox_op_data")
    #     self.comboBox_pick_method.setMinimumSize(QSize(150, 40))
    #     # self.comboBox_pick_method.setMaximumSize(QSize(200, 16777215))
    #     self.comboBox_pick_method.setFont(font_comboBox)
    #     self.comboBox_pick_method.setAutoFillBackground(False)
    #     self.comboBox_pick_method.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
    #                                           "border-radius: 5px;\n"
    #                                           "border: 2px solid rgb(33, 37, 43);\n"
    #                                           "padding: 5px;\n"
    #                                           "padding-left: 10px;\n"
    #                                           "font: 14pt \"Segoe UI\";")
    #     self.comboBox_pick_method.setIconSize(QSize(16, 16))
    #     self.comboBox_pick_method.setFrame(True)
    #     h_layout2.addWidget(self.label_pick_method)
    #     h_layout2.addWidget(self.comboBox_pick_method)
    #     return layout

    def setup_row_3_left_1(self):
        layout = QHBoxLayout()

        v_layout1 = QVBoxLayout() # 只放标题
        v_layout2 = QVBoxLayout()

        layout.addLayout(v_layout1)
        layout.addLayout(v_layout2)

        layout.setStretchFactor(v_layout1, 1)
        layout.setStretchFactor(v_layout2, 8)

        hline1 = QLabel()
        hline1.setMaximumSize(QSize(16777215, 10))
        hline1.setStyleSheet(u"")
        hline1.setFrameShape(QFrame.HLine)

        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()

        bottom_space1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        bottom_space2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        bottom_space3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        v_layout2.addItem(bottom_space1)
        v_layout2.addLayout(h_layout_1)
        v_layout2.addItem(bottom_space2)
        v_layout2.addWidget(hline1)
        v_layout2.addItem(bottom_space3)
        v_layout2.addLayout(h_layout_2)

        v_layout2.setStretchFactor(h_layout_1, 3)
        v_layout2.setStretchFactor(hline1, 1)
        v_layout2.setStretchFactor(h_layout_2, 5)

        h_layout_1_1 = QHBoxLayout()
        h_layout_1_2 = QHBoxLayout()
        self.test_acc_layout = QHBoxLayout()

        bottom_space4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        bottom_space5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_layout_1.addLayout(h_layout_1_1)
        h_layout_1.addItem(bottom_space4)
        h_layout_1.addLayout(h_layout_1_2)
        h_layout_1.addItem(bottom_space5)
        h_layout_1.addLayout(self.test_acc_layout)

        v_layout_2_1 = QVBoxLayout()
        v_layout_2_2 = QVBoxLayout()
        v_layout_2_3 = QVBoxLayout()

        # v_layout_2_1.setAlignment(Qt.AlignCenter)
        # v_layout_2_2.setAlignment(Qt.AlignCenter)
        # v_layout_2_2.setAlignment(Qt.AlignCenter)

        h_layout_2.addLayout(v_layout_2_1)
        h_layout_2.addLayout(v_layout_2_2)
        h_layout_2.addLayout(v_layout_2_3)

        self.old_acc_progress = QVBoxLayout()
        self.new_acc_progress = QVBoxLayout()
        self.all_acc_progress = QVBoxLayout()

        self.label_increment_test = QLabel(self.page_IL)
        self.label_increment_test.setMinimumSize(QSize(50, 80))
        # self.label_increment_test.setMaximumSize(QSize(16777215, 20))
        self.label_increment_test.setStyleSheet(u"font: 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_increment_test.setAlignment(Qt.AlignLeft)

        v_layout1.addWidget(self.label_increment_test)

        # 第一行： 筛选方法 ： 下拉框以及测试按钮
        self.label_pick_method = QLabel()
        self.label_pick_method.setObjectName(u"label_IL_data")
        # self.label_pick_method.setMaximumSize(QSize(16777215, 20))
        self.label_pick_method.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_pick_method.setAlignment(Qt.AlignCenter | Qt.AlignTrailing | Qt.AlignVCenter)

        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_pick_method = QComboBox(self.page_IL)
        for i in range(3):
            self.comboBox_pick_method.addItem("")
        self.comboBox_pick_method.setObjectName(u"comboBox_op_data")
        self.comboBox_pick_method.setMinimumSize(QSize(150, 40))
        # self.comboBox_pick_method.setMaximumSize(QSize(200, 16777215))
        self.comboBox_pick_method.setFont(font_comboBox)
        self.comboBox_pick_method.setAutoFillBackground(False)
        self.comboBox_pick_method.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                                "border-radius: 5px;\n"
                                                "border: 2px solid rgb(33, 37, 43);\n"
                                                "padding: 5px;\n"
                                                "padding-left: 10px;\n"
                                                "font: 14pt \"Segoe UI\";")
        self.comboBox_pick_method.setIconSize(QSize(16, 16))
        self.comboBox_pick_method.setFrame(True)
        h_layout_1_1.addWidget(self.label_pick_method)
        h_layout_1_1.addWidget(self.comboBox_pick_method)

        self.label_task_size = QLabel(self.page_IL)
        self.label_task_size.setObjectName(u"label_IL_data")
        # self.label_pick_method.setMaximumSize(QSize(16777215, 20))
        self.label_task_size.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_task_size.setAlignment(Qt.AlignCenter | Qt.AlignTrailing | Qt.AlignVCenter)

        self.comboBox_task_size = QComboBox(self.page_IL)
        for i in range(2):
            self.comboBox_task_size.addItem("")
        self.comboBox_task_size.setObjectName(u"comboBox_op_data")
        self.comboBox_task_size.setMinimumSize(QSize(100, 40))
        # self.comboBox_pick_method.setMaximumSize(QSize(200, 16777215))
        self.comboBox_task_size.setFont(font_comboBox)
        self.comboBox_task_size.setAutoFillBackground(False)
        self.comboBox_task_size.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                                "border-radius: 5px;\n"
                                                "border: 2px solid rgb(33, 37, 43);\n"
                                                "padding: 5px;\n"
                                                "padding-left: 10px;\n"
                                                "font: 14pt \"Segoe UI\";")
        self.comboBox_task_size.setIconSize(QSize(16, 16))
        self.comboBox_task_size.setFrame(True)
        h_layout_1_2.addWidget(self.label_task_size)
        h_layout_1_2.addWidget(self.comboBox_task_size)

        self.label_old_acc = QLabel(self.page_IL)
        self.label_old_acc.setObjectName(u"label_IL_data")
        # self.label_pick_method.setMaximumSize(QSize(16777215, 20))
        self.label_old_acc.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_old_acc.setAlignment(Qt.AlignLeft | Qt.AlignTrailing | Qt.AlignVCenter)

        self.label_new_acc = QLabel(self.page_IL)
        self.label_new_acc.setObjectName(u"label_IL_data")
        # self.label_pick_method.setMaximumSize(QSize(16777215, 20))
        self.label_new_acc.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_new_acc.setAlignment(Qt.AlignLeft | Qt.AlignTrailing | Qt.AlignVCenter)

        self.label_all_acc = QLabel(self.page_IL)
        self.label_all_acc.setObjectName(u"label_IL_data")
        # self.label_pick_method.setMaximumSize(QSize(16777215, 20))
        self.label_all_acc.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_all_acc.setAlignment(Qt.AlignLeft | Qt.AlignTrailing | Qt.AlignVCenter)

        # layout_old = QVBoxLayout()
        # layout_old.setAlignment()
        # layout_new = QVBoxLayout()
        # layout_all = QVBoxLayout()
        # layout_old.addWidget(self.label_old_acc)
        # layout_new.addWidget(self.label_new_acc)
        # layout_all.addWidget(self.label_all_acc)
        #
        # v_layout_2_1.addLayout(self.old_acc_progress)
        # v_layout_2_1.addLayout(layout_old)
        # v_layout_2_2.addLayout(self.new_acc_progress)
        # v_layout_2_2.addLayout(layout_new)
        # v_layout_2_3.addLayout(self.all_acc_progress)
        # v_layout_2_3.addLayout(layout_all)

        v_layout_2_1.addLayout(self.old_acc_progress)
        v_layout_2_1.addWidget(self.label_old_acc)
        v_layout_2_2.addLayout(self.new_acc_progress)
        v_layout_2_2.addWidget(self.label_new_acc)
        v_layout_2_3.addLayout(self.all_acc_progress)
        v_layout_2_3.addWidget(self.label_all_acc)

        return layout

    def setup_row_3_left_2(self):
        layout = QHBoxLayout()
        v_layout_1 = QVBoxLayout()
        v_layout_2 = QVBoxLayout()
        v_layout_3 = QVBoxLayout()

        layout.addLayout(v_layout_1)
        layout.addLayout(v_layout_2)
        layout.addLayout(v_layout_3)

        layout.setStretchFactor(v_layout_1, 2)
        layout.setStretchFactor(v_layout_2, 5)
        layout.setStretchFactor(v_layout_3, 5)

        h_layout_1 = QHBoxLayout()
        h_layout_2 = QVBoxLayout()
        v_layout_2.addLayout(h_layout_1)
        v_layout_2.addLayout(h_layout_2)

        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        h_layout3 = QHBoxLayout()

        bottom_space2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        bottom_space3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        bottom_space4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        bottom_space5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        h_layout_2.addItem(bottom_space2)
        h_layout_2.addLayout(h_layout1)
        h_layout_2.addItem(bottom_space3)
        h_layout_2.addLayout(h_layout2)
        h_layout_2.addItem(bottom_space4)
        h_layout_2.addLayout(h_layout3)
        h_layout_2.addItem(bottom_space5)

        h_layout_1_1 = QHBoxLayout()
        h_layout_1_2 = QHBoxLayout()
        self.next_sample_layout = QHBoxLayout()

        h_layout_1.addLayout(h_layout_1_1)
        h_layout_1.addLayout(h_layout_1_2)
        h_layout_1.addLayout(self.next_sample_layout)

        layout_23 = QHBoxLayout()
        layout_23.addLayout(h_layout_1_2)
        layout_23.addLayout(self.next_sample_layout)
        layout_23.setAlignment(Qt.AlignRight | Qt.AlignTop)

        self.label_data_pick = QLabel()
        self.label_data_pick.setObjectName(u"label_IL_data")
        self.label_data_pick.setMinimumSize(QSize(200, 80))
        # self.label_data_pick.setMaximumSize(QSize(16777215, 20))
        self.label_data_pick.setStyleSheet(u"font: 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.label_data_pick.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        v_layout_1.addWidget(self.label_data_pick)
        bottom_space1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        v_layout_1.addItem(bottom_space1)


        self.comboBox_class_type = QComboBox(self.page_IL)
        for i in range(12):
            self.comboBox_class_type.addItem("")
        self.comboBox_class_type.setObjectName(u"comboBox_op_data")
        self.comboBox_class_type.setMinimumSize(QSize(150, 40))
        self.comboBox_class_type.setMaximumSize(QSize(200, 16777215))
        font_comboBox = QFont()
        font_comboBox.setPointSize(14)
        font_comboBox.setBold(False)
        font_comboBox.setItalic(False)
        self.comboBox_class_type.setFont(font_comboBox)
        self.comboBox_class_type.setAutoFillBackground(False)
        self.comboBox_class_type.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
                                              "border-radius: 5px;\n"
                                              "border: 2px solid rgb(33, 37, 43);\n"
                                              "padding: 5px;\n"
                                              "padding-left: 10px;\n"
                                              "font: 14pt \"Segoe UI\";")
        self.comboBox_class_type.setIconSize(QSize(16, 16))
        self.comboBox_class_type.setFrame(True)
        h_layout_1_2.addWidget(self.comboBox_class_type)
        bottom_space6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_layout_1_2.addItem(bottom_space6)

        self.label_true = QLabel()
        self.label_true.setObjectName(u"label_IL_data")
        self.label_true.setMaximumSize(QSize(16777215, 20))
        self.label_true.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_true_value = QLabel()
        self.label_true_value.setObjectName(u"label_IL_data")
        self.label_true_value.setMaximumSize(QSize(16777215, 20))
        self.label_true_value.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.label_pred = QLabel()
        self.label_pred.setObjectName(u"label_IL_data")
        self.label_pred.setMaximumSize(QSize(16777215, 20))
        self.label_pred.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_pred_value = QLabel()
        self.label_pred_value.setObjectName(u"label_IL_data")
        self.label_pred_value.setMaximumSize(QSize(16777215, 20))
        self.label_pred_value.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.label_time = QLabel()
        self.label_time.setObjectName(u"label_IL_data")
        self.label_time.setMaximumSize(QSize(16777215, 20))
        self.label_time.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_time_value = QLabel()
        self.label_time_value.setObjectName(u"label_IL_data")
        self.label_time_value.setMaximumSize(QSize(16777215, 20))
        self.label_time_value.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        h_layout1.addWidget(self.label_true)
        h_layout1.addWidget(self.label_true_value)
        h_layout2.addWidget(self.label_pred)
        h_layout2.addWidget(self.label_pred_value)
        h_layout3.addWidget(self.label_time)
        h_layout3.addWidget(self.label_time_value)

        self.pic_sample = QLabel()
        self.pic_sample.setObjectName(u"pic_sample")
        self.pic_sample.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_sample.setAlignment(Qt.AlignCenter)
        v_layout_3.addWidget(self.pic_sample)

        return layout

    def setup_row_3_right(self):
        layout = QVBoxLayout()

        self.pic_matrix = QLabel()
        self.pic_matrix.setObjectName(u"pic_tl_source")
        self.pic_matrix.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pic_matrix.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.pic_matrix)

        self.label_matrix = QLabel(self.page_IL)
        self.label_matrix.setText("Choose Dataset")
        self.label_matrix.setObjectName(u"label_IL_data")
        self.label_matrix.setMaximumSize(QSize(16777215, 20))
        self.label_matrix.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_matrix.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label_matrix)

        return layout


    def setup_page_IL_3(self):
        self.page_IL = QWidget()
        self.page_IL.setObjectName(u"page_IL")

        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page_IL.sizePolicy().hasHeightForWidth())
        self.page_IL.setSizePolicy(sizePolicy1)
        # 首先定义了page2的整体布局为垂直布局
        self.page_IL_layout = QVBoxLayout(self.page_IL)
        self.page_IL_layout.setSpacing(0)
        self.page_IL_layout.setObjectName(u"page_2_layout")
        # self.page_IL_layout.setContentsMargins(5, 5, 5, 5)

        self.page_IL_title_layout = self.setup_row_title()
        self.page_IL_layout.addLayout(self.page_IL_title_layout)

        self.page_row_1_layout = self.setup_row_1_layout_()
        self.page_IL_layout.addLayout(self.page_row_1_layout)

        self.hline1 = QLabel(self.page_IL)
        self.hline1.setMaximumSize(QSize(16777215, 10))
        self.hline1.setStyleSheet(u"")
        self.hline1.setFrameShape(QFrame.HLine)
        self.page_IL_layout.addWidget(self.hline1)

        # page2中的滚动区域是。。。
        self.page_IL_scroll_area = QScrollArea(self.page_IL)
        self.page_IL_scroll_area.setObjectName(u"scroll_area")
        self.page_IL_scroll_area.setStyleSheet(u"background: transparent;")
        self.page_IL_scroll_area.setFrameShape(QFrame.Box)
        self.page_IL_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.page_IL_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.page_IL_scroll_area.setWidgetResizable(True)
        # 这里的content是。。。
        self.page_IL_contents = QWidget()
        self.page_IL_contents.setObjectName(u"contents")
        # self.page_IL_contents.setGeometry(QRect(0, 0, 840, 1000))
        # self.page_IL_contents.setGeometry(QRect(0, 0, 1200, 1200))
        self.page_IL_contents.setStyleSheet(u"background: transparent;")
        # 设置该页面总体的layout
        self.page_IL_verticalLayout = QVBoxLayout(self.page_IL_contents)
        # self.page_IL_verticalLayout.setSpacing(15)
        self.page_IL_verticalLayout.setObjectName(u"verticalLayout")
        self.page_IL_verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.page_row_2_layout = self.setup_row_2_layout__()
        self.page_IL_verticalLayout.addLayout(self.page_row_2_layout)

        # self.page_row_3 = QVBoxLayout()
        self.page_row_3_layout = QHBoxLayout()
        # self.page_row_3.addLayout(self.page_row_3_layout)
        self.page_row_3_left_layout = QVBoxLayout()
        self.page_row_3_right_layout = QVBoxLayout()
        self.page_row_3_layout.addLayout(self.page_row_3_left_layout)
        self.hline2 = QLabel(self.page_IL)
        self.hline2.setStyleSheet(u"")
        self.hline2.setMaximumSize(QSize(1, 16777215))
        self.hline2.setStyleSheet(u"color: rgb(27, 30, 35);")
        self.hline2.setFrameShape(QFrame.VLine)


        self.page_row_3_layout.addWidget(self.hline2)
        self.page_row_3_layout.addLayout(self.page_row_3_right_layout)
        self.page_row_3_layout.setStretchFactor(self.page_row_3_left_layout, 70)
        self.page_row_3_layout.setStretchFactor(self.hline2, 2)
        self.page_row_3_layout.setStretchFactor(self.page_row_3_right_layout, 48)

        self.page_row_3_left_layout_1 = self.setup_row_3_left_1()

        self.hline3 = QLabel(self.page_IL)
        self.hline3.setMaximumSize(QSize(16777215, 10))
        self.hline3.setStyleSheet(u"")
        self.hline3.setFrameShape(QFrame.HLine)
        self.page_IL_layout.addWidget(self.hline3)
        self.page_row_3_left_layout_2 = self.setup_row_3_left_2()

        self.page_row_3_right = self.setup_row_3_right()

        self.page_row_3_left_layout.addLayout(self.page_row_3_left_layout_1)
        self.page_row_3_left_layout.addWidget(self.hline3)
        self.page_row_3_left_layout.addLayout(self.page_row_3_left_layout_2)

        self.page_row_3_left_layout.setStretchFactor(self.page_row_3_left_layout_1, 50)
        self.page_row_3_left_layout.setStretchFactor(self.hline3, 1)
        self.page_row_3_left_layout.setStretchFactor(self.page_row_3_left_layout_2, 40)

        self.page_row_3_right_layout.addLayout(self.page_row_3_right)

        self.page_IL_verticalLayout.addLayout(self.page_row_3_layout)

        self.page_IL_verticalLayout.setStretchFactor(self.page_row_2_layout, 2)
        self.page_IL_verticalLayout.setStretchFactor(self.page_row_3_layout, 4)

        self.page_IL_scroll_area.setWidget(self.page_IL_contents)
        self.page_IL_layout.addWidget(self.page_IL_scroll_area)

        self.page_IL_layout.setStretchFactor(self.page_IL_title_layout, 5)
        self.page_IL_layout.setStretchFactor(self.page_row_1_layout, 5)
        self.page_IL_layout.setStretchFactor(self.hline1, 1)
        self.page_IL_layout.setStretchFactor(self.hline3, 1)
        self.page_IL_layout.setStretchFactor(self.page_IL_scroll_area, 90)

        self.pages.addWidget(self.page_IL)

    def setupUi(self, MainPages):
        self.setup_main(MainPages)
        # if not MainPages.objectName():
        #     MainPages.setObjectName(u"MainPages")
        # # 首先设置一下默认的内容区域大小
        # MainPages.resize(860, 600)
        # # 这里开始时创建page1 设置一下布局
        # self.main_pages_layout = QVBoxLayout(MainPages)
        # self.main_pages_layout.setSpacing(0)
        # self.main_pages_layout.setObjectName(u"main_pages_layout")
        # self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        # # 堆载窗口控件，就是多个页面来回切换，可以往该空间中添加多个页面，每个页面都是一个QWidget
        # self.pages = QStackedWidget(MainPages)
        # self.pages.setObjectName(u"pages")

        self.setup_page_1()

        # 开始创建page2中的元素 -------------------------------------------
        self.setup_page_2()
        # -------------------------------------------------------------------------------
        # 接下来是创建了第三个页面
        # self.page_3 = QWidget()
        # self.page_3.setObjectName(u"page_3")
        # self.page_3.setStyleSheet(u"QFrame {\n""font-size: 16pt;\n""}")
        # # 设置page三布局为垂直布局
        # self.page_3_layout = QVBoxLayout(self.page_3)
        # # 设置page3布局名字吧
        # self.page_3_layout.setObjectName(u"page_3_layout")
        # self.empty_page_label = QLabel(self.page_3)
        # self.empty_page_label.setObjectName(u"empty_page_label")
        # self.empty_page_label.setFont(font)
        # self.empty_page_label.setAlignment(Qt.AlignCenter)
        #
        # self.page_3_layout.addWidget(self.empty_page_label)
        # # 把page3添加到pages中
        # self.pages.addWidget(self.page_3)

        # page_IL-------------------------------------------------------------------

        # 新添加代码 page_op--------------------------------------------------------------------------------

        # self.setup_page_IL()
        # self.setup_page_IL_1()
        # self.setup_page_IL_2()
        self.setup_page_IL_3()

        self.setup_page_OP()

        # 以上为page_OP代码------------------------------------------------------------

        # 以下为page_TL代码

        # self.page_TL = QWidget()
        # self.page_TL.setObjectName(u"page_TL")
        # self.verticalLayout_3 = QVBoxLayout(self.page_TL)
        # self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        # self.title_label_op_2 = QLabel(self.page_TL)
        # self.title_label_op_2.setObjectName(u"title_label_op_2")
        # self.title_label_op_2.setMaximumSize(QSize(16777215, 40))
        # self.title_label_op_2.setFont(font3)
        # self.title_label_op_2.setStyleSheet(u"font: 26pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.title_label_op_2.setAlignment(Qt.AlignCenter)
        #
        # self.verticalLayout_3.addWidget(self.title_label_op_2)
        #
        # self.label_28 = QLabel(self.page_TL)
        # self.label_28.setObjectName(u"label_28")
        # self.label_28.setMaximumSize(QSize(16777215, 10))
        #
        # self.verticalLayout_3.addWidget(self.label_28)
        #
        # self.horizontalLayout_4 = QHBoxLayout()
        # self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        # self.horizontalLayout_14 = QHBoxLayout()
        # self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        # self.label_op_data_2 = QLabel(self.page_TL)
        # self.label_op_data_2.setObjectName(u"label_op_data_2")
        # self.label_op_data_2.setMaximumSize(QSize(16777215, 50))
        # self.label_op_data_2.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.label_op_data_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        #
        # self.horizontalLayout_14.addWidget(self.label_op_data_2)
        #
        # self.horizontalLayout_4.addLayout(self.horizontalLayout_14)
        #
        # self.horizontalLayout_27 = QHBoxLayout()
        # self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        # self.comboBox_tl_method = QComboBox(self.page_TL)
        # self.comboBox_tl_method.addItem("")
        # self.comboBox_tl_method.addItem("")
        # self.comboBox_tl_method.addItem("")
        # self.comboBox_tl_method.addItem("")
        # self.comboBox_tl_method.addItem("")
        # self.comboBox_tl_method.setObjectName(u"comboBox_tl_method")
        # self.comboBox_tl_method.setMinimumSize(QSize(160, 40))
        # self.comboBox_tl_method.setMaximumSize(QSize(100, 50))
        # self.comboBox_tl_method.setFont(font4)
        # self.comboBox_tl_method.setAutoFillBackground(False)
        # self.comboBox_tl_method.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
        #                                       "border-radius: 5px;\n"
        #                                       "border: 2px solid rgb(33, 37, 43);\n"
        #                                       "padding: 5px;\n"
        #                                       "padding-left: 10px;\n"
        #                                       "font: 14pt \"Segoe UI\";")
        # self.comboBox_tl_method.setIconSize(QSize(16, 16))
        # self.comboBox_tl_method.setFrame(True)
        #
        # self.horizontalLayout_27.addWidget(self.comboBox_tl_method)
        #
        # self.horizontalLayout_4.addLayout(self.horizontalLayout_27)
        #
        # self.horizontalLayout_28 = QHBoxLayout()
        # self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        # self.label_11 = QLabel(self.page_TL)
        # self.label_11.setObjectName(u"label_11")
        # self.label_11.setMinimumSize(QSize(0, 80))
        # self.label_11.setMaximumSize(QSize(16777215, 100))
        #
        # self.horizontalLayout_28.addWidget(self.label_11)
        #
        # self.horizontalLayout_4.addLayout(self.horizontalLayout_28)
        #
        # self.horizontalLayout_38 = QHBoxLayout()
        # self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        # self.label_op_snr_2 = QLabel(self.page_TL)
        # self.label_op_snr_2.setObjectName(u"label_op_snr_2")
        # self.label_op_snr_2.setMaximumSize(QSize(16777215, 50))
        # self.label_op_snr_2.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.label_op_snr_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        #
        # self.horizontalLayout_38.addWidget(self.label_op_snr_2)
        #
        # self.horizontalLayout_4.addLayout(self.horizontalLayout_38)
        #
        # self.horizontalLayout_39 = QHBoxLayout()
        # self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        # self.comboBox_tl_dataset = QComboBox(self.page_TL)
        # self.comboBox_tl_dataset.addItem("")
        # self.comboBox_tl_dataset.setObjectName(u"comboBox_tl_dataset")
        # self.comboBox_tl_dataset.setMinimumSize(QSize(150, 40))
        # self.comboBox_tl_dataset.setMaximumSize(QSize(120, 50))
        # self.comboBox_tl_dataset.setFont(font4)
        # self.comboBox_tl_dataset.setAutoFillBackground(False)
        # self.comboBox_tl_dataset.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
        #                                        "border-radius: 5px;\n"
        #                                        "border: 2px solid rgb(33, 37, 43);\n"
        #                                        "padding: 5px;\n"
        #                                        "padding-left: 10px;\n"
        #                                        "font: 14pt \"Segoe UI\";")
        # self.comboBox_tl_dataset.setIconSize(QSize(16, 16))
        # self.comboBox_tl_dataset.setFrame(True)
        #
        # self.horizontalLayout_39.addWidget(self.comboBox_tl_dataset)
        #
        # self.horizontalLayout_4.addLayout(self.horizontalLayout_39)
        #
        # self.horizontalLayout_40 = QHBoxLayout()
        # self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        # self.label_12 = QLabel(self.page_TL)
        # self.label_12.setObjectName(u"label_12")
        # self.label_12.setMaximumSize(QSize(16777215, 50))
        #
        # self.horizontalLayout_40.addWidget(self.label_12)
        #
        # self.horizontalLayout_4.addLayout(self.horizontalLayout_40)
        #
        # self.horizontalLayout_41 = QHBoxLayout()
        # self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        # self.label_op_snr_3 = QLabel(self.page_TL)
        # self.label_op_snr_3.setObjectName(u"label_op_snr_3")
        # self.label_op_snr_3.setMaximumSize(QSize(16777215, 50))
        # self.label_op_snr_3.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.label_op_snr_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        #
        # self.horizontalLayout_41.addWidget(self.label_op_snr_3)
        #
        # self.horizontalLayout_4.addLayout(self.horizontalLayout_41)
        #
        # self.horizontalLayout_42 = QHBoxLayout()
        # self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        # self.comboBox_tl_snr = QComboBox(self.page_TL)
        # self.comboBox_tl_snr.addItem("")
        # self.comboBox_tl_snr.setObjectName(u"comboBox_tl_snr")
        # self.comboBox_tl_snr.setMinimumSize(QSize(80, 40))
        # self.comboBox_tl_snr.setMaximumSize(QSize(120, 50))
        # self.comboBox_tl_snr.setFont(font4)
        # self.comboBox_tl_snr.setAutoFillBackground(False)
        # self.comboBox_tl_snr.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
        #                                    "border-radius: 5px;\n"
        #                                    "border: 2px solid rgb(33, 37, 43);\n"
        #                                    "padding: 5px;\n"
        #                                    "padding-left: 10px;\n"
        #                                    "font: 14pt \"Segoe UI\";")
        # self.comboBox_tl_snr.setIconSize(QSize(16, 16))
        # self.comboBox_tl_snr.setFrame(True)
        #
        # self.horizontalLayout_42.addWidget(self.comboBox_tl_snr)
        #
        # self.horizontalLayout_4.addLayout(self.horizontalLayout_42)
        #
        # self.horizontalLayout_44 = QHBoxLayout()
        # self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        # self.label_14 = QLabel(self.page_TL)
        # self.label_14.setObjectName(u"label_14")
        # self.label_14.setMaximumSize(QSize(16777215, 50))
        #
        # self.horizontalLayout_44.addWidget(self.label_14)
        #
        # self.horizontalLayout_4.addLayout(self.horizontalLayout_44)
        #
        # self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        #
        # self.label_58 = QLabel(self.page_TL)
        # self.label_58.setObjectName(u"label_58")
        # self.label_58.setMaximumSize(QSize(16777215, 10))
        # self.label_58.setStyleSheet(u"")
        # self.label_58.setFrameShape(QFrame.HLine)
        #
        # self.verticalLayout_3.addWidget(self.label_58)
        #
        # self.scroll_area_tl = QScrollArea(self.page_TL)
        # self.scroll_area_tl.setObjectName(u"scroll_area_tl")
        # self.scroll_area_tl.setStyleSheet(u"background: transparent;")
        # self.scroll_area_tl.setFrameShape(QFrame.NoFrame)
        # self.scroll_area_tl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll_area_tl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll_area_tl.setWidgetResizable(True)
        # self.contents_tl = QWidget()
        # self.contents_tl.setObjectName(u"contents_tl")
        # self.contents_tl.setGeometry(QRect(0, 0, 1254, 872))
        # self.verticalLayout_5 = QVBoxLayout(self.contents_tl)
        # self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        # self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout_43 = QHBoxLayout()
        # self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        # self.verticalLayout_8 = QVBoxLayout()
        # self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        # self.label_tran4 = QLabel(self.contents_tl)
        # self.label_tran4.setObjectName(u"label_tran4")
        # self.label_tran4.setMinimumSize(QSize(0, 40))
        # self.label_tran4.setMaximumSize(QSize(16777215, 50))
        # self.label_tran4.setFrameShape(QFrame.NoFrame)
        # self.label_tran4.setFrameShadow(QFrame.Sunken)
        # self.label_tran4.setAlignment(Qt.AlignCenter)
        #
        # self.verticalLayout_8.addWidget(self.label_tran4)
        #
        # self.pic_tl_source = QLabel(self.contents_tl)
        # self.pic_tl_source.setObjectName(u"pic_tl_source")
        # self.pic_tl_source.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        # self.pic_tl_source.setAlignment(Qt.AlignCenter)
        #
        # self.verticalLayout_8.addWidget(self.pic_tl_source)
        #
        # self.horizontalLayout_43.addLayout(self.verticalLayout_8)
        #
        # self.label_31 = QLabel(self.contents_tl)
        # self.label_31.setObjectName(u"label_31")
        # self.label_31.setMaximumSize(QSize(1, 16777215))
        # self.label_31.setStyleSheet(u"color: rgb(27, 30, 35);")
        # self.label_31.setFrameShape(QFrame.VLine)
        #
        # self.horizontalLayout_43.addWidget(self.label_31)
        #
        # self.verticalLayout_10 = QVBoxLayout()
        # self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        # self.label_tran5 = QLabel(self.contents_tl)
        # self.label_tran5.setObjectName(u"label_tran5")
        # self.label_tran5.setMinimumSize(QSize(0, 40))
        # self.label_tran5.setMaximumSize(QSize(16777215, 50))
        # self.label_tran5.setFrameShape(QFrame.NoFrame)
        # self.label_tran5.setFrameShadow(QFrame.Sunken)
        # self.label_tran5.setAlignment(Qt.AlignCenter)
        #
        # self.verticalLayout_10.addWidget(self.label_tran5)
        #
        # self.pic_tl_target = QLabel(self.contents_tl)
        # self.pic_tl_target.setObjectName(u"pic_tl_target")
        # self.pic_tl_target.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        # self.pic_tl_target.setAlignment(Qt.AlignCenter)
        #
        # self.verticalLayout_10.addWidget(self.pic_tl_target)
        #
        # self.horizontalLayout_43.addLayout(self.verticalLayout_10)
        #
        # self.verticalLayout_5.addLayout(self.horizontalLayout_43)
        #
        # self.label_29 = QLabel(self.contents_tl)
        # self.label_29.setObjectName(u"label_29")
        # self.label_29.setMaximumSize(QSize(16777215, 10))
        # self.label_29.setStyleSheet(u"color: rgb(27, 30, 35);")
        # self.label_29.setFrameShape(QFrame.HLine)
        #
        # self.verticalLayout_5.addWidget(self.label_29)
        #
        # self.horizontalLayout_45 = QHBoxLayout()
        # self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        # self.verticalLayout_12 = QVBoxLayout()
        # self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        # self.horizontalLayout_47 = QHBoxLayout()
        # self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        # self.label_tran6 = QLabel(self.contents_tl)
        # self.label_tran6.setObjectName(u"label_tran6")
        # self.label_tran6.setMinimumSize(QSize(0, 50))
        # self.label_tran6.setMaximumSize(QSize(250, 16777215))
        # self.label_tran6.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.label_tran6.setFrameShape(QFrame.NoFrame)
        # self.label_tran6.setFrameShadow(QFrame.Sunken)
        #
        # self.horizontalLayout_47.addWidget(self.label_tran6)
        #
        # self.comboBox_tl_shot = QComboBox(self.contents_tl)
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.addItem("")
        # self.comboBox_tl_shot.setObjectName(u"comboBox_tl_shot")
        # self.comboBox_tl_shot.setMinimumSize(QSize(120, 40))
        # self.comboBox_tl_shot.setMaximumSize(QSize(100, 16777215))
        # self.comboBox_tl_shot.setFont(font4)
        # self.comboBox_tl_shot.setAutoFillBackground(False)
        # self.comboBox_tl_shot.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
        #                                     "border-radius: 5px;\n"
        #                                     "border: 2px solid rgb(33, 37, 43);\n"
        #                                     "padding: 5px;\n"
        #                                     "padding-left: 10px;\n"
        #                                     "font: 14pt \"Segoe UI\";")
        # self.comboBox_tl_shot.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        # self.comboBox_tl_shot.setIconSize(QSize(16, 16))
        # self.comboBox_tl_shot.setFrame(True)
        #
        # self.horizontalLayout_47.addWidget(self.comboBox_tl_shot)
        #
        # self.verticalLayout_12.addLayout(self.horizontalLayout_47)
        #
        # self.horizontalLayout_57 = QHBoxLayout()
        # self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        # self.label_tran6_2 = QLabel(self.contents_tl)
        # self.label_tran6_2.setObjectName(u"label_tran6_2")
        # self.label_tran6_2.setMinimumSize(QSize(0, 50))
        # self.label_tran6_2.setMaximumSize(QSize(250, 16777215))
        # self.label_tran6_2.setStyleSheet(u"font: 16pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        # self.label_tran6_2.setFrameShape(QFrame.NoFrame)
        # self.label_tran6_2.setFrameShadow(QFrame.Sunken)
        #
        # self.horizontalLayout_57.addWidget(self.label_tran6_2)
        #
        # self.comboBox_tl_samples = QComboBox(self.contents_tl)
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.addItem("")
        # self.comboBox_tl_samples.setObjectName(u"comboBox_tl_samples")
        # self.comboBox_tl_samples.setMinimumSize(QSize(120, 40))
        # self.comboBox_tl_samples.setMaximumSize(QSize(100, 16777215))
        # self.comboBox_tl_samples.setFont(font4)
        # self.comboBox_tl_samples.setAutoFillBackground(False)
        # self.comboBox_tl_samples.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
        #                                        "border-radius: 5px;\n"
        #                                        "border: 2px solid rgb(33, 37, 43);\n"
        #                                        "padding: 5px;\n"
        #                                        "padding-left: 10px;\n"
        #                                        "font: 14pt \"Segoe UI\";")
        # self.comboBox_tl_samples.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        # self.comboBox_tl_samples.setIconSize(QSize(16, 16))
        # self.comboBox_tl_samples.setFrame(True)
        #
        # self.horizontalLayout_57.addWidget(self.comboBox_tl_samples)
        #
        # self.verticalLayout_12.addLayout(self.horizontalLayout_57)
        #
        # self.horizontalLayout_48 = QHBoxLayout()
        # self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        # self.label_20 = QLabel(self.contents_tl)
        # self.label_20.setObjectName(u"label_20")
        # self.label_20.setMinimumSize(QSize(0, 50))
        # self.label_20.setMaximumSize(QSize(20, 16777215))
        #
        # self.horizontalLayout_48.addWidget(self.label_20)
        #
        # self.layout_tl_test_base = QHBoxLayout()
        # self.layout_tl_test_base.setObjectName(u"layout_tl_test_base")
        #
        # self.horizontalLayout_48.addLayout(self.layout_tl_test_base)
        #
        # self.label_37 = QLabel(self.contents_tl)
        # self.label_37.setObjectName(u"label_37")
        # self.label_37.setMaximumSize(QSize(20, 16777215))
        #
        # self.horizontalLayout_48.addWidget(self.label_37)
        #
        # self.layout_tl_test_adv = QHBoxLayout()
        # self.layout_tl_test_adv.setObjectName(u"layout_tl_test_adv")
        #
        # self.horizontalLayout_48.addLayout(self.layout_tl_test_adv)
        #
        # self.label_57 = QLabel(self.contents_tl)
        # self.label_57.setObjectName(u"label_57")
        # self.label_57.setMaximumSize(QSize(20, 16777215))
        #
        # self.horizontalLayout_48.addWidget(self.label_57)
        #
        # self.verticalLayout_12.addLayout(self.horizontalLayout_48)
        #
        # self.label_30 = QLabel(self.contents_tl)
        # self.label_30.setObjectName(u"label_30")
        # self.label_30.setMaximumSize(QSize(16777215, 10))
        # self.label_30.setStyleSheet(u"color: rgb(27, 30, 35);")
        # self.label_30.setFrameShape(QFrame.HLine)
        #
        # self.verticalLayout_12.addWidget(self.label_30)
        #
        # self.label_tran7 = QLabel(self.contents_tl)
        # self.label_tran7.setObjectName(u"label_tran7")
        # self.label_tran7.setMinimumSize(QSize(0, 50))
        # self.label_tran7.setMaximumSize(QSize(16777215, 50))
        # self.label_tran7.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)
        #
        # self.verticalLayout_12.addWidget(self.label_tran7)
        #
        # self.horizontalLayout_49 = QHBoxLayout()
        # self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        # self.label_tran8 = QLabel(self.contents_tl)
        # self.label_tran8.setObjectName(u"label_tran8")
        # self.label_tran8.setMinimumSize(QSize(0, 50))
        # self.label_tran8.setFrameShape(QFrame.NoFrame)
        # self.label_tran8.setFrameShadow(QFrame.Sunken)
        # self.label_tran8.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        #
        # self.horizontalLayout_49.addWidget(self.label_tran8)
        #
        # self.label_16 = QLabel(self.contents_tl)
        # self.label_16.setObjectName(u"label_16")
        #
        # self.horizontalLayout_49.addWidget(self.label_16)
        #
        # self.layout_base_acc = QHBoxLayout()
        # self.layout_base_acc.setObjectName(u"layout_base_acc")
        #
        # self.horizontalLayout_49.addLayout(self.layout_base_acc)
        #
        # self.label_13 = QLabel(self.contents_tl)
        # self.label_13.setObjectName(u"label_13")
        #
        # self.horizontalLayout_49.addWidget(self.label_13)
        #
        # self.verticalLayout_12.addLayout(self.horizontalLayout_49)
        #
        # self.horizontalLayout_50 = QHBoxLayout()
        # self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        # self.label_tran8_2 = QLabel(self.contents_tl)
        # self.label_tran8_2.setObjectName(u"label_tran8_2")
        # self.label_tran8_2.setMinimumSize(QSize(0, 50))
        # self.label_tran8_2.setFrameShape(QFrame.NoFrame)
        # self.label_tran8_2.setFrameShadow(QFrame.Sunken)
        # self.label_tran8_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        #
        # self.horizontalLayout_50.addWidget(self.label_tran8_2)
        #
        # self.label_17 = QLabel(self.contents_tl)
        # self.label_17.setObjectName(u"label_17")
        #
        # self.horizontalLayout_50.addWidget(self.label_17)
        #
        # self.layout_adv_acc = QHBoxLayout()
        # self.layout_adv_acc.setObjectName(u"layout_adv_acc")
        #
        # self.horizontalLayout_50.addLayout(self.layout_adv_acc)
        #
        # self.label_15 = QLabel(self.contents_tl)
        # self.label_15.setObjectName(u"label_15")
        #
        # self.horizontalLayout_50.addWidget(self.label_15)
        #
        # self.verticalLayout_12.addLayout(self.horizontalLayout_50)
        #
        # self.horizontalLayout_45.addLayout(self.verticalLayout_12)
        #
        # self.verticalLayout_11 = QVBoxLayout()
        # self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        # self.layout_base_matrix = QLabel(self.contents_tl)
        # self.layout_base_matrix.setObjectName(u"layout_base_matrix")
        # self.layout_base_matrix.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        # self.layout_base_matrix.setAlignment(Qt.AlignCenter)
        #
        # self.verticalLayout_11.addWidget(self.layout_base_matrix)
        #
        # self.label_tran10 = QLabel(self.contents_tl)
        # self.label_tran10.setObjectName(u"label_tran10")
        # self.label_tran10.setMaximumSize(QSize(16777215, 30))
        # self.label_tran10.setFrameShape(QFrame.NoFrame)
        # self.label_tran10.setFrameShadow(QFrame.Sunken)
        # self.label_tran10.setAlignment(Qt.AlignCenter)
        #
        # self.verticalLayout_11.addWidget(self.label_tran10)
        #
        # self.horizontalLayout_45.addLayout(self.verticalLayout_11)
        #
        # self.verticalLayout_7 = QVBoxLayout()
        # self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        # self.layout_adv_matrix = QLabel(self.contents_tl)
        # self.layout_adv_matrix.setObjectName(u"layout_adv_matrix")
        # self.layout_adv_matrix.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        # self.layout_adv_matrix.setAlignment(Qt.AlignCenter)
        #
        # self.verticalLayout_7.addWidget(self.layout_adv_matrix)
        #
        # self.label_tran11 = QLabel(self.contents_tl)
        # self.label_tran11.setObjectName(u"label_tran11")
        # self.label_tran11.setMaximumSize(QSize(16777215, 30))
        # self.label_tran11.setFrameShape(QFrame.NoFrame)
        # self.label_tran11.setFrameShadow(QFrame.Sunken)
        # self.label_tran11.setAlignment(Qt.AlignCenter)
        #
        # self.verticalLayout_7.addWidget(self.label_tran11)
        #
        # self.horizontalLayout_45.addLayout(self.verticalLayout_7)
        #
        # self.verticalLayout_5.addLayout(self.horizontalLayout_45)
        #
        # self.scroll_area_tl.setWidget(self.contents_tl)
        #
        # self.verticalLayout_3.addWidget(self.scroll_area_tl)
        #
        # self.pages.addWidget(self.page_TL)
        # 以上为page_TL代码-----------------

        # 创建信号显示页面
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"QFrame {\n""font-size: 16pt;\n""}")
        self.page_4_layout = QVBoxLayout(self.page_4)
        self.page_4_layout.setObjectName(u"page_4_layout")

        self.pages.addWidget(self.page_4)

        # 接下来如果我们要创建新的页面，就像上面的page3和page2一样，下面的东西可以不用动

        self.main_pages_layout.addWidget(self.pages)

        self.retranslateUi(MainPages)

        self.retranslateUi_page_IL(MainPages)

        self.pages.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainPages)

    def retranslateUi_page_IL(self, MainPages):
        self.page_IL_title_label.setText(u"电磁信号增量分类验证系统")
        # self.page_IL_description_label.setText(u"Here will be all the custom widgets, they will be added over time on this page.\n"
        #                                     "I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.")
        self.label_IL_data.setText(u"数据集：")
        self.label_IL_data1.setText(u"信噪比：")
        self.label_IL_data2.setText(u"旧类选择：")
        # self.label_IL_data2.setText(u"测试集比例")
        # self.label_IL_data3.setText(u"随机种子")
        # # self.label_IL_data4.setText(u"旧类别数")
        # self.label_IL_data5.setText(u"旧类别数")
        # self.label_IL_data6.setText(u"内存大小")
        # # self.label_IL_data7.setText(u"使用旧类数据?")
        # # self.label_IL_data7.setText(u"内存大小")
        # self.label_IL_data8.setText(u"新类别个数")
        # self.label_IL_data9.setText(u"每次新增类别数")
        #
        # self.label_old_oa.setText(u"旧类别OA")
        # self.label_new_oa.setText(u"新类别OA")
        # self.label_all_oa.setText(u"所有类别OA")

        self.label_old_class.setText(u"旧类别：")
        self.label_new_class.setText(u"新增类别：")
        self.label_matrix.setText("调制识别结果混淆矩阵图")
        # self.label_test_type.setText(u"测试数据类别：")
        self.label_task_size.setText(u"每次新增类别数：")
        self.label_pick_method.setText(u"样本筛选方法：")
        self.label_increment_test.setText(QCoreApplication.translate("MainPages",  # 优化 模型
                                                                   u"<html><head/><body><p><span style=\" font-weight:700;\">\u589e\u91cf\u6a21</span></p><p><span style=\" font-weight:700;\">\u578b\u6d4b\u8bd5</span></p></body></html>",
                                                                   None))

        self.label_true.setText(u"真实调制:")
        self.label_pred.setText(u"识别调制:")
        self.label_time.setText(u"耗时:")

        # self.label_old_acc.setText(u"旧类OA")
        # self.label_new_acc.setText(u"新类OA")
        # self.label_all_acc.setText(u"总体OA")

        self.label_data_pick.setText(QCoreApplication.translate("MainPages",  # 优化 模型
                                                                     u"<html><head/><body><p><span style=\" font-weight:700;\">\u6570\u636e</span></p><p><span style=\" font-weight:700;\">\u9009\u62e9</span></p></body></html>",
                                                                     None))



        self.comboBox_IL_data.setItemText(0, QCoreApplication.translate("MainPages", u"RML2016.04c", None))

        # for i, j in enumerate(range(-20, 20, 2)):
        #     self.comboBox_IL_data1.setItemText(i, QCoreApplication.translate("MainPages", u"{}".format(j), None))
        self.comboBox_IL_data1.setItemText(0, QCoreApplication.translate("MainPages", u"{}".format(12), None))

        # for i, j in enumerate(range(1, 6, 1)):
        #     self.comboBox_IL_data2.setItemText(i, QCoreApplication.translate("MainPages", u"{}".format(j / 10), None))


        # for i, j in enumerate(range(1, 11, 1)):
        #     self.comboBox_IL_data3.setItemText(i, QCoreApplication.translate("MainPages", u"{}".format(j), None))

        # for i, j in enumerate(range(5, 11, 1)):
        #     self.comboBox_IL_data4.setItemText(i, QCoreApplication.translate("MainPages", u"{}".format(j), None))

        # for i, j in enumerate(range(5, 12, 1)):
        #     self.comboBox_IL_data5.setItemText(i, QCoreApplication.translate("MainPages", u"{}".format(j), None))

        # for i, j in enumerate(range(0, 1200, 200)):
        #     self.comboBox_IL_data6.setItemText(i, QCoreApplication.translate("MainPages", u"{}".format(j), None))

        # for i, j in enumerate(range(1, 4, 1)):
        #     self.comboBox_IL_data9.setItemText(i, QCoreApplication.translate("MainPages", u"{}".format(j), None))


        # for i, j in enumerate(["所有类别", "旧类别", "新类别"]):
        #     self.comboBox_test_type.setItemText(i, QCoreApplication.translate("MainPages", u"{}".format(j), None))

        self.comboBox_class_type.setItemText(0, QCoreApplication.translate("MainPages", u"随机", None))
        for i, j, in enumerate(modName[0:]):
            self.comboBox_class_type.setItemText(i+1, QCoreApplication.translate("MainPages", u"{}".format(j.decode("utf-8")), None))

        for i, j, in enumerate(["NMI", "Random", "Prototype"]):
            self.comboBox_pick_method.setItemText(i, QCoreApplication.translate("MainPages", u"{}".format(j), None))

        for i, j in enumerate([1, 2]):
            self.comboBox_task_size.setItemText(i, QCoreApplication.translate("MainPages", u"{}".format(j), None))


    # setupUi
    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        # self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To PyOneDark GUI", None))
        # self.label.setText(u"Welcome To PyOneDark GUI")
        # self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        # self.description_label.setText(QCoreApplication.translate("MainPages",
        #                                                           u"Here will be all the custom widgets, they will be added over time on this page.\n"
        #                                                           "I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.",
        #                                                           None))
        # self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))

        # self.title_label_op.setText(QCoreApplication.translate("MainPages",                   # 面向电磁信号目标特征的网络模型优化
        #                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700;\">\u9762\u5411\u7535\u78c1\u4fe1\u53f7\u76ee\u6807\u7279\u5f81\u7684\u7f51\u7edc\u6a21\u578b\u4f18\u5316</span></p></body></html>",
        #                                                        None))
        self.title_label_op.setText(QCoreApplication.translate("MainPages",  # 电磁信号增量分类系统
                                                               u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700;\">\u7535\u78c1\u4fe1\u53f7\u589e\u91cf\u5206\u7c7b\u7cfb\u7edf</span></p></body></html>",
                                                               None))

        self.label_27.setText("")
        self.label_op_data.setText(QCoreApplication.translate("MainPages", u"\u6570\u636e\u96c6\uff1a", None))
        self.comboBox_op_data.setItemText(0, QCoreApplication.translate("MainPages", u"RML2016.04c", None))

        self.label_2.setText("")
        self.label_op_snr.setText(QCoreApplication.translate("MainPages", u"\u4fe1\u566a\u6bd4\uff1a", None))
        self.comboBox_op_snr.setItemText(0, QCoreApplication.translate("MainPages", u"6dB-SNR", None))

        self.label_3.setText("")
        self.label_op_sample.setText(
            QCoreApplication.translate("MainPages", u"\u6d4b\u8bd5\u6837\u672c\u9009\u62e9\uff1a", None))
        self.comboBox_op_sample.setItemText(0, QCoreApplication.translate("MainPages", u"1-4055", None))
        self.comboBox_op_sample.setItemText(1, QCoreApplication.translate("MainPages", u"1-500", None))
        self.comboBox_op_sample.setItemText(2, QCoreApplication.translate("MainPages", u"501-1000", None))
        self.comboBox_op_sample.setItemText(3, QCoreApplication.translate("MainPages", u"1001-1500", None))
        self.comboBox_op_sample.setItemText(4, QCoreApplication.translate("MainPages", u"1501-2000", None))
        self.comboBox_op_sample.setItemText(5, QCoreApplication.translate("MainPages", u"2001-2500", None))
        self.comboBox_op_sample.setItemText(6, QCoreApplication.translate("MainPages", u"2501-3000", None))
        self.comboBox_op_sample.setItemText(7, QCoreApplication.translate("MainPages", u"3001-3500", None))
        self.comboBox_op_sample.setItemText(8, QCoreApplication.translate("MainPages", u"3501-4000", None))
        self.comboBox_op_sample.setItemText(9, QCoreApplication.translate("MainPages", u"4001-4055", None))

        self.label_4.setText("")
        self.label_5.setText("")
        self.label_59.setText("")
        self.pic_op_data_1.setText("")
        self.pic_op_data_2.setText("")
        self.pic_op_data_3.setText("")
        self.pic_op_data_4.setText("")
        self.pic_op_data_5.setText("")
        self.pic_op_data_6.setText("")
        self.pic_op_data_7.setText("")
        self.pic_op_data_8.setText("")
        self.label_6.setText("")
        # self.label_op_base_model.setText(QCoreApplication.translate("MainPages",                                 # 未优化
        #                                                             u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">\u672a\u4f18\u5316</span></p><p align=\"center\"><span style=\" font-weight:700;\">\u6a21\u578b</span></p></body></html>",
        #                                                             None))
        self.label_op_base_model.setText(QCoreApplication.translate("MainPages",  # 混淆矩阵
                                                                    u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">\u6df7\u6dc6\u77e9\u9635</span></p><p align=\"center\"></p></body></html>",
                                                                    None))

        self.label_7.setText("")
        self.label_op_shot_base.setText(  # 每类样本数：
            QCoreApplication.translate("MainPages", u"\u6bcf\u7c7b\u6837\u672c\u6570\uff1a", None))
        self.comboBox_op_shot_base.setItemText(0, QCoreApplication.translate("MainPages", u"10-shot", None))
        self.comboBox_op_shot_base.setItemText(1, QCoreApplication.translate("MainPages", u"20-shot", None))
        self.comboBox_op_shot_base.setItemText(2, QCoreApplication.translate("MainPages", u"30-shot", None))
        self.comboBox_op_shot_base.setItemText(3, QCoreApplication.translate("MainPages", u"40-shot", None))
        self.comboBox_op_shot_base.setItemText(4, QCoreApplication.translate("MainPages", u"50-shot", None))
        self.comboBox_op_shot_base.setItemText(5, QCoreApplication.translate("MainPages", u"60-shot", None))
        self.comboBox_op_shot_base.setItemText(6, QCoreApplication.translate("MainPages", u"70-shot", None))
        self.comboBox_op_shot_base.setItemText(7, QCoreApplication.translate("MainPages", u"80-shot", None))
        self.comboBox_op_shot_base.setItemText(8, QCoreApplication.translate("MainPages", u"90-shot", None))
        self.comboBox_op_shot_base.setItemText(9, QCoreApplication.translate("MainPages", u"100-shot", None))

        self.label_10.setText("")
        self.label_9.setText("")
        self.label_op_adv_model.setText(QCoreApplication.translate("MainPages",  # 优化 模型
                                                                   u"<html><head/><body><p><span style=\" font-weight:700;\">\u4f18\u5316</span></p><p><span style=\" font-weight:700;\">\u6a21\u578b</span></p></body></html>",
                                                                   None))
        self.label_op_choice_method.setText(  # 优化方法
            QCoreApplication.translate("MainPages", u"\u4f18\u5316\u65b9\u6cd5\uff1a", None))
        self.comboBox_op_method.setItemText(0, QCoreApplication.translate("MainPages", u"Dropout", None))
        self.comboBox_op_method.setItemText(1, QCoreApplication.translate("MainPages", u"InstanceNrom", None))
        self.comboBox_op_method.setItemText(2, QCoreApplication.translate("MainPages", u"GroupNorm", None))

        # 下拉框条目
        self.label_op_shot_adv.setText(  # 每类样本数：
            QCoreApplication.translate("MainPages", u"\u6bcf\u7c7b\u6837\u672c\u6570\uff1a", None))
        self.comboBox_op_shot_adv.setItemText(0, QCoreApplication.translate("MainPages", u"10-shot", None))
        self.comboBox_op_shot_adv.setItemText(1, QCoreApplication.translate("MainPages", u"20-shot", None))
        self.comboBox_op_shot_adv.setItemText(2, QCoreApplication.translate("MainPages", u"30-shot", None))
        self.comboBox_op_shot_adv.setItemText(3, QCoreApplication.translate("MainPages", u"40-shot", None))
        self.comboBox_op_shot_adv.setItemText(4, QCoreApplication.translate("MainPages", u"50-shot", None))
        self.comboBox_op_shot_adv.setItemText(5, QCoreApplication.translate("MainPages", u"60-shot", None))
        self.comboBox_op_shot_adv.setItemText(6, QCoreApplication.translate("MainPages", u"70-shot", None))
        self.comboBox_op_shot_adv.setItemText(7, QCoreApplication.translate("MainPages", u"80-shot", None))
        self.comboBox_op_shot_adv.setItemText(8, QCoreApplication.translate("MainPages", u"90-shot", None))
        self.comboBox_op_shot_adv.setItemText(9, QCoreApplication.translate("MainPages", u"100-shot", None))

        # self.label_8.setText("")
        # self.pic_op_matrix1.setText("")
        # self.pic_op_matrix2.setText("")
        # self.title_label_op_2.setText(QCoreApplication.translate("MainPages",
        #                                                          u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:700;\">\u57fa\u4e8e\u9009\u62e9\u6027\u77e5\u8bc6\u8fc1\u79fb\u7684\u7535\u78c1\u4fe1\u53f7\u8bc6\u522b\u6280\u672f</span></p></body></html>",
        #                                                          None))
        # self.label_28.setText("")
        # self.label_op_data_2.setText(QCoreApplication.translate("MainPages",
        #                                                         u"<html><head/><body><p>\u9009\u62e9\u6027\u77e5\u8bc6\u8fc1\u79fb\u7b97\u6cd5\u6a21\u578b\u9009\u62e9\uff1a</p></body></html>",
        #                                                         None))
        # self.comboBox_tl_method.setItemText(0, QCoreApplication.translate("MainPages", u"Baseline", None))
        # self.comboBox_tl_method.setItemText(1, QCoreApplication.translate("MainPages", u"Co-Tuning", None))
        # self.comboBox_tl_method.setItemText(2, QCoreApplication.translate("MainPages", u"BSS", None))
        # self.comboBox_tl_method.setItemText(3, QCoreApplication.translate("MainPages", u"Stochnorm", None))
        # self.comboBox_tl_method.setItemText(4, QCoreApplication.translate("MainPages", u"BSS+Stochnorm", None))
        #
        # self.label_11.setText("")
        # self.label_op_snr_2.setText(QCoreApplication.translate("MainPages",
        #                                                        u"<html><head/><body><p>\u8c03\u5236\u4fe1\u53f7\u6570\u636e\u96c6\uff1a</p></body></html>",
        #                                                        None))
        # self.comboBox_tl_dataset.setItemText(0, QCoreApplication.translate("MainPages", u"RML2016.04c", None))
        #
        # self.label_12.setText("")
        # self.label_op_snr_3.setText(
        #     QCoreApplication.translate("MainPages", u"<html><head/><body><p>\u4fe1\u566a\u6bd4\uff1a</p></body></html>",
        #                                None))
        # self.comboBox_tl_snr.setItemText(0, QCoreApplication.translate("MainPages", u"6dB-SNR", None))
        #
        # self.label_14.setText("")
        # self.label_58.setText("")
        # self.label_tran4.setText(QCoreApplication.translate("MainPages",                                  # 源域调制信号类别：
        #                                                     u"<html><head/><body><p><span style=\" font-size:14pt;\">\u6e90\u57df\u8c03\u5236\u4fe1\u53f7\u7c7b\u522b\uff1a</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">8PSK</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:14pt;\">\u3001</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">BPSK</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:14pt;\">\u3001</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">CPFSK</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:14pt;\">\u3001</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">GFSK</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:14pt;\">\u3001</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">PAM4</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:14pt;\">\u3001</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">QAM16 </span></p></body></html>",
        #                                                     None))
        # self.pic_tl_source.setText("")
        # self.label_31.setText("")
        # self.label_tran5.setText(QCoreApplication.translate("MainPages",
        #                                                     u"<html><head/><body><p><span style=\" font-size:14pt;\">\u76ee\u6807\u57df\u8c03\u5236\u4fe1\u53f7\u7c7b\u522b\uff1a</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">QPSK</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:14pt;\">\u3001</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">AM-DSB</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:14pt;\">\u3001</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">AM-SSB</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:14pt;\">\u3001</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">QAM64</span><span style=\" font-family:'\u5b8b\u4f53'; font-size:14pt;\">\u3001</span><span style=\" font-family:'Times New Roman,serif'; font-size:14pt;\">WBFM</span></p></body></html>",
        #                                                     None))
        # self.pic_tl_target.setText("")
        # self.label_29.setText("")
        # self.label_tran6.setText(QCoreApplication.translate("MainPages",
        #                                                     u"<html><head/><body><p><span style=\" font-size:14pt;\">\u76ee\u6807\u57df\u8bad\u7ec3\u96c6\u6bcf\u7c7b\u6837\u672c\u6570\u91cf\uff1a</span></p></body></html>",
        #                                                     None))
        # self.comboBox_tl_shot.setItemText(0, QCoreApplication.translate("MainPages", u"5-shot", None))
        # self.comboBox_tl_shot.setItemText(1, QCoreApplication.translate("MainPages", u"10-shot", None))
        # self.comboBox_tl_shot.setItemText(2, QCoreApplication.translate("MainPages", u"15-shot", None))
        # self.comboBox_tl_shot.setItemText(3, QCoreApplication.translate("MainPages", u"20-shot", None))
        # self.comboBox_tl_shot.setItemText(4, QCoreApplication.translate("MainPages", u"25-shot", None))
        # self.comboBox_tl_shot.setItemText(5, QCoreApplication.translate("MainPages", u"30-shot", None))
        # self.comboBox_tl_shot.setItemText(6, QCoreApplication.translate("MainPages", u"35-shot", None))
        # self.comboBox_tl_shot.setItemText(7, QCoreApplication.translate("MainPages", u"40-shot", None))
        # self.comboBox_tl_shot.setItemText(8, QCoreApplication.translate("MainPages", u"45-shot", None))
        # self.comboBox_tl_shot.setItemText(9, QCoreApplication.translate("MainPages", u"50-shot", None))
        # self.comboBox_tl_shot.setItemText(10, QCoreApplication.translate("MainPages", u"55-shot", None))
        # self.comboBox_tl_shot.setItemText(11, QCoreApplication.translate("MainPages", u"60-shot", None))
        # self.comboBox_tl_shot.setItemText(12, QCoreApplication.translate("MainPages", u"65-shot", None))
        # self.comboBox_tl_shot.setItemText(13, QCoreApplication.translate("MainPages", u"70-shot", None))
        # self.comboBox_tl_shot.setItemText(14, QCoreApplication.translate("MainPages", u"75-shot", None))
        # self.comboBox_tl_shot.setItemText(15, QCoreApplication.translate("MainPages", u"80-shot", None))
        # self.comboBox_tl_shot.setItemText(16, QCoreApplication.translate("MainPages", u"85-shot", None))
        # self.comboBox_tl_shot.setItemText(17, QCoreApplication.translate("MainPages", u"90-shot", None))
        # self.comboBox_tl_shot.setItemText(18, QCoreApplication.translate("MainPages", u"95-shot", None))
        # self.comboBox_tl_shot.setItemText(19, QCoreApplication.translate("MainPages", u"100-shot", None))
        #
        # self.label_tran6_2.setText(QCoreApplication.translate("MainPages",
        #                                                       u"<html><head/><body><p><span style=\" font-size:14pt;\">\u6d4b\u8bd5\u96c6\u6837\u672c\u6570\u91cf\u9009\u62e9\uff1a</span></p></body></html>",
        #                                                       None))
        # self.comboBox_tl_samples.setItemText(0, QCoreApplication.translate("MainPages", u"1-1510", None))
        # self.comboBox_tl_samples.setItemText(1, QCoreApplication.translate("MainPages", u"1-500", None))
        # self.comboBox_tl_samples.setItemText(2, QCoreApplication.translate("MainPages", u"501-1000", None))
        # self.comboBox_tl_samples.setItemText(3, QCoreApplication.translate("MainPages", u"1001-1510", None))
        # self.comboBox_tl_samples.setItemText(4, QCoreApplication.translate("MainPages", u"1-200", None))
        # self.comboBox_tl_samples.setItemText(5, QCoreApplication.translate("MainPages", u"201-400", None))
        # self.comboBox_tl_samples.setItemText(6, QCoreApplication.translate("MainPages", u"401-600", None))
        # self.comboBox_tl_samples.setItemText(7, QCoreApplication.translate("MainPages", u"601-800", None))
        # self.comboBox_tl_samples.setItemText(8, QCoreApplication.translate("MainPages", u"801-1000", None))
        # self.comboBox_tl_samples.setItemText(9, QCoreApplication.translate("MainPages", u"1001-1200", None))
        # self.comboBox_tl_samples.setItemText(10, QCoreApplication.translate("MainPages", u"1201-1400", None))
        # self.comboBox_tl_samples.setItemText(11, QCoreApplication.translate("MainPages", u"1400-1510", None))
        #
        # self.label_20.setText("")
        # self.label_37.setText("")
        # self.label_57.setText("")
        # self.label_30.setText("")
        # self.label_tran7.setText(QCoreApplication.translate("MainPages",     # 电磁信号识别准确率：
        #                                                     u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">\u7535\u78c1\u4fe1\u53f7\u8bc6\u522b\u51c6\u786e\u7387\uff1a</span></p></body></html>",
        #                                                     None))
        # self.label_tran8.setText(QCoreApplication.translate("MainPages",
        #                                                     u"<html><head/><body><p><span style=\" font-size:14pt;\">\u76ee\u6807\u57df\u6837\u672c\u76f4\u63a5\u8bad\u7ec3\uff1a</span></p></body></html>",
        #                                                     None))
        # self.label_16.setText("")
        # self.label_13.setText("")
        # self.label_tran8_2.setText(QCoreApplication.translate("MainPages",
        #                                                       u"<html><head/><body><p><span style=\" font-size:14pt;\">\u7ecf\u9009\u62e9\u6027\u77e5\u8bc6\u8fc1\u79fb\u540e\uff1a</span></p></body></html>",
        #                                                       None))
        # self.label_17.setText("")
        # self.label_15.setText("")
        # self.layout_base_matrix.setText("")
        # self.label_tran10.setText(QCoreApplication.translate("MainPages",               # 目标域样本直接训练混淆矩阵
        #                                                      u"<html><head/><body><p><span style=\" font-size:14pt;\">\u76ee\u6807\u57df\u6837\u672c\u76f4\u63a5\u8bad\u7ec3\u6df7\u6dc6\u77e9\u9635</span></p></body></html>",
        #                                                      None))
        # self.layout_adv_matrix.setText("")
        # self.label_tran11.setText(QCoreApplication.translate("MainPages", # 选择性知识迁移训练混淆矩阵
        #                                                      u"<html><head/><body><p><span style=\" font-size:14pt;\">\u9009\u62e9\u6027\u77e5\u8bc6\u8fc1\u79fb\u8bad\u7ec3\u6df7\u6dc6\u77e9\u9635</span></p></body></html>",
        #                                                      None))

    # retranslateUi


class ComboCheckBox(QComboBox):
    def __init__(self, items):  # items==[str,str...]
        super(ComboCheckBox, self).__init__()
        self.items = items
        # self.items.insert(0, bytes("全部", "utf-8"))
        self.row_num = len(self.items)
        self.selectedrow_num = 0
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        self.qListWidget = QListWidget()

        # self.addQCheckBox(0)
        self.qCheckBox.append(QCheckBox())
        qItem = QListWidgetItem(self.qListWidget)
        self.qCheckBox[0].setText("全部")
        self.qListWidget.setItemWidget(qItem, self.qCheckBox[0])

        self.qCheckBox[0].stateChanged.connect(self.All)
        for i in range(1, self.row_num+1):
            self.addQCheckBox(i)
            self.qCheckBox[i].stateChanged.connect(self.show)
        self.setModel(self.qListWidget.model())
        self.setView(self.qListWidget)
        self.setLineEdit(self.qLineEdit)

    def addQCheckBox(self, i):

        self.qCheckBox.append(QCheckBox())
        qItem = QListWidgetItem(self.qListWidget)
        self.qCheckBox[i].setText(self.items[i-1].decode("utf-8"))
        self.qListWidget.setItemWidget(qItem, self.qCheckBox[i])

    def getCheckItems(self):
        checkedItems = []
        for i in range(1, self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                checkedItems.append(self.qCheckBox[i].text())
        self.selectedrow_num = len(checkedItems)
        return checkedItems

    def show(self):
        show = ''
        Outputlist = self.getCheckItems()
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()
        for i in Outputlist:
            show += i + ';'
        if self.selectedrow_num == 0:
            self.qCheckBox[0].setCheckState(Qt.Unchecked)
        elif self.selectedrow_num == self.row_num - 1:
            self.qCheckBox[0].setCheckState(Qt.Checked)
        else:
            self.qCheckBox[0].setCheckState(Qt.PartiallyChecked)
        # print(show)
        self.qLineEdit.setText(show)
        self.qLineEdit.setReadOnly(True)

    def All(self, state):
        if state == Qt.Checked:
            for i in range(1, self.row_num):
                self.qCheckBox[i].setChecked(True)
        elif state == Qt.PartiallyChecked:
            if self.selectedrow_num == 0:
                self.qCheckBox[0].setCheckState(Qt.Checked)
        elif state == Qt.Unchecked:
            self.clear()

    def clear(self):
        for i in range(self.row_num):
            self.qCheckBox[i].setChecked(False)