# -*- coding: utf-8 -*-
"""
GrafHash.py : ** REQUIRED ** El vostre codi de la classe GrafHash.
"""
from ElementData import ElementData


class GrafHash:

    __slots__ = ['_nodes', '_out']

    class Vertex:
        __slots__ = '_valor'

        def __init__(self, x):
            self._valor = x

        def __str__(self):
            return str(self._valor)

    def __init__(self) -> None:
        self._nodes = {}
        self._out = {}

    def __repr__(self):
        cad = "===============GRAF===================\n"

        for it in self._out.items():
            cad1 = "__________________________________________________________________________________\n"
            cad1 = cad1+str(it[0])+" : "
            for valor in it[1].items():
                cad1 = cad1+str(str(valor[0])+"(" + str(valor[1])+")"+" , ")

            cad = cad + cad1 + "\n"

        return cad

    def __iter__(self):
        for n, e in self._nodes:
            yield n, e

    def __len__(self) -> int:
        return len(self._nodes)

    def insert_vertex(self, key, e: ElementData) -> None:
        if type(e) is not ElementData:
            raise TypeError("Not ElementData type")
        self._nodes[key] = self.Vertex(e)
        self._out[key] = {}
        

    def insert_edge(self, n1, n2, p=1):
        self._out[n1][n2] = p
        self._out[n2][n1] = p

    def vertices(self):
        """Return una iteracio de tots els vertexs del graf."""
        return self._nodes.__iter__()

    def edges(self, x):
        """Return una iteracio de tots els nodes veins de x al graf."""
        # return self._out[x].items()
        return iter(self._out[x].__iter__())

    def get(self, key) -> ElementData:
        return self._nodes[key]._valor

    def __contains__(self, key):
        try:
            self._nodes[key]
            return True
        except KeyError:
            return False 

    def __getitem__(self, key):
        return self._nodes[key] 

    def __delitem__(self, key):
        del self._nodes[key]
        del self._out[key]
        for i in self._out.items:
            if key in i:
                del i[key]

    def del_edge(self, key1, key2):
        del self._out[key1][key2]
        del self._out[key2][key1]

    def exist_edge(self, key1, key2):
        try:
            self._out[key1][key2]
            self._out[key2][key1]
            return True
        except KeyError:
            return False

    def modify_edge_weight(self, key1, key2, new):
        if self.exist_edge(key1, key2):
            self._out[key1][key2] = new
            self._out[key2][key1] = new
            return new
        raise KeyError("Edge doesn't exist")
    
    def edge_weight(self, key1, key2):
        return self._out[key1][key2]
