from PyQt5 import QtWidgets, QtCore
import sys,os
from buttonform import buttonForm

class page(QtWidgets.QWidget):
    def __init__(self,bank,table,editform,parrent=None):
        QtWidgets.QWidget.__init__(self,parrent)
        self.__VBox=QtWidgets.QVBoxLayout()
        self.__HBox=QtWidgets.QHBoxLayout()
        self.__table=table
        self.__editForm=editform
        self.__buttonForm=buttonForm(self)

        self.__VBox.addWidget(self.__table)
        self.__HBox.addWidget(self.__editForm)
        self.__HBox.addWidget(self.__buttonForm)
        self.__VBox.addLayout(self.__HBox)
        self.setLayout(self.__VBox)
        
        #self.__table.curRowCh.connect(self.curRowCh)

        self.__buttonForm.editRec.connect(self.editRec)
        self.__buttonForm.newRec.connect(self.newRec)
        self.__buttonForm.delRec.connect(self.delRec)
        
    def curRowCh(self):self.__editForm.setCurrentCode(self.__table.getCurrentCode())
    def update(self):
        self.__table.update()
        self.__editForm.setCurrentCode(self.__table.getCurrentCode())
    def newRec(self):
        self.__editForm.new()
        self.__table.update()
    def editRec(self):
        self.__editForm.save()
        self.__table.update()
    def delRec(self):
        self.__editForm.delr()
        self.__table.update()
