# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
import sys,os

class buttonForm(QtWidgets.QWidget):
    newRec=QtCore.pyqtSignal()
    editRec=QtCore.pyqtSignal()
    delRec=QtCore.pyqtSignal()
    def __init__(self,parrent=None):
        QtWidgets.QWidget.__init__(self,parrent)
        self.__buttonsVBox=QtWidgets.QVBoxLayout()
    
        self.__newButton=QtWidgets.QPushButton(u"Добавить")
        self.__editButton=QtWidgets.QPushButton(u"Изменить")
        self.__delButton=QtWidgets.QPushButton(u"Удалить")
    
        self.__buttonsVBox.addWidget(self.__newButton)
        self.__buttonsVBox.addWidget(self.__editButton)
        self.__buttonsVBox.addWidget(self.__delButton)
        self.__buttonsVBox.addStretch(1)
    
        self.setLayout(self.__buttonsVBox)
    
        self.__newButton.clicked.connect(self.newClick)
        self.__editButton.clicked.connect(self.editClick)
        self.__delButton.clicked.connect(self.delClick)
    
    def newClick(self):self.newRec.emit()
    def editClick(self):self.editRec.emit()
    def delClick(self):self.delRec.emit()