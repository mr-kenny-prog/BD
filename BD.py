from PyQt5.QtWidgets import QWidget
import os
import sys
from PyQt5.QtGui import QMouseEvent
import numpy as np
import pandas as pd 
import math
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5 import QtGui
from PyQt5.QtGui import *
from  PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
								QApplication, QVBoxLayout, QWidget,
								QLabel, QGridLayout, QPushButton,
								QHBoxLayout, QLineEdit, QComboBox,
								QMainWindow, QMenuBar, QMenu, QAction, QTableWidgetItem, QMessageBox
							)

sys.path.insert(1, './ui_files')
from ui_BD import Ui_BD

class BD(QWidget):
    def Add_string(self,idx):
        if (idx == 1):
            motors = pd.read_csv('motors.csv',index_col=[0,1])
            manufcturer = self.ui.manufcturer_1.text()
            model = self.ui.model_1.text()
            type = self.ui.type_1.currentText()
            voltage = self.ui.voltage_1.currentText()   
            current = self.ui.current_1.text()
            speed = self.ui.speed_1.text()
            moment = self.ui.moment_1.text()
            col = motors.index.names + list(motors.columns)
            data = [manufcturer, model, type, voltage, current,speed,moment]
            new_motor = pd.DataFrame(columns=col).set_index(motors.index.names)
            new_motor.loc[(manufcturer,model),:] = pd.Series(data={col[2] : type, col[3] : voltage, col[4]: current,col[5]:speed,col[6]: moment})
            test = pd.concat([motors,new_motor], axis=1, join='inner')
            if (list(test.index) == []):
                motors= pd.concat([motors,new_motor], join='outer')
                motors.to_csv(f'motors.csv',index=True)
                rowPosition = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(rowPosition)
                self.ui.tableWidget.setVerticalHeaderItem(rowPosition, QTableWidgetItem(f'Двигатель {rowPosition + 1}'))
                for i in range(len(col)):
                    data_motor_val = QTableWidgetItem(str(data[i]))
                    self.ui.tableWidget.setItem(rowPosition,i,data_motor_val)
            else: 
                msg = QMessageBox(self)
                #msg.setWindowIcon(QIcon("im.png"))
                msg.setWindowTitle("Существующее значение")
                msg.setText("Данный мотор уже существует")
                buttonAceptar = msg.addButton("Ок", QMessageBox.YesRole)
                msg.setDefaultButton(buttonAceptar)
                msg.exec_()
                if msg.clickedButton() == buttonAceptar:
                    pass
        if (idx == 2):
            pneumatic = pd.read_csv('pneumatic.csv',index_col=[0,1])
            manufcturer = self.ui.manufactorer_2.text()
            model = self.ui.model_2.text()
            working_stroke = self.ui.working_stroke_2.text()
            diametr = self.ui.diametr_2.text()
            pressure = self.ui.pressure_2.text()   
            col = pneumatic.index.names + list(pneumatic.columns)
            data = [manufcturer, model, working_stroke, diametr, pressure]
            new_pneumatic = pd.DataFrame(columns=col).set_index(pneumatic.index.names)
            new_pneumatic.loc[(manufcturer,model),:] = pd.Series(data={col[2] : working_stroke, col[3] : diametr, col[4]: pressure})
            test = pd.concat([pneumatic,new_pneumatic], axis=1, join='inner')
            if (list(test.index) == []):
                pneumatic= pd.concat([pneumatic,new_pneumatic], join='outer')
                pneumatic.to_csv(f'pneumatic.csv',index=True)
                rowPosition = self.ui.tableWidget_2.rowCount()
                self.ui.tableWidget_2.insertRow(rowPosition)
                self.ui.tableWidget_2.setVerticalHeaderItem(rowPosition, QTableWidgetItem(f'Цилиндр {rowPosition + 1}'))
                for i in range(len(col)):
                    data_pneumatic_val = QTableWidgetItem(str(data[i]))
                    self.ui.tableWidget_2.setItem(rowPosition,i,data_pneumatic_val)
            else: 
                msg = QMessageBox(self)
                #msg.setWindowIcon(QIcon("im.png"))
                msg.setWindowTitle("Существующее значение")
                msg.setText("Данный цилиндр уже существует")
                buttonAceptar = msg.addButton("Ок", QMessageBox.YesRole)
                msg.setDefaultButton(buttonAceptar)
                msg.exec_()
                if msg.clickedButton() == buttonAceptar:
                    pass
        if (idx == 3):
            price = pd.read_csv('price.csv',index_col=[0,1])
            manufcturer = self.ui.manufctorer_3.text()
            model = self.ui.model_3.text()
            price_val = self.ui.price_3.text()   
            col = price.index.names + list(price.columns)
            data = [manufcturer, model, price_val]
            new_price = pd.DataFrame(columns=col).set_index(price.index.names)
            new_price.loc[(manufcturer,model),:] = pd.Series(data={col[2] : price_val})
            test = pd.concat([price,new_price], axis=1, join='inner')
            if (list(test.index) == []):
                price= pd.concat([price,new_price], join='outer')
                price.to_csv(f'price.csv',index=True)
                rowPosition = self.ui.tableWidget_3.rowCount()
                self.ui.tableWidget_3.insertRow(rowPosition)
                self.ui.tableWidget_3.setVerticalHeaderItem(rowPosition, QTableWidgetItem(f'Цена {rowPosition + 1}'))
                for i in range(len(col)):
                    data_price_val = QTableWidgetItem(str(data[i]))
                    self.ui.tableWidget_3.setItem(rowPosition,i,data_price_val)
            else: 
                msg = QMessageBox(self)
                #msg.setWindowIcon(QIcon("im.png"))
                msg.setWindowTitle("Существующее значение")
                msg.setText("Данная цена уже существует")
                buttonAceptar = msg.addButton("Ок", QMessageBox.YesRole)
                msg.setDefaultButton(buttonAceptar)
                msg.exec_()
                if msg.clickedButton() == buttonAceptar:
                    pass
            


    #teste
    
    def change_cell_motor(self,row,column):
        #print(self.ui.tableWidget.model().index(row,column).data())
        motors = pd.read_csv('motors.csv',index_col=[0,1])
        motors.iat[row, column-2] = self.ui.tableWidget.model().index(row,column).data()
        motors.to_csv(f'motors.csv',index=True)
                        
    def change_cell_pneumatic(self,row,column):
        #print(self.ui.tableWidget.model().index(row,column).data())
        pneumatic = pd.read_csv('pneumatic.csv',index_col=[0,1])
        pneumatic.iat[row, column-2] = self.ui.tableWidget_2.model().index(row,column).data()
        pneumatic.to_csv(f'pneumatic.csv',index=True)
                        
                        
    def change_cell_price(self,row,column):
        #print(self.ui.tableWidget.model().index(row,column).data())
        price = pd.read_csv('price.csv',index_col=[0,1])
        price.iat[row, column-2] = self.ui.tableWidget_3.model().index(row,column).data()
        price.to_csv(f'price.csv',index=True)
                        
        
          
    def reload_table(self, name, table, type):
        motors = pd.read_csv(f'{name}.csv',index_col=[0,1])
        table.setColumnCount(len(motors.columns)+len(motors.index.names))
        table.setRowCount(len(motors.index))
        #print(len(motors.index))
        motor_number = range(len(motors.index))
        Rows_names = list(map(lambda x: f'{type} {x+1}', motor_number))
        table.setHorizontalHeaderLabels(motors.index.names + list(motors.columns))
        table.setVerticalHeaderLabels(Rows_names)
        for j,idx_val in zip(range(len(list(motors.index))),list(motors.index)):
              for i in range(len(idx_val)):
                    item_idx_val = QTableWidgetItem(str(idx_val[i]))
                    table.setItem(j,i,item_idx_val)
        for i in range(len(motors.columns)):
                for j, col_val in zip (range(len(motors[f'{motors.columns[i]}'])),motors[f'{motors.columns[i]}']):
                        item_col_val = QTableWidgetItem(str(col_val))
                        table.setItem(j,i + len(motors.index.names),item_col_val)
        motors.to_csv(f'{name}.csv',index=True)
                        
          

    def __init__(self):
        super().__init__()
        self.ui =  Ui_BD()
        self.ui.setupUi(self)
        
		#Заполнение интерфейса с Бд для моторов 
        self.reload_table('motors',self.ui.tableWidget,'Двигатель')
        
		#Заполнение интерфейса с Бд для Цилиндров 
        self.reload_table('pneumatic',self.ui.tableWidget_2,'Цилиндр')
        
		#Заполнение интерфейса с Бд для стоимости 
        self.reload_table('price',self.ui.tableWidget_3,'Цена')
        

        self.ui.tableWidget.cellChanged.connect(self.change_cell_motor)
        self.ui.tableWidget_2.cellChanged.connect(self.change_cell_pneumatic)
        self.ui.tableWidget_3.cellChanged.connect(self.change_cell_price)

        self.ui.add_1.clicked.connect(lambda: self.Add_string(1))
        self.ui.add_2.clicked.connect(lambda: self.Add_string(2))
        self.ui.add_3.clicked.connect(lambda: self.Add_string(3))