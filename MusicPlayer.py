# -*- coding: utf-8 -*-
"""
p1_main.py : ** REQUIRED ** El vostre codi de la classe MusicPlayer.
"""
import cfg
import vlc
import time
import eyed3
import numpy
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

    def play_file(self, file: str):
        self._player = vlc.MediaPlayer(file)
        self._player.play()
        timeout = time.time() + int(numpy.ceil(eyed3.load(file).info.time_secs))
        return timeout

    def play_song(self, uuid: str, mode: int):
        try:
            self._music_data.load_metadata(uuid)
            if 0 <= mode < 2:
                self.print_song(uuid)
            if 0 < mode <= 2:
                timeout = self.play_file(
                    self._music_data.get_filename(uuid))
                while time.time() < timeout:
                    try:
                        time.sleep(1)
                    except KeyboardInterrupt:  # STOP amb <CTRL>+<C> a la consola
                        break
                    except:
                        break
                self._player.stop()
        except OSError:
            return
