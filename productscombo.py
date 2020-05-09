from dbcombobox import dbComboBox

class productscombo(dbComboBox):
    def update(self):
        self.clear()
        for a in self._store.getProductCodes():
            self.addItem(a,self._store.getProductName(a))
        self.setCurrentCode(self._store.getSellProductCode(self.getCurrentRec()))
