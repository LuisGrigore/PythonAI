from PIL import Image
import io

class Service:
    def __init__(self, model, image_path):
        self.model = model
        self.image_path = image_path

    def save_preprocessed_image(self, blob):
        image = Image.open(io.BytesIO(blob))

        image = image.resize((28, 28), Image.BILINEAR)
        image_with_backround = Image.new("RGB", image.size, (255, 255, 255))
        image_with_backround.paste(image, (0, 0), image)

        image_with_backround.save(self.image_path, format='PNG')

    def classify(self,blob):
        self.save_preprocessed_image(blob)
        return self.model.classify(image_path=self.image_path)