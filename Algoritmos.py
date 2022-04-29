
class Detector:

    def __init__(self):
        pass

    def mean_image(self, image_list:list):
        mean = image_list[0].image
        for image in image_list:
            mean += image.image
        return mean / len(image_list)