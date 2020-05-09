from PyQt5 import QtWidgets, QtCore
import sys,os
from dbtablewidget import dbTableWidget

class sellsTable(dbTableWidget):
 def __init__(self,store,parrent=None):
   dbTableWidget.__init__(self,store,parrent)
   self.setColumnCount(5)
   self.setHorizontalHeaderLabels([u'изделие',u'дата',u'фамилия',u'имя',u'отчество'])
 def update(self):
   self.clearContents()
   self.setRowCount(len(self._store.getSellCodes()))
   r=0
   for a in self._store.getSellCodes():
     self.setItem(r,0,QtWidgets.QTableWidgetItem(str(self._store.getSellProductName(a))))
     self.setItem(r,1,QtWidgets.QTableWidgetItem(str(self._store.getSellDate(a))))
     self.setItem(r,2,QtWidgets.QTableWidgetItem(str(self._store.getSellSurname(a))))
     self.setItem(r,3,QtWidgets.QTableWidgetItem(str(self._store.getSellName(a))))
     self.setItem(r,4,QtWidgets.QTableWidgetItem(str(self._store.getSellSecname(a))))
     self.appendRowCode(r,a)
     r+=1
   self.resizeColumnsToContents()
   self.resizeRowsToContents()
   self.setCurrentCell(0,0)
