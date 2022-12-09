import pyfirmata
from pyfirmata import Arduino, SERVO
from time import sleep

port = '*'
pinH = 3
pinV = 4
board = Arduino(port)
board.digital[pinH].mode = pyfirmata.OUTPUT
board.digital[pinV].mode = pyfirmata.OUTPUT

class MotorDireita:
    def __init__(self,pinH: int = 3):
        self.pinH = pinH

class MotorEsquerda:
    def __init__(self, pinV: int = 4):
        self.pinV = pinV
