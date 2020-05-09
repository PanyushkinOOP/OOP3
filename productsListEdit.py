from products import products
from productslist import productsList
from generalListEdit import generalListEdit

class productsListEdit(generalListEdit):
    def newRec(self, code=0, name= '', typel= '', material= None, weight= 0, price=0):
        self.appendList(products(code, name, typel, material, weight, price))

    def setName(self, code, value):
        self.findByCode(code).setName(value)

    def setTypel(self, code, value):
        self.findByCode(code).setTypel(value)
        
    def setMaterial(self, code, value):
        self.findByCode(code).setMaterial(value)

    def setWeight(self, code, value):
        self.findByCode(code).setWeight(value)
        
    def setPrice(self, code, value):
        self.findByCode(code).setPrice(value)
        
    def getName(self, code):
        return self.findByCode(code).getName()

    def getTypel(self, code):
        return self.findByCode(code).getTypel()
    
    def getMaterialCode(self, code):
        return self.findByCode(code).getMaterialCode()

    def getMaterialName(self, code):
        return self.findByCode(code).getMaterialName()

    def getMaterialPriceForGramm(self, code):
        return self.findByCode(code).getMaterialPriceForGramm()

    def getMaterialInfo(self, code):
        return self.findByCode(code).getMaterialInfo()
    
    def getWeight(self, code):
        return self.findByCode(code).getWeight()
    
    def getPrice(self, code):
        return self.findByCode(code).getPrice()

    def getProductInfo(self, code):
        return self.findByCode(code).getProductInfo()
    
    def getListProductInfo(self):
      s = ''
      for code in self.getCodes():
       s += self.findByCode(code).getProductInfo() + ',\n'
      return s

 
