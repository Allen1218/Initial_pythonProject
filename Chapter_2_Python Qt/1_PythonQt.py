from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


import PySide2

class Stats:
    def __init__(self):
        # 从UI中加载
        qfile_stats = QFile("UI/export_0.1.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        # 从UI定义中动态创建一个响应的窗口对象
        # 注意：里面的空间对象也成为窗口对象的属性了
        # 比如：self.ui.button, self.ui.textEdit

        self.ui = QUiLoader().load(qfile_stats)
        # self.ui.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = 1


app = QApplication()
stats = Stats()
stats.ui.show()
app.exec_()