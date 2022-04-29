from Almacen import Warehouse
from Image import Image

wr = Warehouse()
wr.load_train_images('/home/pedro/images/train_jpg')
for img in wr.train_images:
    img.display_img()