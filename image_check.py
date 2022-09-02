import pyautogui
import cv2
import numpy as np

img = pyautogui.screenshot()

open_cv_image = np.array(img.crop((302, 687, 463, 848)))

# Convert RGB to BGR,opencv read image as BGR,but Pillow is RGB
open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)

cv2.imshow('image.jpg', open_cv_image)

k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite("image.png", open_cv_image)
