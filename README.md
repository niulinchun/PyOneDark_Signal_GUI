# PyOneDark_Signal_GUI
An incremental recognition system of electromagnetic signal

main窗口

# 在ui_main_pages.py中添加主页面中每个页面的Frame划分
# ui_main.py 是把整个窗口分割为左菜单、列、内容、右列、下几个Frame，但是并没有给这些Frame中添加控件
# setup_main_window.py 是把具体的控件添加到划分好的Frame中，比如ui_main.py和ui_main_pages.py中的Frame中添加按钮，然后添加信号槽
# (菜单按钮，还有导航按钮，列按钮) 添加到对应的Frame中，并且连接了对应的槽



先set_ui
    左边菜单 QFrame（left_menu_frame）
    然后左边菜单的布局QHBoxLayout（left_menu_layout）
    然后是一个自定义的左边菜单类PyLeftMenu （left_menu），把该类添加到左边菜单布局中
    self.left_menu_layout.addWidget(self.left_menu)

    左边的列QFrame（left_column_frame）
    左边列的布局QVBoxLayout（left_column_layout）
    然后是一个自定义的左边列类PyLeftColumn（left_column）
    self.left_column_layout.addWidget(self.left_column)

    右边的app QFrame（right_app_frame）
    app布局QVBoxLayout（right_app_layout）
    
    顶部导航QFrame（title_bar_frame）
    顶部导航的布局self.title_bar_layout = QVBoxLayout(self.title_bar_frame)
    顶部导航类PyTitleBar（title_bar）
    self.title_bar_layout.addWidget(self.title_bar)
    
    右边的内容区域self.content_area_frame = QFrame()
    内容区域布局self.content_area_layout = QHBoxLayout(self.content_area_frame)
    内容区域又分左右
    self.content_area_left_frame = QFrame()
    self.right_column_frame = QFrame()
    
    
    
    

再set_gui