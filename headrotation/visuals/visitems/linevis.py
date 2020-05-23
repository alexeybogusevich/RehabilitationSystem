#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/22/19, 11:53 AM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.
#

from visuals.visitems.visitem import VisualItem

import numpy as np
import OpenGL.GL as gl
import OpenGL.arrays.vbo as glvbo


class LineVisItem(VisualItem):

    def __init__(self, points):
        super(LineVisItem, self).__init__()
        self.vbo_points = None
        self.vbo_indices = None
        self.mouse_is_pressed = False
        self.points = points
        self.lines = np.arange(len(points)).reshape(len(points) // 2, 2).astype(np.uint32)

    def initGL(self):
        self.vbo_points = glvbo.VBO(self.points, usage=gl.GL_DYNAMIC_DRAW)
        self.vbo_indices = glvbo.VBO(self.lines, target=gl.GL_ELEMENT_ARRAY_BUFFER)

    def drawGL(self):
        gl.glPushAttrib(gl.GL_CURRENT_BIT)
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        self.draw()
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glPopAttrib()

    def draw(self):
        gl.glPushAttrib(gl.GL_CURRENT_BIT)

        self.vbo_points.bind()
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.vbo_points)

        self.vbo_indices.bind()

        gl.glLineWidth(5.0)
        gl.glColor4f(1.0, 0.1, 0.1, 1.0)
        #gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
        gl.glDrawElements(gl.GL_LINES, 2 * len(self.lines), gl.GL_UNSIGNED_INT, None)

        # gl.glPointSize(5.0)
        # gl.glDrawElements(gl.GL_POINTS, len(self.points), gl.GL_UNSIGNED_INT, None)

        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)

        self.vbo_indices.unbind()
        self.vbo_points.unbind()

        gl.glPopAttrib()

    def mousePressed(self, x, y, button):
        self.mouse_is_pressed = True

    def mouseMoved(self, x, y, button):
        pass

    def mouseReleased(self, x, y, button):
        self.mouse_is_pressed = False

    def setPoints(self, points):
        self.points = points
        self.vbo_points.set_array(points, points.nbytes)
