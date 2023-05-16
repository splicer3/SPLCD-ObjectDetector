# SPLCD-ObjectDetector

Open Source **project site** for easy object detection using **Flask**, **TailwindCSS**, **Flowbite** components and **WebcamJS**.

<p align="center">
<img src="https://user-images.githubusercontent.com/104271382/237925682-89be2835-2732-4574-aa30-cdeb7ad6d52f.png" alt="LogoFull-Blue" style="max-width: 100%; width:300px; height:300px;">
</p>

## Installation
Install conda or miniconda following the [anaconda docs](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) and run `conda env create -f environment.yml` and eventually `npm install` (the nodejs modules folder is provided).  
Then run the app with `flask run` or `gunicorn -w 4 app:app`(make sure the conda environment is activated).

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
