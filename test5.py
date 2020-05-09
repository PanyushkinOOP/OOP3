from PyQt5 import QtWidgets, QtCore
import sys,os
sys.path.insert(0, "./store")
from store import store
from datasql import datasql
from sellseditform import sellsEditForm as testwidget

app = QtWidgets.QApplication(sys.argv)

sto1=store()
data=datasql()
data.read('old.sqlite',sto1)

tw=testwidget(sto1)
tw.setCurrentCode(1)
tw.show()

sys.exit(app.exec_())
