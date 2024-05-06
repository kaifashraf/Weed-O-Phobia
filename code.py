!nvidia-smi
!pip install ultralytics==8.0.196
from IPython import display
display.clear_output()
from IPython.display import display, Image

import ultralytics
ultralytics.checks()
from ultralytics import YOLO
import os
!yolo mode=checks

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="gZiW61v7yAby55REkjQv")
project = rf.workspace("haashim").project("weed-detection-no2uj")
version = project.version(4)
dataset = version.download("yolov8")

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="gZiW61v7yAby55REkjQv")
project = rf.workspace("haashim").project("weed-detection-no2uj")
version = project.version(4)
dataset = version.download("yolov8")
!yolo task=detect mode= predict model= yolov8n.pt data={dataset.location}/data.yaml 

!ls runs/detect/train/

Image(filename='runs/detect/train/confusion_matrix.png', width=600)
