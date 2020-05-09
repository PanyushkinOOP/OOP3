class productspage:
    def __init__(self,store):
        self.__sto=store

    def index(self):
        s='<a href=..>%s</a>/<a href=addform>%s</a>'%(u'назад',u'добавить')
        s+='<table><th bgcolor=gray></th><th bgcolor=gray>%s</th><th bgcolor=gray>%s</th><th bgcolor=gray>%s</th><th bgcolor=gray>%s</th><th bgcolor=gray>%s</th>'%(u'название',u'тип',u'материал',u'вес',u'цена')
        r=1
        bg=''
        for c in self.__sto.getProductCodes():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'%self.__sto.getProductName(c)
            s+='<td>%s</td>'%self.__sto.getProductTypel(c)
            s+='<td>%s</td>'%self.__sto.getProductMaterialCode(c)
            s+='<td>%s</td>'%self.__sto.getProductWeight(c)
            s+='<td>%s</td>'%self.__sto.getProductPrice(c)
            s+='<td><a href=editform?code=%s>%s</a></td>'%(c,u'редактировать')
            s+='<td><a href=delr?code=%s>%s</a></td></tr>'%(c,u'удалить')
            r+=1
            if bg:bg=''
            else:bg=' bgcolor=silver'
        s+='</table>'
        return s
    
    index.exposed=True

    def materialsCombo(self,code=0):
        s='<select name=material>'
        for c in self.__sto.getMaterialCodes():
            if (code in self.__sto.getProductCodes())and(c==self.__sto.getProductMaterialCode(code)):v=' selected'
            else:v=''
            s+='<option%s value=%s>%s</option>'%(v,str(c),self.__sto.getMaterialName(c))
        s+='</select>'
        return s

    def productform(self,code=0,add=True):
        name,typel,material,weight,price='','',0,0,0
        if add:a='addaction'
        else: a='editaction?code=%s'%code
        if code in self.__sto.getProductCodes():
            name=self.__sto.getProductName(code)
            typel=self.__sto.getProductTypel(code)
            material=self.__sto.getProductMaterialCode(code)
            weight=self.__sto.getProductWeight(code)
            price=self.__sto.getProductPrice(code)
        s = '''<form action=%s method=post>
             <table>
                <tr><td>%s</td><td><input type=text name=name value='%s'></td></tr>
                <tr><td>%s</td><td><input type=text name=typel value='%s'></td></tr>
                <tr><td>%s</td><td><input type=text name=material value='%s'></td></tr>
                <tr><td>%s</td><td><input type=number name=weight value=%s></td></tr>
                <tr><td>%s</td><td><input type=number name=price value=%s></td></tr>
                <tr><td><input type=submit></td><td></td></tr>
            </table>
            </form>''' % (a, u'название', name, u'тип', typel,u'материал',material, u'вес', str(weight), u'цена', str(price))
        return s

    def addaction(self,name,typel,material,weight,price):
        code=self.__sto.getProductNewCode()
        self.__sto.newProduct(code)
        self.__sto.setProductName(code,name)
        self.__sto.setProductTypel(code,typel)
        self.__sto.setProductMaterial(code,int(material))
        self.__sto.setProductWeight(code,weight)
        self.__sto.setProductPrice(code,price)
        return 'изделие добавлено<br><a href=index>назад</a>'
    
    addaction.exposed=True

    def addform(self):
        s=u'Добавить новое изделие<br>'
        s+=self.productform(0)
        return s
    
    addform.exposed=True

    def editform(self,code):
        s=u'Редактировать изделие<br>'
        s+=self.productform(int(code),False)
        return s

    editform.exposed=True
  
    def editaction(self,code,name,typel,material,weight,price):
        self.__sto.setProductName(int(code),name)
        self.__sto.setProductTypel(int(code),typel)
        self.__sto.setProductMaterial(int(code),int(material))
        self.__sto.setProductWeight(int(code),weight)
        self.__sto.setProductPrice(int(code),price)
        return 'изделие изменено<br><a href=index>назад</a>'
    
    editaction.exposed=True

    def delr(self,code):
        self.__sto.removeProduct(int(code))
        return 'изделие удалено<br><a href=index>назад</a>'
    
    delr.exposed=True
