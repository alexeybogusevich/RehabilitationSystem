#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/23/19, 12:32 AM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

import sys
from PyQt5 import QtCore
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import easygui
from database.database_access import *
from report.generator import *

class StatRecords(QtCore.QObject):

    valuesChangedL = QtCore.pyqtSignal(str, float, float, float, int)
    valuesChangedR = QtCore.pyqtSignal(str, float, float, float, int)

    def __init__(self, parent=None):
        super(StatRecords, self).__init__(parent)
        self.patientId = 2
        self.yaw_l = []
        self.yaw_r = []
        self.pitch_l = []
        self.pitch_r = []
        self.roll_l = []
        self.roll_r = []

    def updateYaw(self, yaw_val):
        if yaw_val < 0.0:
            self.yaw_l.append(yaw_val)
            self.valuesChangedL.emit("yaw", *self.stat(self.yaw_l))
        else:
            self.yaw_r.append(yaw_val)
            self.valuesChangedR.emit("yaw", *self.stat(self.yaw_r))

    def updatePitch(self, pitch_val):
        if pitch_val < 0.0:
            self.pitch_l.append(pitch_val)
            self.valuesChangedL.emit("pitch", *self.stat(self.pitch_l))
        else:
            self.pitch_r.append(pitch_val)
            self.valuesChangedR.emit("pitch", *self.stat(self.pitch_r))

    def updateRoll(self, roll_val):
        if roll_val < 0.0:
            self.roll_l.append(roll_val)
            self.valuesChangedL.emit("roll", *self.stat(self.roll_l))
        else:
            self.roll_r.append(roll_val)
            self.valuesChangedR.emit("roll", *self.stat(self.roll_r))

    def stat(self, arr):
        amin = min(arr) if len(arr) > 0 else 0
        amax = max(arr) if len(arr) > 0 else 0
        avg = np.average(arr) if len(arr) > 0 else 0
        return amin, amax, avg, len(arr)

    def saveRaw(self, filename):
        with open(filename, "w") as fout:
            fout.write("Pitch_Left, " + ", ".join(map(str, self.pitch_l)) + "\n")
            fout.write("Pitch_Right, " + ", ".join(map(str, self.pitch_r)) + "\n")
            fout.write("Yaw_Left, " + ", ".join(map(str, self.yaw_l)) + "\n")
            fout.write("Yaw_Right, " + ", ".join(map(str, self.yaw_r)) + "\n")
            fout.write("Roll_Left, " + ", ".join(map(str, self.roll_l)) + "\n")
            fout.write("Roll_Right, " + ", ".join(map(str, self.roll_r)) + "\n")

    def writeToDb(self):
        max_yaw_l = self.stat(self.yaw_l)[1]
        max_yaw_r = self.stat(self.yaw_r)[1]
        max_roll_l = self.stat(self.roll_l)[1]
        max_roll_r = self.stat(self.roll_r)[1]
        max_pitch_l = self.stat(self.pitch_l)[1]
        max_pitch_r = self.stat(self.pitch_r)[1]
        
        context = connectToDb()
        cursor = context.cursor()

        insertExamination(
        cursor,context, PatientID=self.patientId,
        YawLeft=max_yaw_l,YawRight=max_yaw_r, 
        RollLeft=max_roll_r, RollRight=max_roll_r,
        PitchDown=max_pitch_l, PitchUp=max_pitch_r)
        cursor.close()
        del cursor

    def generateReport(self, file_path):
        max_yaw_l = list(self.stat(self.yaw_l))[1]
        max_yaw_r = list(self.stat(self.yaw_r))[1]
        max_roll_l = list(self.stat(self.roll_l))[1]
        max_roll_r = list(self.stat(self.roll_r))[1]
        max_pitch_l = list(self.stat(self.pitch_l))[1]
        max_pitch_r = list(self.stat(self.pitch_r))[1]
        root = tk.Tk()
        root.withdraw()
        context = connectToDb()
        cursor = context.cursor()
        pId = self.patientId
        patient = getPatientById(pId)
        generator.create_report(
        output_file = file_path,
        _rollleft=max_roll_l,
        _rollright=max_roll_r,
        _yawleft=max_yaw_l,
        _yawright=max_yaw_r,
        _pitchdown=max_pitch_l,
        _pitchup=max_pitch_r,
        _name=patient[1],
        _card=patient[8],
        _number=patient[6],
        )
        cursor.close()
        del cursor

    def saveExcel(self, filename):
        df = pd.DataFrame(
            {
                "Angle": ["Min", "Max", "Avg", "Rep"],
                "Pitch_Left": list(self.stat(self.pitch_l)),
                "Pitch_Right": list(self.stat(self.pitch_r)),
                "Yaw_Left": list(self.stat(self.yaw_l)),
                "Yaw_Right": list(self.stat(self.yaw_r)),
                "Roll_Left": list(self.stat(self.roll_l)),
                "Roll_Right": list(self.stat(self.roll_r)),
            }
        )

        df = df.set_index(["Angle"])

        with pd.ExcelWriter(filename) as writer:
            df.to_excel(writer)
