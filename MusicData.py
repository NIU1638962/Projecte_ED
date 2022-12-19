from typing import Iterator, Tuple
import uuid
import eyed3
from cfg import ROOT_DIR
import os
from PlayList import PlayList


# Func3


class MusicData:
    def __init__(self):
        self.__songs = {}

    def __len__(self):
        return len(self.__songs)

    def __iter__(self):
        for uuid in self.__songs.keys():
            yield uuid

    def __repr__(self) -> str:
        return str(self.__songs)

    def add_song(self, uuid: str, file: str):
        if uuid == "" or uuid in self.__songs.keys() or file == "":
            return None
        # diccionari songs de forma {"uuid":["file",...,...]}
        self.__songs[uuid] = [file]

    def remove_song(self, uuid: str):
        try:
            del self.__songs[uuid]
        except:
            return None

    def load_metadata(self, uuid: str):
        metadata = eyed3.load(ROOT_DIR + os.sep + self.__songs[uuid][0])

        self.__songs[uuid] = [self.__songs[uuid][0]]

        self.__songs[uuid].append(str(metadata.tag.title).lower())
        self.__songs[uuid].append(str(metadata.tag.artist).lower())
        self.__songs[uuid].append(str(metadata.tag.album).lower())
        self.__songs[uuid].append(str(metadata.tag.genre).lower())
        self.__songs[uuid].append(metadata.info.time_secs)

        return True

    def get_filename(self, uuid: str) -> str:
        try:
            return self.__songs[uuid][0]
        except KeyError:
            return None
        except IndexError:
            return None

    def get_title(self, uuid: str) -> str:
        try:
            return self.__songs[uuid][1]
        except KeyError:
            return None
        except IndexError:
            return None

    def get_artist(self, uuid: str) -> str:
        try:
            return self.__songs[uuid][2]
        except KeyError:
            return None
        except IndexError:
            return None

    def get_album(self, uuid: str) -> str:
        try:
            return self.__songs[uuid][3]
        except KeyError:
            return None
        except IndexError:
            return None

    def get_genre(self, uuid: str) -> str:
        try:
            return self.__songs[uuid][4]
        except KeyError:
            return None
        except IndexError:
            return None

    def get_duration(self, uuid: str):
        try:
            return self.__songs[uuid][5]
        except KeyError:
            return None

    def existent(self, file: str) -> bool:
        return file in [v[0] for v in self.__songs.items()]

    def read_playlist(self, obj_playlist: PlayList):
        pass

    def get_song_rank(seld, uuid: str) -> int:
        pass

    def get_next_songs(self, uuid: str) -> Iterator[Tuple[str, float]]:
        pass

    def get_previous_songs(self, uuid: str) -> Iterator[Tuple[str, float]]:
        pass

    def get_song_distance(self, uuid1:str, uuid2:str) -> Iterator[Tuple[int, float]]:
        pass

    def get_similar(self, uuid: str, max_list:int) -> list:
        pass

    def get_topfive(self) -> list:
        pass