# -*- coding: utf-8 -*-
"""
p1_main.py : ** REQUIRED ** El vostre codi de la classe SearchMetadata.
"""
import cfg


class SearchMetadata:
    def __init__(self, music_data):
        self.__music_data = music_data

    def title(self, sub: str) -> list:
        try:
            sub = str(sub).lower()
        except TypeError:
            return []
        return [i for i in self.__music_data if sub in self.__music_data.get_title(i)]

    def artist(self, sub: str) -> list:
        try:
            sub = str(sub).lower()
        except TypeError:
            return []
        return [i for i in self.__music_data if sub in self.__music_data.get_artist(i)]

    def album(self, sub: str) -> list:
        try:
            sub = str(sub).lower()
        except TypeError:
            return []
        return [i for i in self.__music_data if sub in self.__music_data.get_album(i)]

    def genre(self, sub: str) -> list:
        try:
            sub = str(sub).lower()
        except TypeError:
            return []
        return [i for i in self.__music_data if sub in self.__music_data.get_genre(i)]

    def and_operator(self, list1: list, list2: list) -> list:
        t1 = set(list1)
        t2 = set(list2)
        return list(t1.intersection(t2))

    def or_operator(self, list1: list, list2: list) -> list:
        t1 = set(list1)
        t2 = set(list2)
        return list(t1.union(t2))
