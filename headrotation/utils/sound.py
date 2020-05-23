#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/22/19, 6:50 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

from PyQt5 import QtMultimedia
from PyQt5 import QtCore


class SoundPlayer(QtCore.QThread):

    def __init__(self):
        super(SoundPlayer, self).__init__()
        self.url = QtCore.QUrl.fromLocalFile("/Users/dkotsur/Projects/KNU/MUAE-HealthCare/data/sounds/finish.wav")
        self.sound = QtMultimedia.QSound("/Users/dkotsur/Projects/KNU/MUAE-HealthCare/data/sounds/finish.wav")

    def __del__(self):
        self.wait()

    def run(self):
        print("play")
        self.sound.play()