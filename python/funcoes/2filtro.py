import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
import sys
from absl import app, flags, logging
from absl.flags import FLAGS
import os

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

    img = cv2.imread("./../caso9/09.JPG")
    i = 13

    #remoção de ruido Gaussiano
    if (i == 1):
        kernel = 3
        desvio = 0
        suavização = cv2.GaussianBlur(img, (kernel, kernel), desvio)
        texto = "./../Gaussiano_({},{})_Desvio{}.png".format(kernel, kernel, desvio)
        cv2.imwrite(texto, suavização)

    # remoção de ruido Mediana
    elif (i == 2):
        kernel = 3
        suavizacao = cv2.medianBlur(img, kernel)
        texto = "./../mediana_{}.png".format(kernel)
        cv2.imwrite(texto, suavizacao)

        cv2.destroyAllWindows()

    # ruido Gaussiano -> gamma -> CLAHE
    elif (i == 3):
        kernel = 3
        desvio = 0
        suavização = cv2.GaussianBlur(img, (kernel, kernel), desvio)

        parametroGamma = 0.85
        out_gamma = correcaoGamma(suavização, parametroGamma)

        parametroCLAHE = 2
        CLAHE_matriz = 2
        out_clahe = equalizeCLAHE(out_gamma, parametroCLAHE, CLAHE_matriz)

        texto = "./../Gaussiano_({}x{})_Desvio{}_gamma({})_CLAHE({}, {}).png".format(kernel,kernel, desvio, parametroGamma, parametroCLAHE, CLAHE_matriz)

        cv2.imwrite(texto, out_clahe)

    # equalize CLAHE
    elif (i == 4):

        lst_param_CLAHE = [1, 2, 3]
        lst_CLAHE_matriz = [2, 4, 8]

        for i in range(0, len(lst_CLAHE_matriz)):
            for j in range(0, len(lst_CLAHE_matriz)):

                parametroCLAHE = lst_param_CLAHE[i]
                CLAHE_matriz = lst_CLAHE_matriz[j]
                out_clahe = equalizeCLAHE(img, parametroCLAHE, CLAHE_matriz)

                texto = "./../CLAHE_({},{}).png".format(parametroCLAHE, CLAHE_matriz)
                cv2.imwrite(texto, out_clahe)

    # correcao de gamma
    elif (i == 7):

        # filtros = [0.5, 0.6, 0.7, 0.8, 0.9, 0.55, 0.65, 0.75, 0.85, 0.95]
        filtros = [1.2, 1.4, 1.8, 2, 2.2, 2.6,3,3.5,4,5,6]

        for i in range(0, len(filtros)):
            parametro = filtros[i]
            out = correcaoGamma(img, parametro)

            texto = "./../output_gamma_" + str(parametro) + ".png"
            cv2.imwrite(texto, out)

    # gamma -> square
    elif (i == 8):

        parametroGamma = [0.8, 0.9, 0.85, 0.95, 1.1, 1.2, 1.4, 1.8, 1.6,2, 2.2, 2.4,2.6]

        for i in range(0, len(parametroGamma)):
            parametro = parametroGamma[i]
            out = correcaoGamma(img, parametro)

            parametroSquare = [0.0030,0.0032,0.0034,0.0036,0.0038, 0.004]

            for j in range(0, len(parametroSquare)):
                out_square = funcionSquare(out, parametroSquare[j])

                texto = "./../gamma_{}_square_{}.png".format(parametroGamma[i], parametroSquare[j])
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

        lst_param_CLAHE = [1,2,3]
        lst_CLAHE_matriz = [2,4,8]

        for i in range(0, len(lst_param_CLAHE)):
            for j in range(0, len(lst_CLAHE_matriz)):
                parametroGamma = 0.75
                out_gamma = correcaoGamma(img, parametroGamma)

                parametroCLAHE = lst_param_CLAHE[i]
                CLAHE_matriz = lst_CLAHE_matriz[j]
                out_clahe = equalizeCLAHE(out_gamma, parametroCLAHE, CLAHE_matriz)

                texto = "./../output_gamma(" + str(parametroGamma) + ")_output_CLAHE_" + str(
                    parametroCLAHE) + "_(" + str(CLAHE_matriz) + ").png"
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

    #HDR com imagens com varios graus de exposição
    elif (i == 13):
        diretorio = "./../caso9/HDR"  # substitua pelo caminho do diretório que você deseja listar

        arquivos = os.listdir(diretorio)
        img_list = []
        for arquivo in arquivos:
            texto = diretorio+"/"+arquivo
            img = cv2.imread(texto)
            img_list.append(img)

        output = funcionHDR(img_list)
        texto = "./../output_HDR_gamma.png"
        cv2.imwrite(texto, output)

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass