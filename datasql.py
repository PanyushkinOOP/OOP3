import os
import sqlite3 as db

emptydb = """
PRAGMA foreign_keys = ON;

create table materials
(code integer primary key,
 name text,
 priceForGramm integer);

create table product
(code integer primary key,
 name text,
 type1 text,
 weight integer,
 price integer,
 material integer);

create table sell
(code integer primary key,
 date text,
 surname text,
 name text,
 secname text,
 product integer references product(code) on update cascade on delete set null);
"""

class datasql:
 def read(self,inp,sto):
  conn = db.connect(inp)
  curs = conn.cursor()
  curs.execute("select code,name,priceForGramm from materials")
  data=curs.fetchall()
  for r in data:sto.newMaterial(r[0],r[1],r[2])
  curs.execute("select code,name,type1,material,weight,price from product")
  data=curs.fetchall()
  for r in data:
      sto.newProduct(r[0],r[1],r[2],sto.findMaterialByCode(int(r[3])),r[4],r[5])
  curs.execute("select code,product,date,surname,name,secname from sell")
  data=curs.fetchall()
  for r in data:sto.newSell(r[0],sto.findProductByCode(int(r[1])),r[2],r[3],r[4],r[5])
  
 def write(self,out,sto):
  conn = db.connect(out)
  curs = conn.cursor()
  curs.executescript(emptydb)
  for c in sto.getMaterialCodes():
   curs.execute("insert into materials(code,name,priceForGramm) values('%s','%s','%s')"%(
     str(c),
     sto.getMaterialName(c),
     int(sto.getMaterialPriceForGramm(c))))
  for c in sto.getProductCodes():
    curs.execute("insert into product(code,name,type1,material,weight,price) values('%s','%s','%s','%s','%s','%s')"%(
      str(c),
      sto.getProductName(c),
      sto.getProductType(c),
      int(sto.getProductMaterialCode(c)),
      int(sto.getProductPrice(c)),
      int(sto.getProductWeight(c))))
  for c in sto.getSellCodes():
    curs.execute("insert into sell(code,product,date,surname,name,secname) values('%s','%s','%s','%s','%s','%s')"%(
      str(c),
      int(sto.getSellProductCode(c)),
      sto.getSellDate(c),
      sto.getSellSurname(c),
      sto.getSellName(c),
      sto.getSellSecname(c)))
    
  conn.commit()
  conn.close()
