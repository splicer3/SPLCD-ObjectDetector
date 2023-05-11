from PIL import Image
import base64

from flask import Flask, render_template, Response, jsonify, request, session, make_response, redirect, url_for

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, FileField, DecimalRangeField, IntegerRangeField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired, NumberRange
import os

import cv2
import ObjectDetector as Detector  # Importing the ObjectDetector class from ObjectDetector.py

app = Flask(__name__)

app.config["SECRET_KEY"] = "totally-secret-key"
app.config["UPLOAD_FOLDER"] = "static/uploads"


class UploadFileForm(FlaskForm):
    # file variable stores the uploaded video file path
    file = FileField("File", validators=[InputRequired()])
    # Confidence slider to set the confidence threshold, controlled by user
    # conf_slider = IntegerRangeField("Confidence: ", default=50,
    # validators=[InputRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField("Run")


# Generating video output from the ObjectDetector class
def generate_frames(stream_path, conf=0.5):
    print("Stream path: ", stream_path)
    output = Detector.ObjectDetector("models/yolov8s.pt", "labels/labels.txt").detect(stream_path, conf)

    for detection_ in output:
        ref, buffer = cv2.imencode(".jpg", detection_)
        # Converting the image to bytes as required by Flask
        frame = buffer.tobytes()
        # Yielding individual frames
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def saveForm(form):
    if form.validate_on_submit():
        # Saving the uploaded file to the UPLOAD_FOLDER
        f = form.file.data
        filename = secure_filename(f.filename)
        savepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], filename)
        f.save(savepath)
        # Saving the video path to the session
        session["video_path"] = savepath
        print("Save path: ", savepath)


# Homepage routes
@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    session.clear()
    return render_template("index.html")


# Webcam detection route
@app.route('/webcam', methods=["GET", "POST"])
def webcam():
    # Clearing the session if the user is coming from the upload route
    clear_session = request.args.get('clear_session')
    if clear_session:
        session.clear()
    return render_template("webcamView.html")


# Upload detection route
@app.route('/upload', methods=["GET", "POST"])
def upload():
    # Clearing the session if the user is coming from the webcam route
    clear_session = request.args.get('clear_session')
    if clear_session:
        session.clear()
        return redirect(url_for('upload'))
    # Creating an instance of the UploadFileForm class
    form = UploadFileForm()
    # If the form is submitted and validated
    saveForm(form)
    # Redirecting to the detection route
    return render_template("upload.html", form=form)


@app.route('/detection', methods=["GET", "POST"])
def detection():
    # Getting the video path and confidence threshold from the session
    video_path = session.get('video_path', None)
    # Generating the frames
    return Response(generate_frames(stream_path=video_path), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/webcamdetection', methods=["POST"])
def webcamdetection():
    data_uri = request.json['data_uri']
    # Parse the data URI to get the binary image data
    binary_data = base64.b64decode(data_uri.split(',')[1])
    # Save the image data as a PNG file
    with open('./static/uploads/captured_image_001.png', 'wb') as f:
        f.write(binary_data)
    # Store the path to the saved image file in the session
    session['video_path'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"],
                                         'captured_image_001.png')
    print(session['video_path'])
    # Call the detection function with the path to the saved image file
    return detection()

if __name__ == '__main__':
    app.run(debug=True)
