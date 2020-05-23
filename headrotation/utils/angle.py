#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/19/19, 11:24 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

import numpy as np


class Angle(object):

    def __init__(self):
        self.points = None
        self._yaw = 0.0
        self._pitch = 0.0
        self._roll = 0.0

    def set(self, points):
        self.points = points
        rotate_skul = np.array([0.0, 0.0, 0.0])
        for i in range(7):
            rotate_skul += (self.points[i] - self.points[16 - i])
        rotate_skul /= np.linalg.norm(rotate_skul)

        self._yaw = self.__yaw_angle(-rotate_skul)
        self._roll = -self.__roll_angle(-rotate_skul)

        # determine eye axis
        rotate_eye = self.right_eye_normal() + self.left_eye_normal()
        rotate_eye /= np.linalg.norm(rotate_eye)

        self._pitch = -self.__pitch_angle(rotate_eye)

    def yaw(self):
        return self._yaw

    def pitch(self):
        return self._pitch

    def roll(self):
        return self._roll

    def __eye_normal(self, start_i, end_i, return_center=False):
        center = self.points[start_i:(end_i+1)].mean(axis=0)
        norm = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        for i in range(6):
            ni = (i + 1) % 6
            v1, v2 = self.points[start_i + i] - center, self.points[start_i + ni] - center
            v1 /= np.linalg.norm(v1)
            v2 /= np.linalg.norm(v2)
            vn = np.cross(v1, v2)
            vn /= np.linalg.norm(vn)
            norm += vn
        norm = norm / np.linalg.norm(norm)
        if return_center:
            return norm, center
        return norm

    def __angle(self, vec, main_axis, rotation_axis):
        vec /= np.linalg.norm(vec)
        cos_angle = np.dot(vec, main_axis)
        angle = np.arccos(cos_angle) * 180 / np.pi
        rot_norm = np.cross(vec, main_axis)
        rot_norm /= np.linalg.norm(rot_norm)
        if np.dot(rot_norm, rotation_axis) > 0.0:
            angle = -angle
        return angle

    def __yaw_angle(self, vec):
        vec = vec.copy()
        vec[1] = 0.0
        return self.__angle(vec, np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]))

    def __pitch_angle(self, vec):
        return self.__roll_angle(vec)

    def __roll_angle(self, vec):
        main_axis = vec.copy()
        main_axis[1] = 0.0
        main_axis /= np.linalg.norm(main_axis)
        rotation_axis = np.cross(main_axis, np.array([0.0, 1.0, 0.0]))
        rotation_axis /= np.linalg.norm(rotation_axis)
        return self.__angle(vec, main_axis, rotation_axis)

    def right_eye_normal(self, return_center=False):
        return self.__eye_normal(36, 41, return_center)

    def left_eye_normal(self, return_center=False):
        return self.__eye_normal(42, 47, return_center)