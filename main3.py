from store import store
from datasql import datasql as data
from dataxml import dataxml as data2

sto1=store()
dat1=data()
dat2=data2()
dat2.read('old.xml',sto1)
dat1.write('old.sqlite',sto1)
sto1.clear()
dat1.read('old.sqlite',sto1)
dat2.write('new.xml',sto1)
#for s in sto1.getBibliostrs():
# print(s)
