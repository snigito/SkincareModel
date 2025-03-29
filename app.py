from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load model once when the app starts
MODEL_PATH = "skin_model.h5"
IMAGE_SIZE = (224, 224)

print("🔁 Loading model...")
model = load_model(MODEL_PATH)
print("✅ Model loaded!")

# Get class names from the Training Images folder structure
CLASS_NAMES = sorted([
    folder for folder in os.listdir("Training Images")
    if os.path.isdir(os.path.join("Training Images", folder))
])

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    print("📥 Received image for prediction")

    img_file = request.files["image"]
    img_path = os.path.join("temp.jpg")
    img_file.save(img_path)

    # Preprocess the image
    img = image.load_img(img_path, target_size=IMAGE_SIZE)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    print("🔍 Making prediction...")
    predictions = model.predict(img_array)[0]
    top_indices = predictions.argsort()[::-1]
    top_classes = [(CLASS_NAMES[i], float(predictions[i])) for i in top_indices]

    return jsonify({
        "predictions": [
            {"class": cls, "confidence": round(conf * 100, 2)}
            for cls, conf in top_classes
        ]
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

