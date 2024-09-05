import numpy as np
from PIL import Image

# Load and preprocess the image

def preprocess_hold(image_path, target_size=(224, 224)):
    image = Image.open(image_path)
    image = image.convert('RGB')

    image = image.resize(target_size)

    image_array = np.array(image)

    image_array = image_array / 255.0

    return image_array

print(preprocess_hold('../data/raw/holds/testhold1.png'))
