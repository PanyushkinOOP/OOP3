from PyQt4 import QtGui, QtCore
import sys,os
from buttonform import buttonForm

class page(QtGui.QWidget):
  def __init__(self,library,table,editform,parrent=None):
    QtGui.QWidget.__init__(self,parrent)
    self.__VBox=QtGui.QVBoxLayout()
    self.__HBox=QtGui.QHBoxLayout()
    self.__table=table
    self.__editForm=editform
    self.__buttonForm=buttonForm(self)

    self.__VBox.addWidget(self.__table)
    self.__HBox.addWidget(self.__editForm)
    self.__HBox.addWidget(self.__buttonForm)
    self.__VBox.addLayout(self.__HBox)
    self.setLayout(self.__VBox)
    self.connect(self.__table,QtCore.SIGNAL('curRowCh()'),self.curRowCh)
    self.connect(self.__buttonForm,QtCore.SIGNAL('editRec()'),self.editRec)
    self.connect(self.__buttonForm,QtCore.SIGNAL('newRec()'),self.newRec)
    self.connect(self.__buttonForm,QtCore.SIGNAL('delRec()'),self.delRec)
    
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
