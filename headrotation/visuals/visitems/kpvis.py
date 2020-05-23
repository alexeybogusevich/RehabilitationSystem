#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/22/19, 11:53 AM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.
#
from visuals.visitems.visitem import VisualItem

import numpy as np
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.arrays.vbo as glvbo


class KPVisItem(VisualItem):

    def __init__(self, points):
        super(KPVisItem, self).__init__()
        self.mouse_is_pressed = False
        self.points = points
        self.c = None

    def initGL(self):
        self.c = [glu.gluNewQuadric() for _ in range(68)]

    def drawGL(self):
        gl.glPushAttrib(gl.GL_CURRENT_BIT)
        self.draw()
        gl.glPopAttrib()

    def draw(self):
        gl.glPushAttrib(gl.GL_CURRENT_BIT)

        # gl.glEnable(gl.GL_DEPTH_TEST)
        # gl.glDepthFunc(gl.GL_LESS)
        #
        #gl.glEnable(gl.GL_CULL_FACE)
        gl.glCullFace(gl.GL_FRONT)
        gl.glFrontFace(gl.GL_CCW)
        #
        # gl.glEnable(gl.GL_LIGHTING)
        # gl.glEnable(gl.GL_LIGHT0)
        # gl.glEnable(gl.GL_COLOR_MATERIAL)
        # gl.glColorMaterial(gl.GL_FRONT_AND_BACK, gl.GL_AMBIENT_AND_DIFFUSE)

        gl.glPushMatrix()
        gl.glMatrixMode(gl.GL_MODELVIEW)
        #gl.glLoadIdentity()
        gl.glColor3f(1.0, 0.0, 0.0)
        gl.glPointSize(10.0)

        gl.glBegin(gl.GL_POINTS)
        for i, cid in enumerate(self.c):
            gl.glVertex3f(self.points[i][0], self.points[i][1], self.points[i][2])
            #gl.glTranslatef(self.points[i][0], self.points[i][1], self.points[i][2])
            #cid = glu.gluNewQuadric()
            #gl.glTranslatef(self.points[i][0], self.points[i][1], self.points[i][2])
            #glu.gluSphere(cid, 5.0, 20, 20)
        gl.glEnd()
        gl.glPopMatrix()
        gl.glPopAttrib()

    def mousePressed(self, x, y, button):
        self.mouse_is_pressed = True

    def mouseMoved(self, x, y, button):
        pass

    def mouseReleased(self, x, y, button):
        self.mouse_is_pressed = False

    def setPoints(self, pts):
        self.points = pts
