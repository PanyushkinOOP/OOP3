from PyQt5 import QtWidgets, QtCore
import sys,os
sys.path.insert(0, "./store")
from store import store
from datasql import datasql
from materialstable import materialsTable as testwidget

app = QtWidgets.QApplication(sys.argv)

sto1=store()
data=datasql()
data.read('old.sqlite',sto1)

tw=testwidget(sto1)
tw.update()
tw.show()

sys.exit(app.exec_())
