import cv2 # pip install opencv-python

# 1.Read Image
img = cv2.imread('gandhiji.jpg')

# 2.Convert RGB Image into Grayscale Image
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 3.Convert Grayscale Image into Negative Image (Inverted Image)
img_negative = cv2.bitwise_not(img_gray)

# 4.Apply Blur on Negative Image
img_blur = cv2.blur(img_negative,(20,20))

# 5.Final Sketch
img_sketch = cv2.divide(img_gray,255-img_blur,scale=256)
# 6.Show Image
cv2.imshow('Gandhiji',img_sketch)
cv2.waitKey(0)
