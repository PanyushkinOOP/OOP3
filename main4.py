from PyQt5 import QtWidgets, QtCore, QtGui
from datasql import datasql
from dataxml import dataxml
from store import store
from tab import tabWidget
import sys, os

app = QtWidgets.QApplication(sys.argv)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle(u'Магазин')
        self.dataxml=dataxml()
        self.datasql=datasql()
        self.store=store()
        
        self.tabWidget=tabWidget(self.store,self)
        self.tabWidget.currentChanged.connect(self.onChange)
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.update()

        self.newDatabase = QtWidgets.QAction(QtGui.QIcon(), "Новая", self)
        self.newDatabase.setStatusTip("Новая база данных")
        self.newDatabase.triggered.connect(self.newAction)

        self.openXml = QtWidgets.QAction(QtGui.QIcon(), "Открыть XML", self)
        self.openXml.setStatusTip("Открыть базу данных через XML")
        self.openXml.triggered.connect(self.openXmlAction)

        self.openSql = QtWidgets.QAction(QtGui.QIcon(), "Открыть SQL", self)
        self.openSql.setStatusTip("Открыть базу данных через SQL")
        self.openSql.triggered.connect(self.openSqlAction)

        self.saveXml = QtWidgets.QAction(QtGui.QIcon(),"Сохранить XML", self)
        self.saveXml.setStatusTip("Сохранить базу данных в XML")
        self.saveXml.triggered.connect(self.saveXmlAction)

        self.saveSql = QtWidgets.QAction(QtGui.QIcon(), "Сохранить SQL", self)
        self.saveSql.setStatusTip("Сохранить базу данных в SQL")
        self.saveSql.triggered.connect(self.saveSqlAction)

        self.menu = self.menuBar()
        self.menuFile = self.menu.addMenu("&Файл")
        self.menuFile.addAction(self.newDatabase)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.openSql)
        self.menuFile.addAction(self.openXml)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.saveSql)
        self.menuFile.addAction(self.saveXml)

        self.statusBar()

    def newAction(self):
        self.store.clear()
        self.tabWidget.update()

    def openXmlAction(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть через XML", os.getcwd(), "*.xml")

        if filename:
            self.store.clear()
            self.dataxml.read(filename[0],self.store)
            self.tabWidget.update()

    def openSqlAction(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть через SQL", os.getcwd(), "*.sqlite")

        if filename:
            self.store.clear()
            self.datasql.read(filename[0],self.store)
            self.tabWidget.update()

    def saveXmlAction(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить как XML", os.getcwd(), "*.xml")
        if filename:self.dataxml.write(filename[0],self.store)

    def saveSqlAction(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить как SQL", os.getcwd(), "*.sqlite")
        if filename:self.datasql.write(filename[0],self.store)
        
    def onChange(self, i):
        self.tabWidget.update()

       
mw=Window()
mw.show()
sys.exit(app.exec_())
