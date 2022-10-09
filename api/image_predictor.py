import easyocr
from PIL import Image

class ImagePredictor:

    def init_ocr(self):
        return easyocr.Reader(['id', 'en'])

    def predict_from_file(self, file_object):
        ocr = self.init_ocr()
        return ocr.readtext(file_object)
