import serial
import time
from pynput import keyboard
ser=serial.Serial('com20',9600,bytesize=7,parity='E',stopbits=1)
def race(number1,number2):
    D=[0x3A,0x30,0x31,0x31,0x30,0x31,0x34,0x35,0x43,0x30,0x30,0x30,0x32,0x30,0x34,0x30,0x31,0x46,0x34,0x30,0x33,0x45,0x38,0x39,0x39,0x0D,0X0A]
    hexadecimal_result = format(number1, "03X")
    hexadecimal_result2 = format(number2, "03X")
    r=hexadecimal_result.zfill(4)
    r2=hexadecimal_result2.zfill(4)
    D[15]=ord(r[0])
    D[16]=ord(r[1])
    D[17]=ord(r[2])
    D[18]=ord(r[3])
    D[19]=ord(r2[0])
    D[20]=ord(r2[1])
    D[21]=ord(r2[2])
    D[22]=ord(r2[3])
 
    c=[]
    c1=[]
    l=len(D)    
    for i in range(l):
        if i ==0:
            continue
        elif i==l-4:
            break
        c.append(chr(D[i]))
        if i%2==0:
            c1.append(c[i-2]+c[i-1])
    lrc=0
    for i in range(len(c1)):
        lrc=lrc+int(c1[i],16)
    if lrc>256:
        lrc=lrc-256
        lrc=256-lrc
    else:
        lrc=256-lrc  
    hexa = format(lrc, "02X")
    lrc=hexa.zfill(2)
    D[23]=ord(lrc[0])
    D[24]=ord(lrc[1])
    ser.write(D)
    r=ser.readline()
    
def forward(number1,number2):
    f=[0x3A,0x30,0x31,0x30,0x46,0x30,0x35,0x30,0x30,0x30,0x30,0x30,0x36,0x30,0x31,0x33,0x42,0x41,0x39,0x0D,0x0A]
    ser.write(f)
    r=ser.readline()
    race(number1,number2)
def left(number1,number2):
    l=[0x3A,0x30,0x31,0x30,0x46,0x30,0x35,0x30,0x30,0x30,0x30,0x30,0x36,0x30,0x31,0x31,0x42,0x43,0x39,0x0D,0x0A]
    ser.write(l)
    r=ser.readline()
    race(number1,number2)
def right(number1,number2):
    r=[0x3A,0x30,0x31,0x30,0x46,0x30,0x35,0x30,0x30,0x30,0x30,0x30,0x36,0x30,0x31,0x33,0x46,0x41,0x35,0x0D,0x0A]
    ser.write(r)
    r=ser.readline()
    race(number1,number2)
def back(number1,number2):
    b=[0x3A,0x30,0x31,0x30,0x46,0x30,0x35,0x30,0x30,0x30,0x30,0x30,0x36,0x30,0x31,0x31,0x46,0x43,0x35,0x0D,0x0A]
    ser.write(b)
    r=ser.readline()
    race(number1,number2)

def on_press(key):
   
    
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))
      
        key=repr(key)
       
        if key=='<Key.left: <37>>':
            print('left')
            left(500,500)
        elif key=='<Key.right: <39>>':
            print('right')
            right(500,500)
        elif key=='<Key.up: <38>>':
            print('up')
            forward(500,500)
        elif key=='<Key.down: <40>>':
            print('down')
            back(500,500)
        
        

def on_release(key):
    print('Key released: {0}'.format(
        key))
    back(0,0)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()