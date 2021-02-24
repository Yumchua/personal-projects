import pyautogui as pg
import time
import win32api
import win32con
from PIL import Image
import pytesseract as pt
import pandas as pd

save_string_q = r"C:\Users\bchua1\Downloads\question.png"
save_string_a = r"C:\Users\bchua1\Downloads\answer.png"

q_lim = 42
a_lim_special = 4
a_lim = 5
a_lim_threshold = 8
click_delay = 0.01
found_q = False
size_scale = 4
size_scale_a = 1

# gbr_data = pd.read_excel('gbr answer key.xlsx', engine='openpyxl', header=None)
# gbr_data = gbr_data.iloc[::5, :]
# gbr_data = gbr_data.iloc[:, [1, 2]]
#
# gbr_data.to_csv(r"C:\Users\Brian\Desktop\manta folder\gbr_complete.csv", index=False)
gbr_data = pd.read_csv('gbr_complete.csv')

q_list = []
for i in range(0, len(gbr_data)):
    q_list.append(gbr_data.iloc[i, 0])
a_list = []
for i in range(0, len(gbr_data)):
    a_list.append(gbr_data.iloc[i, 1])

answer_position_1 = (750, 620)
answer_position_2 = (1160, 620)
answer_position_3 = (750, 725)
answer_position_4 = (1160, 725)

wrong_position_1 = (955, 595)
wrong_position_2 = (955, 570)

# one line, region 1 (590, 565, 330, 60)
# one line, region 2 (990, 565, 330, 60)
# one line, region 3 (590, 670, 330, 60)
# one line, region 4 (990, 670, 330, 60)

# while True:
#     print(pg.position())
#     time.sleep(1)

pt.pytesseract.tesseract_cmd = r"C:\Users\bchua1\Downloads\Tesseract-OCR\tesseract.exe"

print("timer starts now")
time.sleep(7)
while True:
    question_count = 0
    while question_count != 10:
        time.sleep(0.2)
        q_img = pg.screenshot(region=(550, 430, 820, 110))
        q_img.save(save_string_q)
        im_q = Image.open(save_string_q)
        new_size = tuple(size_scale*x for x in im_q.size)
        im_q = im_q.resize(new_size, Image.ANTIALIAS)
        output_q_full = pt.image_to_string(im_q)
        output_q = output_q_full[0:q_lim]
        print(output_q)
        for i in range(0, len(q_list)):
            if output_q in q_list[i] and len(output_q_full) <= 66:
                found_q = True
                print(f"This is question index {i}.")
                print(f"The answer is {a_list[i]}.")
                a_img = pg.screenshot(region=(590, 565, 330, 60))
                a_img.save(save_string_a)
                im_a = Image.open(save_string_a)
                new_size = tuple(size_scale_a*x for x in im_a.size)
                im_a = im_a.resize(new_size, Image.ANTIALIAS)
                output_a_full = pt.image_to_string(im_a)
                if len(output_a_full) <= a_lim_threshold:
                    output_a = output_a_full[0:a_lim_special]
                else:
                    output_a = output_a_full[0:a_lim]
                print(output_a)
                if str(output_a.lower()) in str(a_list[i].lower()):
                    win32api.SetCursorPos(answer_position_1)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                    time.sleep(click_delay)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                else:
                    a_img = pg.screenshot(region=(990, 565, 330, 60))
                    a_img.save(save_string_a)
                    im_a = Image.open(save_string_a)
                    new_size = tuple(size_scale_a*x for x in im_a.size)
                    im_a = im_a.resize(new_size, Image.ANTIALIAS)
                    output_a_full = pt.image_to_string(im_a)
                    if len(output_a_full) <= a_lim_threshold:
                        output_a = output_a_full[0:a_lim_special]
                    else:
                        output_a = output_a_full[0:a_lim]
                    print(output_a)
                    if str(output_a.lower()) in str(a_list[i].lower()):
                        win32api.SetCursorPos(answer_position_2)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                        time.sleep(click_delay)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                    else:
                        a_img = pg.screenshot(region=(590, 670, 330, 60))
                        a_img.save(save_string_a)
                        im_a = Image.open(save_string_a)
                        new_size = tuple(size_scale_a*x for x in im_a.size)
                        im_a = im_a.resize(new_size, Image.ANTIALIAS)
                        output_a_full = pt.image_to_string(im_a)
                        if len(output_a_full) <= a_lim_threshold:
                            output_a = output_a_full[0:a_lim_special]
                        else:
                            output_a = output_a_full[0:a_lim]
                        print(output_a)
                        if str(output_a.lower()) in str(a_list[i].lower()):
                            win32api.SetCursorPos(answer_position_3)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                            time.sleep(click_delay)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                        else:
                            a_img = pg.screenshot(region=(990, 670, 330, 60))
                            a_img.save(save_string_a)
                            im_a = Image.open(save_string_a)
                            new_size = tuple(size_scale_a*x for x in im_a.size)
                            im_a = im_a.resize(new_size, Image.ANTIALIAS)
                            output_a_full = pt.image_to_string(im_a)
                            if len(output_a_full) <= a_lim_threshold:
                                output_a = output_a_full[0:a_lim_special]
                            else:
                                output_a = output_a_full[0:a_lim]
                            print(output_a)
                            if str(output_a.lower()) in str(a_list[i].lower()):
                                win32api.SetCursorPos(answer_position_4)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                                time.sleep(click_delay)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                            else:
                                win32api.SetCursorPos(answer_position_1)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                                time.sleep(click_delay)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            elif output_q in q_list[i] and 66 < len(output_q_full) <= 146:
                found_q = True
                print(f"This is question index {i}.")
                print(f"The answer is {a_list[i]}.")
                a_img = pg.screenshot(region=(590, 592, 330, 60))
                a_img.save(save_string_a)
                im_a = Image.open(save_string_a)
                new_size = tuple(size_scale_a*x for x in im_a.size)
                im_a = im_a.resize(new_size, Image.ANTIALIAS)
                output_a_full = pt.image_to_string(im_a)
                if len(output_a_full) <= a_lim_threshold:
                    output_a = output_a_full[0:a_lim_special]
                else:
                    output_a = output_a_full[0:a_lim]
                print(output_a)
                if str(output_a.lower()) in str(a_list[i].lower()):
                    win32api.SetCursorPos(answer_position_1)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                    time.sleep(click_delay)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                else:
                    a_img = pg.screenshot(region=(990, 592, 330, 60))
                    a_img.save(save_string_a)
                    im_a = Image.open(save_string_a)
                    new_size = tuple(size_scale_a*x for x in im_a.size)
                    im_a = im_a.resize(new_size, Image.ANTIALIAS)
                    output_a_full = pt.image_to_string(im_a)
                    if len(output_a_full) <= a_lim_threshold:
                        output_a = output_a_full[0:a_lim_special]
                    else:
                        output_a = output_a_full[0:a_lim]
                    print(output_a)
                    if str(output_a.lower()) in str(a_list[i].lower()):
                        win32api.SetCursorPos(answer_position_2)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                        time.sleep(click_delay)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                    else:
                        a_img = pg.screenshot(region=(590, 697, 330, 60))
                        a_img.save(save_string_a)
                        im_a = Image.open(save_string_a)
                        new_size = tuple(size_scale_a*x for x in im_a.size)
                        im_a = im_a.resize(new_size, Image.ANTIALIAS)
                        output_a_full = pt.image_to_string(im_a)
                        if len(output_a_full) <= a_lim_threshold:
                            output_a = output_a_full[0:a_lim_special]
                        else:
                            output_a = output_a_full[0:a_lim]
                        print(output_a)
                        if str(output_a.lower()) in str(a_list[i].lower()):
                            win32api.SetCursorPos(answer_position_3)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                            time.sleep(click_delay)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                        else:
                            a_img = pg.screenshot(region=(990, 697, 330, 60))
                            a_img.save(save_string_a)
                            im_a = Image.open(save_string_a)
                            new_size = tuple(size_scale_a*x for x in im_a.size)
                            im_a = im_a.resize(new_size, Image.ANTIALIAS)
                            output_a_full = pt.image_to_string(im_a)
                            if len(output_a_full) <= a_lim_threshold:
                                output_a = output_a_full[0:a_lim_special]
                            else:
                                output_a = output_a_full[0:a_lim]
                            print(output_a)
                            if str(output_a.lower()) in str(a_list[i].lower()):
                                win32api.SetCursorPos(answer_position_4)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                                time.sleep(click_delay)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                            else:
                                win32api.SetCursorPos(answer_position_1)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                                time.sleep(click_delay)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            elif output_q in q_list[i] and len(output_q_full) > 146:
                found_q = True
                print(f"This is question index {i}.")
                print(f"The answer is {a_list[i]}.")
                a_img = pg.screenshot(region=(590, 619, 330, 60))
                a_img.save(save_string_a)
                im_a = Image.open(save_string_a)
                new_size = tuple(size_scale_a*x for x in im_a.size)
                im_a = im_a.resize(new_size, Image.ANTIALIAS)
                output_a_full = pt.image_to_string(im_a)
                if len(output_a_full) <= a_lim_threshold:
                    output_a = output_a_full[0:a_lim_special]
                else:
                    output_a = output_a_full[0:a_lim]
                print(output_a)
                if str(output_a.lower()) in str(a_list[i].lower()):
                    win32api.SetCursorPos(answer_position_1)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                    time.sleep(click_delay)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                else:
                    a_img = pg.screenshot(region=(990, 619, 330, 60))
                    a_img.save(save_string_a)
                    im_a = Image.open(save_string_a)
                    new_size = tuple(size_scale_a*x for x in im_a.size)
                    im_a = im_a.resize(new_size, Image.ANTIALIAS)
                    output_a_full = pt.image_to_string(im_a)
                    if len(output_a_full) <= a_lim_threshold:
                        output_a = output_a_full[0:a_lim_special]
                    else:
                        output_a = output_a_full[0:a_lim]
                    print(output_a)
                    if str(output_a.lower()) in str(a_list[i].lower()):
                        win32api.SetCursorPos(answer_position_2)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                        time.sleep(click_delay)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                    else:
                        a_img = pg.screenshot(region=(590, 724, 330, 60))
                        a_img.save(save_string_a)
                        im_a = Image.open(save_string_a)
                        new_size = tuple(size_scale_a*x for x in im_a.size)
                        im_a = im_a.resize(new_size, Image.ANTIALIAS)
                        output_a_full = pt.image_to_string(im_a)
                        if len(output_a_full) <= a_lim_threshold:
                            output_a = output_a_full[0:a_lim_special]
                        else:
                            output_a = output_a_full[0:a_lim]
                        print(output_a)
                        if str(output_a.lower()) in str(a_list[i].lower()):
                            win32api.SetCursorPos(answer_position_3)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                            time.sleep(click_delay)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                        else:
                            a_img = pg.screenshot(region=(990, 724, 330, 60))
                            a_img.save(save_string_a)
                            im_a = Image.open(save_string_a)
                            new_size = tuple(size_scale_a*x for x in im_a.size)
                            im_a = im_a.resize(new_size, Image.ANTIALIAS)
                            output_a_full = pt.image_to_string(im_a)
                            if len(output_a_full) <= a_lim_threshold:
                                output_a = output_a_full[0:a_lim_special]
                            else:
                                output_a = output_a_full[0:a_lim]
                            print(output_a)
                            if str(output_a) in str(a_list[i]):
                                win32api.SetCursorPos(answer_position_4)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                                time.sleep(click_delay)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                            else:
                                win32api.SetCursorPos(answer_position_1)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                                time.sleep(click_delay)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        if found_q is True:
            found_q = False
        else:
            win32api.SetCursorPos(answer_position_1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(click_delay)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        win32api.SetCursorPos((1500, 500))
        time.sleep(3.5)
        win32api.SetCursorPos(wrong_position_1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(click_delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        win32api.SetCursorPos(wrong_position_2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(click_delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        win32api.SetCursorPos((1500, 500))
        question_count += 1
        continue
    time.sleep(5)
    win32api.SetCursorPos((950, 725))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(click_delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(10)
    win32api.SetCursorPos((780, 845))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(click_delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(6)
