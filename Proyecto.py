import serial
import time
import matplotlib.pyplot as plt
import csv
import numpy


def imp(any):
    progx = []
    progx = range(len(any))
    plt.plot(progx, any)
    plt.ylabel('Amplitude')
    plt.xlabel('Time/s')
    plt.show()


def hoja(tim, any, digy):
    file = [tim, any, tim, digy]
    newfile = open('data.csv', 'w')
    arch = csv.writer(newfile, delimiter=',')
    arch.writerow(['time', 'any', 'time', 'digy'])
    arch.writerows(zip(*file))
    print('Archivo csv creado')  # confirmacion


any = []
digy = []
##definicion de serial
ser = serial.Serial(
    port='COM4',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)
ser.isOpen()
##valores para lecturas
An = "An"
Pu1 = "P1"
Pu2 = "P2"
p2 = 0
a = 0
n1 = 0
n2 = 0
tim = []
##lecturas
while 1:
    a += 1
    tim.append(a)
    lec = str(ser.readline().strip())
    if lec == An:
        n1 = int(ser.readline().strip())
        any.append(n1)
    if lec == Pu1:
        n2 = (int(ser.readline().strip()))
        digy.append(n2)
    if lec == Pu2:
        p2 = (int(ser.readline().strip()))
        if p2 == 1:
            ser.write('1')
            time.sleep(1)
            ser.write('2')
            time.sleep(1)
            ser.write('3')
            time.sleep(1)
            ser.write('4')
            time.sleep(1)
            ser.write('5')
            time.sleep(1)
            ser.close()
            print(any)
            print(digy)
            imp(any)
            imp(digy)
            hoja(tim, any, digy)
