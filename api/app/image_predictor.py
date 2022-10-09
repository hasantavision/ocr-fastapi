import easyocr
from PIL import Image


class ImagePredictor:
    @staticmethod
    def init_ocr():
        return easyocr.Reader(['id', 'en'], model_storage_directory="/code/app/model")

    def predict_from_file(self, file_object):
        ocr = self.init_ocr()
        return ocr.readtext(file_object)
