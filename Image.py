from enum import Enum
from matplotlib import pyplot

prohibicion = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 16]
peligro = [11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
stop = [14]
direccion_prohibida = [14]
ceda_paso = [13]
direccion_obligatoria = [38]


class SignalType(Enum):
    PROHIBIDO = 1
    PELIGRO = 2
    STOP = 3
    DIRECCION_PROHIBIDA = 4
    CEDA_EL_PASO = 5
    DIRECCION_OBLIGATORIA = 6
    OTRA = 7


class Image:

    def __init__(self, st: int, image):
        self.signal_type = None
        self.return_type(st)
        self.image = image

    def return_type(self, type: int):
        if type in prohibicion:
            self.signal_type = SignalType.PROHIBIDO
        elif type in peligro:
            self.signal_type = SignalType.PELIGRO
        elif type in stop:
            self.signal_type = SignalType.STOP
        elif type in direccion_prohibida:
            self.signal_type = SignalType.DIRECCION_PROHIBIDA
        elif type in ceda_paso:
            self.signal_type = SignalType.CEDA_EL_PASO
        elif type in direccion_obligatoria:
            self.signal_type = SignalType.DIRECCION_OBLIGATORIA
        else:
            self.signal_type = SignalType.OTRA

    def display_img(self):
        pyplot.imshow(self.image)
        pyplot.show()
