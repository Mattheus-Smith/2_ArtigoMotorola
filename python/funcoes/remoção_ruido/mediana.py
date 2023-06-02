# import numpy as np
# import cv2
#
# imagem = cv2.imread("./../../caso33/33.jpg")
# kernel = np.ones((5,5), np.float32)/25
# out = cv2.filter2D(imagem, -1, kernel)
#
# cv2.imwrite("original.png", imagem)
# cv2.imwrite("output.png", out)
#
# cv2.destroyAllWindows()

import numpy as np
import cv2

imagem = cv2.imread("./../../caso33/33.jpg")
suavizacao = cv2.medianBlur(imagem, 7)

cv2.imwrite("output7.png", suavizacao)

cv2.destroyAllWindows()