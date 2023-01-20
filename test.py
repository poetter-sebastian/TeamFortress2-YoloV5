import cv2
import torch
from PIL import Image

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp/weights/best.pt')  # or yolov5m, yolov5l, yolov5x, custom

# Images
img = 'Labled/20211018222332_1.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img, size=640)  # includes NMS

# Results
results.print()  
results.save()  # or .show()

results.xyxy[0]  # img1 predictions (tensor)
results.pandas().xyxy[0]  # img1 predictions (pandas)

input("Please enter something: ")