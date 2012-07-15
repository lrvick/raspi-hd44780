from hd44780 import HD44780
from datetime import datetime
from time import sleep

lcd = HD44780()

while True:
    sleep(1)
    lcd.clear()
    lcd.message(datetime.now().strftime('  %I : %M : %S \n%a %b %d %Y'))
