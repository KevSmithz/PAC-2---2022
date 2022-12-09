from pyfirmata import *

port = '*'
pinC = 2
board = Arduino(port)
board.analog[pinC].mode = pyfirmata.INPUT

distancia = 0
class Sensor:
    def __init__(self, pinC: 2 = int, distancia : float = 0):
        self.pinC = pinC
        self.distancia = distancia