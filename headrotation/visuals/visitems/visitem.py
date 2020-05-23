#!/usr/bin/env python
#
# Copyright (C) Software Competence Center Hagenberg GmbH (SCCH)
# All rights reserved.
#
# This document contains proprietary information belonging to SCCH.
# Passing on and copying of this document, use and communication of its
# contents is not permitted without prior written authorization.
#
# Created on: 03/11/16 13:28
# by:  Dmytro Kotsur
#
########################################################################################################################


class VisualItem(object):

    def __init__(self):
        self.viewer = None
        self.visible = True
        # how many scene distance in one screen pixel
        self._internal_distance_threshold = 1.0

    def initGL(self):
        pass

    def drawGL(self):
        pass

    def setVisible(self, visible=True):
        self.visible = visible

    def setInternalDistanceThreshold(self, threshold):
        self._internal_distance_threshold = threshold
    #
    # Mouse events
    #

    def mousePressed(self, x, y, button):
        pass

    def mouseReleased(self, x, y, button):
        pass

    def mouseMoved(self, x, y, button):
        pass