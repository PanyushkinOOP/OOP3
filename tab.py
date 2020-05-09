from PyQt5 import QtWidgets, QtCore
import sys,os
from page import page
from materialseditform import materialsEditForm
from materialstable import materialsTable
from productseditform import productsEditForm
from productstable import productsTable
from sellseditform import sellsEditForm
from sellstable import sellsTable

class tabWidget(QtWidgets.QTabWidget):
    def __init__(self,store,parent=None):
        QtWidgets.QTabWidget.__init__(self,parent)
        self.__materialsPage=page(store,materialsTable(store),materialsEditForm(store))
        self.addTab(self.__materialsPage,u"Материал")
        self.__productsPage=page(store,productsTable(store),productsEditForm(store))
        self.addTab(self.__productsPage,u"Изделие")
        self.__sellsPage=page(store,sellsTable(store),sellsEditForm(store))
        self.addTab(self.__sellsPage,u"Продажа")
    def update(self):
        self.__materialsPage.update()
        self.__productsPage.update()
        self.__sellsPage.update()
