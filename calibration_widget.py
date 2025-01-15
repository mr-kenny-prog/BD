from PyQt5.QtWidgets import QWidget
import sys
import PyQt5.QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import os
sys.path.insert(1, './ui_files')
from ui_calibration import Ui_Calibration
import re
from pyModbusTCP.client import ModbusClient
last_state = "DARK"
index = 1

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np
from stl import mesh
from pathlib import Path

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib import transforms
import textwrap
from datetime import datetime
import matplotlib

from Characteristics import characteristics_widget


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=7, height=4, dpi=100, projection = True):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor = [15/255, 23/255, 25/255,1])
        if (projection):
            self.axes = self.fig.add_subplot(111, facecolor = [15/255, 23/255, 25/255,1], projection='3d')
        else: 
            self.axes = self.fig.add_subplot(111, facecolor = [15/255, 23/255, 25/255,1])
        super(MplCanvas, self).__init__(self.fig)


class Calibration_widget(QWidget):
    global index
    def __init__(self):
        global index
        super().__init__()
        self.ui = Ui_Calibration()
        self.ui.setupUi(self)
        characteristics = characteristics_widget()

        self.canvas = MplCanvas(self, width=5, height=5, dpi=100)
        hlayout = QVBoxLayout(self.ui.frame_4)
        toolbar = NavigationToolbar(self.canvas, self)
        hlayout.addWidget(toolbar)
        hlayout.addWidget(self.canvas)

        
        self.canvas_2d = MplCanvas(self, width=5, height=5, dpi=100, projection=False)
        hlayout_2d = QVBoxLayout(self.ui.frame)
        toolbar_2d = NavigationToolbar(self.canvas_2d, self)
        hlayout_2d.addWidget(toolbar_2d)
        hlayout_2d.addWidget(self.canvas_2d)
        
        

        self.currentSTL = None
        self.lastDir = None
        self.droppedFilename = None

        self.Kristi_graph()
        self.wheel_graph()

        self.ui.openGLWidget.setCameraPosition(distance=3000)
        self.ui.openGLWidget.setBackgroundColor((15, 23, 25, 0.1))
        self.ui.openGLWidget_2.setCameraPosition(distance=3000)
        self.ui.openGLWidget_2.setBackgroundColor((15, 23, 25, 0.1))
        self.ui.openGLWidget_4.setCameraPosition(distance=3000)
        self.ui.openGLWidget_4.setBackgroundColor((15, 23, 25, 0.1))
        self.ui.openGLWidget_5.setCameraPosition(distance=3000)
        self.ui.openGLWidget_5.setBackgroundColor((15, 23, 25, 0.1))
        self.ui.openGLWidget_6.setCameraPosition(distance=3000)
        self.ui.openGLWidget_6.setBackgroundColor((15, 23, 25, 0.1))

        g = gl.GLGridItem()
        g.setSize(20, 20)
        g.setSpacing(5, 5)
        self.ui.openGLWidget.addItem(g)
        self.ui.openGLWidget_2.addItem(g)
        self.STL_Kristi()
        self.STL_Rama()
        self.STL_razval()
        self.STL_koleso()
        self.STL_reductor()
        characteristics.ui.pushButton.clicked.connect(self.STL_Kristi)
        characteristics.ui.pushButton_5.clicked.connect(self.STL_koleso)
        characteristics.ui.pushButton_15.clicked.connect(self.STL_Rama)
        characteristics.ui.pushButton_17.clicked.connect(self.STL_razval)

        self.ui.pushButton_15.clicked.connect(lambda: self.Open_kompas(rf"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Каркас\Каркас.a3d"))
        self.ui.pushButton_17.clicked.connect(lambda: self.Open_kompas(rf"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Сход-развал\Сход-развал.a3d"))
        self.ui.pushButton_5.clicked.connect(lambda: self.Open_kompas(rf"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Колесо\Адаптивное Колесо.a3d"))
        self.ui.pushButton_7.clicked.connect(lambda: self.Open_kompas(rf"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\редуктор\Редуктор цилиндрический.a3d"))
        self.ui.pushButton.clicked.connect(lambda: self.Open_kompas(rf"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Кристи.m3d"))



    def Open_kompas (self, link):
        path = rf"C:\ProgramData\ASCON\KOMPAS-3D\20\Python 3\App\Lib\site-packages\pythonwin\show_model.py"
        os.system(" ".join(["python", fr'"{path}"', fr'"{link}"']))

    def STL_Kristi(self):
        self.showSTL(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Кристи.stl", self.ui.openGLWidget)
        self.lastDir = Path(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Кристи.stl").parent

    def STL_Rama(self):
        self.showSTL(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Каркас.stl", self.ui.openGLWidget_2)
        self.lastDir = Path(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Каркас.stl").parent

    def STL_razval(self):
        self.showSTL(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Развал.stl", self.ui.openGLWidget_4)
        self.lastDir = Path(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Развал.stl").parent

    def STL_koleso(self):
        self.showSTL(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Адаптивное Колесо.stl", self.ui.openGLWidget_5)
        self.lastDir = Path(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Адаптивное Колесо.stl").parent

    def STL_reductor(self):
        self.showSTL(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Редуктор.stl", self.ui.openGLWidget_6)
        self.lastDir = Path(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\Редуктор.stl").parent

    def showSTL(self, filename, object):
        #if self.currentSTL:
            #object.removeItem(self.currentSTL)
        points, faces = self.loadSTL(filename)
        meshdata = gl.MeshData(vertexes=points, faces=faces)
        mesh = gl.GLMeshItem(meshdata=meshdata, smooth=False, drawFaces=True, drawEdges=True,
                             edgeColor=(1, 0.4, 0.22, 1), color=(0.16, 0.2, 0.19, 1))
        object.addItem(mesh)
        self.currentSTL = mesh

    def loadSTL(self, filename):
        m = mesh.Mesh.from_file(filename)
        shape = m.points.shape
        points = m.points.reshape(-1, 3)
        faces = np.arange(points.shape[0]).reshape(-1, 3)
        return points, faces
    
    def Kristi_graph (self):
        self.canvas.axes.cla()
        plt.grid()

        file = open(
            r'C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\PARAM.txt',
            '+r', encoding='utf-8').readlines()
        param = [0.01, 3, 0.04, 30]
        i = 0
        for line in file:
            if (i == 1):
                param[0] = int(float(re.sub('\n', '', line.split(':')[1])) * 1000)
            if (i == 2):
                param[1] = int(float(re.sub('\n', '', line.split(':')[1])) * 1000)
            if (i == 3):
                param[2] = int(float(re.sub('\n', '', line.split(':')[1])) * 1000)
            if (i == 5):
                param[3] = int(float(re.sub('\n', '', line.split(':')[1])) * 1000)
            i += 1

        s = param[0]
        g = 9.81
        f = 0
        m = param[1]
        r = param[2]
        pi =  3.14
        tan = 7.5
        m_sum = param[3]
        self.canvas.axes.set_xlabel("Угловое ускорение", fontsize=14, color='w')
        self.canvas.axes.set_ylabel("Угловая скорость", fontsize=14, color='w')
        self.canvas.axes.set_zlabel("Амортизация", fontsize=14, color='w')
        self.canvas.axes.spines['bottom'].set_color('#ffffff')
        #ax.spines['top'].set_color('#ffffff')
        self.canvas.axes.xaxis.label.set_color('#ffffff')
        self.canvas.axes.tick_params(axis='x', colors='#ffffff')

        self.canvas.axes.spines['left'].set_color('#ffffff')
        #ax.spines['right'].set_color('#ffffff')
        self.canvas.axes.yaxis.label.set_color('#ffffff')
        self.canvas.axes.tick_params(axis='y', colors='#ffffff')

        self.canvas.axes.spines['left'].set_color('#ffffff')
        #ax.spines['right'].set_color('#ffffff')
        self.canvas.axes.zaxis.label.set_color('#ffffff')
        self.canvas.axes.tick_params(axis='z', colors='#ffffff')
        agrid = np.linspace(-50, 50, 500)
        bgrid = np.linspace(-50, 50, 500)
        a, b = np.meshgrid(agrid, bgrid)
        z = -((m * (-pow(a, 2) * np.sqrt(2) * r * np.sin(pi / 4 + f) + b * r + np.sqrt(2) * r * np.cos(pi / 4 + f) * b)) / (np.sqrt(pow(-pow(a, 2) * np.sqrt(2) * r * np.cos(pi / 4 + f) - np.sqrt(2) * r * np.sin(pi / 4 + f) * b, 2) + pow(-pow(a, 2) * np.sqrt(2) * r * np.sin(pi / 4 + f) + b * r + np.sqrt(2) * r * np.cos(pi / 4 + f) * b, 2)))) - (m * (-pow(a, 2) * np.sqrt(2) * r * np.cos(pi / 4 + f) - np.sqrt(2) * r * np.sin(pi / 4 + f) * b)) / (np.sqrt(1 + pow((-pow(a, 2) * np.sqrt(2) * r * np.sin(pi / 4 + f) + b * r + np.sqrt(2) * r * np.cos(pi / 4 + f) * b) / (-pow(a, 2) * np.sqrt(2) * r * np.cos(pi / 4 + f)	- np.sqrt(2) * r * np.sin(pi / 4 + f) * b), 2))) * tan - (1 / 4 * m * (pow(r + s / 2, 2) + pow(r - s / 2, 2)) * b)/ (np.sqrt(2) * r * np.cos(pi / 4 + f)) - m * g
        self.canvas.axes.plot_surface(a, b, z, rstride=5, cstride=5, cmap='plasma')

    def wheel_graph (self):
        self.canvas_2d.axes.cla()

        M_y=300
        f=0.7
        l=0.8 
        b=0.3
        M_p =100
        self.canvas_2d.axes.set_xlabel("Угол наклона лестницы", fontsize=14, color='w')
        self.canvas_2d.axes.set_ylabel("Диаметр колеса", fontsize=14, color='w')
        self.canvas_2d.axes.spines['bottom'].set_color('#ffffff')
        #ax.spines['top'].set_color('#ffffff')
        self.canvas_2d.axes.xaxis.label.set_color('#ffffff')
        self.canvas_2d.axes.tick_params(axis='x', colors='#ffffff')

        self.canvas_2d.axes.spines['left'].set_color('#ffffff')
        #ax.spines['right'].set_color('#ffffff')
        self.canvas_2d.axes.yaxis.label.set_color('#ffffff')
        self.canvas_2d.axes.tick_params(axis='y', colors='#ffffff')
        a = np.linspace(-1, 1, 500)
        b = 2*((1+f**2)*(np.sin((a-3.14/2))*np.sqrt(np.abs(l**2+b**2 - (np.cos((a-3.14/2)) * (l*np.tan((a-3.14/2)) - b))/(np.tan((a-3.14/2))))) + np.cos((a-3.14/2))))/(4*(1-f)*(f*np.cos((a-3.14/2)) - np.sin((a-3.14/2))) + M_p/M_y*f*(f+1)*(np.sin((a-3.14/2))*np.sqrt(np.abs(l**2+b**2 - (np.cos((a-3.14/2)) * (l*np.tan((a-3.14/2)) - b))/(np.tan((a-3.14/2))))) + np.cos((a-3.14/2))) - 4*(1+f**2)*np.sin((a-3.14/2))) + 0.4
        self.canvas_2d.axes.plot(a, b, 'w', linewidth=1)
        plt.grid()

    