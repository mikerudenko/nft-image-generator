import pyautogui
from time import sleep
from settings import *
import random
import json


class AI:
    @staticmethod
    def open_program_search():
        pyautogui.click(program_search)
        sleep(0.1)

    def open_browser(self):
        self.open_program_search()
        pyautogui.typewrite(browser_name, interval=random.uniform(0, 0.2))
        sleep(0.1)
        pyautogui.press('enter')
        sleep(0.3)


ai = AI()
ai.open_browser()
i = 5053
while i < 5290:
    pyautogui.click(search_field)
    pyautogui.typewrite(create_item_url, interval=random.uniform(0, 0.01))
    pyautogui.press('enter')
    sleep(5)
    pyautogui.click(d_n_d)
    sleep(1)
    pyautogui.typewrite(str(i) + ".png", interval=random.uniform(0,ќ 0.01))
    sleep(0.3)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite("Style Cat # " + str(i),
                        interval=random.uniform(0, 0.01))
    for _ in range(8):
        pyautogui.press('tab')
    pyautogui.press('enter')
    f = open('./metadata/' + str(i))
    meta_file = json.load(f)
    for attr in meta_file['attributes']:
        pyautogui.typewrite(attr['trait_type'])
        pyautogui.press('tab')
        pyautogui.typewrite(attr['value'])
        if attr['trait_type'] != 'Mustache':
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('shift')
            pyautogui.press('tab')
            pyautogui.keyDown('shift')
            pyautogui.press('tab')

    pyautogui.press('tab')
    sleep(1)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(-100)
    pyautogui.click(create)
    sleep(3)
    pyautogui.click(close)
    sleep(4)
    pyautogui.click(sell)
    sleep(3)
    pyautogui.click(amount)
    sleep(1.4)
    pyautogui.typewrite(item_price, interval=random.uniform(0, 0.01))
    sleep(1.4)
    # pyautogui.press('tab')
    # pyautogui.press('tab')
    # pyautogui.press('enter')
    # pyautogui.click(select_date)
    # pyautogui.click(custom_date_option)
    # pyautogui.press('tab')
    # pyautogui.typewrite(custom_date, interval=random.uniform(0, 0.01))
    pyautogui.click(post)
    sleep(7)
    pyautogui.click(sign_start_button)
    sleep(5)
    i += 1
