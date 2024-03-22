import numpy as np
from keras.applications import VGG16
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.preprocessing import image

def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # VGG16 expects input images to be of size (224, 224)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess input according to VGG16 requirements
    return img_array

def predict_image(image_path):
    model = VGG16(weights='imagenet', include_top=True)  # Load pre-trained VGG16 model
    processed_image = load_and_preprocess_image(image_path)
    predictions = model.predict(processed_image)
    decoded_predictions = decode_predictions(predictions, top=3)[0]  # Get top 3 predictions
    return decoded_predictions

if __name__ == "__main__":
    image_path = 'sargis.jpg'  # Replace 'example_image.jpg' with the path to your image
    predictions = predict_image(image_path)
    print("Predictions:")
    for i, (imagenet_id, label, score) in enumerate(predictions):
        print(f"{i + 1}. {label}: {score:.2f}")
