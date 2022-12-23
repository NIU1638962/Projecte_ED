import cfg
import os.path

# Func1


class MusicFiles:
    __slots__ = '__llista_songs', '__added', '__removed'
    
    def __init__(self):
        self.__llista_songs = []
        self.__added = []
        self.__removed = []

    def reload_fs(self, path: str):
        "mantenir a memòria una representació dels arxius que hi han al disc"

        # llista de cançons que será la nova llista
        songs_aux = []

        self.__added = []
        self.__removed = []

        # root = cfg.get_root()
        for subdir, _, files in os.walk(path):
            for file in files:
                if file[-4:] == ".mp3":
                    file_path = os.path.join(subdir, file)
                    songs_aux.append(file_path)

        # comprovar que s'ha afegit una nova cançó
        for song in songs_aux:
            if song not in self.__llista_songs:
                self.__added.append(os.path.join(path, song))

        # comprovar si s'ha eliminat alguna cançó
        for song in self.__llista_songs:
            if song not in songs_aux:
                self.__removed.append(os.path.join(path, song))

        self.__llista_songs = songs_aux

    def files_added(self) -> list:
        return self.__added

    def files_removed(self) -> list:
        return self.__removed
    
    def __len__(self):
        return len(self.__llista_songs)
    def __iter__(self):
        return self.__llista_songs.__iter__()
    def __str__(self):
        return self.__llista_songs.__str__()
    def __repr__(self):
        return self.__llista_songs.__repr__()

