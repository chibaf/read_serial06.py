import serial, sys
import re
from pylab import *

strPort = sys.argv[2]   # serial port
swrite =serial.Serial("/dev/cu.usbmodem14101", 9600)   # send to arduino
ser=serial.Serial(strPort, 115200) 
print("connected to: " + ser.portstr)

file=sys.argv[1]  # file name
regex = re.compile('\d+')  # for extracting number from strings
f=open(file,"w+")
y=[0]*100
data=[];itime=0
while True:
  try:
    itime=0
    val=0
    a = int(val).to_bytes(1, byteorder="little")
    ser.write(a)  # make SSR off
    line = ser.readline()
    try:
      match = regex.findall(str(line))   # extracting number from strings
      f1=match[4]+"."+match[5]+", "+match[6]+"."+match[7]+", "+match[8]+"."+match[9]+", "+match[10]+"."+match[11]+", "+match[12]+"."+match[13]+", "+match[14]+"."+match[15]+", "+match[16]+"."+match[17]+", "+match[18]+"."+match[19]+", "+match[20]+"."+match[21]+", "+match[22]+"."+match[23]
      sec=float(match[1])*60.0+float(match[2])+float(match[3])*0.1
      data.append(itime*0.1)    # set time and temps to data
      data.append(float(match[4]+"."+match[5]))
      data.append(float(match[6]+"."+match[7]))
      data.append(float(match[8]+"."+match[9]))
      data.append(float(match[10]+"."+match[11]))
      data.append(float(match[12]+"."+match[13]))
      data.append(float(match[14]+"."+match[15]))
      data.append(float(match[16]+"."+match[17]))
      data.append(float(match[18]+"."+match[19]))
      data.append(float(match[20]+"."+match[21]))
      data.append(float(match[22]+"."+match[23]))
    except:
      print(str(line))#;print(word)
      exit()
#        print(data)
    if(match[3]=="0"):
      print(str(sec)+":"+f1)
    f.write(str(sec)+", "+f1+"\n")
    x=range(0, 100, 1)
    y.insert(0, data[1])  # Tc No.6
    y.pop(100)
    clf()
    ylim(0, 1000)
    plot(x, y)
    pause(0.05) 
    itime=itime+1
    data=[]
    val=200  # make SSR on
    a = int(val).to_bytes(1, byteorder="little")  # make SSR on
    ser.write(a)  # make SSR on
  except KeyboardInterrupt:
    print(str(line))
    print ('exiting')
    break
ser.flush()
ser.close()
f.close()
