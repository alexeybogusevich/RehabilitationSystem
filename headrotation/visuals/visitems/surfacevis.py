#!/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/20/19, 10:10 AM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

#
#

from visuals.visitems.visitem import VisualItem

import numpy as np
import OpenGL.GL as gl
import OpenGL.arrays.vbo as glvbo


class SurfaceVisItem(VisualItem):

    def __init__(self, points, triangles, normals, cull_back=True, is_ccw=False):
        super(SurfaceVisItem, self).__init__()
        self.vbo_points = None
        self.vbo_normals = None
        self.vbo_indices = None
        self.mouse_is_pressed = False
        self.points = points
        self.normals = -normals
        self.triangles = triangles
        self.angle_x = 0.0
        self.angle_y = 0.0
        self.angle_z = 0.0
        self.cull_back = cull_back
        self.is_ccw = is_ccw

    def initGL(self):
        self.vbo_points = glvbo.VBO(self.points, usage=gl.GL_DYNAMIC_DRAW)
        self.vbo_normals = glvbo.VBO(self.normals, usage=gl.GL_DYNAMIC_DRAW)
        self.vbo_indices = glvbo.VBO(self.triangles, target=gl.GL_ELEMENT_ARRAY_BUFFER)

    def drawGL(self):
        gl.glPushAttrib(gl.GL_CURRENT_BIT)
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glEnableClientState(gl.GL_NORMAL_ARRAY)
        self.draw()
        gl.glDisableClientState(gl.GL_NORMAL_ARRAY)
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glPopAttrib()

    def draw(self):
        gl.glPushAttrib(gl.GL_CURRENT_BIT)
        gl.glPushMatrix()

        # gl.glEnable(gl.GL_DEPTH_TEST)
        # gl.glDepthFunc(gl.GL_LESS)
        #
        gl.glEnable(gl.GL_CULL_FACE)
        if self.cull_back:
            gl.glCullFace(gl.GL_BACK)
        else:
            gl.glCullFace(gl.GL_FRONT)

        if self.is_ccw:
            gl.glFrontFace(gl.GL_CCW)
        else:
            gl.glFrontFace(gl.GL_CW)
        #
        # gl.glEnable(gl.GL_LIGHTING)
        # gl.glEnable(gl.GL_LIGHT0)
        # gl.glEnable(gl.GL_COLOR_MATERIAL)
        # gl.glColorMaterial(gl.GL_FRONT_AND_BACK, gl.GL_AMBIENT_AND_DIFFUSE)
        #
        # # self.gl.glMaterialfv(gl.GL_FRONT, gl.GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
        # # self.gl.glMaterialf(gl.GL_FRONT, gl.GL_SHININESS, 5.0)
        # # self.gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, (0.1, 0.1, 0.1, 1.0))
        #
        # gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, (0.0, 0.0, -100.0, 1.0))
        #gl.glShadeModel(gl.GL_SMOOTH)

        gl.glRotatef(self.angle_x, 1.0, 0.0, 0.0)
        gl.glRotatef(self.angle_y, 0.0, 1.0, 0.0)
        gl.glRotatef(self.angle_z, 0.0, 0.0, 1.0)

        self.vbo_points.bind()
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.vbo_points)

        self.vbo_indices.bind()
        self.vbo_normals.bind()
        gl.glEnableClientState(gl.GL_NORMAL_ARRAY)
        gl.glNormalPointer(gl.GL_FLOAT, 0, self.vbo_normals)

        gl.glLineWidth(0.5)
        #gl.glColor4f(1.0, 0.1, 0.1, 1.0)
        #gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
        gl.glColor4f(0.5, 0.5, 0.5, 1.0)
        gl.glDrawElements(gl.GL_TRIANGLES, 3 * len(self.triangles), gl.GL_UNSIGNED_INT, None)

        # gl.glPointSize(5.0)
        # gl.glDrawElements(gl.GL_POINTS, len(self.points), gl.GL_UNSIGNED_INT, None)

        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glDisableClientState(gl.GL_NORMAL_ARRAY)

        self.vbo_normals.unbind()
        self.vbo_indices.unbind()
        self.vbo_points.unbind()

        # gl.glDisable(gl.GL_DEPTH_TEST)
        gl.glDisable(gl.GL_CULL_FACE)
        # gl.glDisable(gl.GL_LIGHTING)
        # gl.glDisable(gl.GL_LIGHT0)
        # gl.glDisable(gl.GL_COLOR_MATERIAL)

        gl.glPopMatrix()
        gl.glPopAttrib()

    def mousePressed(self, x, y, button):
        self.mouse_is_pressed = True

    def mouseMoved(self, x, y, button):
        pass

    def mouseReleased(self, x, y, button):
        self.mouse_is_pressed = False

    def setPoints(self, points):
        self.vbo_points.set_array(points, points.nbytes)
        #print(points.min(axis=0), points.max(axis=0))
