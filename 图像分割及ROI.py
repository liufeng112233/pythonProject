# -*- codeing = utf-8 -*-
# @time :2024/3/22 16:40
# @Project: pythonProject
# @Author : 刘风
# @File : 图像分割及ROI.py
# @Software :PyCharm
import cv2 as cv
import numpy as np
img1 = cv.imread('image_project/img.jpg')
img2 = cv.imread('image_project/img.jpg')
e1 = cv.getTickCount()
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
e2 = cv.getTickCount()
t = (e2-e1)/cv.getTickFrequency()
print(t)
cv.useOptimized()  # 判断是否采用opencv的优化代码