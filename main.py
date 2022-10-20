from PySide2.QtWidgets import QApplication, QMessageBox, QPushButton, QGridLayout
from PySide2.QtUiTools import QUiLoader

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
#hhhh
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('main.ui')

        # self.ui.button.clicked.connect(self.handleCalc)
        #隐藏组件选择界面
        self.ui.dockWidget.hide()

        #展示组件选择界面
        self.ui.radioButton.clicked.connect(self.radioButtonHandleCalc)

        #选择组件
        self.ui.pushButton_4.clicked.connect(self.selectComponentHandleCalc)

    def radioButtonHandleCalc(self):
       '''
       展示组件选择界面
       :return:
       '''
       self.ui.dockWidget.show()

    def selectComponentHandleCalc(self):
        '''
        选择组件
        :return:
        '''
        #获取组件属性
        print( self.ui.pushButton_4.text())
        #移动添加按钮
        self.ui.radioButton.setGeometry(530,90,19,19)
        #总线上添加组件
        button = QPushButton('统计', self.ui)
        button.resize(300,300)
        button.move(1000, 100)
        self.ui.verticalLayout.addWidget(button)

        #关系组件选择窗口
        self.ui.dockWidget.hide()

if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()