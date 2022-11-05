# -*- coding: utf-8 -*-
"""
p1_main.py : ** REQUIRED ** El vostre codi de la classe MusicPlayer.
"""
import cfg
import vlc
import time
from MusicData import MusicData


class MusicPlayer:

    def __init__(self, music_data: MusicData):
        self._music_Data = music_data

    def print_song(self, uuid: str):
        pass

    def play_file(self, file: str):
        # player = vlc.MediaPlayer(uri_file)
        # player.play()
        # timeout = time.time() + duration
        pass

    def play_song(self, uuid: str, mode: int):
        if 0 <= mode < 2:
            self.print_song(uuid)
        if 0 < mode <= 2:
            self.play_file()
        while True:
            if time.time() < timeout:
                try:
                    time.sleep(1)
                except KeyboardInterrupt:  # STOP amb <CTRL>+<C> a la consola
                    break
                else:
                    break
            player.stop()
