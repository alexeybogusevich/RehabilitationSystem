#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/19/19, 9:13 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.


import OpenGL.GL as gl
from PyQt5 import QtWidgets

from visuals.camera import CameraOrtho2D
from visuals.visitems import visitem


class GLViewer(QtWidgets.QOpenGLWidget):

    def __init__(self, versionprofile=None, parent=None):
        super(GLViewer, self).__init__(parent)
        self.__profile = versionprofile

        self.__camera = None
        self.__items = []

        self.gl = False

        self.initial_scene_width = 1000.0
        self.initial_scene_height = 1000.0

    def addItem(self, item):
        if not isinstance(item, visitem.VisualItem):
            raise TypeError("item should be only subclass of visitem.VisualItem")
        # add item
        self.__items.append(item)
        item.viewer = self
        # initialized if it was not initialized
        if self.gl:
            item.initGL()

    def fitInRect(self, width, height):
        self.initial_scene_width = width
        self.initial_scene_height = height
        self.__camera.fitInRect(width, height)

    def initializeGL(self):
        """
        Initialize OpenGL, VBOs, upload data on the GPU, etc.
        """
        print("> [INFO]:")
        print(">  1) OpenGL Version: " + str(gl.glGetString(gl.GL_VERSION)))
        print(">  2) GLSL Version: " + str(gl.glGetString(gl.GL_SHADING_LANGUAGE_VERSION)) + "\n")

        # Set initialization flag
        self.gl = True  # self.context().versionFunctions(self.__profile)
        # self.gl.initializeOpenGLFunctions()

        # Create a camera
        self.__camera = CameraOrtho2D(scale=2.0)

        gl.glClearColor(0.0, 0.0, 0.0, 1.0)
        gl.glEnable(gl.GL_MULTISAMPLE)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glDepthFunc(gl.GL_LESS)

        gl.glEnable(gl.GL_CULL_FACE)
        gl.glCullFace(gl.GL_FRONT)
        gl.glFrontFace(gl.GL_CCW)
        #
        gl.glEnable(gl.GL_NORMALIZE)
        gl.glEnable(gl.GL_LIGHTING)
        gl.glEnable(gl.GL_LIGHT0)
        gl.glEnable(gl.GL_COLOR_MATERIAL)
        gl.glColorMaterial(gl.GL_FRONT_AND_BACK, gl.GL_AMBIENT_AND_DIFFUSE)
        #
        # # self.gl.glMaterialfv(gl.GL_FRONT, gl.GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
        # # self.gl.glMaterialf(gl.GL_FRONT, gl.GL_SHININESS, 5.0)
        # # self.gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, (0.1, 0.1, 0.1, 1.0))
        #
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, (0.0, 0.0, 100.0, 1.0))
        # self.gl.glLightfv(gl.GL_LIGHT0, gl.GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        # self.gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))
        # self.gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPECULAR, (0.0, 0.0, 1.0, 1.0))

        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

        gl.glEnable(gl.GL_ALPHA_TEST)
        gl.glAlphaFunc(gl.GL_NOTEQUAL, 0)

        gl.glEnable(gl.GL_LINE_SMOOTH)
        gl.glEnable(gl.GL_POLYGON_SMOOTH)
        gl.glEnable(gl.GL_POINT_SMOOTH)

        gl.glHint(gl.GL_LINE_SMOOTH_HINT, gl.GL_NICEST)
        gl.glHint(gl.GL_POLYGON_SMOOTH_HINT, gl.GL_NICEST)
        gl.glHint(gl.GL_POINT_SMOOTH_HINT, gl.GL_NICEST)
        #
        # self.gl.glEnableClientState(gl.GL_TEXTURE_COORD_ARRAY)

        for item in self.__items:
            item.initGL()

        # Initialize camera
        self.__camera.setup(self.width(), self.height())
        self.fitInRect(self.initial_scene_width, self.initial_scene_height)

    def paintGL(self):
        """
        Paint the scene.
        """
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        self.__camera.look(0.0, 0.0)

        for item in self.__items:
            if item.visible:
                item.drawGL()

    def resizeGL(self, width, height):
        self.__camera.setup(width, height)



