# SPLCD-ObjectDetector

Open Source **project site** for easy object detection using **Flask**, **TailwindCSS**, **Flowbite** components and **WebcamJS**.

## Installation
You need to `pip install` the requirements.txt file provided in the repo and eventually `npm install` (the nodejs modules folder is provided).  
Then run the app with `flask run` or `gunicorn -w 4 app:app`.

## Technologies used

* **Flask** for backend; 
* **TailwindCSS** and **Flowbite** for fast, utility-first, recyclable and mobile-ready frontend graphics;
* **WebcamJS** for easy access to the user's webcam, technically in maintenance mode but more than enough for a personal project;
* **Ultralytics YOLOV8** model for object detection, in this case using pretrained weights (`yolov8n.pt`).

## Purpose

This is a **personal project** and it's only objective is to showcase a **simple and modular way to implement object detection for multiple streams in a well presented, easy to understand web app**. Normally, object detection is already accessible through jupyter notebooks and Google Colabs, however they might still be too technical for the average Joe. This simple web app _takes away all the code_ from the user, and presents the results in a more eye-pleasing package. Currently, this project is using a general-purpose model that isn't very accurate for a lot of stuff, but **the model could always be swapped for a better performing one trained in one's domain of choice**.

## Credits

[Flask](http://flask.palletsprojects.com/)  
[TailwindCSS](https://tailwindcss.com)  
[Flowbite](https://flowbite.com)  
[WebcamJS](https://github.com/jhuckaby/webcamjs)
