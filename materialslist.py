from generallist import generalList

class materialslist(generalList):
  def getName(self,code):return self.findByCode(code).getName()
  def getPriceForGramm(self,code):return self.findByCode(code).getPriceForGramm()

  def getListMaterialsInfo(self):
    s = ''
    for code in self.getCodes():
      s += self.findByCode(code).getMaterialsInfo() + ',\n'
    return s[:-2]
