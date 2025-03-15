from transformers import pipeline
from PIL import Image

pipe = pipeline("image-classification", model="jhoppanne/Dogs-Breed-Image-Classification-V2")

class BreedDetector:
    def __init__(self):
        self.pipe = pipe

    def detect_breed(self, image_file):
        # Convert the uploaded file to a format compatible with the pipeline
        image = Image.open(image_file)
        result = self.pipe(image)
        return result[0]['label']