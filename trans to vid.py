############################################
###     transfer pictures to video      ###
###     Author:Yang Huanqi              ###
###     Date: 2018.4                    ###
###########################################

import cv2
import glob

fps = 10  # 保存视频的FPS，可以适当调整

# 可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc(*'x264')
videoWriter = cv2.VideoWriter('saveVideo.avi', fourcc, fps, (480, 360), False)  # 最后一个是保存图片的尺寸
imgs = glob.glob('D:\PedestrianDetection\imag\*.png')
for imgname in imgs:
    frame = cv2.imread(imgname)
    videoWriter.write(frame)
videoWriter.release()