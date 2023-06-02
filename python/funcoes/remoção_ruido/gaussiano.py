import cv2

imagem = cv2.imread("./../../caso33/33.jpg")

suavização = cv2.GaussianBlur(imagem, (3,3), 0)

cv2.imwrite("Gaussiano_(3,3).png", suavização)

# # cria uma janela vazia
# cv2.namedWindow('Imagem', cv2.WINDOW_NORMAL)
#
# # define o tamanho da janela
# cv2.resizeWindow('Imagem', 800, 600)
#
# # mostra a imagem usando OpenCV
# cv2.imshow("Imagem", suavização)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

