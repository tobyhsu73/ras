import serial  # 引用pySerial模組
import serial.tools.list_ports
import time
import TOFSense_concatenate as tofsense    #自己寫的檔案，放同工作目錄
data = {}
    #副程式 讀取所有tofsence
def tofreadall(ser):
    ser.flushInput()
    ID_list = [0,2,4] 
    for ID in ID_list:
       
       tofsense.ask(ser,ID)    #發送偵測指令
       time.sleep(0.01)
    for ID in ID_list:   
       #print("ser.in_waiting",ser.in_waiting)    #顯示緩存中的字節數
       gotbata = tofsense.read(ser)
       data[gotbata["id"]] = gotbata    #依照ID存入
       #if gotbata["id"] !=-1:
       #    print("ID:",gotbata["id"],"  distance =",gotbata["distance"])
       gotbata = tofsense.read(ser)
       data[gotbata["id"]] = gotbata    #依照ID存入
       #if gotbata["id"] !=-1:
       #    print("ID:",gotbata["id"],"  distance =",gotbata["distance"])

#=================================主程式=================================
def toffin():

    BAUD_RATES = 115200    #鮑率115200
    usbport = "/dev/ttyUSB0"
    ser = serial.Serial(usbport, BAUD_RATES)   # 初始化序列通訊埠
    time.sleep(0.01)
    ser.flushInput()  #清空接收緩存
    return(ser)

def tofget():
    ser=toffin()
    tofreadall(ser)
    tofreadall(ser)
    ser.close()
    return(data)
    
    
    """
    try:
        data = {}
    
        tofreadall()
        tofreadall()
        
        #f-string
          
       
        time.sleep(0.1)
            
    except KeyboardInterrupt:
        ser.close()    # 清除序列通訊物件
        s.close()
        print('斷開連線\n再見！')
    except:
        ser.close()    # 清除序列通訊物件
   
    print('發生錯誤，斷開連線')
    """
