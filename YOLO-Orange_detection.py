"""Use YOLO to detect and count oranges on my orange tree; eventually detect ripe vs. unripe"""

import cv2
import torch
import numpy as np
from ultralytics import YOLO

model = YOLO(".venv/yolo11n-seg.pt")

image1 = cv2.imread('assets/Orange_trees/orange1.jpg')
image2 = cv2.imread('assets/Orange_trees/orange2.jpg')

results1 = model('assets/Orange_trees/orange1.jpg', show=True, save=True)
results2 = model('assets/Orange_trees/orange2.jpg', show=True, save=True)

orange_count1 = 0
orange_count2 = 0

for result1 in results1:
    for box in result1.boxes:
        class_id = int(box.cls[0]) #oranges class ID = 49
        confidence = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        # print(f"Detected class ID: {class_id} (Confidence: {confidence:.2f}")

        if class_id == 49:
            orange_count1 += 1
            cv2.rectangle(image1, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image1, f"Orange {confidence:.2f}", (x1, y1 - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

for result2 in results2:
    for box in result2.boxes:
        class_id = int(box.cls[0]) #oranges class ID = 49
        confidence = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        # print(f"Detected class ID: {class_id} (Confidence: {confidence:.2f}")

        if class_id == 49:
            orange_count2 += 1
            cv2.rectangle(image2, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image2, f"Orange {confidence:.2f}", (x1, y1 - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


# cv2.imshow("Orange1 Detection", image1)
# cv2.imshow("Orange2 Detection", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()