import sys
import os
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore

sys.path.insert(1, './ui_files')
from colorSettings import Ui_colorSetting

class ColorSettingsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=None)

        self.ui = Ui_colorSetting()
        self.ui.setupUi(self)

        self.ui.r1.selectionChanged.connect(self.osk)
        self.ui.r2.selectionChanged.connect(self.osk)
        self.ui.g1.selectionChanged.connect(self.osk)
        self.ui.g2.selectionChanged.connect(self.osk)
        self.ui.b1.selectionChanged.connect(self.osk)
        self.ui.b2.selectionChanged.connect(self.osk)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.update_theme)
        self.timer.start()

    def osk(self):
        os.system("start osk.exe /I")

    def update_theme(self):
        file = open('Theme.txt', "+r").readlines()
        if (file[0] == "LIGHT"):
            self.setStyleSheet("\n"
                               "background: #e1e1e1;\n"
                               "\n"
                               "")
            self.ui.g2.setStyleSheet("position: absolute;\n"
                                     "top:50%;\n"
                                     "background-color:#115195;\n"
                                        "color: #e1e1e1;\n"
                                       "border-radius:8px; \n"
                                     "padding:10px;\n"
                                     "min-height:20px; \n"
                                     "min-width: 50px;")
            self.ui.b2.setStyleSheet("position: absolute;\n"
                                     "top:50%;\n"
                                     "background-color:#115195;\n"
                                        "color: #e1e1e1;\n"
                                       "border-radius:8px; \n"
                                     "padding:10px;\n"
                                     "min-height:20px; \n"
                                     "min-width: 50px;")
            self.ui.b1.setStyleSheet("position: absolute;\n"
                                     "top:50%;\n"
                                     "background-color:#115195;\n"
                                        "color: #e1e1e1;\n"
                                       "border-radius:8px; \n"
                                     "padding:10px;\n"
                                     "min-height:20px; \n"
                                     "min-width: 50px;")
            self.ui.g1.setStyleSheet("position: absolute;\n"
                                     "top:50%;\n"
                                     "background-color:#115195;\n"
                                        "color: #e1e1e1;\n"
                                       "border-radius:8px; \n"
                                     "padding:10px;\n"
                                     "min-height:20px; \n"
                                     "min-width: 50px;")
            self.ui.r1.setStyleSheet("position: absolute;\n"
                                     "top:50%;\n"
                                     "background-color:#115195;\n"
                                        "color: #e1e1e1;\n"
                                       "border-radius:8px; \n"
                                     "padding:10px;\n"
                                     "min-height:20px; \n"
                                     "min-width: 50px;")
            self.ui.r2.setStyleSheet("position: absolute;\n"
                                     "top:50%;\n"
                                     "background-color:#115195;\n"
                                        "color: #e1e1e1;\n"
                                       "border-radius:8px; \n"
                                     "padding:10px;\n"
                                     "min-height:20px; \n"
                                     "min-width: 50px;")
            self.ui.apply.setStyleSheet("QPushButton{\n"
                                        "position: absolute;\n"
                                        "top:50%;\n"
                                        "background-color:#115195;\n"
                                        "color: #e1e1e1;\n"
                                        "border-radius:8px; \n"
                                        "padding:10px;\n"
                                        "min-height:30px; \n"
                                        "min-width: 120px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "position: absolute;\n"
                                        "top:50%;\n"
                                        "background-color:#349ef1;\n"
                                        "color: #e1e1e1;\n"
                                        "border-radius:8px; \n"
                                        "padding:10px;\n"
                                        "min-height:30px; \n"
                                        "min-width: 120px;\n"
                                        "}")

        if (file[0] == "DARK"):
            self.setStyleSheet("\n"
                               "background: rgb(30, 30, 30);\n"
                               "\n"
                               "")
            self.ui.g2.setStyleSheet("position: absolute;\n"
                                  "top:50%;\n"
                                  "background-color:#343434;\n"
                                  "color: #ff9500;\n"
                                  "border-radius:8px; \n"
                                  "padding:10px;\n"
                                  "min-height:20px; \n"
                                  "min-width: 50px;")
            self.ui.b2.setStyleSheet("position: absolute;\n"
                                  "top:50%;\n"
                                  "background-color:#343434;\n"
                                  "color: #ff9500;\n"
                                  "border-radius:8px; \n"
                                  "padding:10px;\n"
                                  "min-height:20px; \n"
                                  "min-width: 50px;")
            self.ui.b1.setStyleSheet("position: absolute;\n"
                                  "top:50%;\n"
                                  "background-color:#343434;\n"
                                  "color: #ff9500;\n"
                                  "border-radius:8px; \n"
                                  "padding:10px;\n"
                                  "min-height:20px; \n"
                                  "min-width: 50px;")
            self.ui.g1.setStyleSheet("position: absolute;\n"
                                  "top:50%;\n"
                                  "background-color:#343434;\n"
                                  "color: #ff9500;\n"
                                  "border-radius:8px; \n"
                                  "padding:10px;\n"
                                  "min-height:20px; \n"
                                  "min-width: 50px;")
            self.ui.r1.setStyleSheet("position: absolute;\n"
                                  "top:50%;\n"
                                  "background-color:#343434;\n"
                                  "color: #ff9500;\n"
                                  "border-radius:8px; \n"
                                  "padding:10px;\n"
                                  "min-height:20px; \n"
                                  "min-width: 50px;")
            self.ui.r2.setStyleSheet("position: absolute;\n"
                                  "top:50%;\n"
                                  "background-color:#343434;\n"
                                  "color: #ff9500;\n"
                                  "border-radius:8px; \n"
                                  "padding:10px;\n"
                                  "min-height:20px; \n"
                                  "min-width: 50px;")
            self.ui.apply.setStyleSheet("QPushButton{\n"
                                     "position: absolute;\n"
                                     "top:50%;\n"
                                     "background-color:#343434;\n"
                                     "color: #ff9500;\n"
                                     "border-radius:8px; \n"
                                     "padding:10px;\n"
                                     "min-height:30px; \n"
                                     "min-width: 120px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "position: absolute;\n"
                                     "top:50%;\n"
                                     "background-color:rgba(109, 109, 109, 242);\n"
                                     "color: #ff9500;\n"
                                     "border-radius:8px; \n"
                                     "padding:10px;\n"
                                     "min-height:30px; \n"
                                     "min-width: 120px;\n"
                                     "}")
