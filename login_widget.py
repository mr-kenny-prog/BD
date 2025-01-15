from PyQt5.QtWidgets import QWidget
import sys
import os
sys.path.insert(1, 'ui_files')
from ui_login import Ui_Login
from subprocess import Popen
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
import re
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
class Login_widget(QWidget):
    global state,flag
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.currentSTL = None
        self.lastDir = None
        self.droppedFilename = None
        self.ui.openGLWidget.setCameraPosition(distance=3000)
        self.ui.openGLWidget.setBackgroundColor((15, 23, 25, 0.1))
        g = gl.GLGridItem()
        g.setSize(20, 20)
        g.setSpacing(5, 5)
        self.ui.openGLWidget.addItem(g)
        #self.showSTL(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\КДМЕ23.stl")
        #self.lastDir = Path(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\КДМЕ23.stl ").parent
        self.ui.pushButton.clicked.connect(self.showDialog)
        self.ui.pushButton_6.clicked.connect(self.showDialog_model)

    def showDialog_model(self):
        directory = Path(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота")
        if self.lastDir:
            directory = self.lastDir
        fname = QFileDialog.getOpenFileName(self, "Open file", str(directory), "STL (*.stl)")
        if fname[0]:
            self.showSTL(fname[0])
            self.lastDir = Path(fname[0]).parent

    def showDialog(self):

        file = open(
            r'C:\Users\egorp\Desktop\КДМЕ23\Программа для автоматического генерирования робота\MATH_MODEL\ConsoleApplication1\PARAM.txt',
            '+r', encoding='utf-8').readlines()
        param = [200,40,150,40,200]
        i = 0
        for line in file:
            if (i == 1):
                param[1] = int(float(re.sub('\n','',line.split(':')[1])) * 1000)
                param[3] = int(float(re.sub('\n','',line.split(':')[1])) * 1000)
            if (i == 6):
                param[0] = int(float(re.sub('\n','',line.split(':')[1])) * 1000)
                param[4] = int(float(re.sub('\n','',line.split(':')[1])) * 1000)
            if (i == 13):
                param[2] = int(float(re.sub('\n','',line.split(':')[1])) * 1000)
            i+=1

        print(param)
        path = rf"C:\ProgramData\ASCON\KOMPAS-3D\20\Python 3\App\Lib\site-packages\pythonwin\Robot_generate.py"
        os.system(" ".join(["python", fr'"{path}"', str(param[0]), str(param[1]),str(param[2]),str(param[3]),str(param[4])]))

        self.showSTL(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\КДМЕ23.stl")
        self.lastDir = Path(r"C:\Users\egorp\Desktop\КДМЕ23\Сборка робота\КДМЕ23.stl ").parent


    def showSTL(self, filename):
        if self.currentSTL:
            self.ui.openGLWidget.removeItem(self.currentSTL)
        points, faces = self.loadSTL(filename)
        meshdata = gl.MeshData(vertexes=points, faces=faces)
        mesh = gl.GLMeshItem(meshdata=meshdata, smooth=False, drawFaces=True, drawEdges=True,
                             edgeColor=(1, 0.4, 0.22, 1), color=(0.16, 0.2, 0.19, 1))
        self.ui.openGLWidget.addItem(mesh)
        self.currentSTL = mesh

    def loadSTL(self, filename):
        m = mesh.Mesh.from_file(filename)
        shape = m.points.shape
        points = m.points.reshape(-1, 3)
        faces = np.arange(points.shape[0]).reshape(-1, 3)
        return points, faces