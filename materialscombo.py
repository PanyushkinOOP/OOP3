from dbcombobox import dbComboBox

class materialscombo(dbComboBox):
    def update(self):
        self.clear()
        for a in self._store.getMaterialCodes():
            self.addItem(a,self._store.getMaterialName(a))
        self.setCurrentCode(self._store.getProductMaterialCode(self.getCurrentRec()))
