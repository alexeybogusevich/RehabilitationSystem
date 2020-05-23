#!/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/22/19, 11:53 AM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.
#
#

from visuals.visitems.visitem import VisualItem

import numpy as np
import OpenGL.GL as gl
import OpenGL.arrays.vbo as glvbo


class ToyVisItem(VisualItem):

    def __init__(self, points):
        super(ToyVisItem, self).__init__()
        self.vbo = None
        self.mouse_is_pressed = False
        self.points = points

    def initGL(self):
        self.vbo = glvbo.VBO(self.points, usage=gl.GL_STATIC_DRAW)
        #self.vbo_control_points = glvbo.VBO(self.creator.get_curve_points(), usage=gl.GL_DYNAMIC_DRAW)

    def drawGL(self):
        gl.glPushAttrib(gl.GL_CURRENT_BIT)
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        self.draw()
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glPopAttrib()

    def draw(self):
        self.vbo.bind()
        gl.glVertexPointer(2, gl.GL_FLOAT, 0, self.vbo)
        gl.glColor4f(1.0, 0.0, 0.0, 1.0)
        gl.glDrawArrays(gl.GL_LINE_STRIP, 0, len(self.vbo))
        self.vbo.unbind()

        # self.vbo_control_points.bind()
        # gl.glVertexPointer(2, gl.GL_FLOAT, 0, self.vbo_control_points)
        # gl.glColor4f(0.5, 0.5, 0.5, 1.0)
        # gl.glDrawArrays(gl.GL_LINES, 0, len(self.vbo_control_points))
        #
        # gl.glPointSize(4.0)
        # gl.glDrawArrays(gl.GL_POINTS, 0, len(self.vbo_control_points))
        #
        # self.vbo_control_points.unbind()

    # def updateGLBuffers(self):
    #     self.vbo_bezier.set_array(self.creator.get_curve_points())
    #     self.vbo_control_points.set_array(self.creator.get_landmark_points())

    def mousePressed(self, x, y, button):
        self.mouse_is_pressed = True
        #self.creator.add_control_point(x, y)
        # self.updateGLBuffers()

    def mouseMoved(self, x, y, button):
        pass
        # if self.mouse_is_pressed:
        #     self.creator.set_tangent_point(x, y)
        # self.updateGLBuffers()

    def mouseReleased(self, x, y, button):
        self.mouse_is_pressed = False
