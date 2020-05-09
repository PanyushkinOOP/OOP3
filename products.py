from general import general
from materials import materials

class products(general):
  def __init__(self, code=0, name='', typel='', material= None, weight='', price=''):
   general.__init__(self, code)
   self.setName(name)
   self.setTypel(typel)
   self.setMaterial(material)
   self.setWeight(weight)
   self.setPrice(price)

  def setName(self, val): self.__name = val
  def setTypel(self, val): self.__typel = val
  def setMaterial(self, val):
      self.__materials = val
  def setWeight(self, val): self.__weight = val
  def setPrice(self, val): self.__price = val

  def getName(self): return self.__name
  def getTypel(self): return self.__typel
  
  def getMaterialCode(self):
      if self.__materials: return self.__materials.getCode()
  def getMaterialName(self):
      if self.__materials: return self.__materials.getName()
  def getMaterialPriceForGramm(self):
      if self.__materials: return self.__materials.getPriceForGramm()
  def getMaterialInfo(self):
      if self.__materials: return self.__materials.getMaterialInfo()

  def getWeight(self): return self.__weight
  def getPrice(self): return self.__price


  def getProductInfo(self):
      s=' ' + ' ' + self.getMaterialInfo() + str(self.getWeight()) + str(self.getPrice())
      return s
