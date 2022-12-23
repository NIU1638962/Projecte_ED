import eyed3
import os
import sys
from GrafHash import GrafHash
from ElementData import ElementData
import numpy as np
from PlayList import PlayList

# Func3


class MusicData:
    __slots__ = '__songs', '__graf'
    
    def __init__(self):
        self.__songs = {}
        self.__graf = GrafHash()
        
    @property
    def graf(self):
        return self.__graf
    @graf.setter
    def graf(self, value):
        self.__graf = value
        
    def __len__(self):
        return len(self.__songs)

    def __iter__(self):
        for uuid in self.__songs.keys():
            yield uuid

    def add_song(self, uuid: str, file: str):
        if uuid == "" or uuid in self.__songs.keys() or file == "":
            return None
        # diccionari songs de forma {"uuid":["file",...,...]}
        # self.__songs[uuid] = [file]
        abs = os.path.abspath(file)
        data = ElementData(filename = abs)
        self.graf.insert_vertex(uuid, data)

    def remove_song(self, uuid: str):
        try:
            self.graf.__delitem__(uuid)
        except:
            return None

    def load_metadata(self, uuid: str):
        metadata = eyed3.load(self.get_filename(uuid))
        if metadata is None:
            print("ERROR: Arxiu MP3 error")
            sys.exit(1)
        try:
            edata = ElementData(metadata.tag.title, metadata.tag.artist, metadata.tag.album, metadata.tag.genre.name, int(np.ceil(metadata.info.time_secs)))
            self.graf.nodes[uuid].data = edata
        except:
            
            edata = ElementData(metadata.tag.title, metadata.tag.artist, metadata.tag.album, "None", int(np.ceil(metadata.info.time_secs)))
            self.graf.nodes[uuid].data = edata

        return True
    
    def read_playlist(self, obj_playlist: PlayList):
        for uuid_1, uuid_2 in obj_playlist:
            if self.__songs.exist_edge(uuid_1, uuid_2):
                self.__songs.modify_edge_weight(uuid_1, uuid_2, self.__songs.edge_weight(uuid_1, uuid_2) + 1)
            else:
                self.__songs.insert_edge(uuid_1, uuid_2, 1)

    def get_filename(self, uuid: str) -> str:
        try:
            if self.graf.__contains__(uuid):
                return self.graf.nodes[uuid].data.filename
        except KeyError:
            return None
        except IndexError:
            return None

    def get_title(self, uuid: str) -> str:
        try:
            if self.graf.__contains__(uuid):
                return self.graf.nodes[uuid].data.title
        except KeyError:
            return None
        except IndexError:
            return None

    def get_artist(self, uuid: str) -> str:
        try:
            if self.graf.__contains__(uuid):
                return self.graf.nodes[uuid].data.artist
        except KeyError:
            return None
        except IndexError:
            return None

    def get_album(self, uuid: str) -> str:
        try:
            if self.graf.__contains__(uuid):
                return self.graf.nodes[uuid].data.album
        except KeyError:
            return None
        except IndexError:
            return None

    def get_genre(self, uuid: str) -> str:
        try:
            if self.graf.__contains__(uuid):
                return self.graf.nodes[uuid].data.genre
        except KeyError:
            return None
        except IndexError:
            return None

    def get_duration(self, uuid: str):
        try:
            if self.graf.__contains__(uuid):
                return self.graf.nodes[uuid].data.duration
            else:
                return 0
        except KeyError:
            return None

    def existent(self, file: str) -> bool:
        return file in [v[0] for v in self.__songs.items()]
    
    def get_song_rank(self, uuid : str) -> int:
        """ 
        
        Retornar el ranking sumant tots els pesos de les arestes conectades amb el node
        
        """
        
        sum_arestes = 0
        for v in self.graf.e_out[uuid]:
            pes_aresta = self.graf.e_out[uuid][v]
            sum_arestes += pes_aresta
        for v in self.graf.e_in[uuid]:
            pes_aresta = self.graf.e_in[uuid][v]
            sum_arestes += pes_aresta
        return sum_arestes
    
    def get_next_songs(self, uuid : str) -> tuple:
        """
        Retorna un iterador (uuid, pes)
        
        """
        for next in self.graf.e_out[uuid]:
            pes_aresta = self.graf.e_out[uuid][next]
            tupla = (next, pes_aresta)
            yield tupla
    def get_previous_songs(self, uuid : str) -> tuple:
        """
        Retorna un iterador (uuid, pes)
        
        """
        for previous in self.graf.e_in[uuid]:
            pes_aresta = self.graf.e_in[uuid][previous]
            tupla = (previous, pes_aresta)
            yield tupla
    def get_song_distance(self, uuid1 : str, uuid2 : str) -> tuple:
        """
        Retorna una tupla (num_arestes, sum_arestes) tots totals
        """
        path = self.graf.camiMesCurt(uuid1,uuid2)
        
        if len(path)==0:
            return (0,0)
        
        sum_arestes = 0
        for pos in range(len(path)-1):
            nodeAct = path[pos]
            nextNode = path[pos+1]
            pes = self.graf.e_out[nodeAct][nextNode]
            sum_arestes += pes
        num_arestes = len(path) - 1
        return num_arestes, sum_arestes
    
    def __eq__(self, other):
        return self.graf.nodes == other.graf.nodes
    
    def __ne__(self, other):
        return self.graf.nodes != other.graf.nodes
    
    def __lt__(self, other):
        return self.__len__() < other.__len__()
    
    def __hash__(self):
        return hash(self.graf)
    
    def __str__(self):
        return self.graf.__str__()
    
    def __repr__(self):
        return self.graf.__repr__()
