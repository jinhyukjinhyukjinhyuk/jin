#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import time
import pyautogui
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# 검색어 입력
keyword = pyautogui.prompt("검색어를 입력해주세요.")

# 저장 폴더 중복 검사
folder_exists = os.path.exists(keyword)

# 조건에 따른 저장 폴더 생성
if not folder_exists:
    os.mkdir(keyword)

# 브라우저 자동 꺼짐 방지하기
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Chrome 드라이버 설치 및 설정
driver_manager = ChromeDriverManager()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# 크롬 열고, 화면 최대화
driver.maximize_window()

# 검색어 입력했을 때, 구글 이미지 검색 결과 페이지
driver.get(f"https://www.google.com/search?tbm=isch&q={keyword}")

# 웹페이지가 로딩될 때까지 10초 기다림
driver.implicitly_wait(10)

# 이미지 저장 함수
def save_image(image_url, save_path):
    response = requests.get(image_url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

# 무한 스크롤 처리
# 스크롤 내리기 전 위치
before_h = driver.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤 내리기
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    # 스크롤 사이의 페이지 로딩 시간
    time.sleep(3)
    # 스크롤 후 높이
    after_h = driver.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 이미지 요소 찾기
image_elements = driver.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")

# 이미지 저장
for i, image_element in enumerate(image_elements):
    image_url = image_element.get_attribute('src')
    if image_url.startswith('data:image'):
        # 이미지 URL이 data URL인 경우 스킵
        continue
    save_path = os.path.join(keyword, f"{keyword}_{i+1}.jpg")
    save_image(image_url, save_path)

# 브라우저 종료
driver.quit()

