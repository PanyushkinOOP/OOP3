from general import general
from products import products

class sells(general):
  def __init__(self, code=0, product= None, date='', surname='', name='', secname=''):
   general.__init__(self, code)
   self.setProduct(product)
   self.setDate(date)
   self.setSurname(surname)
   self.setName(name)
   self.setSecname(secname)

  def setProduct(self, val):
      self.__products = val
  def setDate(self, val): self.__date = val
  def setSurname(self, val): self.__surname = val
  def setName(self, val): self.__name = val
  def setSecname(self, val): self.__secname = val
  
  def getProductCode(self):
      if self.__products: return self.__products.getCode()
  def getProductName(self):
      if self.__products: return self.__products.getName()
  def getProductTypel(self):
      if self.__products: return self.__products.getTypel()
  def getProductMaterial(self):
      if self.__products: return self.__products.getMaterial()
  def getProductWeight(self):
      if self.__products: return self.__products.getWeight()
  def getProductPrice(self):
      if self.__products: return self.__products.getPrice()
  def getProductInfo(self):
      if self.__products: return self.__products.getProductInfo()

  def getDate(self): return self.__date
  def getSurname(self): return self.__surname
  def getName(self): return self.__name
  def getSecname(self): return self.__secname


  def getSellInfo(self):
      s=self.getProductInfo() + ' ' + ' ' + ' ' + ' '
      return s
