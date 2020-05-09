
import os,xml.dom.minidom
import base64

class dataxml:
    def read(self,inp,sto):
        dom=xml.dom.minidom.parse(inp)
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
            if(node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='material'):
                code,name,PriceForGramm=0,"",0
                for t in node.attributes.items():
                     if t[0]=="code":
                         code=int(t[1])
                     if t[0]=="name":
                         name=t[1]
                     if t[0]=="PriceForGramm":
                         PriceForGramm=t[1]
                sto.newMaterial(code,name,PriceForGramm)
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='product'):
                code,name,type1,material,weight,price=0,"","",None,0,0
                for t in node.attributes.items():
                    if t[0]=="code":
                        code=int(t[1])
                    if t[0]=="name":
                        name=t[1]
                    if t[0]=="type":
                        type1=t[1]
                    if t[0]=="material":
                        material=sto.findMaterialByCode(int(t[1]))
                    if t[0]=="weight":
                        weight=t[1]
                    if t[0]=="price":
                        price=t[1]
                sto.newProduct(code,name,type1,material,weight,price)
            if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName=='sell'):
                code,product,date,surname,name,secname=0,None,"","","",""
                for t in node.attributes.items():
                    if t[0]=="code":
                        code=int(t[1])
                    if t[0]=="product":
                        product=sto.findProductByCode(int(t[1]))
                    if t[0]=="date":
                        date=t[1]
                    if t[0]=="surname":
                        surname=t[1]
                    if t[0]=="name":
                        name=t[1]
                    if t[0]=="secname":
                        secname=t[1]
                sto.newSell(code,product,date,surname,name,secname)

    def write(self,out,sto):
        dom=xml.dom.minidom.Document()
        root=dom.createElement("store")
        dom.appendChild(root)
        for c in sto.getMaterialCodes():
            mt=dom.createElement("material")
            mt.setAttribute('code',str(c))
            mt.setAttribute('name',sto.getMaterialName(c))
            mt.setAttribute('PriceForGramm',str(sto.getMaterialPriceForGramm(c)))
            root.appendChild(mt)
        for c in sto.getProductCodes():
            pro=dom.createElement("product")
            pro.setAttribute('code',str(c))
            pro.setAttribute('name',sto.getProductName(c))
            pro.setAttribute('type',sto.getProductType(c))
            pro.setAttribute('material',str(sto.getProductMaterialCode(c)))
            pro.setAttribute('weight',str(sto.getProductWeight(c)))
            pro.setAttribute('price',str(sto.getProductPrice(c)))
            root.appendChild(pro)
        for c in sto.getSellCodes():
            sel=dom.createElement("sell")
            sel.setAttribute('code',str(c))
            sel.setAttribute('product',str(sto.getSellProductCode(c)))
            sel.setAttribute('date',sto.getSellDate(c))
            sel.setAttribute('surname',sto.getSellSurname(c))
            sel.setAttribute('name',sto.getSellName(c))
            sel.setAttribute('secname',sto.getSellSecname(c))
            root.appendChild(sel)
        f = open(out,"w")
        f.write(dom.toprettyxml(encoding='utf-8'))
