import vlc
import time
from MusicData import MusicData
import uuid

class MusicPlayer:
    __slots__ = '__music_data','__player'
    
    def __init__(self, music_data: MusicData):
        """
        Inicialitza la classe.

        Parameters
        ----------
        music_data : MusicData
            Objecte del tipus MusicData que te guardades totes les cançons i
            les seves metadades.

        Returns
        -------
        None.

        """
        self.__music_data = music_data.graf
        self.__player = None

    def print_song(self, uuid: str):
        """
        Imprimeix per pantalla les metadades d'una canço.

        Parameters
        ----------
        uuid : str
            Indicador unic de la canço.

        Returns
        -------
        None.

        """
        try: 
            print("Titol :", self.__music_data[uuid].data.title)
            print(" Artista :", self.__music_data[uuid].data.artist)
            print("Album :",self.__music_data[uuid].data.album)
            print("Genere :", self.__music_data[uuid].data.genre)
            print("Duracio : ", self.songs[uuid].data.duration)
        except:
            return None

    def play_file(self, file: str):
        try:
            uuid_gen = uuid.uuid5(uuid.NAMESPACE_URL, file)
            player = vlc.MediaPlayer(file) 
            print("Reproduint : ")
            player.play()
            timeout = time.time() + self.songs[uuid_gen].data.duration 
            while True:
                if time.time() < timeout:
                    try:
                        time.sleep(1)
                    except KeyboardInterrupt:  # STOP amb <CTRL>+<C> a la consola
                        break
                else:
                    break
            player.stop()
        except:
            None
    
    def play_song(self, uuid: str, mode: int):
        #MODE 0  # Imprimir per pantalla
        #MODE 1  # Imprimir per pantalla i reproduïr so
        #MODE 2  # Reproduïr so
        
        if mode == 0:
            self.print_song
        elif mode == 1:
            self.print_song
            self.play_file
        elif mode == 2:
            self.play_file
            
    def __hash__(self):
        return hash(self.__music_data)
    
    def __eq__(self, other):
        return self.__music_data == other.__music_data
    
    def __ne__(self, other):
        return self.__music_data != other.__music_data
    
    def __lt__(self, other):
        return self.__len__() < other.__len__()

    def __str__(self):
        return self.__music_data.__str__()
    
    def __repr__(self):
        return self.__music_data.__repr__()
