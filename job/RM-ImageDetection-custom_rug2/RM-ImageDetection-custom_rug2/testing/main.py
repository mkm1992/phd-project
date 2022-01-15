import numpy as np
import cv2 
import PIL
from PIL import Image

import matplotlib.pyplot as plt


name =  'm3.jpg'
img= cv2.imread(name)

#imag2 = imag
img =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img =  cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
plt.imshow(img)
plt.show()