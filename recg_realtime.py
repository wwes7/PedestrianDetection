############################################
###     real time show the result       ###
###     Author:Yang Huanqi              ###
###     Date: 2018.4                    ###
###########################################

from __future__ import print_function
from imutils.object_detection import non_max_suppression
import argparse
import imutils
import numpy as np
import cv2

cap = cv2.VideoCapture('video/person.mkv')

hog = cv2.HOGDescriptor()   #初始化方向梯度直方图描述子
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


while(cap.isOpened()):

    ret,frame = cap.read()
    frame = cv2.detailEnhance(frame, )
    (rects, weights) = hog.detectMultiScale(frame, winStride=(8,8),
                                            padding=(2,2), scale=1.5)


    # 应用非极大抑制方法，通过设置一个阈值来抑制那些重叠的边框
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)


    cv2.imshow('frame',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
