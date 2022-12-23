from MusicFiles import MusicFiles
from MusicData import MusicData
from MusicID import MusicID
import cfg


class SearchMetadata:
    __slots__ = '__music_data'
    
    def __init__(self, music_data: MusicData):
        """
        Inicialitza la classe.

        Parameters
        ----------
        music_data : MusicData
            Objecte del tipus MusicData que te guardades totes les cançons i
            les seves metadades.

        Returns
        -------
        None.

        """
        # Guardem l'objecte com del tipus MusicData per fer les consultes
        self.__music_data = music_data
    

    def title(self, sub: str) -> list:
        """
        Busca en les cançons guardades a la classe MusicData donada a la
        inicialització que contenen a la metadata 'title' el substring sub.

        Parameters
        ----------
        sub : str
            Substring que ha de contenir el resultats de la recerca en la
            metadata 'title'.

        Returns
        -------
        list
            Retorna un lista dels uuids(str) de les cançons que contenen el
            substring. Si el parametre no es pot convertir a un string en
            minuscules retorna una llista amb totes les cançons.

        """
        sub = self.__str_tran(sub)
        return [i for i in self.__music_data if self.__music_data.load_metadata(i) and sub in self.__music_data.get_title(i)]

    def artist(self, sub: str) -> list:
        """
        Busca en les cançons guardades a la classe MusicData donada a la
        inicialització que contenen a la metadata 'artist' el substring sub.

        Parameters
        ----------
        sub : str
            Substring que ha de contenir el resultats de la recerca en la
            metadata 'artist'.

        Returns
        -------
        list
            Retorna un lista dels uuids(str) de les cançons que contenen el
            substring. Si el parametre no es pot convertir a un string en
            minuscules retorna una llista amb totes les cançons.

        """
        sub = self.__str_tran(sub)
        return [i for i in self.__music_data if sub in self.__music_data.get_artist(i)]

    def album(self, sub: str) -> list:
        """
        Busca en les cançons guardades a la classe MusicData donada a la
        inicialització que contenen a la metadata 'album' el substring sub.

        Parameters
        ----------
        sub : str
            Substring que ha de contenir el resultats de la recerca en la
            metadata 'album'.

        Returns
        -------
        list
            Retorna un lista dels uuids(str) de les cançons que contenen el
            substring. Si el parametre no es pot convertir a un string en
            minuscules retorna una llista amb totes les cançons.

        """
        sub = self.__str_tran(sub)
        return [i for i in self.__music_data if self.__music_data.load_metadata(i) and sub in self.__music_data.get_album(i)]

    def genre(self, sub: str) -> list:
        """
        Busca en les cançons guardades a la classe MusicData donada a la
        inicialització que contenen a la metadata 'genre' el substring sub.

        Parameters
        ----------
        sub : str
            Substring que ha de contenir el resultats de la recerca en la
            metadata 'genre'.

        Returns
        -------
        list
            Retorna un lista dels uuids(str) de les cançons que contenen el
            substring. Si el parametre no es pot convertir a un string en
            minuscules retorna una llista amb totes les cançons.

        """
        sub = self.__str_tran(sub)
        return [i for i in self.__music_data if self.__music_data.load_metadata(i) and sub in self.__music_data.get_genre(i)]

    def and_operator(self, list1: list, list2: list) -> list:
        """
        Retorna una llista amb els uuids(str) que es troben a totes dues
        llistes donades a la vegada com a parametres.

        Parameters
        ----------
        list1 : list
            Llista de uuids(str).
        list2 : list
            Llista de uuids(str).

        Returns
        -------
        list
            Llista de uuids(str).

        """
        t1 = set(list1)
        t2 = set(list2)
        return list(t1.intersection(t2))

    def or_operator(self, list1: list, list2: list) -> list:
        """
        Retorna una llista amb tots els uuids(str) sense repeticions de totes
        dues llistes donades com a parametres.

        Parameters
        ----------
        list1 : list
            Llista de uuids(str).
        list2 : list
            Llista de uuids(str).

        Returns
        -------
        list
            Llista de uuids(str).

        """
        t1 = set(list1)
        t2 = set(list2)
        return list(t1.union(t2))

    def __str_tran(self, sub):
        """
        Transforma uns conjunt de dades a string a través de metode str()
        (si pot fer-ho) i ho converteix tot a mínuscules. Si no es pot
        convertir a string retorna el string buit "".

        Parameters
        ----------
        sub
            Varable a forrmatejar en string.

        Returns
        -------
        str
            Variable sub formatejada a string en minúscules o strin buit "".

        """
        try:
            return str(sub).lower()
        except TypeError:
            return ""
    
    def get_similar(self, uuid : str, max_list : int) -> list:
        """
        Retorna una llista dels uuid's amb major semblança prenent com a parametre 
        la mida maxima de la llista i el uuid a comparar

        Parameters
        ----------
        uuid : str
            uuid a comparar
        max_list : int
            mida maxima de la llista

        Returns
        -------
        list
            llista dels uuid's amb major semblança de major a menor

        """
        visitat, _ = self.__music_data.graf.DFS(uuid)
        llista_total = []
        AB, BA = 0, 0
        for node in visitat:
            AB_value, AB_nodes = self.__music_data.get_song_distance(uuid, node) 
            BA_value, BA_nodes = self.__music_data.get_song_distance(node, uuid)
            if (AB_value != 0):
                AB = (AB_nodes/AB_value) * (self.__music_data.get_song_rank(uuid)/2)
            if (BA_value != 0):
                BA = (BA_nodes/BA_value) * (self.__music_data.get_song_rank(node)/2)
                
            similarity = AB + BA
            if similarity != 0:
                tuple = (similarity, node)
                llista_total.append(tuple)
        sorted_list = sorted(llista_total, reverse = True)
        return [x[1] for x in sorted_list][:max_list]
    
    def get_topfive(self) -> list:
        """
        Returns
        -------
        list
            5 millors cançons de tota la col·lecció

        """
        llista_rangs = []
        for song in self.__music_data.graf:
            rang = self.__music_data.get_song_rank(song)
            llista_rangs.append((rang, song))
            
        top_5_list = [x[1] for x in sorted(llista_rangs, reverse = True)][:5]
        
        similarity = []
        similars_5_lists = []
        
        for uuid in top_5_list:
            similars_5_lists.append(self.get_similar(uuid, 5))
            
        top_25_list = similars_5_lists[0]
        
        for uuid in similars_5_lists[1:]:
            top_25_list = self.or_operator(top_25_list, uuid) 
            
        for i in top_25_list:
            llista = []
            for j in top_25_list:
                if i != j:
                    AB, BA = 0, 0
                    AB_value, AB_nodes = self.music.get_song_distance(i, j)
                    BA_value, BA_nodes = self.music.get_song_distance(j, i)

                    if (AB_value != 0):
                        AB = (AB_nodes/AB_value)*(self.music.get_song_rank(i)/2)
                        
                    if (BA_value != 0):
                        BA = (BA_nodes/BA_value)*(self.music.get_song_rank(j)/2)
                        
                    similar = AB + BA
                    llista.append(similar)
            similarity.append((sum(llista), str(i)))
        
        sorted_list = sorted(similarity, reverse = True)
        cinc_millors = [x[1] for x in sorted_list if x in self.music.graf][:5]
        
        return cinc_millors
    
    def __len__(self):
        return self.__music_data.__len__()
    
    def __iter__(self):
        return self.__music_data.__iter__()
    
    def __str__(self):
        return self.__music_data.__str__()
    
    def __repr__(self):
        return self.__music_data.__repr__()
