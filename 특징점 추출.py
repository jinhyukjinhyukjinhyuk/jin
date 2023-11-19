#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

def find_matches(image1, image2):
    # SIFT 특징점 검출 및 기술자 생성
    sift = cv2.SIFT_create()

    # 이미지 로드 및 그레이스케일 변환
    img1 = cv2.imread(image1)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    img2 = cv2.imread(image2)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # 특징점 검출 및 기술자 계산
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    # 특징점 매칭
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # 매칭 결과 시각화
    result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:137], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv2.imshow('Matches', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# logo1.jpg와 scene1.jpg 간에 특징점 매칭 수행
find_matches('logo1.jpg', 'scene1.jpg')

# logo2.jpg와 scene2.jpg 간에 특징점 매칭 수행
find_matches('logo2.jpg', 'scene2.jpg')

