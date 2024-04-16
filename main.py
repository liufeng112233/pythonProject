import cv2 as cv  # 默认读取的图片的格式是BGR，而不是常规的RGB格式
import numpy as np
import matplotlib.pyplot as plt


def cv_show(name, img):
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def plot_all():
    img1 = np.zeros((512, 512, 3), np.uint8)
    cv.line(img1, (0, 0), (511, 511), (255, 0, 0), 5)  # 绘制直线
    cv.rectangle(img1, (384, 0), (510, 128), (0, 255, 0), 3)  # 绘制矩形
    cv.circle(img1, (447, 63), 63, (0, 0, 255), -1)  # 绘制圆
    cv.ellipse(img1,(256,256),(100,50),0,0,180,255,-1)   # 绘制椭圆
    # 绘制多边形
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(img1, [pts], True, (0, 255, 255))
    # 向图像添加文本
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img1, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

    cv.imshow("line", img1)
    cv.waitKey(0)
    cv.destroyAllWindows()

def plot_mouse():  # 鼠标绘制圆形，点击位置绘制图像
    def draw_circle(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img, (x, y), 100, (255, 0, 0), -1)

    # 创建一个黑色的图像，一个窗口，并绑定到窗口的功能
    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    while (1):
        cv.imshow('image', img)
        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()


# img.shape
if __name__ == '__main__':
    name = 'image'
    img = cv.imread("F:\pythonProject\image_project/img.jpg")
    # cv_show(name, img)
    # plot_all()
    # plot_mouse()
