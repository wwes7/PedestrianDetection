############################################
###     extract pictures from video     ###
###     Author:Yang Huanqi              ###
###     Date: 2018.4                    ###
###########################################

import cv2
import detect
vc = cv2.VideoCapture('test.mkv') #读入视频文件
c=0
rval=vc.isOpened()
#timeF = 1  #视频帧计数间隔频率
while rval:   #循环读取视频帧
    c = c + 100000000000
    rval, frame = vc.read()
#    if(c%timeF == 0): #每隔timeF帧进行存储操作
#        cv2.imwrite('smallVideo/smallVideo'+str(c) + '.jpg', frame) #存储为图像
    if rval:
        cv2.imwrite('D:\PedestrianDetection\images'+str(c).zfill(8) + '.jpg', frame) #存储为图像
        cv2.waitKey(1)
    else:
        break
vc.release()