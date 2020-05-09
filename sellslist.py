from generallist import generalList

class sellsList(generalList):
  def getProduct(self,code):return self.findByCode(code).getProduct()
  def getDate(self,code):return self.findByCode(code).getDate()
  def getSurname(self,code):return self.findByCode(code).getSurname() 
  def getName(self,code):return self.findByCode(code).getName()
  def getSecname(self,code):return self.findByCode(code).getSecname()

  def getListSellsInfo(self):
    s = ''
    for code in self.getCodes():
      s += self.findByCode(code).getSellsInfo() + ',\n'
    return s[:-2]
