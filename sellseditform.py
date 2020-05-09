import os
from PyQt5 import QtWidgets, QtCore, QtGui
from editform import editForm
from dbcombobox import dbComboBox
from productscombo import productscombo

class sellsEditForm(editForm):
    def __init__(self, store, parrent=None):
        editForm.__init__(self, store, parrent=None)
        self.pixlabel = QtWidgets.QLabel()

        self.productscombo = productscombo(store)
        self.dateEdit = QtWidgets.QLineEdit()
        self.surnameEdit = QtWidgets.QLineEdit()
        self.nameEdit = QtWidgets.QLineEdit()
        self.secnameEdit = QtWidgets.QLineEdit()

        self._grid.addWidget(QtWidgets.QLabel(u'Изделие'), 0, 0)
        self._grid.addWidget(self.productscombo, 0, 1)

        self._grid.addWidget(QtWidgets.QLabel(u'Дата'), 1, 0)
        self._grid.addWidget(self.dateEdit, 1, 1)

        self._grid.addWidget(QtWidgets.QLabel(u'Фамилия'), 2, 0)
        self._grid.addWidget(self.surnameEdit, 2, 1)

        self._grid.addWidget(QtWidgets.QLabel(u'Имя'), 3, 0)
        self._grid.addWidget(self.nameEdit, 3, 1)
        
        self._grid.addWidget(QtWidgets.QLabel(u'Отчество'), 4, 0)
        self._grid.addWidget(self.secnameEdit, 4, 1)


        self.__pixVBox = QtWidgets.QVBoxLayout()
        self.__pixVBox.addWidget(self.pixlabel)
        self.__pixVBox.addStretch(1)
        self._hbox.insertLayout(0, self.__pixVBox)

    def update(self):
        if self.getCurrentCode() in self._store.getSellCodes():
            self.productscombo.setCurrentRec(self.getCurrentCode())
            self.dateEdit.setText(self._store.getSellDate(self.getCurrentCode()))
            self.surnameEdit.setText(self._store.getSellSurname(self.getCurrentCode()))
            self.nameEdit.setText(self._store.getSellName(self.getCurrentCode()))
            self.secnameEdit.setText(self._store.getSellSecname(self.getCurrentCode()))


    def save(self):
        
        self._store.setSellProduct(self.getCurrentCode(), self.productscombo.getCurrentCode())
        self._store.setSellDate(self.getCurrentCode(), self.dateEdit.text())
        self._store.setSellSurname(self.getCurrentCode(), self.surnameEdit.text())
        self._store.setSellName(self.getCurrentCode(), self.nameEdit.text())
        self._store.setSellSecname(self.getCurrentCode(), self.secnameEdit.text())


    def new(self):
        code = self._store.getSellNewCode()
        product = self._store.findProductByCode(self.productscombo.getCurrentCode())
        self._store.setSellDate(code, self.dateEdit.text())
        self._store.setSellSurname(code, self.surnameEdit.text())
        self._store.setSellName(code, self.nameEdit.text())
        self._store.setSellSecname(code, self.secnameEdit.text())
        self._store.newSell(code, product, date, surname, name, secname)

    def delr(self):
        self._store.removeSell(self.getCurrentCode())
        if self._store.getSellCodes(): self.setCurrentCode(self._store.getSellCodes()[0])
