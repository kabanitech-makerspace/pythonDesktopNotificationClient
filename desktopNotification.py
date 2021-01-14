# author  : kabanitech
# website : www.kabanitech.com
#---------------------------------
import ast
import time
import requests
from datetime import datetime
from plyer import notification
from pyfiglet import Figlet
from termcolor import colored, cprint  

previusTimeStamp = 0;
notificationInterval = 300;  #  5 sec
warningLevel = 50;
firstNotification = True;
url = 'https://kabanitechfloodsensor.herokuapp.com/python';

def titleArt(title):
    asc_title = "        " + title
    f = Figlet(font='standard')
    for i in range (35):
        cprint("-",'white', end="", flush=True)
        cprint("-",'cyan', end="", flush=True)
    print("")
    cprint (f.renderText(asc_title),'cyan')
    for i in range (35):
        cprint("-",'white', end="", flush=True)
        cprint("-",'cyan', end="", flush=True)
        time.sleep(.005)
    print("")
    cprint(":: www.kabanitech.com ::",'red',end="", flush=True)
    cprint("                          Author : kabanitech",'blue')
    cprint("                                                        Version : 1.0",'blue')
    for i in range (35):
        cprint("-",'white', end="", flush=True)
        cprint("-",'cyan', end="", flush=True)
        time.sleep(.005)
    print("")
    
titleArt("Kabani Tech")
 
def pushNotification():
    global previusTimeStamp
    previusTimeStamp = time.time()
    notification.notify(
    title = "WARNING",
    message = "water level is too high",
    app_name = "KabaniTech",
    app_icon = "/kabani_icon.ico",
    timeout = 10
    )
    
def getWaterLevel():
    x = requests.get(url)
    #x = requests.get('http://localhost:3000/python')
    res = ast.literal_eval(x.content.decode("utf-8"))
    return int(res["WaterLevel"])

while True:
    currentWaterLevel = getWaterLevel()
    print(currentWaterLevel)
    if currentWaterLevel > warningLevel :
        print("water level is too high")
        interval = time.time() - previusTimeStamp;
        if firstNotification :
             pushNotification()
             firstNotification = False;
        elif interval > notificationInterval :
            pushNotification()
    time.sleep(5)