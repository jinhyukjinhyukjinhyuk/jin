#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torchvision.transforms as transforms
from yolov4.utils import load_weights, detect_objects

# 모델 로드
model = Yolov4(classes=['person', 'animal'])
load_weights(model, "weights/yolov4-coco.weights")

# 변환 로드
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
])

# 이미지 로드
image = cv2.imread("image.jpg")
image = transform(image)

# 객체 탐지
boxes, labels, scores = detect_objects(model, image)

# 객체 인식
for box, label, score in zip(boxes, labels, scores):
    if label == 'person':
        print("사람")
    else:
        print("동물")

