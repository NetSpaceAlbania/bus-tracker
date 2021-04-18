#transivers
#arduino
#transiver tests
import serial
import time
import nRF24L01.h
import RF24.h

sport ='COM$'
baud_rate = 9600


serial_data = serial.Serial(sport, baud_rate)




sdata = serial_data.readline()



new code 2
##########################################3
import Serial
import time

s=serial.Serial(port=???,...) #set porten baudrate etj etj
delay(3)  #set nje time delay per te bere connection me porten

# kto i bera global sa per test mund ti ndyshojme pastaj
global Id           #id e bus dhe te linjes
global krahu =0      #krahu nenkupton vajte apo kthim


#funx ketu ben check stacionit dhe ne baze te stacionit percakton krahun e autobuzit
def check_stacionin:
    stacioni = s.readline()
    if stacioni == 0:
        krahu = 0
    if stacioni == 'F':
        krahu = 1


#funx ketu ben transmetimin e te dhenave ne stacion
def transimit:
    s.Write(Id,krahu)
    s.close()



while 1:
    check_stacionin()
    transimit()
##########################################33
