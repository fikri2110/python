import streamlit as st
import easymodbus.modbusClient
import time

x = 0

#----------------------------mulai fungsi ---------------------------------
#fungsi tulis plc
def tulisplcon():
    modbusclient = easymodbus.modbusClient.ModbusClient('192.168.4.165', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(3,True)
    modbusclient.close()
def tulisplcoff():
    modbusclient = easymodbus.modbusClient.ModbusClient('192.168.4.165', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(3,False)
    modbusclient.close()

def tulisplconQ02():
    modbusclient = easymodbus.modbusClient.ModbusClient('192.168.4.165', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(2,True)
    modbusclient.close()
def tulisplcoffQ02():
    modbusclient = easymodbus.modbusClient.ModbusClient('192.168.4.165', 502)
    modbusclient.connect()
    QW128 = modbusclient.write_single_coil(2,False)
    modbusclient.close()    
    
#----------------------------akhir fungsi ---------------------------------

st.write("""# Belajar Web dengan Python
         Ini adalah aplikasi web Python koneksi ke SpeedPLC/ModbusTCPip
          """)
#adding a button
    
if st.button('Q0.3 ON'):
    st.write(tulisplcon()) #
else:
    None

if st.button('Q0.3 OFF'):
    st.write(tulisplcoff()) #
else:
    None
    

p = st.empty()
ps = st.empty()

while x < 10:
    modbusclient = easymodbus.modbusClient.ModbusClient('192.168.4.165', 502)
    modbusclient.connect()
    QW128 = modbusclient.read_holdingregisters(64,1) #QW128 --> 40064
    modbusclient.close()
    QW128x = str(QW128)
    QW128x = QW128x.replace("[","")
    QW128x = QW128x.replace("]","")
    QW128s = "Q0.3 sudah di ON kan sebanyak : " + QW128x
    p.write(QW128s)
    
    modbusclient = easymodbus.modbusClient.ModbusClient('192.168.4.35', 502)
    modbusclient.connect()
    QW128su = modbusclient.read_inputregisters(0,1) #
    modbusclient.close()
    QW128xs = str(QW128su)
    QW128xs = QW128xs.replace("[","")
    QW128xs = QW128xs.replace("]","")
    QW128F = float(QW128xs)/10
    QW128ss = "Suhu Udara : " + str(QW128F) + "°C"
    ps.write(QW128ss)
    
    time.sleep(3)

