from PyQt5.QtWidgets import QWidget
import os
import sys
from PyQt5.QtGui import QMouseEvent
import numpy as np
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5 import QtGui
from PyQt5.QtGui import *
from  PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
								QApplication, QVBoxLayout, QWidget,
								QLabel, QGridLayout, QPushButton,
								QHBoxLayout, QLineEdit, QComboBox,
								QMainWindow, QMenuBar, QMenu, QAction
							)

sys.path.insert(1, './ui_files')
from ui_karkas import Ui_Calibration

class characteristics_widget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui =  Ui_Calibration()
        self.ui.setupUi(self)
        self.ui.frame_4.setStyleSheet(
                f"border-image: url(Data/karkas.png);")
        self.ui.frame_3.setStyleSheet(
                f"border-image: url(Data/razval.png);")
        self.ui.frame.setStyleSheet(
                f"border-image: url(Data/wheel.png);")
        self.ui.frame_2.setStyleSheet(
                f"border-image: url(Data/kristi.png);")

        #self.ui.pushButton.clicked.connect(lambda: self.Kristi_calculate(str(float(self.ui.lineEdit.text()) * 1000), str(float(self.ui.lineEdit_2.text()) * 1000)))
        #self.ui.pushButton_5.clicked.connect(lambda: self.wheel_calculate(str(float(self.ui.lineEdit_5.text()) * 1000), str(float(self.ui.lineEdit_6.text())*1000)))
        #self.ui.pushButton_15.clicked.connect(lambda: self.karkas_calculate(str(float(self.ui.lineEdit_15.text()) * 1000), str((float(self.ui.lineEdit_16.text()) - 4* float(self.ui.lineEdit_17.text()))* 1000 / 2 / np.sqrt(2) ), str(float(self.ui.lineEdit_14.text()) * 1000), str(float(self.ui.lineEdit_17.text()) * 1000) ))
        #self.ui.pushButton_17.clicked.connect(lambda: self.razval_calculate(str(float(self.ui.lineEdit_10.text()) * 1000), str(float(self.ui.lineEdit_11.text()) * 1000)))





    
    def Kristi_calculate (self, R,S):
        #path = rf"C:\ProgramData\ASCON\KOMPAS-3D\20\Python 3\App\Lib\site-packages\pythonwin\show_model.py"
        #os.system(" ".join(["python", fr'"{path}"', fr'"{link}"']))
        file = open(r'C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\PARAM.txt', '+r', encoding='utf-8').readlines()
        file[1] = f'Толщина звена в подвеске Кристи (м): {float(S)/1000}\n'
        file[2] = f'Масса звена в подвеске Кристи (кг): {2*3.14*float(R)/1000 / 4 * float(S)/1000 * float(S)/1000 * 7856}\n'
        file[3] = f'Радиус звена в подвеске Кристи (м): {float(R)/1000}\n'
        file[4] = f'Угол наклона пружины в подвеске Кристи( tan ): {str(float(self.ui.lineEdit_3.text()))}\n'
        file[5] = f'Нагрузка на одно колесо (кг): {str(float(self.ui.lineEdit_4.text()))}\n'
        out = open(r'C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\PARAM.txt', 'w', encoding='utf-8')
        out.writelines(file)
        out.close()

        path_model = rf"C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\math_model.exe"
        os.system(" ".join(["start", fr'"{path_model}"']))


    def wheel_calculate (self, R, S):
        file = open(
            r'C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\PARAM.txt',
            '+r', encoding='utf-8').readlines()
        file[6] = f'Радиус первого диска в адаптивном колесе (м): {float(R) / 1000}\n'
        file[8] = f'Начальная угловая скорость в адаптивном колесе (рад/c): {str(float(self.ui.lineEdit_7.text()))}\n'
        file[9] = f'Начальное угловое ускорение в адаптивном колесе (рад): {str(float(self.ui.lineEdit_8.text()))}\n'
        file[10] = f'Масса стержня в адаптивном колесе (кг): {(float(R)/1000 - (2*float(R)/1000-3)*0.87 / 2 + float(R)/1000*2/3 + 0.6*float(S)/1000)*float(S)/1000*(float(S)/1000)/3 * 7856}\n'
        file[11] = f'Масса ползуна с наконечником в адаптивном колесе (кг): {2*3.14*float(R)/1000 / 8 * float(S)/1000 * 3*float(S)/1000 * 7856}\n'
        file[12] = f'Масса начального диска в адаптивном колесе (кг): {3.14 * ((float(R)/1000)**2) * (float(S)/1000) / 4 * 7856}\n'
        out = open(r'C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\PARAM.txt','w', encoding='utf-8')
        out.writelines(file)
        out.close()

        path_model = rf"C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\math_model.exe"
        os.system(" ".join(["start", fr'"{path_model}"']))

        path = rf"C:\ProgramData\ASCON\KOMPAS-3D\20\Python 3\App\Lib\site-packages\pythonwin\adaptive_wheel_generate.py"
        os.system(" ".join(["python", fr'"{path}"', R, S]))
        
    def karkas_calculate (self,L, R, Z, S ):
        path = rf"C:\ProgramData\ASCON\KOMPAS-3D\20\Python 3\App\Lib\site-packages\pythonwin\karkas-generate.py"
        os.system(" ".join(["python", fr'"{path}"', L, R, Z, S ]))
        

    def razval_calculate (self, L, S):
        file = open(
            r'C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\PARAM.txt',
            '+r', encoding='utf-8').readlines()
        file[13] = f'Длина звена системы развал (м): {float(L) / 1000}\n'
        file[15] = f'Начальная угловая скорость в системе развал (рад/c): {str(float(self.ui.lineEdit_12.text()))}\n'
        file[16] = f'Начальное угловое ускорение в системе развал (рад): {str(float(self.ui.lineEdit_13.text()))}\n'
        out = open(
            r'C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\PARAM.txt',
            'w', encoding='utf-8')
        out.writelines(file)
        out.close()

        path_model = rf"C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\math_model.exe"
        os.system(" ".join(["start", fr'"{path_model}"']))

        path = rf"C:\ProgramData\ASCON\KOMPAS-3D\20\Python 3\App\Lib\site-packages\pythonwin\razval_generate.py"
        os.system(" ".join(["python", fr'"{path}"', L, S]))
       