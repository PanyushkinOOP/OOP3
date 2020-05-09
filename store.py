from materialsListEdit import materialsListEdit
from productsListEdit import productsListEdit
from sellsListEdit import sellsListEdit

class store:
    def __init__(self):
        self.__materials = materialsListEdit()
        self.__products = productsListEdit()
        self.__sells = sellsListEdit()

    def removeMaterial(self, code):
        a = True
        for c in self.__products.getCodes():
            if code == self.__products.getMaterialCode(c):
                a = False
                break
        if a:
            self.__materials.removeList(code)

    def removeProduct(self, code):
        a = True
        for c in self.__sells.getCodes():
            if code == self.__sells.getProductCode(c):
                a = False
                break
        if a:
            self.__products.removeList(code)


    def clear(self):
        self.__materials.clear()
        self.__products.clear()
        self.__sells.clear()

    def newMaterial(self, code=0, name='', priceForGramm=0):
        self.__materials.newRec(code, name, priceForGramm)

    def findMaterialByCode(self, code):
        return self.__materials.findByCode(code)

    def getMaterialNewCode(self):
        return self.__materials.getNewCode()

    def getMaterialCodes(self):
        return self.__materials.getCodes()

    def getMaterialName(self, code):
        return self.__materials.getName(code)

    def getMaterialPriceForGramm(self, code):
        return self.__materials.getPriceForGramm(code)

    def getMaterialInfo(self, code):
        return self.__materials.getListMaterialsInfo(code)

    def setMaterialName(self, code, value):
        self.__materials.setName(code, value)

    def setMaterialPriceForGramm(self, code, value):
        self.__materials.setPriceForGramm(code, value)
    
    def getListMaterialsInfo(self):
        return self.__materials.getListMaterialsInfo()

    def newProduct(self, code=0, name='', typel='', material= None, weight=0, price=0):
        self.__products.newRec(code, name, typel, material, weight, price)

    def findProductByCode(self, code):
        return self.__products.findByCode(code)

    def setProductName(self, code, value):
        self.__products.setName(code, value)

    def setProductTypel(self, code, value):
        self.__products.setTypel(code, value)

    def setProductMaterial(self, code, val):
        self.__products.setMaterial(code, self.findMaterialByCode(val))

    def setProductWeight(self, code, value):
        self.__products.setWeight(code, value)
        
    def setProductPrice(self, code, value):
        self.__products.setPrice(code, value)

    def getProductCodes(self):
        return self.__products.getCodes()

    def getProductNewCode(self):
        return self.__products.getNewCode()

    def getProductName(self, code):
        return self.__products.getName(code)

    def getProductTypel(self, code):
        return self.__products.getTypel(code)

    def getProductMaterialCode(self, code):
        return self.__products.getMaterialCode(code)

    def getProductMaterialName(self, code):
        return self.__products.getMaterialName(code)

    def getProductMaterialPriceForGramm(self, code):
        return self.__products.getMaterialPriceForGramm(code)

    def getProductMaterialInfo(self, code):
        return self.__products.getMaterialInfo(code)
    
    def getProductWeight(self, code):
        return self.__products.getWeight(code)
    
    def getProductPrice(self, code):
        return self.__products.getPrice(code)

    def getProductInfo(self, code):
        return self.__products.getProductInfo(code)

#############################################

    def removeSell(self, code):
        self.__sells.removeList(code)

    def newSell(self, code=0, product= None, date= '', surname= '', name= '', secname= ''):
        self.__sells.newRec(code,product,date,surname,name,secname)

    def findSellByCode(self, code):
        return self.__sells.findByCode(code)

    def setSellProduct(self, code, val):
        self.__sells.setProduct(code, self.findProductByCode(val))

    def setSellDate(self, code, value):
        self.__sells.setDate(code, value)

    def setSellSecname(self, code, value):
        self.__sells.setSecname(code, value)

    def setSellName(self, code, value):
        self.__sells.setName(code, value)
        
    def setSellSurname(self, code, value):
        self.__sells.setSurname(code, value)

    def getSellCodes(self):
        return self.__sells.getCodes()

    def getSellNewCode(self):
        return self.__sells.getNewCode()
    
    def getSellProductCode(self, code):
        return self.__sells.getProductCode(code)

    def getSellProductName(self, code):
        return self.__sells.getProductName(code)

    def getSellProductTypel(self, code):
        return self.__sells.getProductTypel(code)

    def getSellProductMaterial(self, code):
        return self.__sells.getProductMaterial(code)

    def getSellProductWeight(self, code):
        return self.__sells.getProductWeight(code)
    
    def getSellProductPrice(self, code):
        return self.__sells.getProductPrice(code)

    def getSellProductInfo(self, code):
        return self.__sells.getProductInfo(code)

    def getSellDate(self, code):
        return self.__sells.getDate(code)

    def getSellSecname(self, code):
        return self.__sells.getSecname(code)
    
    def getSellName(self, code):
        return self.__sells.getName(code)
    
    def getSellSurname(self, code):
        return self.__sells.getSurname(code)

    def getSellInfo(self, code):
        return self.__sells.getSellInfo(code)

    def infoMaterials(self):
        return self.__materials.getListMaterialsInfo()
    def infoProducts(self):
        return self.__products.getListProductInfo()
    def infoSells(self):
        return self.__sells.getListSellInfo()
