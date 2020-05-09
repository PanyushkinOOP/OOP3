from PyQt5 import QtWidgets, QtCore
import sys,os
from dbtablewidget import dbTableWidget

class productsTable(dbTableWidget):
  def __init__(self,store):
    dbTableWidget.__init__(self,store)
    self.setColumnCount(5)
    self.setHorizontalHeaderLabels(['название','тип','материал','вес','цена'])
  def update(self):
    self.clearContents()
    self.setRowCount(len(self._store.getProductCodes()))
    r=0
    for a in self._store.getProductCodes():
      self.setItem(r,0,QtWidgets.QTableWidgetItem(str(self._store.getProductName(a))))
      self.setItem(r,1,QtWidgets.QTableWidgetItem(str(self._store.getProductTypel(a))))
      self.setItem(r,2,QtWidgets.QTableWidgetItem(str(self._store.getProductMaterialCode(a))))
      self.setItem(r,3,QtWidgets.QTableWidgetItem(str(self._store.getProductWeight(a))))
      self.setItem(r,4,QtWidgets.QTableWidgetItem(str(self._store.getProductPrice(a))))
      self.appendRowCode(r,a)
      r+=1
    self.resizeColumnsToContents()
    self.resizeRowsToContents()
    self.setCurrentCell(0,0)
