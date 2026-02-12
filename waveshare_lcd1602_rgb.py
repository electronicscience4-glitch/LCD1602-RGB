import time
from machine import I2C

class Waveshare_LCD1602_RGB:
    def __init__(self, i2c, cols, rows):
        self.i2c = i2c
        self.cols = cols
        self.rows = rows
        self.LCD_ADDR = 0x3E
        self.RGB_ADDR = 0x60
        
    def init(self):
        # سەرەتاییکردنی شاشە
        self.write_cmd(0x38)  # 8-bit, 2 lines
        self.write_cmd(0x39)  # 8-bit, 2 lines, IS=1
        self.write_cmd(0x14)  # Internal OSC frequency
        self.write_cmd(0x70)  # Contrast set
        self.write_cmd(0x56)  # Power/ICON/Contrast control
        self.write_cmd(0x6C)  # Follower control
        time.sleep(0.2)
        self.write_cmd(0x38)  # 8-bit, 2 lines, IS=0
        self.write_cmd(0x0C)  # Display ON
        self.write_cmd(0x01)  # Clear display
        time.sleep(0.002)
        
    def write_cmd(self, cmd):
        self.i2c.writeto(self.LCD_ADDR, bytes([0x00, cmd]))
        
    def write_data(self, data):
        self.i2c.writeto(self.LCD_ADDR, bytes([0x40, data]))
        
    def setCursor(self, col, row):
        addr = 0x80 + (0x40 * row) + col
        self.write_cmd(addr)
        
    def print(self, text):
        for char in text:
            self.write_data(ord(char))
            
    def send_string(self, text):
        self.print(text)
            
    def setRGB(self, r, g, b):
        self.i2c.writeto(self.RGB_ADDR, bytes([0x00, 0x00]))
        self.i2c.writeto(self.RGB_ADDR, bytes([0x01, 0x00]))
        self.i2c.writeto(self.RGB_ADDR, bytes([0x08, 0xAA]))
        
        self.i2c.writeto(self.RGB_ADDR, bytes([0x04, r]))
        self.i2c.writeto(self.RGB_ADDR, bytes([0x03, g]))
        self.i2c.writeto(self.RGB_ADDR, bytes([0x02, b]))