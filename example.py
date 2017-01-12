# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from bsUI import *

if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())