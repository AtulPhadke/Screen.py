import pygame
import time
import datetime
import requests
from pprint import pprint


pygame.init()
screen = pygame.display.set_mode((1024, 600))
rectBlack = pygame.Rect(0, 0, 1024, 600)
clock = pygame.time.Clock()
def ResetButton():
    x, y = pygame.mouse.get_pos()
    if x >= 750 and x <= 1025 and y <= 700 and y >= 500:
        button = pygame.image.load("HoverRoundedRectangle.png")
        button = pygame.transform.scale(button, (275, 200))
        screen.blit(button, (750, 500))
        if event.type == pygame.KEYDOWN:
            print("Hg")
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("HI")
    else:
        button = pygame.image.load("Rounded Rectangle.png")
        button = pygame.transform.scale(button, (275, 200))
        screen.blit(button, (750, 500))

def Megamanand10800A():
    megaman = "Megman/sprite_09.png"
    loadingicons = pygame.image.load(megaman)
    loadingicons = pygame.transform.scale(loadingicons, (200, 200))
    screen.blit(loadingicons, (780, 180))
    Team = pygame.font.Font('BebasNeueBold.ttf', 90)
    Teams = Team.render("10800A", 40, (255, 255, 255))
    screen.blit(Teams, (770, 380))
def MaximumH20(maximum):
    H20 = 500
    if H20 <= (maximum/30):
        image = "Brokenup/frame_00_delay-0.33s.png"
        
    elif (maximum/30)*2 <= H20 <= (maximum/30)*3:
        image = "Brokenup/frame_01_delay-0.33s.png"

    elif (maximum/30)*3 <= H20 <= (maximum/30)*4:
        image = "Brokenup/frame_02_delay-0.33s.png"
  
    elif (maximum/30)*4 <= H20 <= (maximum/30)*5:
        image = "Brokenup/frame_03_delay-0.33s.png"
      
    elif (maximum/30)*5 <= H20 <= (maximum/30)*6:
        image = "Brokenup/frame_04_delay-0.33s.png"
        
    elif (maximum/30)*6 <= H20 <= (maximum/30)*7:
        image = "Brokenup/frame_05_delay-0.33s.png"
        
    elif (maximum/30)*7 <= H20 <= (maximum/30)*8:
        image = "Brokenup/frame_06_delay-0.33s.png"
       
    elif (maximum/30)*8 <= H20 <= (maximum/30)*9:
        image = "Brokenup/frame_07_delay-0.33s.png"

    elif (maximum/30)*9 <= H20 <= (maximum/30)*10:
        image = "Brokenup/frame_08_delay-0.33s.png"
  
    elif (maximum/30)*10 <= H20 <= (maximum/30)*11:
        image = "Brokenup/frame_09_delay-0.33s.png"
        
    elif (maximum/30)*11 <= H20 <= (maximum/30)*12:
        image = "Brokenup/frame_10_delay-0.33s.png"
        
    elif (maximum/30)*12 <= H20 <= (maximum/30)*13:
        image = "Brokenup/frame_11_delay-0.33s.png"
        
    elif (maximum/30)*13 <= H20 <= (maximum/30)*14:
        image = "Brokenup/frame_12_delay-0.33s.png"
        
    elif (maximum/30)*14 <= H20 <= (maximum/30)*15:
        image = "Brokenup/frame_13_delay-0.33s.png"
        
    elif (maximum/30)*15 <= H20 <= (maximum/30)*16:
        image = "Brokenup/frame_14_delay-0.33s.png"
        
    elif (maximum/30)*16 <= H20 <= (maximum/30)*17:
        image = "Brokenup/frame_15_delay-0.33s.png"
        
    elif (maximum/30)*17 <= H20 <= (maximum/30)*18:
        image = "Brokenup/frame_16_delay-0.33s.png"
        
    elif (maximum/30)*18 <= H20 <= (maximum/30)*19:
        image = "Brokenup/frame_17_delay-0.33s.png"
        
    elif (maximum/30)*19 <= H20 <= (maximum/30)*20:
        image = "Brokenup/frame_18_delay-0.33s.png"
        
    elif (maximum/30)*20 <= H20 <= (maximum/30)*21:
        image = "Brokenup/frame_19_delay-0.33s.png"
        
    elif (maximum/30)*21 <= H20 <= (maximum/30)*22:
        image = "Brokenup/frame_20_delay-0.33s.png"
        
    elif (maximum/30)*22 <= H20 <= (maximum/30)*23:
        image = "Brokenup/frame_21_delay-0.33s.png"
        
    elif (maximum/30)*23 <= H20 <= (maximum/30)*24:
        image = "Brokenup/frame_22_delay-0.33s.png"
        
    elif (maximum/30)*24 <= H20 <= (maximum/30)*25:
        image = "Brokenup/frame_23_delay-0.33s.png"
        
    elif (maximum/30)*25 <= H20 <= (maximum/30)*26:
        image = "Brokenup/frame_24_delay-0.33s.png"
        
    elif (maximum/30)*26 <= H20 <= (maximum/30)*27:
        image = "Brokenup/frame_25_delay-0.33s.png"
        
    elif (maximum/30)*27 <= H20 <= (maximum/30)*28:
        image = "Brokenup/frame_26_delay-0.33s.png"
        
    elif (maximum/30)*28 <= H20 <= (maximum/30)*29:
        image = "Brokenup/frame_27_delay-0.33s.png"
        
    elif (maximum/30)*29 <= H20 >= maximum:
        image = "Brokenup/frame_28_delay-0.33s.png"
        
    elif H20 >= maximum:
        image = "Brokenup/frame_29_delay-0.33s.png"

    loadingicon = pygame.image.load(image)
    loadingicon = pygame.transform.scale(loadingicon, (200, 200))
    screen.blit(loadingicon, (20, 450))
        
def GetTempData():
    x = datetime.datetime.now()
    url = 'http://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'.format("Nashua")
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    templow = data['main']['temp_min']
    templow = templow*(9/5) + 32
    temphigh = data['main']['temp_max']
    temphigh = temphigh*(9/5) + 32
    weathers = data['weather'][0]['main']
    temp = temp*(9/5) + 32
    return temp, templow, temphigh, weathers
        
def GetWeatherTempData(temp, templow, temphigh, weathers):
        x = datetime.datetime.now()
        if temp <= 40:
            status = 'Cold'
            Status = pygame.font.Font('Users/atulphadke/Downloads/NanumGothic-Regular.ttf', 30)
            ColdHotMild = Status.render(status, 10, (255, 255, 255))
            #screen.blit(s, (20, 100))
        elif temp >= 80:
            status = 'Hot'
            Status = pygame.font.Font('Users/atulphadke/Downloads/NanumGothic-Regular.ttf', 30)
            ColdHotMild = Status.render(status, 10, (255, 255, 255))
            #screen.blit(s, (20, 100))
        else:
            status = 'Mild'
            Status = pygame.font.Font('Users/atulphadke/Downloads/NanumGothic-Regular.ttf', 30)
            ColdHotMild = Status.render(status, 10, (255, 255, 255))
            #screen.blit(s, (20, 100))
        if weathers == 'Rain':
            weathericon = pygame.image.load("rain.png")
            Wweathericon = pygame.transform.scale(weathericon, (100, 100))
            #screen.blit(weathericon, (220, 10))
            if 6 <= int(x.strftime("%H")) <= 16:
                weathericon = pygame.image.load("Sunny.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
            elif int(x.strftime("%H")) >= 17 or int(x.strftime("%H")) <= 5:
                weathericon = pygame.image.load("Moon1.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
        elif weathers == 'Clouds':
            weathericon = pygame.image.load("clouds.png")
            Wweathericon = pygame.transform.scale(weathericon, (100, 100))
            #screen.blit(weathericon, (220, 10))
            if 6 <= int(x.strftime("%H")) <= 16:
                weathericon = pygame.image.load("Sunny.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
            elif int(x.strftime("%H")) >= 17 or int(x.strftime("%H")) <= 5:
                weathericon = pygame.image.load("Moon1.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
        elif weathers == 'Snow':
            weathericon = pygame.image.load("snow.png")
            Wweathericon = pygame.transform.scale(weathericon, (100, 100))
            #screen.blit(weathericon, (220, 10))
            if 6 <= int(x.strftime("%H")) <= 16:
                weathericon = pygame.image.load("Sunny.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
            elif int(x.strftime("%H")) >= 17 or int(x.strftime("%H")) <= 5:
                weathericon = pygame.image.load("Moon1.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
        elif weathers == 'Clear':
            weathericon = pygame.image.load("Clear.png")
            Wweathericon = pygame.transform.scale(weathericon, (100, 100))
            #screen.blit(weathericon, (220, 10))
            if 6 <= int(x.strftime("%H")) <= 16:
                weathericon = pygame.image.load("Sunny.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
            elif int(x.strftime("%H")) >= 17 or int(x.strftime("%H")) <= 5:
                weathericon = pygame.image.load("Moon1.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
        return DNweathericon, Wweathericon, ColdHotMild
def displayWeatherData():
        temperature = pygame.font.Font('Users/atulphadke/Downloads/NanumGothic-Regular.ttf', 75)
        Temps = temperature.render(str(int(temp)) + " °F", 50, (255, 255, 255))
        temperaturelow = pygame.font.Font('Users/atulphadke/Downloads/NanumGothic-Regular.ttf', 20)
        low = temperaturelow.render(str(int(templow))+ " °F", 25, (255, 255, 255))
        temperaturehigh = pygame.font.Font('Users/atulphadke/Downloads/NanumGothic-Regular.ttf', 20)
        high = temperaturehigh.render(str(int(temphigh))+ " °F", 25, (255, 255, 255))
        screen.blit(Temps, (20, 20))
        screen.blit(low, (330, 120))
        screen.blit(high, (400, 120))
        screen.blit(DNweathericon, (340, 10))
        screen.blit(Wweathericon, (220, 10))
        screen.blit(ColdHotMild, (20, 100))
def Title():
    Title = pygame.font.Font('Users/atulphadke/Downloads/NanumGothic-Regular.ttf', 25)
    title = Title.render("Water Dispensed", 50, (255, 255, 255))
    screen.blit(title, (20, 450))
def Time():
    z = datetime.datetime.now()
    screen.fill((0,0,0))
    Time = pygame.font.Font('Users/atulphadke/Downloads/NanumGothic-Regular.ttf', 50)
    Time1 = pygame.font.Font('Users/atulphadke/Downloads/NanumGothic-Regular.ttf', 25)
    Time2 = pygame.font.Font('Users/atulphadke/Downloads/NanumGothic-Regular.ttf', 25)
    y = Time.render(z.strftime("%H:%M:%S"), 50, (255, 255, 255))
    q = Time1.render(z.strftime("%b %d %Y"), 50, (255, 255, 255))
    screen.blit(y, (780, 20))
    screen.blit(q, (790, 80))
    if 6 <= int(z.strftime("%H")) <= 13:
            d = Time2.render("Good Morning", 50, (255, 255, 255))
            screen.blit(d, (790, 110))
    if 14 <= int(z.strftime("%H")) <= 16:
            d = Time.render("Good Afternoon", 50, (255, 255, 255))
            screen.blit(d, (790, 110))
    if int(z.strftime("%H")) >= 17 or int(z.strftime("%H")) <= 5:
            d = Time2.render("Good Evening", 50, (255, 255, 255))
            screen.blit(d, (790, 110))

finished = False

url = 'http://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'.format("Nashua")

i = 0
previous_temp = 0.0
previous_weathers = "now"
previous_time = 0
previous_temp = 0.0
previous_tempLow = 0.0
previous_tempHigh = 0.0

while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    finished = True
        if i == 0:
            temp, templow, temphigh, weathers = GetTempData()
            DNweathericon, Wweathericon, ColdHotMild = GetWeatherTempData(temp, templow, temphigh, weathers)
        Time()
        Title()
        new_time = int(time.time())
        
        if new_time - previous_time > 60:
            #print("timer exceeded")
            #print(new_time)
            temp, templow, temphigh, weathers = GetTempData()
            if temp != previous_temp \
               or templow != previous_tempLow \
               or temphigh != previous_tempHigh \
               or weathers != previous_weathers:
                #print("temp info is different")
                DNweathericon, Wweathericon, ColdHotMild = GetWeatherTempData(temp, templow, temphigh, weathers)
                previous_temp = temp
                previous_tempLow = templow
                previous_tempHigh = temphigh
                previous_weathers = weathers
            previous_time = new_time
        displayWeatherData()
        MaximumH20(1000)
        Megamanand10800A()
        ResetButton()
        i = i + 1
        pygame.display.update()
        clock.tick(60)
        
