import os
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load model
model = load_model("../model/plant_disease_model.h5")

# Auto load class names from dataset
TRAIN_DIR = r"C:\PlantCare-AI\dataset\dataset\New Plant Diseases Dataset(Augmented)\New Plant Diseases Dataset(Augmented)\train"
class_names = sorted(os.listdir(TRAIN_DIR))


def predict_image(img_path):

    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)/255

    prediction = model.predict(img_array)
    index = np.argmax(prediction)

    return class_names[index]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["file"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    result = predict_image(filepath)

    plant = result.split("___")[0]

    return render_template(
        "result.html",
        image=filepath,
        plant=plant,
        disease=result
    )


if __name__ == "__main__":
    app.run(debug=True)