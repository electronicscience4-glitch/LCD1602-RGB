from machine import I2C, Pin
from waveshare_lcd1602_rgb import Waveshare_LCD1602_RGB
import math
import time

# ڕێکخستنی I2C بۆ شاشەکە
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)  # بەپێی وەصلکردنەکەت بیگۆڕە

# دروستکردنی شاشە
lcd = Waveshare_LCD1602_RGB(i2c, 16, 2)

t = 0

def setup():
    global t
    # ڕێکخستنی شاشە
    lcd.init()
    lcd.setCursor(0, 0)
    lcd.print("Raspberry PI")
    lcd.setCursor(0, 1)
    lcd.print("Sangar Mawaty")

def loop():
    global t
    # گۆڕینی ڕەنگەکان لە نیوان 0 بۆ 255
    r = int(abs(math.sin(math.radians(t))) * 255)
    g = int(abs(math.sin(math.radians(t + 60))) * 255)
    b = int(abs(math.sin(math.radians(t + 120))) * 255)
    
    t = t + 3
    if t >= 360:
        t = 0
    
    # دیاریکردنی ڕەنگی پشتی شاشە
    lcd.setRGB(r, g, b)
    time.sleep(0.15)

# بەکارهێنانی while True وەک جێگرەوەی loop لە Arduino
setup()
while True:
    loop()