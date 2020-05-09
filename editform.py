from PyQt5 import QtWidgets, QtCore

class editForm(QtWidgets.QWidget):
  def __init__(self,store,parrent=None):
    QtWidgets.QWidget.__init__(self,parrent)
    self._store=store
    self._grid=QtWidgets.QGridLayout()
    self._vbox=QtWidgets.QVBoxLayout()
    self._hbox=QtWidgets.QHBoxLayout()
    self._vbox.addLayout(self._grid)
    self._vbox.addStretch(1)
    self._hbox.addLayout(self._vbox)
    self.setLayout(self._hbox)
  def setCurrentCode(self,value):
    self.__currentCode=value
    self.update()
  def update(self):pass
  def getCurrentCode(self):return self.__currentCode
 
