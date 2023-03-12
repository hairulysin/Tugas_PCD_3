# Hairul Yasin
# F55121011

import cv2
import numpy as np

# Load citra digital
img = cv2.imread('IMG1.jpg')

# Tentukan ukuran kernel
kernel_size = 5

# Lakukan operasi Min Filter
img_min = cv2.erode(img, np.ones((kernel_size, kernel_size), np.uint8))

# Tampilkan citra digital asli dan hasil operasi Min Filter
cv2.imshow('Citra Digital Asli', img)
cv2.imshow('Hasil Operasi Min Filter', img_min)
cv2.waitKey(0)
cv2.destroyAllWindows()
