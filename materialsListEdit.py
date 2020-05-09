from materials import materials
from materialslist import materialslist
from generalListEdit import generalListEdit

class materialsListEdit(materialslist, generalListEdit):
    def newRec(self, code=0, name='', priceForGramm=0):
        self.appendList(materials(code, name, priceForGramm))

    def getName(self, code):
        return self.findByCode(code).getName()

    def getPriceForGramm(self,code):
        return self.findByCode(code).getPriceForGramm()

    def setName(self, code, value):
        self.findByCode(code).setName(value)

    def setPriceForGramm(self, code, value):
        self.findByCode(code).setPriceForGramm(value)
        
    def getMaterialInfo(self, code):
        return self.FindByCode(code).getMaterialInfo()
