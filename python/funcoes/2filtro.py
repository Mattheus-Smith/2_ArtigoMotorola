import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import sys
from absl import app, flags, logging
from absl.flags import FLAGS

from funcoesExtras.correcaoGamma import correcaoGamma
from funcoesExtras.funcionCLAHE import equalizeCLAHE
from funcoesExtras.funcionEqualize import functionEqualization
#from funcionLinear import *
#from funcionLinearPorParte import *
from funcoesExtras.funcionHDR import funcionHDR
from funcoesExtras.funcionQuadrada import funcionQuadrada
from funcoesExtras.funcionSquare import funcionSquare


flags.DEFINE_string('pc', "1", 'identifiy wich pc')

def main(_args):

    img = cv2.imread("./../caso30/30.jpg")
    i = 10

    # equalize CLAHE
    if (i == 1):
        parametroCLAHE = 2
        CLAHE_matriz = 8
        output_CLAHE = equalizeCLAHE(img, parametroCLAHE, CLAHE_matriz)

        texto = "./../output_CLAHE_"+str(parametroCLAHE)+"_("+str(CLAHE_matriz)+").png"
        cv2.imwrite(texto, output_CLAHE)

    # equalize normal
    elif (i == 2):
        out_equalize = functionEqualization(img)

        texto = "./../output_equalize.png"
        cv2.imwrite(texto, out_equalize)

    # funcion Linear
    elif (i == 3):
        a=1
        # parametroA = 0.55
        # parametroB = 25
        # out = funcitonLinear(img, parametroA, parametroB)
        #
        # texto = "./../output_linear_("+str(parametroA)+","+str(parametroB)+").png"
        # cv2.imwrite(texto, out)

    # funcion Linear por Parte
    elif (i == 4):
        a=1
        # parametroA = 0.55
        # parametroB = 25
        # out = funcitonLinear(img, parametroA, parametroB)
        #
        # texto = "./../output_linear_("+str(parametroA)+","+str(parametroB)+").png"
        # cv2.imwrite(texto, out)

    # funcion Quadrado
    elif (i == 5):
        parametroQuadrado = 0.075
        out = funcionQuadrada(img, parametroQuadrado, 255)

        texto = "./../output_quadrada_"+str(parametroQuadrado)+".png"
        cv2.imwrite(texto, out)

    # funcion Square
    elif (i == 6):
        parametroSquare = 0.004
        out = funcionSquare(img, parametroSquare)

        texto = "./../output_Square_"+str(parametroSquare)+".png"
        cv2.imwrite(texto, out)

    # correcao de gamma
    elif (i == 7):
        parametro = 0.7
        out = correcaoGamma(img, parametro)

        texto = "./../output_gamma_"+str(parametro)+".png"
        cv2.imwrite(texto, out)

    # gamma -> square
    elif (i == 8):
        parametroGamma =1.8
        out_gamma = correcaoGamma(img, parametroGamma)

        parametroSquare = 0.004
        out_square = funcionSquare(out_gamma, parametroSquare)

        texto = "./../output_gamma("+str(parametroGamma)+")_Square("+str(parametroSquare)+").png"
        cv2.imwrite(texto, out_square)

    # square -> gamma
    elif (i == 9):
        parametroSquare = 0.0045
        out_square = funcionSquare(img, parametroSquare)

        parametroGamma = 0.85
        out_gamma = correcaoGamma(out_square, parametroGamma)

        texto = "./../output_square(" + str(parametroSquare) + ")_output_gamma(" + str(parametroGamma) + ").png"
        cv2.imwrite(texto, out_gamma)

    # gamma -> equalize CLAHE
    elif(i == 10):
        parametroGamma = 0.7
        out_gamma = correcaoGamma(img, parametroGamma)

        parametroCLAHE = 3
        CLAHE_matriz = 8
        out_clahe = equalizeCLAHE(out_gamma, parametroCLAHE, CLAHE_matriz)

        texto = "./../output_gamma("+str(parametroGamma)+")_output_CLAHE_"+str(parametroCLAHE)+"_("+str(CLAHE_matriz)+").png"
        cv2.imwrite(texto, out_clahe)

    # gamma -> square -> equalize CLAHE
    elif(i == 11):
        parametroGamma = 0.8
        out_gamma = correcaoGamma(img, parametroGamma)

        parametroSquare = 0.0045
        out_square = funcionSquare(out_gamma, parametroSquare)

        parametroCLAHE = 2
        CLAHE_matriz = 8
        out_clahe = equalizeCLAHE(out_square, parametroCLAHE, CLAHE_matriz)

        texto = "./../output_gamma(" + str(parametroGamma) + ")_Square(" + str(
            parametroSquare) + ")_output_CLAHE_" + str(parametroCLAHE) + "_(" + str(
            CLAHE_matriz) + ").png"
        cv2.imwrite(texto, out_clahe)

        # HDR

    #HDR para iamgens de suberexposição
    elif (i == 12):
        out_gamma1 = correcaoGamma(img, 0.45)
        out_gamma2 = correcaoGamma(img, 0.6)
        out_gamma3 = correcaoGamma(img, 0.7)
        out_gamma4 = correcaoGamma(img, 0.8)
        out_gamma5 = correcaoGamma(img, 1.8)
        out_gamma6 = correcaoGamma(img, 4)

        # Loading exposure images into a list
        img_list = [out_gamma1, out_gamma2, out_gamma3, out_gamma4, out_gamma5,out_gamma6]
        #img_list = [cv2.imread(fn) for fn in img_fn]

        output = funcionHDR(img_list)
        texto = "./../output_HDR_gamma.png"
        cv2.imwrite(texto, output)

    elif (i == 13):
        a=1
        #falta elaborar aq

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass