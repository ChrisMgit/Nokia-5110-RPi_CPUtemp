import time
import Adafruit_Nokia_LCD as lcd
import Adafruit_GPIO.SPI as SPI
from PIL import Image, ImageDraw, ImageFont

DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0
disp = lcd.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
disp.begin(contrast=45)
disp.clear()
disp.display()

image = Image.new('1', (lcd.LCDWIDTH, lcd.LCDHEIGHT))
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()
while True:    
    with open('/sys/class/thermal/thermal_zone0/temp') as temp:
        tempC = float(temp.read())/1000
                CPU_Temp = ("%.2f" % tempC) 
        draw.rectangle((0,0,lcd.LCDWIDTH, lcd.LCDHEIGHT), outline=255, fill=255)
        draw.text((10,20), "CPU: "+CPU_Temp,  font=font)
        disp.image(image)
        disp.display()
        time.sleep(3)
