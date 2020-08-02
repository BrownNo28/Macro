# pixel_color

import pyautogui as pag

m_p = pag.position() # m_p = mouse position
print(m_p)

image_screenshot = pag.screenshot()
pixel_rgb = image_screenshot.getpixel(m_p) # pixel rgb
print (pixel_rgb)
