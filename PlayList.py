import cfg


# Func5


class PlayList:
    __slots__ = '__playlist', '__musicID', '__musicPlayer'
    
    def __init__(self, musicID, musicPlayer):
        self.__playlist = []
        self.__musicID = musicID
        self.__musicPlayer = musicPlayer

    def __len__(self):
        return len(self.__playlist)

    def load_file(self, file: str):
        self.__playlist = []

        try:
            with open(file, "r", encoding="latin1") as fitxer:
                for line in fitxer:
                    if line[0] != "#" and line[-5:].strip() == ".mp3":
                        uuid_get = self.__musicID.get_uuid(line[:-1])
                        if uuid_get is not None:
                            if uuid_get not in self.__playlist:
                                self.__playlist.append(uuid_get)
        except:
            raise FileNotFoundError

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
        
    def read_list(self, p_llista: list):
        for uuid in p_llista:
            if uuid not in self.__playlist:
                self.__playlist.append(uuid)
                
    def __iter__(self):
        return self.__playlist.__iter__()
            
    def __str__(self):
        return self.__playlist.__str__()
    
    def __repr__(self):
        return self.__playlist.__repr__()
