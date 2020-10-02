import cv2
import matplotlib.pyplot as plt
import cvlib
from cvlib.object_detection import draw_bbox

image = cv2.imread('test2.jpg')

bbox, label, conf = cvlib.detect_common_objects(image)
output = draw_bbox(image, bbox, label, conf)

plt.figure()
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.show()
