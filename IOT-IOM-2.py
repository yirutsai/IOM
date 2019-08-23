import sys
from time import sleep
import serial
from msvcrt import getch
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
clock = pygame.time.Clock()
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

while True:
    refreshDATA()
    upload()
    sleep(5)

