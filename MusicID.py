# -*- coding: utf-8 -*-
"""
p1_main.py : ** REQUIRED ** El vostre codi de la classe MusicID.
"""
import uuid


class MusicID:

    def __init__(self):
        self._diccionari_uuid = {}
        self._diccionari_remove = {}
        self._len = 0

    def __len__(self):
        return self._len

    def generate_uuid(self, file: str) -> str:
        try:
            if not self._diccionari_remove[self._diccionari_uuid[file]]:
                print("UUID existeix i no eliminat, no s'utilitzara l'arxiu: " + file)
                return None
            raise KeyError("UUID eliminat")
        except KeyError:
            file_uuid = uuid.uuid5(uuid.NAMESPACE_URL, file)
            self._diccionari_uuid[file] = file_uuid
            self._diccionari_remove[file_uuid] = False
            self._len += 1
            return file_uuid

    def get_uuid(self, file: str) -> str:
        try:
            file_uuid = self._diccionari_id[file]
            if self._diccionari_remove[file_uuid] == True:
                raise KeyError("UUID removed")
            return file_uuid
        except KeyError:
            return None

    def remove_uuid(self, file_uuid: str) -> str:
        try:
            if self._diccionari_uuid[file_uuid]:
                raise KeyError("UUID removed")
            self._diccionari_uuid[file_uuid] = True
            self._len - 1
        except KeyError:
            pass
