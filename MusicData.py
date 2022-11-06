import eyed3

#Func3

class MusicData:
    def __init__(self):
        self.__songs = {}
    @property
    def songs(self):
        return self.__songs
    
    @songs.setter
    def songs(self, value):
        self.__songs = value
        
    def add_song(self, uuid: str, file: str):
        if uuid == "" or uuid in self.songs.keys() or file == "":
            return None
        #diccionari songs de forma {"uuid":["file",...,...]}
        self.songs[uuid] = [file]
    def remove_song(self,uuid: str): 
        try:
            del self.songs[uuid]
        except:
            return None
    def load_metadata(self, uuid: str): 
        
        metadata = eyed3.load(self.songs[uuid][0])
            
        self.songs[uuid].append(metadata.tag.title)
        self.songs[uuid].append(metadata.tag.artist)
        self.songs[uuid].append(metadata.tag.album)
        self.songs[uuid].append(metadata.tag.genre)
        
    def get_title(self, uuid: str): #-> str
        return self.songs[uuid][1]
    def get_artist(self, uuid: str): #-> str      
        return self.songs[uuid][2]    
    def get_album(self,uuid: str): #-> str
        return self.songs[uuid][3]
    def get_genre(self,uuid: str): #-> str  
        return self.songs[uuid][4]
 

musicdata = MusicData()
uuid = "a104f469-38bb-4b76-9252-f5af88b36437"
file = "Corpus/Pop/Synth_Pop/King_Elizabeth_-_05_-_City_of_Love.mp3"
musicdata.add_song(uuid, file)

musicdata.load_metadata(uuid)

print(musicdata.get_genre(uuid))
