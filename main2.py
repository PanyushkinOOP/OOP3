from store import store
from dataxml import dataxml as data

sto1=store()
dat1=data()
dat1.read('old.xml',sto1)
sto1.newMaterial(code=5, name='Steal',priceForGramm=200)
sto1.newProduct(code=6,name='Starlight',type1='Ring',material=sto1.findMaterialByCode(4),weight=30,price=6000)
sto1.newSell(code=6,product=sto1.findProductByCode(6),date='10.08.2019',surname='Babulev',name='Nikolay',secname='Alexandrovich')
sto1.removeMaterial(5)
sto1.removeProduct(6)
sto1.removeSell(2)
dat1.write('new.xml',sto1)
