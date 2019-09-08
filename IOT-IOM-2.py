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
    wks = gc.open('機聯網').get_worksheet(0)
    for i in range(len(machine_List)-3):                        #檢查3D印表機的狀態
        machine_List[i].status =wks.cell(5+i,1).value
    universal.status = wks.cell(2,1).value           #檢查universal的狀態
    
    blake.status = wks.cell(3,1).value                 #檢查beambox的狀態
    odin.status = wks.cell(4,1).value

    upload()


def upload():
    if(universal.status =="off"):
        ser.write('a'.encode('utf-8'))
    elif(universal.status =="on"):
        ser.write('A'.encode('utf-8'))
        
    if(blake.status =="off"):
        ser.write('b'.encode('utf-8'))
    elif(blake.status =="on"):
        ser.write('B'.encode('utf-8'))
        
    if(odin.status =="off"):
        ser.write('c'.encode('utf-8'))
    elif(odin.status =="on"):
        ser.write('C'.encode('utf-8'))
        
    if(com3.status =="off"):
        ser.write('g'.encode('utf-8'))
    elif(com3.status =="on"):
        ser.write('G'.encode('utf-8'))
        
    if(com4.status =="off"):
        ser.write('h'.encode('utf-8'))
    elif(com4.status =="on"):
        ser.write('H'.encode('utf-8'))
        
    if(com5.status =="off"):
        ser.write('i'.encode('utf-8'))
    elif(com5.status =="on"):
        ser.write('I'.encode('utf-8'))
        
    if(com6.status =="off"):
        ser.write('j'.encode('utf-8'))
    elif(com6.status =="on"):
        ser.write('J'.encode('utf-8'))
        
    if(com7.status =="off"):
        ser.write('k'.encode('utf-8'))
    elif(com7.status =="on"):
        ser.write('K'.encode('utf-8'))
        
    if(com8.status =="off"):
        ser.write('l'.encode('utf-8'))
    elif(com8.status =="on"):
        ser.write('L'.encode('utf-8'))


ser =serial.Serial("COM3",9600,timeout=2) #arduino連線

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = SAC.from_json_keyfile_name('gSpread1-6ab7029a757a.json', scope) #認證
url2 = 'https://script.google.com/macros/s/AKfycbwPTqTSLMHR-qn0s09OF4EP__Nv_WwokFR66kyKeTMnxbfM750/exec'

gc=gspread.authorize(credentials) #連線google sheet

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
ct =0
ser.write('DEFMNO'.encode('utf-8'))
while True:
    refreshDATA()
    upload()
    while ser.in_waiting:
        mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
        print('控制板回應：', mcu_feedback)
    print("ct:",ct)
    sleep(10)
    ct+=1

