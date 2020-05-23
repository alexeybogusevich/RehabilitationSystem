#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/22/19, 10:55 AM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.
#

from visuals.visitems.visitem import VisualItem
import OpenGL.GL as gl


class PlotVisItem(VisualItem):

    def __init__(self, y=0.0, width=0.1, color=(1.0, 0.0, 0.0), max_points=300, range=(-90, 90)):
        super(PlotVisItem, self).__init__()
        self.mouse_is_pressed = False
        self.max_points = max_points
        self.width = width
        self.window_size = 5
        self.y = y
        self.plot = []
        self.plot_avg = []
        self.color = color
        self.range = range

    def initGL(self):
        pass

    def dump(self, filename):
        import pandas as pd
        import numpy as np

        df = pd.DataFrame()
        df['angle'] = (self.range[1] - self.range[0]) * np.asarray(self.plot_avg) + self.range[0]
        df.to_csv(filename)

    def drawGL(self):
        gl.glPushAttrib(gl.GL_CURRENT_BIT)
        self.draw()
        gl.glPopAttrib()

    def draw(self):
        gl.glPushAttrib(gl.GL_CURRENT_BIT)
        gl.glPushMatrix()

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0.0, 1.0, 1.0, 0.0, -1.0, 1.0)

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

        gl.glLineWidth(3.0)
        gl.glBegin(gl.GL_LINE_STRIP)
        gl.glColor3f(*self.color)
        for i, val in enumerate(self.plot_avg):
            gl.glVertex3f(float(i) / self.max_points, self.y + val * self.width, 0.0)
        gl.glEnd()

        gl.glPopMatrix()
        gl.glPopAttrib()

    def mousePressed(self, x, y, button):
        self.mouse_is_pressed = True

    def mouseMoved(self, x, y, button):
        pass

    def mouseReleased(self, x, y, button):
        self.mouse_is_pressed = False

    def addValue(self, p):
        self.plot.append((p - self.range[0]) / (self.range[1] - self.range[0]))

        window = self.plot[-self.window_size::]
        self.plot_avg.append(sum(window) / len(window))

        self.plot = self.plot[-self.max_points::]
        self.plot_avg = self.plot_avg[-self.max_points::]

        return self.plot_avg[-1] * (self.range[1] - self.range[0]) + self.range[0]



