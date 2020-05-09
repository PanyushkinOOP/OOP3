from PyQt5 import QtWidgets, QtCore
from editform import editForm


class materialsEditForm(editForm):
    def __init__(self, store, parrent=None):
        editForm.__init__(self, store, parrent=None)

        self.nameEdit = QtWidgets.QLineEdit()
        self.PriceForGrammSpin = QtWidgets.QSpinBox()
        self.PriceForGrammSpin.setRange(1, 1000000)

        self._grid.addWidget(QtWidgets.QLabel(u'Название'), 0, 0)
        self._grid.addWidget(self.nameEdit, 0, 1)
        self._grid.addWidget(QtWidgets.QLabel(u'ЦенаЗаГрамм'), 1, 0)
        self._grid.addWidget(self.PriceForGrammSpin, 1, 1)

    def update(self):
        if self.getCurrentCode() in self._store.getMaterialCodes():
            self.nameEdit.setText(self._store.getMaterialName(self.getCurrentCode()))
            self.PriceForGrammSpin.setValue(self._store.getMaterialPriceForGramm(self.getCurrentCode()))

    def save(self):
        self._store.setMaterialName(self.getCurrentCode(), self.nameEdit.text())
        self._store.setMaterialPriceForGramm(self.getCurrentCode(), int(self.PriceForGrammSpin.value()))

    def new(self):
        code = self._store.getMaterialNewCode()
        self._store.newMaterial(code)
        self._store.setMaterialName(code, self.nameEdit.text())
        self._store.setMaterialPriceForGramm(code, self.PriceForGrammSpin.value())

    def delr(self):
        self._store.removeMaterial(self.getCurrentCode())
        if self._store.getMaterialCodes(): self.setCurrentCode(self._store.getMaterialCodes()[0])
