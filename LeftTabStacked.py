from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QStackedWidget, QHBoxLayout,QListWidgetItem, QLabel, QVBoxLayout, QMessageBox
from PyQt5     import QtWidgets
from PyQt5 import QtCore, QtGui
import os
#Custom widgets
from BD import BD



CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
class LeftTabWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(LeftTabWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        # 左右布局(左边一个QListWidget + 右边QStackedWidget)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        # 左侧列表
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)
        # 右侧层叠窗口
        self.stackedWidget = QStackedWidget(self)
        layout.addWidget(self.stackedWidget)
        self.initUi()
    def initUi(self):
        self.listWidget.currentRowChanged.connect(
            self.stackedWidget.setCurrentIndex)
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #================Вкладки меню=================
        item = QListWidgetItem(
            QIcon('Data/gears.ico'), str('Базы\nданных'), self.listWidget
        )
        item.setSizeHint(QSize(16777215, 100))
        
        item.setTextAlignment(Qt.AlignCenter)
        #================Вкладки меню=================
        self.stackedWidget.addWidget(BD())
        closeButton = QtWidgets.QPushButton('Выйти')
        closeButton.setIcon(QIcon('Data/logout.ico'))
        closeButton.setStyleSheet("QPushButton{\n"
                                "background: -+\\;\n"
                                "color: rgba(255,102,56,255);\n"
                                "padding:10px;\n"
                                "min-height:100px; \n"
                                "min-width: 200px;\n"
                                "text-align: left;\n"
                                "font: 20px;\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "background: rgba(255,102,56,255);\n"
                                "border-left: 2px solid rgb(9, 187, 7);\n"
                                "color: rgba(41,51,48,255);\n"
                                "padding:10px;\n"
                                "min-height:100px; \n"
                                "min-width:200px;\n"
                                "font: 20px;\n"
                                "text-align: center;\n"
                                "}")

        listWidgetItem_close = QtWidgets.QListWidgetItem()
        listWidgetItem_close.setSizeHint(closeButton.sizeHint())
        self.listWidget.addItem(listWidgetItem_close)
        self.listWidget.setItemWidget(listWidgetItem_close, closeButton)
        closeButton.clicked.connect(self.exit)

    def exit(self, event):
        msg = QMessageBox(self)
        #msg.setWindowIcon(QIcon("im.png"))
        msg.setWindowTitle("Выход")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы действительно хотите выйти?")

        buttonAceptar = msg.addButton("Да", QMessageBox.YesRole)
        buttonCancelar = msg.addButton("Отменить", QMessageBox.RejectRole)
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            app.quit()
        elif msg.clickedButton() == buttonCancelar:
            pass

Stylesheet = """
    /*去掉item虚线边框*/
    QListWidget, QListView, QTreeWidget, QTreeView {
        outline: 0px;
    }
    /*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/
    QListWidget {
        min-width: 200px;
        max-width: 200px;
        color: rgba(255,102,56,255);    
        font: 20px;
        background: rgb(15, 23, 25);
    }
    /*被选中时的背景颜色和左边框颜色*/
    QListWidget::item:selected {
        background: rgba(255,102,56,255);
        color: rgb(15, 23, 25);
        border-left: 2px solid rgb(9, 187, 7);
    }
    /*鼠标悬停颜色*/
    HistoryPanel::item:hover {
        background: rgba(255,102,56,255);
        color: rgba(41,51,48,255);
    }

    /*右侧的层叠窗口的背景颜色*/
    QStackedWidget {
        background: rgb(15, 23, 25);
    }
    /*模拟的页面*/
    QLabel {
        background: rgb(15, 23, 25);
        color: rgba(255,102,56,255);
    }
    """

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    w = LeftTabWidget()
    w.showFullScreen()
    sys.exit(app.exec_())
