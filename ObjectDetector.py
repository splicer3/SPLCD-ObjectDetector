import math

from ultralytics import YOLO
import cv2

MAX_WIDTH = 720
MAX_HEIGHT = 576


class ObjectDetector:
    # Constructor loads model and labels
    def __init__(self, model_path, labels_path):
        self.model = YOLO(model_path)
        with open(labels_path, "r") as file:
            self.classNames = file.read().splitlines()

    # Detects objects in a video stream
    def detect(self, stream_path, confidence):
        # Initialize video feed and window
        cap = cv2.VideoCapture(stream_path)

        frame_width = int(cap.get(3)) if cap.get(3) < MAX_WIDTH else MAX_WIDTH
        frame_height = int(cap.get(4)) if cap.get(4) < MAX_HEIGHT else MAX_HEIGHT

        while True:  # Loop over frames
            success, img = cap.read()
            resized = image_resize(img, frame_width, frame_height)
            # Detection frame by frame, stream=True to prevent memory overflow
            results = self.model(resized, stream=True, conf=confidence)
            # Looping over each bounding box
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    self.detectImage(box, resized)
            yield resized

    cv2.destroyAllWindows()

    # Detects objects in a single image
    def detectImage(self, box, img):
        # Extracting the coordinates of the bounding box: xMin yMax is the top left corner,
        # xMax, yMin is the bottom right corner
        xMin, yMax, xMax, yMin = box.xyxy[0]
        xMin, yMax, xMax, yMin = int(xMin), int(yMax), int(xMax), int(yMin)
        # Drawing the bounding box
        cv2.rectangle(img, (xMin, yMax), (xMax, yMin), (255, 0, 255), 3)
        conf = math.ceil((box.conf[0] * 100)) / 100
        # Drawing the label and confidence
        cls = int(box.cls[0])
        class_name = self.classNames[cls]
        label = f"{class_name} {conf}"
        t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
        # Drawing the rectangle containing the label and the label
        cv2.rectangle(img, (xMin, yMax), (xMin + t_size[0], yMax - t_size[1] - 3), (255, 0, 255), -1,
                      cv2.LINE_AA)
        cv2.putText(img, label, (xMin, yMax - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)


# Resizes an image while also keeping the aspect ratio
def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None or w < width and h < height:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized
