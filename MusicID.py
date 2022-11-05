# -*- coding: utf-8 -*-
"""
p1_main.py : ** REQUIRED ** El vostre codi de la classe MusicID.
"""
import cfg
import uuid


class MusicID:

    def __init__(self):
        """
        Iniclitza la classe.

        Returns
        -------
        None.

        """
        # Guarda els uuids ja generats
        self._diccionari_uuid = {}
        # Guarda si un uuid ha sigut eliminat True si eliminat, False si no.
        self._diccionari_remove = {}
        # Guarda la quantitat de uuids generats no eliminats.
        self._len = 0

    def __len__(self) -> int:
        return self._len

    def __str__(self) -> str:
        return "\n".join([i + ": " + v for i, v in self._diccionari_uuid.items() if not self._diccionari_remove[v]])

    def generate_uuid(self, file: str) -> str:
        """


        Parameters
        ----------
        file : str
            File generic path from root directory.

        Returns
        -------
        str
            UUID del file generat si no hi estaba previament sense haberse eliminat.
        None
            L'UUID ja existeix i no ha estat esborrat.

        """
        print("File rebut: " + file)
        # Generem UUID.
        file_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, file))
        print("UUID generat: " + file_uuid)
        try:
            # Si no salta un key error al diccionari significa que ja s'ha entrat l'uuid
            if not self._diccionari_remove[file_uuid]:
                # Si no ha estat esborrat no i existeix, informa de la colisió i retorna None.
                print("UUID existeix i no esta eliminat {code except 1}")
                return None
            raise KeyError("UUID esta eliminat, regenerant {code except 2}")
        except KeyError as msg:
            # Si l'UUID ja no ha estat generat o ha estat esborrat,
            print(str(msg))
            self._diccionari_uuid[file] = file_uuid
            self._diccionari_remove[file_uuid] = False
            self._len += 1
            return file_uuid

    def get_uuid(self, file: str) -> str:
        """
        Retorna l'uuid ja generat d'un file.

        Parameters
        ----------
        file : str
            File generic path from root directory.

        Returns
        -------
        str
            UUID del file generat si no hi estaba previament sense haberse eliminat.
        None
            L'UUID ja existeix i no ha estat esborrat.

        """
        try:
            # Generem uuid
            file_uuid = self._diccionari_uuid[file]
            # Si existeix al diccionari
            if self._diccionari_remove[file_uuid]:
                # Si está esborrado crear excepció de no existeix
                raise KeyError("UUID removed")
            # I no está esborrada, retornem la uuid.
            return file_uuid
        except KeyError:
            # Returnar none si no está
            return None

    def remove_uuid(self, file_uuid: str) -> str:
        """
        Elimina l'uuid generat d'un file.

        Parameters
        ----------
        file_uuid : str
            UUID del file.

        Returns
        -------
        str
            UUID eliminat o None si ja estaba eliminat.

        """
        print("UUID rebut: " + file_uuid)
        try:
            # Comprovar que la uuid está creada i no está eliminada
            if self._diccionari_remove[file_uuid]:
                raise KeyError("UUID ja ha estat eliminat {code except 1}")
            print(
                "UUID existeix i no esta eliminat, eliminant {code except 2}")
            self._diccionari_remove[file_uuid] = True
            self._len -= 1
        except KeyError as msg:
            print(str(msg))
            return None
