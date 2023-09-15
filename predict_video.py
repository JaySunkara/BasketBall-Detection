import os

from ultralytics import YOLO
import cv2

model_path = os.path.join('.', 'runs', 'detect', 'train2', 'weights', 'last.pt')

# Load a model
model = YOLO(model_path)  # load a custom model

results = model.predict(source="IMG_9597.mp4", show=True)
