#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/19/19, 2:17 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.
#
from visuals.visitems.visitem import VisualItem

import OpenGL.GL as gl
import OpenGL.GLU as glu


class AxisVisItem(VisualItem):

    def __init__(self, center, angle1, angle2, angle3):
        super(AxisVisItem, self).__init__()
        self.mouse_is_pressed = False
        self.center = center
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.c1 = glu.gluNewQuadric()

    def initGL(self):
        pass

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
        # gl.glCullFace(gl.GL_FRONT)
        # gl.glFrontFace(gl.GL_CCW)
        #
        # gl.glEnable(gl.GL_LIGHTING)
        # gl.glEnable(gl.GL_LIGHT0)
        # gl.glEnable(gl.GL_COLOR_MATERIAL)
        # gl.glColorMaterial(gl.GL_FRONT_AND_BACK, gl.GL_AMBIENT_AND_DIFFUSE)

        #gl.glPushMatrix(gl.GL_MODELVIEW)
        # gl.glColor3f(1.0, 0.0, 0.0)
        # gl.glRotatef(180.0, 1.0, 0.0, 0.0)
        # gl.glTranslatef(self.center[0], self.center[1], self.center[2] - 5)
        # glu.gluCylinder(self.c1, 0.1, 0.1, 50.0, 10, 2)
        #
        # gl.glPopMatrix()
        # self.vbo_points.bind()
        # gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        # gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.vbo_points)
        #
        # self.vbo_indices.bind()
        #
        # gl.glLineWidth(5.0)
        # gl.glColor4f(1.0, 0.1, 0.1, 1.0)
        # gl.glDrawElements(gl.GL_LINES, 2 * len(self.lines), gl.GL_UNSIGNED_INT, None)
        #
        # # gl.glPointSize(5.0)
        # # gl.glDrawElements(gl.GL_POINTS, len(self.points), gl.GL_UNSIGNED_INT, None)
        #
        # gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        #
        # self.vbo_indices.unbind()
        # self.vbo_points.unbind()

        gl.glPopAttrib()

    def mousePressed(self, x, y, button):
        self.mouse_is_pressed = True

    def mouseMoved(self, x, y, button):
        pass

    def mouseReleased(self, x, y, button):
        self.mouse_is_pressed = False

    def setCenter(self, center):
        self.center = center
