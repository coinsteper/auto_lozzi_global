# -*- coding: utf-8 -*-
import pyautogui as pg
from PIL import ImageGrab
from functools import partial
import screeninfo
import time
import random
import os

img_more = r'C:\python\image_processing\auto_lozzi_global\img\more.png'
img_more2 = r'C:\python\image_processing\auto_lozzi_global\img\more2.png'
img_close = r'C:\python\image_processing\auto_lozzi_global\img\close.png'
img_back = r'C:\python\image_processing\auto_lozzi_global\img\back.png'

img_path_x_list = r'C:\python\image_processing\auto_lozzi_global\img\x'

img_x_list = os.listdir(img_path_x_list)

img_playstore = r'C:\python\image_processing\auto_lozzi_global\img\playstore.png'
img_switch = r'C:\python\image_processing\auto_lozzi\img\switch.png'
#ImageGrab.grab(bbox=None, include_layered_windows=True)

tvwindow = pg.getWindowsWithTitle('BlueStacks App Player')
left_g = tvwindow[0].left
top_g = tvwindow[0].top
width_g = tvwindow[0].width
height_g = tvwindow[0].height
start_time = time.time()

def find_and_click(img, pos=0):
    global start_time
    Flag = False
    b_random_click = False
    confi = 0.92
    left_random = 0
    left_top = 0

    top_ = top_g
    left_ = left_g
    width_ = width_g
    height_ = height_g

    find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))

    if find_img != None:        
        time.sleep(0.01)
        start_time = time.time()

        # 더 받기 랜덤한 좌표 클릭해서 봇체크 우회
        if img == img_more or img == img_more2:
            find_img = (find_img.left + random.randrange(-5, 5), find_img.top + random.randrange(-5, 5), find_img.width,
                        find_img.height)
            time.sleep(0.01)
        
        #x 잘못 클릭해서 링크로 빠지는거 방지
        if '_x_' in img:
            
            while True:
                time.sleep(1)
                find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))
                if find_img != None:
                    break

        pg.click(find_img, clicks=1, duration=0.1)

        start_time = time.time()
        Flag = True

    return Flag


def make_switch():
    start_time = time.time()

    while True:
        if time.time() - start_time >= 5:
            break

        time.sleep(0.2)

        if find_and_click(img_playstore):
            time.sleep(0.5)

            while True:
                if time.time() - start_time >= 5:
                    break

                time.sleep(0.2)
                if find_and_click(img_back):
                    start_time = time.time()
                    return True


if __name__ =='__main__':
    try:
        while True:            
            find_and_click(img_more)
            find_and_click(img_more2)
            find_and_click(img_close)

            # x는 동적으로 추가되더라도 잘 실행 되기 위해
            for i in img_x_list:
                find_and_click(img_path_x_list + '\\' + i, 1)

            if time.time() - start_time >= 30:
                make_switch()

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass
