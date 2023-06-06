import cv2
import numpy as np

# Carregando a imagem
imagem = cv2.imread("./../caso8/mse/gamma_0.85_square_0.003.png")
# Convertendo a imagem para o espaço de cores HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Ajustando a saturação
fator_saturacao = 0.9  # Aumentar a saturação em 50%
imagem_hsv[..., 1] = np.clip(imagem_hsv[..., 1] * fator_saturacao, 0, 255)

# Convertendo a imagem de volta para o espaço de cores BGR
imagem_resultante = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR)

# Exibindo a imagem original e a imagem com a saturação ajustada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem com Saturação Ajustada', imagem_resultante)
cv2.waitKey(0)
cv2.destroyAllWindows()
