from ultralytics import YOLO
import cv2

model=YOLO('yolov8m.pt')
results=model(r"C:\Users\lenovo\Downloads\Object-Detection-101\Chapter 5 - Running Yolo\Images\1.png",show=True)
cv2.waitKey(0)