# -*- coding: utf-8 -*-
import pyautogui as pg
#from PIL import ImageGrab
from functools import partial
import screeninfo
import time
import random
import os
import sys
import keyboard
import threading

### box ###
img_box = r'C:\python\image_processing\auto_lozzi_global\img\box.png'
img_more_box_g = r'C:\python\image_processing\auto_lozzi_global\img\more_box_g.png'
img_more_box = r'C:\python\image_processing\auto_lozzi_global\img\more_box.png'
img_more_box2 = r'C:\python\image_processing\auto_lozzi_global\img\more_box2.png'
img_gold_box = r'C:\python\image_processing\auto_lozzi_global\img\goldbox.png'
img_gold_box_open = r'C:\python\image_processing\auto_lozzi_global\img\goldbox_open.png'
img_ok = r'C:\python\image_processing\auto_lozzi_global\img\ok.png'
img_ok2 = r'C:\python\image_processing\auto_lozzi_global\img\ok2.png'

img_more = r'C:\python\image_processing\auto_lozzi_global\img\more.png'
img_more2 = r'C:\python\image_processing\auto_lozzi_global\img\more2.png'
img_close = r'C:\python\image_processing\auto_lozzi_global\img\close.png'
img_close2 = r'C:\python\image_processing\auto_lozzi_global\img\close2.png'
img_close3 = r'C:\python\image_processing\auto_lozzi_global\img\close3.png'
img_back = r'C:\python\image_processing\auto_lozzi_global\img\back.png'
img_appstore = r'C:\python\image_processing\auto_lozzi_global\img\appstore.png'
img_appstore2 = r'C:\python\image_processing\auto_lozzi_global\img\appstore2.png'
img_appstore3 = r'C:\python\image_processing\auto_lozzi_global\img\appstore3.png'
img_web = r'C:\python\image_processing\auto_lozzi_global\img\web.png'

img_path_x_list = r'C:\python\image_processing\auto_lozzi_global\img\x'
img_x_list = os.listdir(img_path_x_list)


### 
img_playstore = r'C:\python\image_processing\auto_lozzi_global\img\playstore.png'
img_switch = r'C:\python\image_processing\auto_lozzi_global\img\switch.png'
#ImageGrab.grab(bbox=None, include_layered_windows=True)

#900 * 1600
#400 * 685
tvwindow = pg.getWindowsWithTitle('BlueStacks App Player')
left_g = tvwindow[0].left
top_g = tvwindow[0].top
width_g = tvwindow[0].width
height_g = tvwindow[0].height
start_time = time.time()
switch_flag = False

def checker():
    global switch_flag
    while True:
        time.sleep(0.5)
        pressed_key = keyboard.is_pressed('INSERT')
        if pressed_key:
            switch_flag = not switch_flag

            if switch_flag:
                print('switch on')
            else :
                print('switch off')                

            time.sleep(0.5)


def find_img(img, pos=0):
    global start_time
    Flag = False
    confi = 0.92
    
    top_ = top_g
    left_ = left_g
    width_ = width_g
    height_ = height_g

    find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))
    if find_img != None:
        Flag = True

    return Flag

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

    if pos == 1:
        top_ = top_ + 10
        width_ = width_ - 260
        height_ = height_ - 600

    elif pos == 2:
        top_ = top_ + 10
        left_ = left_ + 120
        width_ = width_ - 150
        height_ = height_ - 600

    elif pos == 3:
        top_ = top_ + 10
        left_ = left_ + 240
        width_ = width_ - 10
        height_ = height_ - 600
    
    elif pos == 4:
        top_ = top_ + 240
        left_ = left_
        width_ = width_ - 260
        height_ = height_ - 350
    
    elif pos == 5:
        top_ = top_ + 240
        left_ = left_ + 120
        width_ = width_ - 120
        height_ = height_ - 350
    
    elif pos == 6:
        top_ = top_ + 240
        left_ = left_ + 240
        width_ = width_ - 10
        height_ = height_ - 350
    
    elif pos == 7:
        top_ = top_ + 500
        left_ = left_
        width_ = width_ - 260
        height_ = height_

    elif pos == 8:
        top_ = top_ + 500
        left_ = left_ + 120
        width_ = width_ - 120
        height_ = height_

    elif pos == 9:
        top_ = top_ + 500
        left_ = left_ + 240
        width_ = width_ - 10
        height_ = height_

    elif pos == 10:
        top_ = top_
        left_ = left_
        width_ = width_
        height_ = height_ - 600
    
    elif pos == 20:
        top_ = top_ + 240
        left_ = left_
        width_ = width_ - 10
        height_ = height_ - 350
    
    elif pos == 30:
        top_ = top_ + 500
        left_ = left_
        width_ = width_
        height_ = height_

    find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))
    time.sleep(0.2)

    if find_img != None:
        print(img)
        time.sleep(0.01)
        start_time = time.time()

        # 더 받기 랜덤한 좌표 클릭해서 봇체크 우회
        if not 'x' in img:
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

        if img == img_box:
            while True:
                time.sleep(0.1)
                find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))
                if find_img != None:
                    pg.click(find_img, clicks=1, duration=0.1)
                else:
                    break

        start_time = time.time()
        Flag = True
    
    return Flag


def make_switch():
    start_time = time.time()

    while True:
        if time.time() - start_time >= 5:
            break

        time.sleep(0.5)

        find_and_click(img_playstore)

        '''
        if find_and_click(img_playstore):
            time.sleep(0.5)

            while True:
                if time.time() - start_time >= 5:
                    break

                time.sleep(0.2)
                if find_and_click(img_back):
                    start_time = time.time()
                    return True
        '''


def make_screenshot():
    timestr = time.strftime("%d-%H-%M")
    path = os.getcwd()
    filename = path + '\\screenshot\\' + timestr + '.png'
    print(filename)

    try:
        if not os.path.exists(path + '\\screenshot'):
            os.makedirs(path + '\\screenshot')

        start_time = time.time()    
        while True:
            img = pg.locateOnScreen(img_gold_box_open, confidence=0.9, region=(left_g, top_g, width_g, height_g))            
            if img:                
                ret = pg.screenshot(filename, region=(left_g, top_g, width_g-90, height_g-110))            
                break

            if time.time() - start_time >= 5:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)


toggle_check_thread = threading.Thread(target=checker)
#toggle_check_thread.start()

if __name__ =='__main__':
    try:
        switch_flag = False

        while True:
            find_and_click(img_box, 5)
            find_and_click(img_more_box)
            find_and_click(img_more_box2)
            find_and_click(img_more_box_g)            
            b_ret = find_and_click(img_gold_box, 5)
            if b_ret:
                time.sleep(0.2)
                make_screenshot()      
            find_and_click(img_more)
            find_and_click(img_more2)
            find_and_click(img_close)
            find_and_click(img_close2)
            find_and_click(img_close3, 8)
            find_and_click(img_ok)
            find_and_click(img_ok2)

            # 뒤로가야 하는것들
            if find_img(img_appstore, 10) or find_img(img_web, 10) or find_img(img_appstore2, 10) or find_img(img_appstore3, 10):
                time.sleep(0.1)
                find_and_click(img_back)
                
            # x는 동적으로 추가되더라도 잘 실행 되기 위해
            for i in img_x_list:
                find_and_click(img_path_x_list + '\\' + i, 10)

            if switch_flag and time.time() - start_time >= 30:
                make_switch()
            
            print_num = round(time.time() - start_time)
            print('%.2f' % (print_num))
            print(str(print_num) + '\r'.format(i), end='')
            #sys.stdout.flush()
            
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass
