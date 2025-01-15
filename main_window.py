import sys
from PyQt5.QtGui import QMouseEvent
import numpy as np
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
								QApplication, QVBoxLayout, QWidget,
								QLabel, QGridLayout, QPushButton, 
								QHBoxLayout, QLineEdit, QComboBox,
								QMainWindow, QMenuBar, QMenu, QAction
							)


from colorSettingsWidget import ColorSettingsWidget
from videoSettingsWidget import VideoSettingsWidget
from videoFrameLabel import VideoFrameLabel
from videoThread import VideoThread

class Main_Window(QMainWindow):

	def __init__(self):
		super().__init__()

		#WINDOW PARAMETERS
		self.resize(1100, 1000)
		self.setWindowTitle('GRAPHIT')
		self.setWindowIcon(QIcon('./icons/grafit_rosatom.png'))
		self.setMouseTracking(True)

		#CREATING CENTRAL WIDGET
		self.mainWidget = QWidget()
		
		#CREATING LAYOUTS
		mainGrid = QGridLayout()
		hbox = QHBoxLayout()
		videoVBox = QVBoxLayout()

		#LAYOUT SETTINGS
		mainGrid.setRowStretch(0, 1)
		mainGrid.setRowStretch(1, 2)
		mainGrid.setColumnStretch(0, 1)
		mainGrid.setColumnStretch(1, 2)

		mainGrid.addLayout(hbox, 0, 1)
		mainGrid.addLayout(videoVBox, 1, 0)

		#CREATING WIDGETS
		self.colorSettings 	= ColorSettingsWidget()
		self.videoSettings 	= VideoSettingsWidget()
		self.videoFrame 	= VideoFrameLabel()

		info 				= QLabel()


		
		#ADDING WIDGETS TO LAYOUTS
		
		videoVBox.addWidget(self.videoFrame, Qt.AlignmentFlag.AlignLeft)
		videoVBox.addWidget(self.videoSettings, Qt.AlignmentFlag.AlignLeft)
		
		hbox.addWidget(info)
		hbox.addWidget(info)

		#SETTING LAYOUTS TO CENTRAL WIDGET
		self.mainWidget.setLayout(mainGrid)
		self.setCentralWidget(self.mainWidget)
		
		#CREATING MENU BAR
		self._createActions()
		self._createMenuBar()

		#CREATING VIDEO THREAD FROM OPENCV
		self.vidThread = VideoThread()
		self.vidThread.start()


		#CONNECT SLOTS AND SIGNALS
		self.vidThread.frameSignal.connect(self.updateImage)
		self.videoSettings.ui.autocalibrateColor.clicked.connect(self.vidThread.autocalibrate)
		self.videoSettings.ui.colorSettings.clicked.connect(self.openColorSettingsWindow)
		self.videoSettings.ui.useFilter.clicked.connect(self.useVideoFilter)
		self.videoFrame.mouseSignal.connect(self.vidThread.click)
		self.videoSettings.ui.zoomValue.valueChanged.connect(self.readZoomValue)

		#Выглядит по уебански, но работает
		self.colorSettings.ui.apply.clicked.connect(
			lambda: self.vidThread.calibrate(
				int(self.colorSettings.ui.r1.text()),
				int(self.colorSettings.ui.g1.text()),
				int(self.colorSettings.ui.b1.text()),
				int(self.colorSettings.ui.r2.text()),
				int(self.colorSettings.ui.g2.text()),
				int(self.colorSettings.ui.b2.text())
			)
		)
		
		

	def _createMenuBar(self):
		menu_bar = self.menuBar()

		#File menu
		self.fileMenu = menu_bar.addMenu('Файл')

		self.fileMenu.addAction(self.openAction)
		self.fileMenu.addAction(self.loadAction)
		self.fileMenu.addAction(self.saveAsAction)
		self.fileMenu.addAction(self.exitAction)

		#Help menu
		self.helpMenu = menu_bar.addMenu('Помощь')

		self.helpMenu.addAction(self.helpAction)
		self.helpMenu.addAction(self.aboutAction)


	def _createActions(self):
		#File
		self.openAction 		= QAction("Открыть...", self)
		self.loadAction 		= QAction("Загрузить...", self)
		self.saveAsAction 		= QAction("Сохранить как...", self)
		self.exitAction 		= QAction("Выйти", self)

		#Help
		self.helpAction			= QAction("Справка", self)
		self.aboutAction		= QAction("О программе", self)


	def cv2qt(self, cvImg):
		"""Converts cv image to qt image"""
		rgbImage = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
		h, w, ch = rgbImage.shape
		bytesPerLine = ch * w

		qtFormatImage = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
		result = qtFormatImage.scaled(self.videoFrame.imgWidth, self.videoFrame.imgHeight, Qt.KeepAspectRatio)
		return QPixmap.fromImage(result)
	

	@pyqtSlot(np.ndarray)
	def updateImage(self, cvImg):
		"""Updates imageLabel with opencv image"""
		qtImg = self.cv2qt(cvImg)
		self.videoFrame.setPixmap(qtImg)

	def openColorSettingsWindow(self):
		self.colorSettings.show()

	def useVideoFilter(self):
		self.vidThread.useFilter = not self.vidThread.useFilter

	def readZoomValue(self):
		self.vidThread.zoom = self.videoSettings.ui.zoomValue.value()





app = QApplication(sys.argv)
win = Main_Window()
win.show()

exit(app.exec_())




