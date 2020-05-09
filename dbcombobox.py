from PyQt5 import QtWidgets, QtCore
from rowcode import rowCode

class dbComboBox(QtWidgets.QComboBox):
  def __init__(self,store,parent=None):
    QtWidgets.QComboBox.__init__(self,parent)
    self._store=store
    self.__rowCode=rowCode()
    self.setSizeAdjustPolicy(self.AdjustToContents)
  def clear(self):
    self.__rowCode.clear()
    QtWidgets.QComboBox.clear(self)
  def addItem(self,code,text):
    self.__rowCode.appendRowCode(self.count(),code)
    QtWidgets.QComboBox.addItem(self,text)
  def removeItem(self,index):
    self.__rowCode.removeRow(index)
    QtWidgets.QComboBox.removeItem(self,index)
  def getCurrentCode(self):return self.__rowCode.getCode(self.currentIndex())
  def setCurrentCode(self,code):
    if self.__rowCode.getRow(code):self.setCurrentIndex(self.__rowCode.getRow(code))
  def setCurrentRec(self,value):
    self.__currentRec=value
    self.update()
  def getCurrentRec(self):return self.__currentRec
  def update(self):pass
