############################################
###different ways to strengthen pictures###
###     Author:Yang Huanqi              ###
###     Date: 2018.4                    ###
###########################################

import cv2
## 读取图片
img = cv2.imread("1.png")

## 分别进行 铅笔画、风格化、细节增强、边缘保持等处理
dst1_gray, dst1_color = cv2.pencilSketch(img, sigma_s = 50, sigma_r = 0.15, shade_factor = 0.04)
dst2 = cv2.stylization(img, sigma_s = 50, sigma_r = 0.15)
dst3 = cv2.detailEnhance(img, sigma_s = 50, sigma_r = 0.15)
dst4 = cv2.edgePreservingFilter(img, flags=1, sigma_s = 50, sigma_r = 0.15)

## 显示
cv2.imshow("source", img)
cv2.imshow("pencilSketchG", dst1_gray)
cv2.imshow("pencilSketchC", dst1_color)
cv2.imshow("stylization", dst2)
cv2.imshow("detailEnhance", dst3)
cv2.imshow("edgePreserving", dst4)
cv2.waitKey()
cv2.destroyAllWindows()