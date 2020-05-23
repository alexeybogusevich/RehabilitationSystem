#!/usr/bin/env python
#
# Copyright (C) Software Competence Center Hagenberg GmbH (SCCH)
# All rights reserved.
#
# This document contains proprietary information belonging to SCCH.
# Passing on and copying of this document, use and communication of its
# contents is not permitted without prior written authorization.
#
# Created on: 20/10/16 11:01
# by:  Dmytro Kotsur
#
########################################################################################################################


import OpenGL.GL as gl
import OpenGL.GLU as glu
import numpy as np

from PyQt5 import QtCore


class CameraOrtho2D:

    def __init__(self, origin_x=0.0, origin_y=0.0, scale=1.0):
        #self.gl = gl_context
        self.origin_x = -origin_x
        self.origin_y = -origin_y
        self.scale = scale
        self.width = 0.0
        self.height = 0.0
        self.angle = 0.0
        self.axis = np.array([0.0, 0.0, 0.0])

    def setup(self, width, height):
        self.width = width
        self.height = height
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        aspect_ratio = float(self.width) / float(self.height)
        #gl.glOrtho(-aspect_ratio, aspect_ratio, 1.0, -1.0, -1000, 1000)
        #gl.glFrustum(-aspect_ratio, aspect_ratio, -1.0, 1.0, 1.0, 100) # 720, 1280
        gl.glFrustum(-aspect_ratio, aspect_ratio, 0.0, 1.0, 1.0, 1000)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

    def look(self, origin_x, origin_y):
        self.origin_x = origin_x
        self.origin_y = origin_y
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        aspect_ratio = float(self.width) / float(self.height)
        gl.glFrustum(-aspect_ratio, aspect_ratio, -1.0, 1.0, 1.0, 1000)

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gl.glTranslate(self.origin_x, self.origin_y, -300.0)
        # gl.glRotate(self.angle * 50, self.axis[0], self.axis[1], self.axis[2])


    def fitInRect(self, width, height):
        ar1 = float(self.width) / float(self.height)
        ar2 = float(width) / float(height)

        if ar1 > ar2:
            self.scale = 2.0 / height
        else:
            self.scale = 2.0 * ar1 / width

        self.origin_x = -0.5 * width
        self.origin_y = -0.5 * height

