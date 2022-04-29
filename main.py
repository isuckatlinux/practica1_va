from Almacen import Warehouse
from Image import Image
from Algoritmos import Detector
from Image import SignalType


wr = Warehouse()
d = Detector()

wr.load_train_images('/home/pedro/Documentos/train_jpg')
m = d.mean_image(wr.train_images[SignalType.CEDA_EL_PASO])