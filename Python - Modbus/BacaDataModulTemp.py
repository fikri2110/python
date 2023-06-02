import easymodbus.modbusClient
import time
import datetime
from tkinter import *

#fungsi jam
def get_tgljam():
    now = datetime.datetime.now()
    datatgl=now.strftime("%a, %Y/%m/%d") #hari,thn bln tgl 
    datajam = time.strftime("%H:%M:%S", time.localtime())
    lbltgl.config(text=datatgl,
                    font=('arial', 20, 'bold'),
                    bg=bg,fg='blue')
    lbljam.config(text=datajam,
                    font=('arial', 18, 'bold'),
                    bg=bg,fg='blue') 
    root.after(500, get_tgljam)
    
#fungsi Data Modul DHT 11 Hummidity.
def bacaplc():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.read_holdingregisters(64,0) #30001 suhu, humidity 30002
    modbusclient.close()
    QW128 = str(QW128)
    QW128 = QW128.replace("[","")
    QW128 = QW128.replace("]","")
    QW128 = float(QW128)/10    
    QW128s = "HUMIDITY : " + str(QW128)
    lblDataQW128.config(text=QW128s,
                    font=('arial', 28, 'bold'),
                    bg=bg,fg='blue') 
    root.after(500, bacaplc)
    

"""
#fungsi tulis plc
def tulisplcon():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(3,True)
    modbusclient.close()
def tulisplcoff():
    modbusclient = easymodbus.modbusClient.ModbusClient('127.0.0.1', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(3,False)
    modbusclient.close()
"""

#gui
root = Tk()
lebar = 400
tinggi = 600
bg = 'powder blue'
fgLbl = 'black'
geo=str(lebar)+'x'+str(tinggi)
root.geometry(geo)
root.title("pt. Eldikon Engineering")
root.config(bg=bg)

#tampilan jam tgl
lbltgl=Label(root)
lbltgl.place(x=20,y=110)
lbljam=Label(root)
lbljam.place(x=20,y=140)

#tampilan data plc
lblDataQW128=Label(root)
lblDataQW128.place(x=20,y=190)

"""
#tombol tulis plc
btTulisPLCOn = Button(root,text='Turn ON Q0.3',
                        width=15,height=1,
                        font=('arial',10,'bold'),
                        bg='light blue',fg='black',bd=4,
                        command=tulisplcon)                     
btTulisPLCOn.place(x=20,y=300)
btTulisPLCOff = Button(root,text='Turn OFF Q0.3',
                        width=15,height=1,
                        font=('arial',10,'bold'),
                        bg='light blue',fg='black',bd=4,
                        command=tulisplcoff)                     
btTulisPLCOff.place(x=180,y=300)

"""


#looping
root.after(250, get_tgljam)
root.after(250, bacaplc)
root.mainloop()