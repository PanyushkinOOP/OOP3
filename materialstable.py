from PyQt5 import QtWidgets, QtCore
import sys,os
from dbtablewidget import dbTableWidget

class materialsTable(dbTableWidget):
     def __init__(self,store,parent=None):
          dbTableWidget.__init__(self,store,parent)
          self.setColumnCount(2)
          self.setHorizontalHeaderLabels(['название','ЦенаЗаГрамм'])
     def update(self):
          self.clearContents()
          self.setRowCount(len(self._store.getMaterialCodes()))
          r=0
          for a in self._store.getMaterialCodes():
               self.setItem(r,0,QtWidgets.QTableWidgetItem(str(self._store.getMaterialName(a))))
               self.setItem(r,1,QtWidgets.QTableWidgetItem(str(self._store.getMaterialPriceForGramm(a))))
               self.appendRowCode(r,a)
               r+=1
          self.resizeColumnsToContents()
          self.resizeRowsToContents()
          self.setCurrentCell(0,0)
