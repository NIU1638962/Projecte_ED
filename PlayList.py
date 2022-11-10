import cfg

# Func5


class PlayList:
    def __init__(self, musicID, musicPlayer):
        self.__playlist = []
        self.__musicID = musicID
        self.__musicPlayer = musicPlayer

    # @property
    # def playlist(self):
    #     return self.__playlist

    # @playlist.setter
    # def playlist(self, value):
    #     self.__playlist = value

    # @property
    # def musicID(self):
    #     return self.__musicID

    # @property
    # def musicPlayer(self):
    #     return self.__musicPlayer

    def __len__(self):
        return len(self.__playlist)

    def load_file(self, file: str):
        self.__playlist = []

        try:
            fitxer = open(file, "r")
        except:
            raise FileNotFoundError

        for line in fitxer:
            if line[0] != "#" and line[-5:].strip() == ".mp3":
                uuid_get = self.__musicID.get_uuid(line[:-1])
                if uuid_get is not None:
                    if uuid_get not in self.__playlist:
                        self.__playlist.append(uuid_get)
        fitxer.close()

    def play(self, mode):
        for uuid_aux in self.__playlist:
            self.__musicPlayer.play_song(uuid_aux, mode)

    def add_song_at_end(self, uuid: str):
        self.__playlist.append(uuid)

    def remove_first_song(self):
        try:
            self.__playlist.pop(0)
        except:
            return None

    def remove_last_song(self):
        try:
            self.__playlist.pop(-1)
        except:
            return None
