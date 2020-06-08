import numpy as np
import cv2
def blur():
    img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img', img)
    print(img)
    height = img.shape[0]
    width = img.shape[1]

    threshold = 150

    for i in np.arange(3, height - 3):
        for j in np.arange(3, width - 3):
            sum = 0
            for k in np.arange(-3, 4):
                for l in np.arange(-3, 4):
                    a = img.item(i + k, j + k)
                    sum = sum + a
            b = int(sum / 49.0)
            img.itemset((i, j), b)
    cv2.imwrite('img_blur.jpeg', img)

    cv2.imshow('img_blur', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return True
blur()