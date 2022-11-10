import cfg
import uuid
#Func5
class PlayList:
    def __init__(self, musicID, musicPlayer):
        self.__playlist = []
        self.__musicID = musicID
        self.__musicPlayer = musicPlayer
    @property
    def playlist(self):
        return self.__playlist
    
    @playlist.setter
    def playlist(self, value):
        self.__playlist = value
        
    @property
    def musicID(self):
        return self.__musicID
    
    @property
    def musicPlayer(self):
        return self.__musicPlayer    
    
    def load_file(self, file: str):
        self.playlist = []
        
        try:
            fitxer = open(file,"r")
        except:
            raise FileNotFoundError
        
        for line in fitxer:
            if line[0]!="#" and line[-5].strip()==".mp3":
                uuid_get = uuid.uuid5(uuid.NAMESPACE_URL,line.strip())
                if uuid_get in self.musicID.uuid_dict:
                        if uuid_get not in self.playlist:                                                                                                                                                                                                                                                                                                                                                                                                   
                            self.playlist.append(uuid_get)
        fitxer.close()
        
    def play(self,mode): 
        for uuid_aux in self.playlist:
            self.musicPlayer.play_song(uuid_aux, mode) 
        
#Func7 
    def add_song_at_end(self,uuid: str):
        self.playlist.append(uuid)
    def remove_first_song(self): 
        try:
            self.playlist.pop(0)
        except:
            return None
    def remove_last_song(self): 
        try:
            self.llista_repr.pop(-1)
        except:
            return None
