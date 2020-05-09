from general import general

class materials(general):
  def __init__(self, code=0, name='', priceForGramm=0):
   general.__init__(self, code)
   self.setName(name)
   self.setPriceForGramm(priceForGramm)

  def setName(self, value): self.__name = value
  def setPriceForGramm(self, value): self.__priceForGramm = value

  def getName(self): return self.__name
  def getPriceForGramm(self): return self.__priceForGramm

  def getMaterialInfo(self):
      s = ' '+ str(self.getPriceForGramm())
      return s
