import sys
from time import sleep
import serial
from msvcrt import getch
import pygame
import time
import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials as SAC
#######################################################################
class machine():
    def __init__(self,name):
        self.name =name
        self.status =0
        self.user =""
        self.funtioning=0

    def __str__(self):
        return(self.name)
    def showStatus(self):
        print(self.status)

class system1():                                        #單純設定一些參數
    def __init__(self):
        self.inputMode = False
        self.num=0
        self.actNB =""
        self.Mach=""
        self.user =""
        self.admin=""
        self.authorize=""
        self.forcereturn=""
        self.changestate=""
        self.machinetype=""
    


    def keyboard_display(self,E):       
        if(E.key ==pygame.K_BACKSPACE):
            if(self.num>0):
                self.num-=1
                self.actNB = self.actNB[0:num]
                #用東西蓋住原本的字
                pygame.draw.rect(gameDisplay,(255,217,230),(352+15*self.num,550,20,25))
        elif self.num<10:
            if(48<=E.key<=122):
                message_display(chr(E.key),(360+15*self.num,560),20)
                self.actNB+=chr(E.key)
                self.num+=1
        elif self.num ==10:
            self.inputMode = False
            url2 = 'https://script.google.com/macros/s/AKfycbwPTqTSLMHR-qn0s09OF4EP__Nv_WwokFR66kyKeTMnxbfM750/exec'
            payload = {'machine':self.Mach,'cardid':self.actNB,'user':self.user,'admin':self.admin,'authorize':self.authorize,'forcereturn':self.forcereturn,'changestate':self.changestate,'machinetype':self.machinetype,}
            r=requests.get(url2, params=payload)
            pygame.draw.rect(gameDisplay,(255,217,230),(200,550,400,25))
            print(self.actNB)
            pygame.draw.rect(gameDisplay,(0,0,0),(600,500,300,200))
            messsage_display_changeColor(r.text,(600,400),30,(255,255,255),(0,0,0))
            print(r.text)
            self.actNB=""
            self.num =0

    def button(self,msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0]>x and y+h>mouse[1] >y:
            pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
            if click[0] ==1 and action!=None:
                if(action =="Universal"):
                    self.inputMode =True
                    Mach = action
                elif(action =="CNC"):
                    self.inputMode = True
                    Mach = action
                elif(action =="Beambox"):
                    self.inputMode = True
                    Mach = action
                elif(action =="Kingssel"):
                    self.inputMode = True
                    Mach = action
                elif(action =="Refresh"):
                    print("Refreshing Data. Please wait.")
                    refreshDATA()
                    print("Refresh complete.")
                elif(action =="universal"):
                    payload = {'machine':"universal",'cardid':"",'user':"",'admin':"",'authorize':"",'forcereturn':"",'changestate':"Y",'machinetype':"universal",}
                    r=requests.get(url2, params=payload)
                    pygame.draw.rect(gameDisplay,(0,0,0),(600,400,400,200))
                    messsage_display_changeColor(r.text,(600,400),30,(255,255,255),(0,0,0))
                    print(r.text)
                elif(action =="blake"):
                    payload = {'machine':"beambox",'cardid':"",'user':"",'admin':"",'authorize':"",'forcereturn':"",'changestate':"Y",'machinetype':"blake",}
                    r=requests.get(url2, params=payload)
                    pygame.draw.rect(gameDisplay,(0,0,0),(600,400,400,200))
                    messsage_display_changeColor(r.text,(600,400),30,(255,255,255),(0,0,0))
                    print(r.text)
                elif(action=="odin"):
                    payload = {'machine':"beambox",'cardid':"",'user':"",'admin':"",'authorize':"",'forcereturn':"",'changestate':"Y",'machinetype':"odin",}
                    r=requests.get(url2, params=payload)
                    pygame.draw.rect(gameDisplay,(0,0,0),(600,400,400,200))
                    messsage_display_changeColor(r.text,(600,400),30,(255,255,255),(0,0,0))
                    print(r.text)
                elif(action=="com3"):
                    payload = {'machine':"kingssel",'cardid':"",'user':"",'admin':"",'authorize':"",'forcereturn':"",'changestate':"Y",'machinetype':action,}
                    r=requests.get(url2, params=payload)
                    pygame.draw.rect(gameDisplay,(0,0,0),(600,400,400,200))
                    messsage_display_changeColor(r.text,(600,400),30,(255,255,255),(0,0,0))
                    print(r.text)
                elif(action=="com4"):
                    payload = {'machine':"kingssel",'cardid':"",'user':"",'admin':"",'authorize':"",'forcereturn':"",'changestate':"Y",'machinetype':action,}
                    r=requests.get(url2, params=payload)
                    pygame.draw.rect(gameDisplay,(0,0,0),(600,400,400,200))
                    messsage_display_changeColor(r.text,(600,400),30,(255,255,255),(0,0,0))
                    print(r.text)
                elif(action=="com5"):
                    payload = {'machine':"kingssel",'cardid':"",'user':"",'admin':"",'authorize':"",'forcereturn':"",'changestate':"Y",'machinetype':action,}
                    r=requests.get(url2, params=payload)
                    pygame.draw.rect(gameDisplay,(0,0,0),(600,400,400,200))
                    messsage_display_changeColor(r.text,(600,400),30,(255,255,255),(0,0,0))
                    print(r.text)
                elif(action=="com6"):
                    payload = {'machine':"kingssel",'cardid':"",'user':"",'admin':"",'authorize':"",'forcereturn':"",'changestate':"Y",'machinetype':action,}
                    r=requests.get(url2, params=payload)
                    pygame.draw.rect(gameDisplay,(0,0,0),(600,400,400,200))
                    messsage_display_changeColor(r.text,(600,400),30,(255,255,255),(0,0,0))
                    print(r.text)
                elif(action=="com7"):
                    payload = {'machine':"kingssel",'cardid':"",'user':"",'admin':"",'authorize':"",'forcereturn':"",'changestate':"Y",'machinetype':action,}
                    r=requests.get(url2, params=payload)
                    pygame.draw.rect(gameDisplay,(0,0,0),(600,400,400,200))
                    messsage_display_changeColor(r.text,(600,400),30,(255,255,255),(0,0,0))
                    print(r.text)
                elif(action=="com8"):
                    payload = {'machine':"kingssel",'cardid':"",'user':"",'admin':"",'authorize':"",'forcereturn':"",'changestate':"Y",'machinetype':action,}
                    r=requests.get(url2, params=payload)
                    pygame.draw.rect(gameDisplay,(0,0,0),(600,400,400,200))
                    messsage_display_changeColor(r.text,(600,400),30,(255,255,255),(0,0,0))
                    print(r.text)
                elif(action=="註冊"):
                    pass                   
                print("\n"+msg)
                
                #之後放涵式                
        else:
            pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        message_display(msg,(x+w/2,y+h/2),20)

 
    def FSM(self):
        gameDisplay.fill(white)
        message_display("NTUME",(600,480),115)
        pygame.time.delay(1000)
        gameDisplay.fill((255,217,230))
        refreshDATA()
        refresh()
        running=True
        while running:
            self.button("Universal",20,20,140,50,(220,220,220),(180,180,180),"Universal")
            self.button("universal",170,20,110,50,(180,180,180),(120,120,120),"universal")
            self.button("Beambox",20,75,140,50,(220,220,220),(180,180,180),"Beambox")
            self.button("Kingssel",20,185,140,50,(220,220,220),(180,180,180),"Kingssel")
            self.button("CNC",20,300,140,50,(220,220,220),(180,180,180),"CNC")
            self.button("Refresh",950,20,200,70,(220,220,220),(180,180,180),"Refresh")
            self.button("blake",170,80,90,40,(180,180,180),(120,120,120),"blake")
            self.button("odin",170,135,90,40,(180,180,180),(120,120,120),"odin")
            self.button("com3",170,190,90,40,(180,180,180),(120,120,120),"com3")
            self.button("com4",500,190,90,40,(180,180,180),(120,120,120),"com4")
            self.button("com5",830,190,90,40,(180,180,180),(120,120,120),"com5")
            self.button("com6",170,245,90,40,(180,180,180),(120,120,120),"com6")
            self.button("com7",500,245,90,40,(180,180,180),(120,120,120),"com7")
            self.button("com8",830,245,90,40,(180,180,180),(120,120,120),"com8")
            self.button("註冊",20,500,140,50,(220,220,220),(180,180,180),"註冊")
            refresh()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                
                elif event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_ESCAPE:
                        running =False
                    else:
                        if self.inputMode == True:
                            message_display("Student ID:",(280,560),20)
                            self.keyboard_display(event)

                #print(event)
            clock.tick(15)

            
def refresh():
    pygame.display.update()

def message_display(text,place,size):
    largeText = pygame.font.Font("msjhbd.ttc",size)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = place
    gameDisplay.blit(TextSurf, TextRect)
    refresh()

def messsage_display_changeColor(text,place,size,color = (0,0,0), bg_color=(255,217,230)):
    font = pygame.font.Font("msjhbd.ttc",size)
    TEXT = font.render(text,True,color,bg_color)
    gameDisplay.blit(TEXT, place)
    refresh()

def text_objects(text,font):
    textSurface = font.render(text, True,black)
    return textSurface, textSurface.get_rect()


def showStatus(message):
    message_display(message)



def refreshDATA():
    wks = gc.open('永齡').get_worksheet(0)  

    for i in range(len(machine_List)-3):                        #檢查3D印表機的狀態
        machine_List[i].status =wks.cell(5+i,4).value
        machine_List[i].functioning =wks.cell(5+i,3).value
    universal.status = wks.cell(2,4).value           #檢查universal的狀態
    universal.functioning = wks.cell(2,3).value
    
    blake.status = wks.cell(3,4).value                 #檢查beambox的狀態
    blake.functioning =wks.cell(3,3).value
    odin.status = wks.cell(4,4).value
    odin.functioning=wks.cell(4,3).value

    if(universal.status=="on"):
        universal.user = wks.cell(2,5).value
        messsage_display_changeColor(universal.user,(290,32),20,(0,250,0))
    elif(universal.status=="off"):
        messsage_display_changeColor("      off                        ",(290,32),20,(250,0,0))

    if(blake.status=="on"):
        blake.user = wks.cell(3,5).value
        messsage_display_changeColor(blake.user,(270,84),20,(0,250,0))
    elif(blake.status=="off"):
        messsage_display_changeColor("      off                            ",(270,84),20,(250,0,0))

    if(odin.status=="on"):
        odin.user = wks.cell(4,5).value
        messsage_display_changeColor(odin.user,(270,139),20,(0,250,0))
    elif(odin.status=="off"):
        messsage_display_changeColor("      off                             ",(270,139),20,(250,0,0))

    for i in range(len(machine_List)-6):
        if(machine_List[i].status=="on"):
            machine_List[i].user = wks.cell(5+i,5).value
            messsage_display_changeColor(machine_List[i].user,(280+330*i,194),20,(0,250,0))
        elif(machine_List[i].status=="off"):
            messsage_display_changeColor("      off                               ",(250+330*i,194),20,(250,0,0))

    for i in range(len(machine_List)-6,len(machine_List)-3,1):
        if(machine_List[i].status=="on"):
            machine_List[i].user = wks.cell(5+i,5).value
            messsage_display_changeColor(machine_List[i].user,(280+330*(i-3),250),20,(0,250,0))
        elif(machine_List[i].status=="off"):
            messsage_display_changeColor("      off                               ",(250+330*(i-3),250),20,(250,0,0))
    if(com3.functioning =="FALSE"):
        pygame.draw.rect(gameDisplay,(250,0,0),(165,185,100,50))
    elif(com3.functioning =="TRUE"):
        pygame.draw.rect(gameDisplay,(0,250,0),(165,185,100,50))
    if(com4.functioning =="FALSE"):
        pygame.draw.rect(gameDisplay,(250,0,0),(495,185,100,50))
    elif(com4.functioning =="TRUE"):
        pygame.draw.rect(gameDisplay,(0,250,0),(495,185,100,50))
    if(com5.functioning =="FALSE"):
        pygame.draw.rect(gameDisplay,(250,0,0),(825,185,100,50))
    elif(com5.functioning =="TRUE"):
        pygame.draw.rect(gameDisplay,(0,250,0),(825,185,100,50))
    if(com6.functioning =="FALSE"):
        pygame.draw.rect(gameDisplay,(250,0,0),(165,240,100,50))
    elif(com6.functioning =="TRUE"):
        pygame.draw.rect(gameDisplay,(0,250,0),(165,240,100,50))
    if(com7.functioning =="FALSE"):
        pygame.draw.rect(gameDisplay,(250,0,0),(495,240,100,50))
    elif(com7.functioning =="TRUE"):
        pygame.draw.rect(gameDisplay,(0,250,0),(495,240,100,50))
    if(com8.functioning =="FALSE"):
        pygame.draw.rect(gameDisplay,(250,0,0),(825,240,100,50))
    elif(com8.functioning =="TRUE"):
        pygame.draw.rect(gameDisplay,(0,250,0),(825,240,100,50))
    if(odin.functioning =="FALSE"):
        pygame.draw.rect(gameDisplay,(250,0,0),(165,130,100,50))
    elif(odin.functioning =="TRUE"):
        pygame.draw.rect(gameDisplay,(0,250,0),(165,130,100,50))
    if(blake.functioning =="FALSE"):
        pygame.draw.rect(gameDisplay,(250,0,0),(165,75,100,50))
    elif(blake.functioning =="TRUE"):
        pygame.draw.rect(gameDisplay,(0,250,0),(165,75,100,50))
    if(universal.functioning =="FALSE"):
        pygame.draw.rect(gameDisplay,(250,0,0),(165,15,120,60))
    elif(universal.functioning =="TRUE"):
        pygame.draw.rect(gameDisplay,(0,250,0),(165,15,120,60))

    upload()


def upload():
    if(universal.status =="off" or universal.functioning =="FALSE"):
        ser.write('a'.encode('utf-8'))
    elif(universal.status =="on" and universal.functioning =="TRUE"):
        ser.write('A'.encode('utf-8'))
        
    if(blake.status =="off" or blake.functioning =="FALSE"):
        ser.write('b'.encode('utf-8'))
    elif(blake.status =="on" and blake.functioning =="TRUE"):
        ser.write('B'.encode('utf-8'))
        
    if(odin.status =="off" or odin.functioning =="FALSE"):
        ser.write('c'.encode('utf-8'))
    elif(odin.status =="on" and odin.functioning =="TRUE"):
        ser.write('C'.encode('utf-8'))
        
    if(com3.status =="off" or com3.functioning =="FALSE"):
        ser.write('d'.encode('utf-8'))
    elif(com3.status =="on" and com3.functioning =="TRUE"):
        ser.write('D'.encode('utf-8'))
        
    if(com4.status =="off" or com4.functioning =="FALSE"):
        ser.write('e'.encode('utf-8'))
    elif(com4.status =="on" and com4.functioning =="TRUE"):
        ser.write('E'.encode('utf-8'))
        
    if(com5.status =="off" or com5.functioning =="FALSE"):
        ser.write('f'.encode('utf-8'))
    elif(com5.status =="on" and com5.functioning =="TRUE"):
        ser.write('F'.encode('utf-8'))
        
    if(com6.status =="off" or com6.functioning =="FALSE"):
        ser.write('g'.encode('utf-8'))
    elif(com6.status =="on" and com6.functioning =="TRUE"):
        ser.write('G'.encode('utf-8'))
        
    if(com7.status =="off" or com7.functioning =="FALSE"):
        ser.write('h'.encode('utf-8'))
    elif(com7.status =="on" and com7.functioning =="TRUE"):
        ser.write('H'.encode('utf-8'))
        
    if(com8.status =="off" or com8.functioning =="FALSE"):
        ser.write('i'.encode('utf-8'))
    elif(com8.status =="on" and com8.functioning =="TRUE"):
        ser.write('I'.encode('utf-8'))








ser =serial.Serial("COM4",9600,timeout=2) #arduino連線

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = SAC.from_json_keyfile_name('gSpread1-6ab7029a757a.json', scope) #認證
url2 = 'https://script.google.com/macros/s/AKfycbwPTqTSLMHR-qn0s09OF4EP__Nv_WwokFR66kyKeTMnxbfM750/exec'

gc=gspread.authorize(credentials) #連線google sheet
pygame.init()
gameDisplay = pygame.display.set_mode((1200,800))
pygame.display.set_caption('永齡機台管理')
clock = pygame.time.Clock()
white =(255,255,255)
black =(0,0,0)
car_color=(53,115,255)
center = (480,360)
on_bright_color=(0,200,0)
on_color=(0,255,0)
off_bright_color=(255,0,0)
off_color=(200,0,0)
com3 = machine("com3")
com4 = machine("com4")
com5 = machine("com5")
com6 = machine("com6")
com7 = machine("com7")
com8 = machine("com8")
universal = machine("universal")
blake = machine("blake")
odin = machine("odin")
machine_List =[com3,com4,com5,com6,com7,com8,universal,blake,odin]

Sys = system1()
Sys.FSM()
pygame.quit()
