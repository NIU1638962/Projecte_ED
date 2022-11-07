# -*- coding: utf-8 -*-
"""
p1_main.py : ** REQUIRED ** El vostre codi de la classe MusicPlayer.
"""
from cfg import ROOT_DIR
import vlc
import time
from MusicData import MusicData


class MusicPlayer:

    def __init__(self, music_data: MusicData):
        self._music_data = music_data
        self._player = None

    def print_song(self, uuid: str):
        self._music_data.get_title(uuid)
        self._music_data.get_artist(uuid)
        self._music_data.get_album(uuid)
        self._music_data.get_genre(uuid)

    def play_file(self, file: str, mode=0):
        if 0 < mode <= 2:
            if self._music_data.existent(file):
                self._player = vlc.MediaPlayer(ROOT_DIR + "\\" + file)
                self._player.play()

    def play_song(self, uuid: str, mode=0):
        try:
            self._music_data.load_metadata(uuid)
            if 0 <= mode < 2:
                self.print_song(uuid)
            if 0 < mode <= 2:
                self.play_file(
                    self._music_data.get_filename(uuid))
                timeout = time.time() + self._music_data.get_duration(uuid)
                while time.time() < timeout:
                    try:
                        time.sleep(1)
                    except KeyboardInterrupt:  # STOP amb <CTRL>+<C> a la consola
                        break
                    except:
                        break
                self._player.stop()
        except KeyError:
            return None
