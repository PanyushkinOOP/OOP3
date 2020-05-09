from sells import sells
from sellslist import sellsList
from generalListEdit import generalListEdit

class sellsListEdit(generalListEdit):
    def newRec(self, code=0, product= None, date= '', surname= '', name= '', secname=''):
        self.appendList(sells(code, product, date, surname, name, secname))

    def setProduct(self, code, value):
        self.findByCode(code).setProduct(value)

    def setDate(self, code, value):
        self.findByCode(code).setDate(value)

    def setSurname(self, code, value):
        self.findByCode(code).setSurname(value)

    def setName(self, code, value):
        self.findByCode(code).setName(value)
        
    def setSecname(self, code, value):
        self.findByCode(code).setSecname(value)
        
    def getProductCode(self, code):
        return self.findByCode(code).getProductCode()

    def getProductName(self, code):
        return self.findByCode(code).getProductName()

    def getProductTypel(self, code):
        return self.findByCode(code).getProductTypel()
    
    def getProductMaterial(self, code):
        return self.findByCode(code).getProductMaterial()

    def getProductWeight(self, code):
        return self.findByCode(code).getProductWeight()

    def getProductPrice(self, code):
        return self.findByCode(code).getProductPrice()

    def getProductInfo(self, code):
        return self.findByCode(code).getProductInfo()

    def getDate(self, code):
        return self.findByCode(code).getDate()

    def getSurname(self, code):
        return self.findByCode(code).getSurname()
    
    def getName(self, code):
        return self.findByCode(code).getName()
    
    def getSecname(self, code):
        return self.findByCode(code).getSecname()

    def getSellInfo(self, code):
        return self.findByCode(code).getSellInfo()
    
    def getListSellInfo(self):
      s = ''
      for code in self.getCodes():
       s += self.findByCode(code).getSellInfo() + ',\n'
      return s

 
