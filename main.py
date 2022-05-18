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

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import cv2

from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
from app.inference_UI import *
from app.train import IncrementTrain, Pretrain
from app.evaluate import EvalThread
from config import CurrentConfig
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"


# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        # 这里设置ui的时候把父类传进去了
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        # 这里也把父类传进去了
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()
        self.current_config = CurrentConfig()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # 在该函数中可以添加按钮的点击事件
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active     注释掉以下两行
        # top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        # top_settings.set_active(False)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////

        # HOME BTN 点击左侧按钮事件
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1 加载该按钮对应的主页面
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # WIDGETS BTN
        # if btn.objectName() == "btn_widgets":
        #     # Select Menu
        #     self.ui.left_menu.select_only_one(btn.objectName())
        #
        #     # Load Page 2
        #     MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # if btn.objectName() == "btn_show_signal":
        #     self.ui.left_menu.select_only_one(btn.objectName())
        #     MainFunctions.set_page(self, self.ui.load_pages.page_4)

        # 增量展示界面
        if btn.objectName() == "btn_OP":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_OP)

        if btn.objectName() == "btn_IL":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_IL)

        # if btn.objectName() == "btn_TL":
        #     self.ui.left_menu.select_only_one(btn.objectName())
        #
        #     size = max(self.ui.load_pages.pic_tl_source.width(), self.ui.load_pages.pic_tl_source.height())
        #     source_img = cv2.imread("E:/workspace/Pycharm_workspace/PyOneDark_Signal_GUI/gui/images/app_images/transfer_source.png")
        #     print("source_img:", source_img)
        #     target_img = cv2.imread("E:/workspace/Pycharm_workspace/PyOneDark_Signal_GUI/gui/images/app_images/transfer_target.png")
        #     # img_source = cv2QPix(source_img, 0).scaled(size, int(size / 6))
        #     img_source = cv2QPix(source_img, 0)
        #     # img_target = cv2QPix(target_img, 0).scaled(size, int(size / 6))
        #     img_target = cv2QPix(target_img, 0)
        #     self.ui.load_pages.pic_tl_source.setPixmap(img_source)
        #     self.ui.load_pages.pic_tl_target.setPixmap(img_target)
        #     MainFunctions.set_page(self, self.ui.load_pages.page_TL)

        # LOAD USER PAGE
        if btn.objectName() == "btn_add_user":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3 
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

        # BOTTOM INFORMATION
        if btn.objectName() == "btn_info":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="Info tab",
                    icon_path=Functions.set_svg_icon("icon_info.svg")
                )

        # SETTINGS LEFT
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////

        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active 点击顶部导航栏的设置按钮后 如果右边栏不显示， 那么弹出右边的栏， 并且把该设置按钮激活为粉色
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:  # 如果右边栏已经显示，那么点击后应该收回
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn  点击了顶部的设置按钮弹出右边导航后就要收回左边的第二个菜单栏
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)  # 左右的设置按钮转为未激活状态

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    def increment_pages_btn_clicked(self, menu, btn_name):
        if menu == "increment":
            dataset = self.ui.load_pages.comboBox_IL_data.currentText()
            snr = int(self.ui.load_pages.comboBox_IL_data1.currentText())
            old_class = self.ui.load_pages.comboBox_IL_data2.currentText()

            old_class_list = old_class.split(";")[:-1]
            for i in range(len(old_class_list)):
                old_class_list[i] = bytes(old_class_list[i], "utf-8")
            new_class_list = []
            for i in modName:
                k = 0
                for j in old_class_list:
                    if i == j:
                        continue
                    else:
                        k = k + 1
                if k == len(old_class_list):
                    new_class_list.append(i)

            pick_method = self.ui.load_pages.comboBox_pick_method.currentText()
            task_size = self.ui.load_pages.comboBox_task_size.currentText()

            # {随机，具体类别}
            class_type = self.ui.load_pages.comboBox_class_type.currentText()

            print(dataset)
            print(snr)
            print(pick_method)
            print(task_size)
            print(class_type)

            if btn_name == "push_button_plot":


                # print(old_class_list)
                # print(new_class_list)
                #
                image_old, image_new = showDataset_(
                    snr=snr,
                    old_class=old_class_list,
                    new_class=new_class_list,
                    dataset=dataset
                )

                size = self.ui.load_pages.pic_old_class.size()
                old_img_path = cv2.imread("./gui/images/app_images/image_old.png")
                new_img_path = cv2.imread("./gui/images/app_images/image_new.png")
                old_img_path = cv2QPix(old_img_path).scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                new_img_path = cv2QPix(new_img_path).scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                print(type(old_img_path))
                self.ui.load_pages.pic_old_class.setPixmap(old_img_path)
                self.ui.load_pages.pic_new_class.setPixmap(new_img_path)

            if btn_name == "push_button_test":
                old_oa, new_oa, all_oa = inference(snr, pick_method, task_size, old_class_list, dataset)
                old_oa = float("%.2f" % old_oa)
                new_oa = float("%.2f" % new_oa)
                all_oa = float("%.2f" % all_oa)
                self.progress_old_acc.set_value(old_oa)
                self.progress_new_acc.set_value(new_oa)
                self.progress_all_acc.set_value(all_oa)
                matrix = cv2.imread('./gui/images/app_images/confusion_matrix.jpg')
                size = self.ui.load_pages.pic_matrix.size()
                old_img_path = cv2QPix(matrix).scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.ui.load_pages.pic_matrix.setPixmap(old_img_path)

            if btn_name == "push_button_next_sample":
                true, pred, consume_time = next_sample(snr, task_size, pick_method, class_type, old_class_list, dataset)
                consume_time = float("%.5f" % consume_time)
                self.ui.load_pages.label_true_value.setText("{}".format(true))
                self.ui.load_pages.label_pred_value.setText("{}".format(pred))
                self.ui.load_pages.label_time_value.setText("{}".format(consume_time))

                signal_sample = cv2.imread('./gui/images/app_images/signal_sample.jpg')
                size = self.ui.load_pages.pic_sample.size()
                old_img_path = cv2QPix(signal_sample).scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.ui.load_pages.pic_sample.setPixmap(old_img_path)



    # 定义内容页面中的按钮事件
    def pages_btn_clicked(self, menu, btn_name):
        # 像我们的增量系统只有一个menu，只需要实现不同的button点击事件，首要的就是加载数据
        if menu == "increment":
            pretrain_thread = Pretrain(self.current_config.snr, self.current_config.old_class,
                                       self.current_config.memory_size, dataset=self.current_config.dataset)

            increment_thread = IncrementTrain(self.current_config.snr, self.current_config.memory_size, self.current_config.new_class, self.current_config.task_size, self.current_config.dataset)
            eval_thread = EvalThread(self.current_config.snr, self.current_config.new_class, self.current_config.dataset)

            if btn_name == "push_button_loadData":
                self.current_config.dataset = self.ui.load_pages.comboBox_IL_data.currentText()
                self.current_config.snr = self.ui.load_pages.comboBox_IL_data1.currentText()
                self.current_config.test_percent = float(self.ui.load_pages.comboBox_IL_data2.currentText())
                self.current_config.random_seed = int(self.ui.load_pages.comboBox_IL_data3.currentText())
                # dataset = self.ui.load_pages.comboBox_IL_data.currentText()
                # snr = self.ui.load_pages.comboBox_IL_data1.currentText()
                # test_percent = float(self.ui.load_pages.comboBox_IL_data2.currentText())
                # random_seed = int(self.ui.load_pages.comboBox_IL_data3.currentText())

                imgs = showDataset(
                    test_percent=self.current_config.test_percent,
                    snr=self.current_config.snr,
                    random_seed=self.current_config.random_seed,
                    img_num=8,
                    dataset=self.current_config.dataset
                )
                for idx, img in enumerate(imgs):
                    # width = eval(f"self.ui.load_pages.pic_op_data_{idx+1}.width()")
                    # height = eval(f"self.ui.load_pages.pic_op_data_{idx+1}.height()")
                    pic_pos = eval(f"self.ui.load_pages.pic_IL_data_{idx + 1}.setPixmap")
                    width = self.ui.load_pages.pic_IL_data_1.width()
                    height = self.ui.load_pages.pic_IL_data_1.height()
                    img = cv2QPix(img, 0).scaled(width, height)
                    # img = cv2QPix(img, 0)
                    pic_pos(img)
                    cv2.waitKey(100)

            if btn_name == "push_button_pretrain":
                # 开始预训练 并保存模型 返回训练准确率
                # snr = self.ui.load_pages.comboBox_IL_data1.currentText()
                self.current_config.old_class = int(self.ui.load_pages.comboBox_IL_data5.currentText())
                self.current_config.memory_size = int(self.ui.load_pages.comboBox_IL_data6.currentText())
                # acc = pretrain(snr, old_class_num, memory_size, dataset="RML2016.04c")
                pretrain_thread.old_class_num = self.current_config.old_class
                pretrain_thread.memory_size = self.current_config.memory_size
                self.push_button_pretrain.setEnabled(False)
                self.push_button_pretrain.setText(u"正在训练...")
                # pretrain_thread = Pretrain(self.current_config.snr, self.current_config.old_class, self.current_config.memory_size, dataset="RML2016.04c")

                self.timer = QTimer()
                self.timer.timeout.connect(lambda: self.listen_pretrain_thread(pretrain_thread))
                self.timer.start(1000)
                pretrain_thread.start()


            if btn_name == "push_button_increment_train":
                # 开始增量训练 并保存模型 返回训练准确率
                # 新建一个当前参数的类，点击按钮后更新参数
                self.current_config.snr = self.ui.load_pages.comboBox_IL_data1.currentText()
                self.current_config.new_class = int(self.line_edit_new_class.text())
                self.current_config.task_size = int(self.ui.load_pages.comboBox_IL_data9.currentText())
                increment_thread.snr = self.current_config.snr
                increment_thread.new_class = self.current_config.new_class
                increment_thread.task_size = self.current_config.task_size
                self.push_button_increment_train.setEnabled(False)
                self.push_button_increment_train.setText(u"正在训练...")
                self.timer = QTimer()
                self.timer.timeout.connect(lambda: self.listen_increment_thread(increment_thread))
                self.timer.start(1000)
                increment_thread.start()


                # self.circular_progress_pretrain_acc.setVisible(True)
                # self.circular_progress_pretrain_acc.set_value(99)
                # self.circular_progress_increment_train_acc.setVisible(False)
                # self.circular_progress_increment_train_acc.set_value(59)
                # E:/workspace/Pycharm_workspace/PyOneDark_Signal_GUI/gui/images/app_images/confusion_matrix.jpg
                # img = cv2.imread("E:/workspace/Pycharm_workspace/PyOneDark_Signal_GUI/gui/images/app_images/confusion_matrix.jpg")
                # img = cv2.imread("./gui/images/app_images/confusion_matrix.jpg")
                # img = cv2QPix(img)
                # self.ui.load_pages.matrix_label.setPixmap(img)
                # self.ui.load_pages.matrix_label.setScaledContents(True)
                # fig2data()

            if btn_name == "choose_old_class":
                old_class = int(self.ui.load_pages.comboBox_IL_data5.currentText())
                self.line_edit_new_class.setText(str(11 - old_class))


            if btn_name == "push_button_test":
                self.timer = QTimer()
                self.timer.timeout.connect(lambda: self.listen_eval_thread(eval_thread))
                self.timer.start(1000)
                eval_thread.start()

            if btn_name == "pushButton_increment_train":
                pass

    def listen_pretrain_thread(self, pretrain_thread):
        print("开始轮询。。。")
        if pretrain_thread.is_finished:
            self.timer.stop()
            self.push_button_pretrain.setEnabled(True)
            self.push_button_pretrain.setText(u"预训练")
            acc = float("%.2f" % pretrain_thread.result)
            self.circular_progress_pretrain_acc.set_value(acc)

    def listen_increment_thread(self, increment_thread):
        print("开始轮询....")
        if increment_thread.is_finished:
            self.timer.stop()
            self.push_button_increment_train.setEnabled(True)
            self.push_button_increment_train.setText(u"增量训练")
            acc = float("%.2f" % increment_thread.result)
            self.circular_progress_increment_train_acc.set_value(acc)

    def listen_eval_thread(self, eval_thread):
        print("开始轮询")
        if eval_thread.is_finished:
            self.timer.stop()
            self.push_button_test.setEnabled(True)
            self.push_button_test.setText(u"测试")
            acc_list, image = eval_thread.result
            old_oa = float("%.2f" % acc_list[0])
            new_oa = float("%.2f" % acc_list[1])
            all_oa = float("%.2f" % acc_list[2])
            self.circular_progress_old_acc.set_value(old_oa)
            self.circular_progress_new_acc.set_value(new_oa)
            self.circular_progress_all_acc.set_value(all_oa)
            img = cv2QPix(image, 0)
            self.ui.load_pages.matrix_label.setPixmap(img)
            self.ui.load_pages.matrix_label.setScaledContents(True)



    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # 松开按钮事件
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        parent_width = self.width()-100
        parent_height = self.height()
        # print(parent_width, parent_height)
        size = self.ui.load_pages.pic_old_class.size()
        # print(size)
        # print(self.ui.load_pages.pic_old_class.pixmap().size())
        # print(self.ui.load_pages.pic_old_class.pixmap())
        self.ui.load_pages.pic_old_class.resize(size)
        if self.ui.load_pages.pic_old_class.pixmap().isNull() == False:
            old_img_path = cv2.imread("./gui/images/app_images/image_old.png")
            new_img_path = cv2.imread("./gui/images/app_images/image_new.png")
            old_img_path = cv2QPix(old_img_path).scaled(QSize(parent_width/2-20, parent_height/4-5), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            new_img_path = cv2QPix(new_img_path).scaled(QSize(parent_width/2-20, parent_height/4-5), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # img = cv2QPix(img, 0)
            print(type(old_img_path))
            self.ui.load_pages.pic_old_class.setPixmap(old_img_path)
            self.ui.load_pages.pic_new_class.setPixmap(new_img_path)
        self.ui.load_pages.pic_old_class.resize(QSize(parent_width/2, parent_height/4))
        self.ui.load_pages.pic_new_class.resize(QSize(parent_width/2, parent_height/4))
        SetupMainWindow.resize_grips(self)

        matrix_size = self.ui.load_pages.pic_matrix.size()
        if self.ui.load_pages.pic_matrix.pixmap().isNull() == False:
            matrix = cv2.imread('./gui/images/app_images/confusion_matrix.jpg')
            size = self.ui.load_pages.pic_matrix.size()
            old_img_path = cv2QPix(matrix).scaled(QSize(parent_width/2-120, parent_width/2-120), Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.ui.load_pages.pic_matrix.setPixmap(old_img_path)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        # self.dragPos = event.globalPosition()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
