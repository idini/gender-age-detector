<h1 align="center">gender-age-detector</h1>

## Index of contents

- [Requirements](#Requirements)
- [Installation](#Installation)
- [Estimator](#Estimator)
- [Utils](#Utils)

## Requirements
- Python v3.7.3+
- Torch
- Numpy
- Matplotlib
- OpenCV

## Installation

### Install Torch
To install Torch, please don't use ```pip``` or ```conda install```, go to https://pytorch.org/get-started/locally/

### Install dependences and package

Run command from terminal
```pip install git+https://github.com/idini/gender-age-detector.git```

## Estimator

We can estimate in realtime using the webcam 

```python
from GenderAgePoc.GenderAgeEstimatorOnline import GenderAgeEstimatorOnline
ol = GenderAgeEstimatorOnline()
ol.run()
```

or estimate age and gender from a picture

```python
from GenderAgePoc.GenderAgeEstimatorOffline import GenderAgeEstimatorOffline
ol = GenderAgeEstimatorOffline()
ol.predict(image)
# ol.predict(image, draw = True) # draw bbox and estimation on the picture
```

## Utils

We can import a picture using OpenCV

```python
import cv2

img = cv2.imread( <PATH-TO-IMAGE> )
```