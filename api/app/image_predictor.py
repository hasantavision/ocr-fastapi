import easyocr
from PIL import Image


class ImagePredictor:
    def __init__(self):
        self.ocr = self.init_ocr()
        
    @staticmethod
    def init_ocr():
        return easyocr.Reader(['id', 'en'], model_storage_directory="/code/app/model")

    def predict_from_file(self, file_object):
        return self.ocr.readtext(file_object)
