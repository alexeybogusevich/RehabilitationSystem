#!/usr/bin/env python
#
# Copyright (C) Software Competence Center Hagenberg GmbH (SCCH)
# All rights reserved.
#
# This document contains proprietary information belonging to SCCH.
# Passing on and copying of this document, use and communication of its
# contents is not permitted without prior written authorization.
#
# Created on: 03/11/16 16:51
# by:  Dmytro Kotsur
#
########################################################################################################################


import OpenGL.GL as gl
import numpy as np

import visitem


class ImageVisItem(visitem.VisualItem):

    def __init__(self, image=None, x=0, y=0):
        visitem.VisualItem.__init__(self)
        self.x = x
        self.y = y
        self.img_data = image
        if image is not None:
            self.width = image.shape[0]
            self.height = image.shape[1]
        else:
            self.width = 0
            self.height = 0
        self.texture = 0

    def initGL(self):
        self.texture = gl.glGenTextures(1)
        self.__setupImage()

    def __setupImage(self):
        gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 4)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)
        gl.glTexEnvf(gl.GL_TEXTURE_ENV, gl.GL_TEXTURE_ENV_MODE, gl.GL_MODULATE)

        gl.glTexParameter(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP)
        gl.glTexParameter(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP)
        gl.glTexParameter(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        gl.glTexParameter(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)

        if self.img_data is not None:
            gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, self.width, self.height,
                            0, gl.GL_RGB, gl.GL_FLOAT, self.img_data)

        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

    def setImage(self, image):
        # set image data
        self.width = image.shape[1]
        self.height = image.shape[0]
        self.img_data = image

        # initialize OpenGL texture
        self.__setupImage()

    def drawGL(self):
        gl.glPushAttrib(gl.GL_CURRENT_BIT)
        gl.glTexEnvi(gl.GL_TEXTURE_ENV, gl.GL_TEXTURE_ENV_MODE, gl.GL_DECAL)
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)
        arr_points = np.array([[0, 0], [self.width, 0], [self.width, self.height], [0, self.height]], np.float)
        arr_texture = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], np.float)
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glVertexPointer(2, gl.GL_FLOAT, 0, arr_points)
        gl.glTexCoordPointer(2, gl.GL_FLOAT, 0, arr_texture)
        indices = [0, 1, 2, 3]
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glDrawElements(gl.GL_QUADS, 4, gl.GL_UNSIGNED_SHORT, indices)
        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glDisable(gl.GL_TEXTURE_2D)
        gl.glPopAttrib()