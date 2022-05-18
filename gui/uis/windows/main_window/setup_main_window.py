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
from gui.core.functions import Functions
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
# from . import UI_MainWindow
from .functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from .functions_main_window import MainFunctions
from .ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from .functions_main_window import *


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS 左边的导航栏的按钮
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Home",
            "btn_tooltip": "Home page",
            "show_top": True,
            "is_active": True
        },
        # {
        #     "btn_icon": "icon_widgets.svg",
        #     "btn_id": "btn_widgets",
        #     "btn_text": "Show Custom Widgets",
        #     "btn_tooltip": "Show custom widgets",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_add_user.svg",
        #     "btn_id": "btn_show_signal",
        #     "btn_text": "Show Signal",
        #     "btn_tooltip": "Show Signal",
        #     "show_top": True,
        #     "is_active": False
        # },
        {
            "btn_icon": "icon_send.svg",
            "btn_id": "btn_OP",
            "btn_text": "incremental learning",
            "btn_tooltip": "incremental learning",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_send.svg",
            "btn_id": "btn_IL",
            "btn_text": "incremental learning",
            "btn_tooltip": "incremental learning",
            "show_top": True,
            "is_active": False
        },
        # {
        #     "btn_icon": "icon_add_user.svg",
        #     "btn_id": "btn_TL",
        #     "btn_text": "TL",
        #     "btn_tooltip": "TL",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_add_user.svg",
        #     "btn_id": "btn_add_user",
        #     "btn_text": "Add Users",
        #     "btn_tooltip": "Add users",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_file.svg",
        #     "btn_id": "btn_new_file",
        #     "btn_text": "New File",
        #     "btn_tooltip": "Create new file",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_folder_open.svg",
        #     "btn_id": "btn_open_file",
        #     "btn_text": "Open File",
        #     "btn_tooltip": "Open file",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_save.svg",
        #     "btn_id": "btn_save",
        #     "btn_text": "Save File",
        #     "btn_tooltip": "Save file",
        #     "show_top": True,
        #     "is_active": False
        # },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_info",
            "btn_text": "Information",
            "btn_tooltip": "Open informations",
            "show_top": False,
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_settings",
            "btn_text": "Settings",
            "btn_tooltip": "Open settings",
            "show_top": False,
            "is_active": False
        }
    ]

    # ADD TITLE BAR MENUS 界面顶部的菜单按钮
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon": "icon_search.svg",
            "btn_id": "btn_search",
            "btn_tooltip": "Search",
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_top_settings",
            "btn_tooltip": "Top settings",
            "is_active": False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # QMainWindow 调用sender()方法获取到是可以发送信号的，当这个window中的按钮被点击后，它调用sender()判断发出信号的按钮是谁
    # 当某个按钮被点击后为了知道是哪个按钮被点击，
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() is not None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() is not None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() is not None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # 用传统参数设置主要的窗口
    # ///////////////////////////////////////////////////////////////
    # 这里的self指的是main函数中的类
    def setup_gui(self):
        # APP TITLE 应用名字
        # ///////////////////////////////////////////////////////////////
        # 主窗口的名字
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        # 这里的self是主窗口的类
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        # 这里的self值得是main函数中的类的成员函数，因为这里的self指的是main函数中的类，因此没毛病，第一个是
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////
        # 下面的这三个btn是左侧第二列的按钮项，就是点击设置后展开的那一列
        # BTN 1
        self.left_btn_1 = PyPushButton(
            text="Btn 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

        # BTN 2
        self.left_btn_2 = PyPushButton(
            text="Btn With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_2.setIcon(self.icon)
        self.left_btn_2.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        # BTN 3 - Default QPushButton
        self.left_btn_3 = QPushButton("Default QPushButton")
        self.left_btn_3.setMaximumHeight(40)
        self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

        # PAGES
        # ///////////////////////////////////////////////////////////////

        # PAGE 1 - ADD LOGO TO MAIN PAGE
        self.logo_svg = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # PAGE 2 第二页上面的控件
        # CIRCULAR PROGRESS 1 圆圈进度条
        self.circular_progress_1 = PyCircularProgress(
            value=80,   # 80%
            progress_color=self.themes["app_color"]["context_color"],  # 进度条颜色
            text_color=self.themes["app_color"]["text_title"],  # 文本颜色
            font_size=14,   # 字体大小
            bg_color=self.themes["app_color"]["dark_four"] # 背景颜色
        )
        # 设置该进度条的大小
        self.circular_progress_1.setFixedSize(200, 200)

        # CIRCULAR PROGRESS 2 第二个进度条
        self.circular_progress_2 = PyCircularProgress(
            value=45,
            progress_width=4,
            progress_color=self.themes["app_color"]["context_color"],
            text_color=self.themes["app_color"]["context_color"],
            font_size=14,
            bg_color=self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_2.setFixedSize(160, 160)

        # CIRCULAR PROGRESS 3  第三个进度条
        self.circular_progress_3 = PyCircularProgress(
            value=75,
            progress_width=2,
            progress_color=self.themes["app_color"]["pink"],
            text_color=self.themes["app_color"]["white"],
            font_size=14,
            bg_color=self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_3.setFixedSize(140, 140)

        # PY SLIDER 1 滑动条
        self.vertical_slider_1 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_1.setMinimumHeight(100)

        # PY SLIDER 2 滑动条
        self.vertical_slider_2 = PySlider(
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_2.setMinimumHeight(100)

        # PY SLIDER 3 滑动条
        self.vertical_slider_3 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_3.setOrientation(Qt.Horizontal)
        self.vertical_slider_3.setMaximumWidth(200)

        # PY SLIDER 4 滑动条
        self.vertical_slider_4 = PySlider(
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_4.setOrientation(Qt.Horizontal)
        self.vertical_slider_4.setMaximumWidth(200)

        # ICON BUTTON 1
        self.icon_button_1 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_heart.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Icon button - Heart",  # 鼠标指到button上显示的文字
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )

        # ICON BUTTON 2
        self.icon_button_2 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_add_user.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="BTN with tooltip",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )

        # ICON BUTTON 3
        self.icon_button_3 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_add_user.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="BTN actived! (is_actived = True)",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=True
        )

        # PUSH BUTTON 1 Button Without Icon
        self.push_button_1 = PyPushButton(
            text="Button Without Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_1.setMinimumHeight(40)

        # PUSH BUTTON 2 Button With Icon
        self.push_button_2 = PyPushButton(
            text="Button With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_2 = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.push_button_2.setMinimumHeight(40)
        self.push_button_2.setIcon(self.icon_2)

        # PY LINE EDIT 开关按钮
        self.line_edit = PyLineEdit(
            text="",
            place_holder_text="Place holder text",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit.setMinimumHeight(30)

        # TOGGLE BUTTON
        self.toggle_button = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )

        # TABLE WIDGETS 表格控件
        self.table_widget = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(3) # 表格列数
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header 三个列的名字
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("NAME")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("NICK")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("PASS")

        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)

        # 造几行数据
        for x in range(10):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number)  # Insert row 插入一行
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(str("Wanderson")))  # Add name
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(str("vfx_on_fire_" + str(x))))  # Add nick
            self.pass_text = QTableWidgetItem()
            self.pass_text.setTextAlignment(Qt.AlignCenter)
            self.pass_text.setText("12345" + str(x))
            self.table_widget.setItem(row_number, 2, self.pass_text)  # Add pass
            self.table_widget.setRowHeight(row_number, 22)

        # ADD WIDGETS
        # self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_1)
        # self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_2)
        # self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_3)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_1)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_2)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_3)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_4)
        # self.ui.load_pages.row_3_layout.addWidget(self.icon_button_1)
        # self.ui.load_pages.row_3_layout.addWidget(self.icon_button_2)
        # self.ui.load_pages.row_3_layout.addWidget(self.icon_button_3)
        # self.ui.load_pages.row_3_layout.addWidget(self.push_button_1)
        # self.ui.load_pages.row_3_layout.addWidget(self.push_button_2)
        # self.ui.load_pages.row_3_layout.addWidget(self.toggle_button)
        # self.ui.load_pages.row_4_layout.addWidget(self.line_edit)
        # self.ui.load_pages.row_5_layout.addWidget(self.table_widget)
        # ---------------------------------------------------------------------------------------------------

        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////
        # BTN 1
        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_2
        ))
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_1
        ))
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)

        # 新添加的代码------------------------------------------------------------------------------------------------------------------------------------------
        font_style = u'''font: 12pt;
                                 border: none;
                                 padding-left: 10px;
                                 padding-right: 5px;
                                 color: #f8f8f2;
                                 border-radius: 8;
                                 background-color: #282a36;'''
        #
        # self.pushButton_op_data = PyPushButton(
        #     text="选择",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["red"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # self.icon = QIcon(Functions.set_svg_icon("icon_save.svg"))
        # self.pushButton_op_data.setIcon(self.icon)
        # self.pushButton_op_data.setMaximumHeight(40)
        # self.pushButton_op_data.setMinimumWidth(100)
        # self.ui.load_pages.layout_op_data_open.addWidget(self.pushButton_op_data)
        #
        # self.pushButton_op_data.clicked.connect(
        #     lambda: self.pages_btn_clicked("increment", "pushButton_increment_data"))
        #
        # # page_IL setup
        # self.push_button_loadData = PyPushButton(
        #     text="加载数据",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # self.push_button_loadData.setStyleSheet(font_style)
        # self.push_button_loadData.setMinimumHeight(40)
        # self.push_button_loadData.setMinimumWidth(100)
        # self.ui.load_pages.page_IL_layout_loadData.addWidget(self.push_button_loadData)
        # self.push_button_loadData.clicked.connect(lambda: self.pages_btn_clicked("increment", "push_button_loadData"))
        #
        # # 预训练按钮
        # self.push_button_pretrain = PyPushButton(
        #     text="预训练",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # self.push_button_pretrain.setStyleSheet(font_style)
        # self.push_button_pretrain.setMinimumHeight(40)
        # self.push_button_pretrain.setMinimumWidth(100)
        # self.ui.load_pages.page_IL_layout_pretrain.addWidget(self.push_button_pretrain)
        # self.push_button_pretrain.clicked.connect(
        #     lambda: self.pages_btn_clicked("increment", "push_button_pretrain"))
        #
        #
        # self.ui.load_pages.comboBox_IL_data5.currentIndexChanged.connect(lambda: self.pages_btn_clicked("increment", "choose_old_class"))

        # self.isUsed_oldData_checkbox = PyToggle(
        #     width=60,
        #     bg_color=self.themes["app_color"]["dark_two"],
        #     circle_color=self.themes["app_color"]["icon_color"],
        #     active_color=self.themes["app_color"]["context_color"]
        # )
        # self.ui.load_pages.page_IL_layout_checkbox.addWidget(self.isUsed_oldData_checkbox)
        # self.isUsed_oldData_checkbox.stateChanged.connect(lambda: self.pages_btn_clicked("increment", "push_button_isUsed_oldData"))

        # self.line_edit_oldData_number = PyLineEdit(
        #     text="",
        #     place_holder_text="请输入旧类样本个数...",
        #     radius=2,
        #     border_size=1,
        #     color=self.themes["app_color"]["text_foreground"],
        #     selection_color=self.themes["app_color"]["white"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_active=self.themes["app_color"]["dark_three"],
        #     context_color=self.themes["app_color"]["context_color"]
        # )
        # self.line_edit_oldData_number.setEnabled(False)
        # self.line_edit_oldData_number.setMinimumHeight(40)
        # self.line_edit_oldData_number.setMaximumSize(QSize(200, 40))
        # self.ui.load_pages.page_IL_layout_lineedit.addWidget(self.line_edit_oldData_number)

        # self.line_edit_new_class = PyLineEdit(
        #     text="6",
        #     radius=2,
        #     border_size=1,
        #     color=self.themes["app_color"]["text_foreground"],
        #     selection_color=self.themes["app_color"]["white"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_active=self.themes["app_color"]["dark_three"],
        #     context_color=self.themes["app_color"]["context_color"]
        # )
        #
        #
        # self.line_edit_new_class.setStyleSheet(font_style)
        # # new_class_font = QFont()
        # # new_class_font.setPointSize(36)
        # # self.line_edit_new_class.setFont(new_class_font)
        # self.line_edit_new_class.setEnabled(False)
        # self.line_edit_new_class.setMinimumHeight(40)
        # self.line_edit_new_class.setMinimumWidth(100)
        # self.line_edit_new_class.setMaximumSize(QSize(200, 40))
        # self.ui.load_pages.page_IL_layout_new_class.addWidget(self.line_edit_new_class)
        #
        #
        # # 增量训练按钮
        # self.push_button_increment_train = PyPushButton(
        #     text="增量训练",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # # style = self.push_button_increment_train.styleSheet()
        # # print(style)
        # self.push_button_increment_train.setStyleSheet(font_style)
        # self.push_button_increment_train.setMinimumHeight(40)
        # self.push_button_increment_train.setMinimumWidth(100)
        # self.ui.load_pages.page_IL_layout_increment_train.addWidget(self.push_button_increment_train)
        # self.push_button_increment_train.clicked.connect(
        #     lambda: self.pages_btn_clicked("increment", "push_button_increment_train"))
        #
        # # 预训练acc展示
        # self.circular_progress_pretrain_acc = PyCircularProgress(
        #     value=0,  # 80%
        #     progress_color=self.themes["app_color"]["context_color"],  # 进度条颜色
        #     text_color=self.themes["app_color"]["text_title"],  # 文本颜色
        #     font_size=14,  # 字体大小
        #     bg_color=self.themes["app_color"]["dark_four"]  # 背景颜色
        # )
        # # 设置该进度条的大小
        # self.circular_progress_pretrain_acc.setFixedSize(200, 200)
        # self.ui.load_pages.pretrain_acc_layout.addWidget(self.circular_progress_pretrain_acc)
        #
        # # 增量训练acc展示
        # self.circular_progress_increment_train_acc = PyCircularProgress(
        #     value=0,  # 80%
        #     progress_color=self.themes["app_color"]["context_color"],  # 进度条颜色
        #     text_color=self.themes["app_color"]["text_title"],  # 文本颜色
        #     font_size=14,  # 字体大小
        #     bg_color=self.themes["app_color"]["dark_four"]  # 背景颜色
        # )
        # # 设置该进度条的大小
        # self.circular_progress_increment_train_acc.setFixedSize(200, 200)
        # self.ui.load_pages.increment_train_acc_layout.addWidget(self.circular_progress_increment_train_acc)
        #
        #
        # # 增量测试按钮
        # self.push_button_test = PyPushButton(
        #     text="测试",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # # style = self.push_button_increment_train.styleSheet()
        # # print(style)
        # self.push_button_test.setStyleSheet(font_style)
        # self.push_button_test.setMinimumHeight(40)
        # self.push_button_test.setMinimumWidth(100)
        # self.ui.load_pages.page_IL_layout_test.addWidget(self.push_button_test)
        # self.push_button_test.clicked.connect(
        #     lambda: self.pages_btn_clicked("increment", "push_button_test"))
        #
        #
        # self.circular_progress_old_acc = PyCircularProgress(
        #     value=0,  # 80%
        #     progress_color=self.themes["app_color"]["context_color"],  # 进度条颜色
        #     text_color=self.themes["app_color"]["text_title"],  # 文本颜色
        #     font_size=14,  # 字体大小
        #     bg_color=self.themes["app_color"]["dark_four"]  # 背景颜色
        # )
        # self.circular_progress_new_acc = PyCircularProgress(
        #     value=0,  # 80%
        #     progress_color=self.themes["app_color"]["context_color"],  # 进度条颜色
        #     text_color=self.themes["app_color"]["text_title"],  # 文本颜色
        #     font_size=14,  # 字体大小
        #     bg_color=self.themes["app_color"]["dark_four"]  # 背景颜色
        # )
        # self.circular_progress_all_acc = PyCircularProgress(
        #     value=0,  # 80%
        #     progress_color=self.themes["app_color"]["context_color"],  # 进度条颜色
        #     text_color=self.themes["app_color"]["text_title"],  # 文本颜色
        #     font_size=14,  # 字体大小
        #     bg_color=self.themes["app_color"]["dark_four"]  # 背景颜色
        # )
        # # 设置该进度条的大小
        # self.circular_progress_old_acc.setFixedSize(150, 150)
        # # self.circular_progress_old_acc.setMinimumSize(QSize(100, 100))
        # # self.circular_progress_old_acc.setMaximumSize(QSize(200, 200))
        # self.ui.load_pages.row_6_1_layout.addWidget(self.circular_progress_old_acc)
        # self.circular_progress_new_acc.setFixedSize(150, 150)
        # # self.circular_progress_new_acc.setMinimumSize(QSize(100, 100))
        # # self.circular_progress_new_acc.setMaximumSize(QSize(200, 200))
        # self.ui.load_pages.row_6_2_layout.addWidget(self.circular_progress_new_acc)
        # self.circular_progress_all_acc.setFixedSize(150, 150)
        # # self.circular_progress_all_acc.setMinimumSize(QSize(100, 100))
        # # self.circular_progress_all_acc.setMaximumSize(QSize(200, 200))
        # self.ui.load_pages.row_6_3_layout.addWidget(self.circular_progress_all_acc)

        # # 测试按钮
        # push_button_test = PyPushButton(
        #     text="训练",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # push_button_test.setMinimumHeight(40)
        # push_button_test.setMinimumWidth(100)
        # self.ui.load_pages.page_IL_layout_test.addWidget(self.push_button_test)


        # 新的布局页面========================================================================================================================
        self.push_button_loadData = PyPushButton(
            text="可视化",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_loadData.setStyleSheet(font_style)
        self.push_button_loadData.setMinimumHeight(40)
        self.push_button_loadData.setMinimumWidth(100)
        self.push_button_loadData.setMaximumWidth(200)
        self.ui.load_pages.page_IL_layout_loadData.addWidget(self.push_button_loadData)
        self.push_button_loadData.clicked.connect(lambda: self.increment_pages_btn_clicked("increment", "push_button_plot"))

        # self.circular_progress_all_acc = PyCircularProgress(
        #     value=00.00,  # 80%
        #     progress_color=self.themes["app_color"]["context_color"],  # 进度条颜色
        #     text_color=self.themes["app_color"]["text_title"],  # 文本颜色
        #     font_size=26,  # 字体大小
        #     bg_color=self.themes["app_color"]["dark_four"]  # 背景颜色
        # )
        # self.circular_progress_all_acc.setFixedSize(200, 200)
        # self.ui.load_pages.acc_progress_layout.addWidget(self.circular_progress_all_acc)

        self.push_button_test = PyPushButton(
            text="测试准确率",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_test.setStyleSheet(font_style)
        self.push_button_test.setMinimumHeight(40)
        self.push_button_test.setMinimumWidth(100)
        self.push_button_test.setMaximumWidth(200)
        self.ui.load_pages.test_acc_layout.addWidget(self.push_button_test)
        self.push_button_test.clicked.connect(lambda: self.increment_pages_btn_clicked("increment", "push_button_test"))


        self.push_button_next_sample = PyPushButton(
            text="下一个样本",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_next_sample.setStyleSheet(font_style)
        self.push_button_next_sample.setMinimumHeight(40)
        self.push_button_next_sample.setMinimumWidth(100)
        self.push_button_next_sample.setMaximumWidth(200)
        self.ui.load_pages.next_sample_layout.addWidget(self.push_button_next_sample)
        self.push_button_next_sample.clicked.connect(lambda: self.increment_pages_btn_clicked("increment", "push_button_next_sample"))

        self.progress_old_acc = PyCircularProgress(
            value=00.00,  # 80%
            progress_color=self.themes["app_color"]["context_color"],  # 进度条颜色
            text_color=self.themes["app_color"]["text_title"],  # 文本颜色
            font_size=26,  # 字体大小
            bg_color=self.themes["app_color"]["dark_four"]  # 背景颜色
        )
        self.progress_old_acc.setFixedSize(200, 200)
        self.ui.load_pages.old_acc_progress.addWidget(self.progress_old_acc)

        self.progress_new_acc = PyCircularProgress(
            value=00.00,  # 80%
            progress_color=self.themes["app_color"]["context_color"],  # 进度条颜色
            text_color=self.themes["app_color"]["text_title"],  # 文本颜色
            font_size=26,  # 字体大小
            bg_color=self.themes["app_color"]["dark_four"]  # 背景颜色
        )
        self.progress_new_acc.setFixedSize(200, 200)
        self.ui.load_pages.new_acc_progress.addWidget(self.progress_new_acc)

        self.progress_all_acc = PyCircularProgress(
            value=00.00,  # 80%
            progress_color=self.themes["app_color"]["context_color"],  # 进度条颜色
            text_color=self.themes["app_color"]["text_title"],  # 文本颜色
            font_size=26,  # 字体大小
            bg_color=self.themes["app_color"]["dark_four"]  # 背景颜色
        )
        self.progress_all_acc.setFixedSize(200, 200)
        self.ui.load_pages.all_acc_progress.addWidget(self.progress_all_acc)




    def setup_page_IL(self):
        pass

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)
