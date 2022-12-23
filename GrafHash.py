

from ElementData import ElementData
import math

class GrafHash:

    __slots__ = '__nodes', '__e_out', '__e_in'

    class Vertex:
        __slots__ = '__uuid', '__edata'

        def __init__(self, k : str, elementData : ElementData):
            self.__uuid = k
            self.__edata = elementData
        @property
        def uuid(self):
            return self.__uuid
        
        @uuid.setter
        def uuid(self, value):
            self.__uuid = value
        
        @property
        def data(self):
            return self.__edata
        
        @data.setter
        def data(self, value):
            self.__edata = value

        def __hash__(self):
            return hash(self.__edata.filename)
            
        def __eq__(self, other):
            return self.__edata.__eq__(other)
            
        def __ne__(self):
            return self.__edata.__ne__()
            
        def __lt__(self):
            return self.__edata.__lt__()
            
        def __str__(self):
            return " Node - ( "+str(self.__uuid)+": "+str(self.__edata.__str__())+" ) "

    def __init__(self, ln = [], lv = [], lp = [], digraf = True): 
        self.__nodes = {}
        self.__e_out = {}
        self.__e_in={}
        
    @property
    def nodes(self):
        return self.__nodes
    
    @nodes.setter
    def nodes(self, value):
        self.__nodes = value
        
    @property
    def e_out(self):
        return self.__e_out
    
    @e_out.setter
    def e_out(self, value):
        self.__e_out = value
        
    @property
    def e_in(self):
        return self.__e_in
    
    @e_in.setter
    def e_in(self, value):
        self.__e_in = value

    def __repr__(self):
        cad = "===============GRAF===================\n"

        for it in self.__e_out.items():
            cad1 = "__________________________________________________________________________________\n"
            cad1 = cad1+str(it[0])+" : "
            for valor in it[1].items():
                cad1 = cad1+str(str(valor[0])+"(" + str(valor[1])+")"+" , ")

            cad = cad + cad1 + "\n"

        return cad

    def __iter__(self):
        # for n, e in self.nodes:
        #     yield n, e
        return self.nodes.__iter__()

    def __len__(self) -> int:
        return len(self.nodes)
    
    def edges_out(self,x):
        return iter(self.__e_out[x].__iter__())

    def insert_vertex(self, key : str , e: ElementData):
        if type(e) is not ElementData:
            raise TypeError("Not ElementData type")
            
        v = self.Vertex(key, e)
        self.__nodes[key] = v
        self.__e_out[key] = {}
        self.__e_in[key] = {}
        return v
        

    def insert_edge(self, n1, n2, p=1):
        if (n2 in self.__e_out[n1]):
            self.__e_out[n1][n2] = self.__e_out[n1][n2] + 1
            self.__e_in[n2][n1] = self.__e_in[n2][n1] + 1
        elif (n1 in self.__e_out[n2]): 
            self.__e_out[n2][n1] = self.__e_out[n2][n1] + 1
            self.__e_in[n1][n2] = self.__e_in[n1][n2] + 1
        else:
            self.__e_out[n1][n2] = p
            self.__e_in[n2][n1] = p
            
    def minDistance(self, dist, visitat):

        minim = math.inf
        res = ""
        for node,distancia in dist.items():
            if node not in visitat and distancia < minim:
                minim = distancia
                res = node
        return res
    
    def dijkstraModif(self,n1,n3):        
        dist = {}
        for nAux in self.__e_out:
            dist[nAux] = math.inf
        visitat = {}
        dist[n1] = 0
        pred = {}
        pred[n1] = None
        count = 1
        
        while count < len(self.__nodes) - 1:
            nveiAct = self.minDistance(dist, visitat)
            visitat[nveiAct] = True
            
            if nveiAct == n3:
                return dist, pred
            
            elif nveiAct in self.__e_out:
                for n2, p2 in self.__e_out[nveiAct].items():
                    if n2 not in visitat:
                        if (dist[nveiAct] + p2 < dist[n2]):
                            dist[n2] = dist[nveiAct] + p2
                            pred[n2] = nveiAct
            count += 1
            
        return dist, pred
            

    def camiMesCurt(self,n1, n2):
        cami = []
        if n1 in self.__nodes.keys() and n2 in self.__nodes.keys():
            dist, predecessor = self.dijkstraModif(n1,n2)
            
            if n2 in predecessor:
                cami.append(n2)
                nodeAct = n2
                while not nodeAct == n1:
                    vei = predecessor[nodeAct]
                    cami.append(vei)
                    nodeAct = vei
            cami.reverse()
        return cami   
    
    def DFS(self, nInicial):
        visitat = {} 
        recorregut = []
        if nInicial in self.nodes:
            visitat[nInicial] = None
            recorregut.append(nInicial)
            self.DFSRec(nInicial, visitat, recorregut)
        return visitat, recorregut

    def DFSRec(self, n1, visitat, recorregut):                    
        for adjacent in self.__e_out[n1]:
            if adjacent not in visitat:
                recorregut.append(adjacent)
                visitat[adjacent] = n1
                self.DFSRec(adjacent, visitat, recorregut)
        
    def vertices(self):
        return self.nodes.__iter__()

    def edges(self, x):

        return iter(self.e_out[x].__iter__())

    def get(self, key) -> ElementData:
        return self.nodes[key]._valor

    def __contains__(self, key):
        try:
            self.nodes[key]
            return True
        except KeyError:
            return False 

    def __getitem__(self, key):
        try:
            return self.__nodes[key]
        except:
            return None

    def __delitem__(self, key):
        try:
            del self.__nodes[key]
        except:
            return None
