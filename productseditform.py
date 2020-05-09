import os
from PyQt5 import QtWidgets, QtCore, QtGui
from editform import editForm
from dbcombobox import dbComboBox
from materialscombo import materialscombo

class productsEditForm(editForm):
    def __init__(self, store, parrent=None):
        editForm.__init__(self, store, parrent=None)
        self.pixlabel = QtWidgets.QLabel()

        self.nameEdit = QtWidgets.QLineEdit()
        self.typelEdit = QtWidgets.QLineEdit()
        self.materialscombo = materialscombo(store)
        self.WeightSpin = QtWidgets.QSpinBox()
        self.WeightSpin.setRange(1, 1000000)
        self.PriceSpin = QtWidgets.QSpinBox()
        self.PriceSpin.setRange(1, 1000000)

        self._grid.addWidget(QtWidgets.QLabel(u'Название'), 0, 0)
        self._grid.addWidget(self.nameEdit, 0, 1)

        self._grid.addWidget(QtWidgets.QLabel(u'Тип'), 1, 0)
        self._grid.addWidget(self.typelEdit, 1, 1)

        self._grid.addWidget(QtWidgets.QLabel(u'Материал'), 2, 0)
        self._grid.addWidget(self.materialscombo, 2, 1)

        self._grid.addWidget(QtWidgets.QLabel(u'вес'), 3, 0)
        self._grid.addWidget(self.WeightSpin, 3, 1)
        
        self._grid.addWidget(QtWidgets.QLabel(u'Цена'), 4, 0)
        self._grid.addWidget(self.PriceSpin, 4, 1)


        self.__pixVBox = QtWidgets.QVBoxLayout()
        self.__pixVBox.addWidget(self.pixlabel)
        self.__pixVBox.addStretch(1)
        self._hbox.insertLayout(0, self.__pixVBox)

    def update(self):
        if self.getCurrentCode() in self._store.getProductCodes():
            self.nameEdit.setText(self._store.getProductName(self.getCurrentCode()))
            self.typelEdit.setText(self._store.getProductTypel(self.getCurrentCode()))
            self.materialscombo.setCurrentRec(self.getCurrentCode())
            self.WeightSpin.setValue(self._store.getProductWeight(self.getCurrentCode()))
            self.PriceSpin.setValue(self._store.getProductPrice(self.getCurrentCode()))


    def save(self):
        
        self._store.setProductName(self.getCurrentCode(), self.nameEdit.text())
        self._store.setProductTypel(self.getCurrentCode(), self.typelEdit.text())
        self._store.setProductMaterial(self.getCurrentCode(), self.materialscombo.getCurrentCode())
        self._store.setProductWeight(self.getCurrentCode(), int(self.WeightSpin.value()))
        self._store.setProductPrice(self.getCurrentCode(), int(self.PriceSpin.value()))


    def new(self):
        code = self._store.getProductNewCode()
        self._store.setProductName(code, self.nameEdit.text())
        self._store.setProductTypel(code, self.typelEdit.text())
        material = self._store.findMaterialByCode(self.materialscombo.getCurrentCode())
        self._store.setProductWeight(code, self.WeightSpin.value())
        self._store.setProductPrice(code, self.PriceSpin.value())

    def delr(self):
        self._store.removeProduct(self.getCurrentCode())
        if self._store.getProductCodes(): self.setCurrentCode(self._store.getProductCodes()[0])
