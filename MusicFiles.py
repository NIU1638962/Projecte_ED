import cfg
import os.path

# Func1


class MusicFiles:
    def __init__(self):
        self.__llista_songs = []
        self.__added = []
        self.__removed = []

    @property
    def llista_songs(self):
        return self.__llista_songs

    @property
    def added(self):
        return self.__added

    @property
    def removed(self):
        return self.__removed

    @llista_songs.setter
    def llista_songs(self, value):
        self.__llista_songs = value

    @added.setter
    def added(self, value):
        self.__added = value

    @removed.setter
    def removed(self, value):
        self.__removed = value

    def reload_fs(self, path: str):
        "mantenir a memòria una representació dels arxius que hi han al disc"

        # llista de cançons que será la nova llista
        songs_aux = []

        self.added = []
        self.removed = []

        root = cfg.get_root()
        for subdir, _, files in os.walk(root):
            for file in files:
                if file[-4:] == ".mp3":
                    file_path = os.path.join(subdir, file)
                    songs_aux.append(cfg.get_canonical_pathfile(file_path))

        # comprovar que s'ha afegit una nova cançó
        for song in songs_aux:
            if song not in self.llista_songs:
                self.added.append(os.path.join(root, song))

        # comprovar si s'ha eliminat alguna cançó
        for song in self.__llista_songs:
            if song not in songs_aux:
                self.removed.append(os.path.join(root, song))

        self.llista_songs = songs_aux

    def files_added(self):  # -> list
        return self.added

    def files_removed(self):  # -> list
        return self.removed


# path = r" "
# mf = MusicFiles()
# mf.reload_fs(path)
# for song in mf.llista_songs:
#     print(song)
