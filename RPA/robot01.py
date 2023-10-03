import webbrowser as wb
import mouse as m
import pyautogui as pg
import pyperclip as p
from time import sleep
from datetime import datetime

nomdoc="document.pdf"
user="robot01"
password="ROBOT"
n="13424"
num_fc="3543654"
num="76172861872"
Date=str(datetime.now())
# for i in range(4):
#     sleep(3)
#     print(m.get_position())
m.move(1467, 234,True,1)
m.click()
sleep(1)
m.click()
pg.write(user)
sleep(3)
m.move(1466, 353,True,1)
m.click()
pg.write(password)
sleep(2)
m.move(1429, 442,True,1)
m.click()
sleep(2)
m.move(1512,508,True,1)
m.click()
m.move(1471, 199,True,1)
m.click()
pg.write(num)
sleep(2)
m.move(1515, 317,True,1)
m.click()
pg.write(Date)
sleep(2)
m.move(1507, 422,True,1)
m.click()
pg.write(n)
sleep(2)
m.move(1511, 559,True,1)
m.click()
pg.write(user)
sleep(2)
m.move(1503, 676,True,1)
m.click()
pg.write(num_fc)
sleep(2)
m.wheel(-20)
sleep(2)
m.move(1435, 599,True,1)
m.click()
sleep(2)
m.move(1348, 472,True,1)
m.click()
pg.write(nomdoc)
sleep(2)
m.move(1689, 500,True,1)
m.click()
sleep(2)
m.move(1547, 721,True,1)
m.click()
sleep(2)
m.wheel(-10)