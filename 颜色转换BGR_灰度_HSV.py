import cv2 as cv
import numpy as np
# cap = cv.VideoCapture(0)   # 读取视频帧数的句子
while(1):
    # 读取帧
    frame = cv.imread('F:\pythonProject\image_project\img.png')
    cv.imshow('image',frame)
    cv.waitKey(0)
    cv.destroyAllWindows()
    # 转换颜色空间 BGR 到 HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 定义HSV中蓝色的范围
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # 设置HSV的阈值使得只取蓝色
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # 将掩膜和图像逐像素相加
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()