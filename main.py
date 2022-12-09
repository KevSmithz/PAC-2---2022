from pyfirmata import *
import motor
import sensor
import sensorQTR
from .sensorQTR import SensorQTREsquerda, SensorQTRDireita
import serial

port = '*'
board = Arduino(port)

bluetooth=serial.Serial(port, 9600)
print("Connected")
bluetooth.flushInput()

while True:
    sensor.distancia = 0
    sensorQTR.leitura = 300

    if SensorQTRDireita.leitura >=350:
        motor.pinH.Write(0)
        motor.pinV.Write(1)
    if SensorQTREsquerda.leitura <= 350:
        motor.pinV.Write(1)
        motor.pinH.Write(0)

    else:
        motor.pinH.Write(1)
        motor.pinV.Write(1)

    if sensor.distancia <= 0.30:
        motor.pinH.Write(0)
        motor.pinV.Write(0)

    elif sensor.distancia == 0:
        motor.pinH.Write(1)
        motor.pinV.Write(1)





