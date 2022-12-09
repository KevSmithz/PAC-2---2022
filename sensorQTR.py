from pyfirmata import Arduino
import pyfirmata
from time import sleep

port = '*'
pinQ = 1
pinL = 0
leitura = 300
board = Arduino(port)
board.analog[pinQ].mode = pyfirmata.INPUT
board.analog[pinL].mode = pyfirmata.INPUT

class SensorQTREsquerda:
    def __init__(self, pinQ: int = 1, leitura: float = 300):
        self.pinQ = pinQ
        self.leitura = leitura

class SensorQTRDireita:
    def __init__(self, pinL: int = 0, leitura: float = 300):
        self.pinL = pinL
        self.leitura = leitura


