from PyQt5 import QtWidgets, QtCore
from rowcode import rowCode

class dbTableWidget(QtWidgets.QTableWidget):
 def __init__(self,store,parent=None):
   QtWidgets.QTableWidget.__init__(self)
   self.__rowCode=rowCode()
   self._store=store
   #self.currentCellChanged.connect(self.curRowCh)
   self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
 def clearContents(self):
   self.__rowCode.clear()
   QtWidgets.QTableWidget.clearContents(self)
 def getCodes(self):return self.__rowCode.getCodes()
 def getCurrentCode(self):return self.__rowCode.getCode(self.currentRow())
 def appendRowCode(self,row,code):self.__rowCode.appendRowCode(row,code)
 def curRowCh(self):
        self.curRowChSignal.emit()
