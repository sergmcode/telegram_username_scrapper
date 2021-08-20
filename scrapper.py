from platform import python_branch, win32_edition
import pyautogui, time

from pytesseract.pytesseract import TesseractError

import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab

import re

user_list = []
output_file_name = "user_list.json"

print(f'Output file name: {output_file_name}')

for i in range(1, 100):
  pyautogui.moveTo(1851, 1234)  
  
  pyautogui.click()
  time.sleep(0.2)

  try:
  #locate on screen Username
    loc = pyautogui.locateOnScreen('username.png')

    ss = pyautogui.screenshot(region=(loc[0], loc[1]-25, 200, 30))
    # ss.show()

    tesstr = pytesseract.image_to_string(ss)
    print(tesstr.strip())

    if tesstr != '' or tesstr is not None:
      tesstr = tesstr.strip()
      m = re.match('^@[^ ]+$', tesstr)
      if m is not None:
        user_list.append(tesstr)

  except Exception as ex:
    print(ex)

  time.sleep(0.2)
  pyautogui.typewrite(['esc'])

  time.sleep(1)
  #key press 8 times 3 and 1 time 2
  if i % 8 == 0:
    pyautogui.typewrite(['down', 'down'], interval=0.1)
  else:
    pyautogui.typewrite(['down', 'down', 'down'], interval=0.1)


import json
with open(output_file_name, 'w', encoding='utf8') as f:
  json.dump(user_list, f)

  