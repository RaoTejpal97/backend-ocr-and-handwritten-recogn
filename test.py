from urllib import response
import requests

import cv2

image = cv2.imread("./images/donut.png")
# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

BASE_URL = "http://127.0.0.1:5000/"


response = requests.post(BASE_URL+"upload",{"file":image})
print(response.status_code)
print(response.json())