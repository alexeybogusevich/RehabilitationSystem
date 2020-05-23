#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/19/19, 9:15 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

import cv2
import argparse
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from datetime import datetime
from scipy.io import loadmat
# inner packages
from glviewer import GLViewer
from angleswidget import AnglesWidget
from imagewidget import ImageWidget

from visuals.visitems import surfacevis, kpvis, plotvis, linevis
from utils.image import toQImage
from utils.angle import Angle
from facedetector import FaceDetector
from utils.load3d import load3d_obj
from utils.vtracker import VTracker
from utils.stat import StatRecords
from scipy.spatial import Delaunay


DOWNSAMPLE = 2
TEXTSCALE = 1.5 / DOWNSAMPLE


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, args, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.output_filename = datetime.now().strftime("%Y%m%d-%H%M%S")

        self.glviewer = None
        if not args.no3d:
            self.glviewer = GLViewer()
            #self.glviewer.faces = loadmat('../Lib3DDFA/visualize/tri.mat')['tri'] - 1
            self.glviewer.faces = loadmat('C:/Alex/ReabilitationSystem/lib3DDFA/visualize/tri.mat')['tri'] - 1

            #points, triangles, normals = load3d_obj("../data/model3d/male_head_fix3.obj")
            points, triangles, normals = load3d_obj("C:/Alex/ReabilitationSystem/data/model3d/male_head_fix3.obj")
            points[..., 2] = -points[..., 2]
            self.avatar = surfacevis.SurfaceVisItem(points * 5.0, triangles, normals, False, True)

        self.plot_pitch = plotvis.PlotVisItem(0.0, 0.05, (1.0, 0.0, 0.0))
        self.plot_roll = plotvis.PlotVisItem(0.05, 0.05, (0.0, 1.0, 0.0))
        self.plot_yaw = plotvis.PlotVisItem(0.1, 0.05, (0.0, 0.0, 1.0))

        self.facedet = FaceDetector()

        if not args.no3d:
            self.glviewer.addItem(self.avatar)
            self.glviewer.addItem(self.plot_yaw)
            self.glviewer.addItem(self.plot_roll)
            self.glviewer.addItem(self.plot_pitch)

        self.vc = cv2.VideoCapture(args.input)

        self.frame_width = int(self.vc.get(3))
        self.frame_height = int(self.vc.get(4))

        self.show_face = args.show_face

        self.video_out = None
        if args.save_video:
            self.video_out = cv2.VideoWriter("../output/" + self.output_filename + ".mp4",
                                             cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 7,
                                             (self.frame_width // DOWNSAMPLE, self.frame_height // DOWNSAMPLE))

        self.process_timer = QtCore.QTimer()
        self.process_timer.timeout.connect(self.processSourceFrame)
        self.process_timer.start(1)

        self.angle_handler = Angle()

        self.imgwidget = ImageWidget()
        layout2 = QtWidgets.QVBoxLayout()

        self.anglewidget = AnglesWidget()
        self.anglewidget.setMaximumHeight(130)

        layout = QtWidgets.QHBoxLayout()
        layout2.addWidget(self.anglewidget)
        if not args.no3d:
            layout.addWidget(self.glviewer)
        layout.addWidget(self.imgwidget)
        layout2.addItem(layout)

        mainwidget = QtWidgets.QWidget()
        mainwidget.setLayout(layout2)
        self.setCentralWidget(mainwidget)

        self.stat_records = StatRecords()
        self.stat_records.valuesChangedL.connect(self.anglewidget.updateRangeLStatistics)
        self.stat_records.valuesChangedR.connect(self.anglewidget.updateRangeRStatistics)

        self.yaw_tracker = VTracker()
        self.yaw_tracker.maximum_found.connect(self.stat_records.updateYaw)

        self.pitch_tracker = VTracker()
        self.pitch_tracker.maximum_found.connect(self.stat_records.updatePitch)

        self.roll_tracker = VTracker()
        self.roll_tracker.maximum_found.connect(self.stat_records.updateRoll)

        self.draw_triangulation = False
        self.triangulation = None
        self.triangulation_ls = None

        menu = self.menuBar()
        view_menu = menu.addMenu("View")
        triAction = QtWidgets.QAction("Triangulation", parent=self)
        triAction.setCheckable(True)
        triAction.setShortcut("Ctrl+M")
        triAction.toggled.connect(self.drawTriangulation)
        view_menu.addAction(triAction)

    def updateYaw(self, value):
        print("Yaw maxima:", value)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.stat_records.saveRaw("../output/" + self.output_filename + ".txt")
        self.stat_records.saveExcel("../output/" + self.output_filename + ".xlsx")

    def processSourceFrame(self):
        success, frame = self.vc.read()
        if success:
            sz = frame.shape
            frame = cv2.resize(frame, (sz[1] // DOWNSAMPLE, sz[0] // DOWNSAMPLE))
            sz = frame.shape

            frame = cv2.flip(frame, 1)
            pred = self.facedet.predict(frame)

            if pred is None:
                return

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            gray3 = np.stack([gray] * 3, axis=-1)

            vertices, rects, pts68 = pred
            if len(vertices) > 0:

                if self.show_face:
                    for rect in rects:
                        p1 = rect.tl_corner()
                        p2 = rect.br_corner()
                        cv2.rectangle(gray3, (p1.x, p1.y), (p2.x, p2.y), (0, 0, 255), 2)

                if self.triangulation is None:
                    pts68proj = pts68[[0, 1]]
                    self.triangulation = Delaunay(pts68proj.T)
                    self.triangulation_ls = set()

                    for simplex in self.triangulation.simplices:
                        for i in range(3):
                            for j in range(i, 3):
                                if simplex[i] > simplex[j]:
                                    self.triangulation_ls.add((simplex[j], simplex[i]))
                                else:
                                    self.triangulation_ls.add((simplex[i], simplex[j]))

                if self.draw_triangulation:
                    for line in self.triangulation_ls:
                        i1, i2 = line
                        p1 = (pts68[0][i1], pts68[1][i1])
                        p2 = (pts68[0][i2], pts68[1][i2])
                        cv2.line(gray3, p1, p2, (255, 255, 150), 1, cv2.LINE_AA)

                pts = np.zeros(shape=(68, 3), dtype=np.float32)
                pts[:, 0] = (pts68[0] - sz[1]/2)
                pts[:, 1] = (sz[0]/2 - pts68[1])
                pts[:, 2] = pts68[2]

                self.angle_handler.set(pts)
                angle_yaw = self.angle_handler.yaw()
                angle_roll = self.angle_handler.roll()
                angle_pitch = self.angle_handler.pitch()

                self.anglewidget.setPitch(angle_pitch)
                self.anglewidget.setRoll(angle_roll)
                self.anglewidget.setYaw(angle_yaw)

                angle_yaw_s = self.plot_yaw.addValue(angle_yaw)
                angle_roll_s = self.plot_roll.addValue(angle_roll)
                angle_pitch_s = self.plot_pitch.addValue(angle_pitch)

                self.yaw_tracker.update(angle_yaw_s)
                self.roll_tracker.update(angle_roll_s)
                self.pitch_tracker.update(angle_pitch_s)

                self.avatar.angle_y = 180.0 + angle_yaw
                self.avatar.angle_x = -angle_pitch
                self.avatar.angle_z = angle_roll

            qimage = toQImage(gray3)

            w = self.imgwidget.width()
            h = self.imgwidget.height()

            pmap = QtGui.QPixmap(qimage).scaled(sz[1] * h / sz[0], h)
            r = QtCore.QRect((pmap.width() - w) / 2, 0, w, h)

            self.imgwidget.setPixmap(pmap.copy(r))

            if self.video_out is not None:
                out_frame = gray3.copy()
                text_pitch = "Pitch: {0:.0f}".format(angle_pitch_s)
                text_roll = "Roll: {0:.0f}".format(angle_roll_s)
                text_yaw = "Yaw: {0:.0f}".format(angle_yaw_s)

                cv2.putText(out_frame, text_pitch, (5, 50), cv2.FONT_HERSHEY_TRIPLEX, TEXTSCALE, (10, 10, 200))
                cv2.putText(out_frame, text_roll, (5, 90), cv2.FONT_HERSHEY_TRIPLEX, TEXTSCALE, (10, 10, 200))
                cv2.putText(out_frame, text_yaw, (5, 130), cv2.FONT_HERSHEY_TRIPLEX, TEXTSCALE, (10, 10, 200))

                self.video_out.write(out_frame)

        if self.glviewer is not None:
            self.glviewer.repaint()

    def drawTriangulation(self, draw=True):
        self.draw_triangulation = draw


def main(args):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow(args)
    window.showMaximized()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default=0, dest='input')
    parser.add_argument('-n', '--no3d', action='store_true', dest='no3d')
    main(parser.parse_args())
