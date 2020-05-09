import cherrypy
import sys
sys.path.insert(0, "./store")
from store import store
from dataxml import dataxml
from materialspage import materialspage
from productspage import productspage
from sellspage import sellspage

class start:
    def __init__(self):
        self.__store=store()
        self.__dataxml=dataxml()
        self.__dataxml.read('old.xml',self.__store)
        self.materialspage=materialspage(self.__store)
        self.productspage=productspage(self.__store)
        self.sellspage=sellspage(self.__store)
    def index(self):
        return """
               <a href=materialspage\>Материал</a><br>
               <a href=productspage\>Изделие</a><br>
               <a href=sellspage\>Продажа</a><br>
        """
    index.exposed=True
root=start()
cherrypy.config.update({
        'log.screen': True,
})

cherrypy.tree.mount(root)
if __name__ == '__main__':
    cherrypy.engine.start()
    cherrypy.engine.block()

