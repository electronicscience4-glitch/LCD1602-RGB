#include <Wire.h>
#include "Waveshare_LCD1602_RGB.h"
Waveshare_LCD1602_RGB lcd(16,2); // دیاریکردنى ناوى lcd بۆ شاشەکە 
int r,g,b,t=0;
void setup() {
    lcd.init();                  // ڕێکخستنى شاشە 
    lcd.setCursor(0,0);          // دیاریکردنى شوێنى نوسین لاینى یەکەم 
    lcd.send_string("Raspberry PI");// نوسین لە لاینى یەکەم 
    lcd.setCursor(0,1);           // دیاریکردنى شوێنى نوسین لاینى دووەم 
    lcd.send_string("Sangar Mawaty");// نوسین لە لاینى دووەم  
}
void loop() {
// گۆرانکارى لە نرخى ڕەنگەکان لە نیوان 0 بۆ 255 بۆ ئەوەى هەموو ڕەنگەکان دروست بکات 
    r = (abs(sin(3.14*t/180)))*255;
    g = (abs(sin(3.14*(t + 60)/180)))*255;
    b = (abs(sin(3.14*(t + 120)/180)))*255;
    t = t + 3;
// فەرمانى نمایشکردنى ڕەنگى پشتى شاشە 
    lcd.setRGB(r,g,b);
    delay(150); // دیاریکردنى کاتى گۆڕینى ڕەنگەکان 
}
