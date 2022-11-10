# -*- coding: utf-8 -*-
"""
p1_main.py : ** REQUIRED ** El vostre codi de la classe SearchMetadata.
"""
from MusicFiles import MusicFiles
from MusicData import MusicData
from MusicID import MusicID
import cfg


class SearchMetadata:
    def __init__(self, music_data):
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
