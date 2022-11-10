# -*- coding: utf-8 -*-
"""
p1_main.py : ** REQUIRED ** El vostre codi de la classe MusicPlayer.
"""
from cfg import ROOT_DIR
import vlc
import time
from MusicData import MusicData
import os


class MusicPlayer:

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
        self.__music_data = music_data
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
        print(self.__music_data.get_title(uuid))
        print(self.__music_data.get_artist(uuid))
        print(self.__music_data.get_album(uuid))
        print(self.__music_data.get_genre(uuid))
        print(self.__music_data.get_duration(uuid))

    def play_file(self, file: str, mode=0):
        """
        Reprodueix a VCL una canço.

        Parameters
        ----------
        file : str
            path i nom d'arxiu de la canço desde el directori root.
        mode : TYPE, optional
            Si es vol veure només les metadades (0), reproduirles, (1) o tots
            dos a la vegada (2). The default is 0.

        Returns
        -------
        None.

        """
        if 0 < mode <= 2:
            if self.__music_data.existent(file):
                self.__player = vlc.MediaPlayer(ROOT_DIR + os.sep + file)
                self.__player.play()

    def play_song(self, uuid: str, mode=0):
        """
        Iniciar visualització per pantalla o reproducció d'una canço.
        Mentre es reprodueix una canço premre <CTRL>+<C> a la consola per
        finalitzar.

        Parameters
        ----------
        uuid : str
            Indicador unic de la canço.
        mode : int, optional
            Si es vol veure només les metadades (0), reproduirles, (1) o tots
            dos a la vegada (2). The default is 0.

        Returns
        -------
        None.

        """
        try:
            self.__music_data.load_metadata(uuid)
            if 0 <= mode < 2:
                self.print_song(uuid)
            if 0 < mode <= 2:
                self.play_file(
                    self.__music_data.get_filename(uuid))
                timeout = time.time() + self.__music_data.get_duration(uuid)
                while time.time() < timeout:
                    try:
                        time.sleep(1)
                    except KeyboardInterrupt:  # STOP amb <CTRL>+<C> a la consola
                        break
                    except:
                        break
                self.__player.stop()
        except KeyError:
            return None
