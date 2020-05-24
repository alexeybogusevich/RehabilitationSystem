#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/19/19, 9:21 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

import sys

# sys.path.append("..")
import cv2
import dlib
import torch
import numpy as np
import torchvision.transforms as transforms
from lib3DDFA.utils.ddfa import ToTensorGjz, NormalizeGjz
from lib3DDFA import mobilenet_v1

from lib3DDFA.utils.inference import (
    parse_roi_box_from_landmark,
    crop_img,
    predict_68pts,
    predict_dense,
)


class FaceDetector(object):

    # FACEDETECTOR_MODEL_FILE = r"../data/models/opencv_dnn_face_detector/opencv_face_detector_uint8.pb"
    FACEDETECTOR_MODEL_FILE = "C:/Alex/ReabilitationSystem/data/models/opencv_dnn_face_detector/opencv_face_detector_uint8.pb"
    # FACEDETECTOR_CONFIG_FILE = r"../data/models/opencv_dnn_face_detector/opencv_face_detector.pbtxt"
    FACEDETECTOR_CONFIG_FILE = "C:/Alex/ReabilitationSystem/data/models/opencv_dnn_face_detector/opencv_face_detector.pbtxt"
    # LANDMARK_MODEL_FILE = r"../lib3DDFA/models/shape_predictor_68_face_landmarks.dat"
    LANDMARK_MODEL_FILE = (
        "C:/Alex/ReabilitationSystem/data/models/shape_predictor_68_face_landmarks.dat"
    )
    # LANDMARK_3DMODEL_FILE = r"../lib3DDFA/models/phase1_wpdc_vdc.pth.tar"
    LANDMARK_3DMODEL_FILE = (
        "C:/Alex/ReabilitationSystem/lib3DDFA/models/phase1_wpdc_vdc.pth.tar"
    )

    def __init__(self):
        self._init_models()

    def _init_models(self):
        """
        Initialize models
        """
        self.transform = transforms.Compose(
            [ToTensorGjz(), NormalizeGjz(mean=127.5, std=128)]
        )

        checkpoint = torch.load(
            FaceDetector.LANDMARK_3DMODEL_FILE,
            map_location=lambda storage, loc: storage,
        )["state_dict"]
        self.model = getattr(mobilenet_v1, "mobilenet_1")(
            num_classes=62
        )  # 62 = 12(pose) + 40(shape) +10(expression)

        model_dict = self.model.state_dict()
        # because the model is trained by multiple gpus, prefix module should be removed
        for k in checkpoint.keys():
            model_dict[k.replace("module.", "")] = checkpoint[k]
        self.model.load_state_dict(model_dict)
        self.model.eval()

        self.face_regressor = dlib.shape_predictor(FaceDetector.LANDMARK_MODEL_FILE)
        self.net = cv2.dnn.readNetFromTensorflow(
            FaceDetector.FACEDETECTOR_MODEL_FILE, FaceDetector.FACEDETECTOR_CONFIG_FILE
        )

        self.landmark_pts = None

    def detect_faces(self, frame):
        """
        Detect human faces on single frame
        """
        blob = cv2.dnn.blobFromImage(
            frame, 1.0, (300, 300), [104, 117, 123], False, False
        )
        self.net.setInput(blob)
        detections = self.net.forward()
        rects = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.6:
                x1 = int(detections[0, 0, i, 3] * frame.shape[1])
                y1 = int(detections[0, 0, i, 4] * frame.shape[0])
                x2 = int(detections[0, 0, i, 5] * frame.shape[1])
                y2 = int(detections[0, 0, i, 6] * frame.shape[0])
                rects.append(dlib.rectangle(x1, y1, x2, y2))
        return rects

    def predict(self, frame):
        rects = self.detect_faces(frame)
        if len(rects) > 0:
            pts = self.face_regressor(frame, rects[0]).parts()
            pts = np.array([[pt.x, pt.y] for pt in pts]).T
            self.landmark_pts = pts

        if self.landmark_pts is None:
            return

        roi_box = parse_roi_box_from_landmark(self.landmark_pts)
        img = crop_img(frame, roi_box)
        img = cv2.resize(img, dsize=(120, 120), interpolation=cv2.INTER_LINEAR)
        input = self.transform(img).unsqueeze(0)
        with torch.no_grad():
            param = self.model(input)
            param = param.squeeze().cpu().numpy().flatten().astype(np.float32)
        pts68 = predict_68pts(param, roi_box)
        vertex = predict_dense(param, roi_box)
        return vertex, rects, pts68
