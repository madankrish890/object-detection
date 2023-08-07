import cv2
import numpy as np
# print('package imported')
# image read
# img=cv2.imread(r"C:\Users\lenovo\Downloads\d1.jpg")
#
# cv2.imshow('output',img)
# cv2.waitKey(0)


# # video Read
# cap=cv2.VideoCapture(r"D:\pytube\video\titanic_sub.mp4")
#
# while True:
#     success,img=cap.read()
#     cv2.imshow('video',img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

# Webcam
# cap=cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(1,100)
#
# while True:
#     success,img=cap.read()
#     cv2.imshow('video',img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

# Basic functions
# img=cv2.imread(r"C:\Users\lenovo\Downloads\d1.jpg")
# kernel=np.ones((5,5),np.uint8)
#
# imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur=cv2.GaussianBlur(imggray,(7,7),0)
# imgcanny=cv2.Canny(img,150,200)
# imgdialation=cv2.dilate(imgcanny,kernel,iterations=5)
# imgerode=cv2.erode(imgdialation,kernel,iterations=5)
#
# cv2.imshow("Gray image",imggray)
# cv2.imshow("Blur image",imgblur)
# cv2.imshow('Canny image',imgcanny)
# cv2.imshow('img dialation',imgdialation)
# cv2.imshow('img erode',imgerode)

# Resizing

# img=cv2.imread(r"C:\Users\lenovo\Downloads\d1.jpg")
# #print(img.shape) (675, 1200, 3)
# imgresize=cv2.resize(img,(300,200))
# imgcrop=img[200:400,400:800]
#
# cv2.imshow("original image",img)
# cv2.imshow('Resize',imgresize)
# cv2.imshow('crop',imgcrop)
# cv2.waitKey(0)


# img=np.zeros((512,512,3),np.uint8)
# print(img.shape)
# #img[:]=255,0,0
#
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),1)
# cv2.circle(img,(450,50),30,(0,255,0),2)
# cv2.putText(img,"opencv",(256,256),cv2.FONT_ITALIC,1,(350,350,0),2)
# cv2.imshow('image',img)
#
# img=cv2.imread((r"C:\Users\lenovo\Downloads\images.jfif"))
#
# width,height=250,350
#
# pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix=cv2.getPerspectiveTransform(pts1,pts2)
# imgoutput=cv2.warpPerspective(img,matrix,(width,height))
#
#
# cv2.imshow("image",img)
# cv2.imshow('output',imgoutput)
# cv2.waitKey(0)

# img=cv2.imread((r"C:\Users\lenovo\Downloads\images.jfif"))
#
# hor=np.hstack((img,img))
# ver=np.vstack((img,img))
#
# cv2.imshow('Horizontal',hor)
# cv2.imshow('Vertical',ver)
#
# cv2.waitKey(0)


# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver
#
# img = cv2.imread(r"C:\Users\lenovo\Downloads\images")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img]))
#
# # imgHor = np.hstack((img,img))
# # imgVer = np.vstack((img,img))
# #
# # cv2.imshow("Horizontal",imgHor)
# # cv2.imshow("Vertical",imgVer)
# cv2.imshow("ImageStack",imgStack)
#
# cv2.waitKey(0)



