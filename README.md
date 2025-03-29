# SkincareModel API

This project is a **Flask-based API for skin condition classification**, developed as part of a **hackathon project**.

It leverages a pre-trained **TensorFlow** model to analyze skin images and return the top five most likely skin conditions. The API is currently deployed and accessible via:

```
https://skincaremodelapi.onrender.com/predict
```

## 🔧 How It Works
- A user uploads an image via a `POST` request to the `/predict` endpoint.
- The image is processed, resized, and passed through a trained image classification model.
- The API returns a list of the top 5 most probable skin conditions, along with confidence scores.

## 🧪 Example Usage (cURL)
```bash
curl -X POST -F image=@your-image.jpg https://skincaremodelapi.onrender.com/predict
```

## 📂 Files
- `app.py` – Flask API server
- `skin_model.h5` – Pre-trained model file (tracked with Git LFS)
- `requirements.txt` – Project dependencies
- `render.yaml` – Render.com deployment configuration
- `Training Images/` – Placeholder for training data (removed from repo for size)

## ⚙️ Tech Stack
- Python 3.11
- Flask
- TensorFlow / Keras
- Pillow
- Render (for deployment)

## 🙏 Acknowledgments
- This project was built with the help of **AI assistance** for writing, debugging, and deployment support.
- Special thanks to my hackathon team and collaborators.

## 🚀 Deployment
This project is deployed using **Render**, with the following setup:
- Build command: `pip install -r requirements.txt`
- Start command: `python app.py`
- Python version: `3.11`
- Instance type: Starter (512 MB+ RAM required)

---

*Created by Sean Nigito for a Spring 2025 Hackathon*

