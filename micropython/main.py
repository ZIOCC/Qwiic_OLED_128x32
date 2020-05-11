import sht31
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(sda=Pin("Y8"), scl=Pin("Y6"))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

sht = sht31.SHT31(i2c_address=0x44)
rtc = pyb.RTC()


while True:

    shtdata = sht.measure()
    t=rtc.datetime()
    oled.fill(0)
    oled.text("temp:" + str(shtdata[0]), 0, 10)
    oled.text("Humi:" + str(shtdata[1]), 0, 30)
    oled.text("Time:" + str(t[4]) + ":" + str(t[5]) + ":" + str(t[6]), 0, 45)
    print(str(t[6]))
    print(shtdata[0])
    print(shtdata[1])
    oled.show()
    pyb.delay(300)
