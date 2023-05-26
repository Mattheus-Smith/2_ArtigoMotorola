# https://code.adonline.id.au/structural-similarity-index-ssim-in-python/

import cv2
import numpy as np
#from brisque import BRISQUE
from matplotlib import pyplot as plt
from skimage.metrics import mean_squared_error
from skimage.metrics import structural_similarity as ssim
from pylab import *

import imquality.brisque as brisque #pip install --upgrade --force-reinstall -U git+https://github.com/ocampor/image-quality@master
from skimage import io, img_as_float

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the sum of the squared difference between the two images
    mse_error = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    mse_error /= float(imageA.shape[0] * imageA.shape[1])

    return mse_error

def compare(imageA, imageB):
    # Calculate the MSE and SSIM
    # m = mse(imageA, imageB)

    m = np.sqrt(mse(imageA, imageB))
    s = ssim(imageA, imageB)

    return m, s

def caso01():
    img = cv2.imread("./../caso01/01.jpg")
    img_output1 = cv2.imread("./../caso01/output_CLAHE_2_(8).png")
    img_output2 = cv2.imread("./../caso01/output_CLAHE_2_(18).png")
    img_output3 = cv2.imread("./../caso01/output_CLAHE_4_(12).png")
    img_output4 = cv2.imread("./../caso01/output_gamma_2.png")
    img_output5 = cv2.imread("./../caso01/fusion_mertens.jpg")
    img_output6 = cv2.imread("./../caso01/fusion_mertens_sem_4_12.jpg")

    # # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)
    gray5 = cv2.cvtColor(img_output5, cv2.COLOR_BGR2GRAY)
    gray6 = cv2.cvtColor(img_output6, cv2.COLOR_BGR2GRAY)

    m1, s1 = compare(gray0, gray1)
    m2, s2 = compare(gray0, gray2)
    m3, s3 = compare(gray0, gray3)
    m4, s4 = compare(gray0, gray4)
    m5, s5 = compare(gray0, gray5)
    m6, s6 = compare(gray0, gray6)

    # m1,s1 = compare(gray1, gray0)
    # m2,s2 = compare(gray2, gray0)
    # m3,s3 = compare(gray3, gray0)
    # m4,s4 = compare(gray4, gray0)

    print("m1: ", m1, " - s1: ", s1)
    print("m2: ", m2, " - s2: ", s2)
    print("m3: ", m3, " - s3: ", s3)
    print("m4: ", m4, " - s4: ", s4)
    print("m5: ", m5, " - s5: ", s5)
    print("m6: ", m6, " - s6: ", s6)

def caso18():
    img = cv2.imread("./../caso18/18.jpg")

    img_output1 = cv2.imread("./../caso18/18_output_gamma(0.8)_output_CLAHE_2_(10).png")
    img_output2 = cv2.imread("./../caso18/output_gamma(0.8)_output_CLAHE_2_(8).png")
    img_output3 = cv2.imread("./../caso18/output_gamma(0.8)_output_CLAHE_2_(12).png")
    img_output4 = cv2.imread("./../caso18/output_gamma_0.6.png")

    # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)

    m1, s1 = compare(gray1, gray0)
    m2, s2 = compare(gray2, gray0)
    m3, s3 = compare(gray3, gray0)
    m4, s4 = compare(gray4, gray0)

    print("m1: ", m1, " - s1: ", s1) #m1:  18.282992455045612  - s1:  0.861530515980176
    print("m2: ", m2, " - s2: ", s2) #m2:  18.37137185766339  - s2:  0.866292945618499
    print("m3: ", m3, " - s3: ", s3) #m3:  18.150260245443796  - s3:  0.8601643928547064
    print("m4: ", m4, " - s4: ", s4) #m4:  29.23076384243634  - s4:  0.8076717339295783

def caso28():
    img = cv2.imread("./../caso28/28.jpg")

    img_output1 = cv2.imread("./../caso28/output_CLAHE_2_(8).png")
    img_output2 = cv2.imread("./../caso28/output_CLAHE_2_(12).png")
    img_output3 = cv2.imread("./../caso28/output_gamma(0.7)_output_CLAHE_2_(8).png")
    img_output4 = cv2.imread("./../caso28/output_gamma(0.85)_output_CLAHE_2_(8).png")

    # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)

    m1, s1 = compare(gray0, gray1)
    m2, s2 = compare(gray0, gray2)
    m3, s3 = compare(gray0, gray3)
    m4, s4 = compare(gray0, gray4)

    print("m1: ", m1, " - s1: ", s1)
    print("m2: ", m2, " - s2: ", s2)
    print("m3: ", m3, " - s3: ", s3)
    print("m4: ", m4, " - s4: ", s4)

def caso31():
    img = cv2.imread("./../caso31/31.jpg")

    img_output1 = cv2.imread("./../caso31/output_gamma(0.9)_output_CLAHE_2_(8).png")
    img_output2 = cv2.imread("./../caso31/output_gamma(0.9)_output_CLAHE_3_(16).png")

    # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)

    m1, s1 = compare(gray0, gray1)
    m2, s2 = compare(gray0, gray2)

    print("m1: ", m1, " - s1: ", s1) #m1:  23.681296360911777  - s1:  0.5901643957173279
    print("m2: ", m2, " - s2: ", s2) #m2:  30.189494949954586  - s2:  0.46361435806831996

def caso31_v2():
    img = cv2.imread("./../caso31/31.jpg")

    img_output1 = cv2.imread("./../caso31/output_gamma(0.6)_output_CLAHE_2_(8).png")
    img_output2 = cv2.imread("./../caso31/output_gamma(0.7)_output_CLAHE_2_(8).png")
    img_output3 = cv2.imread("./../caso31/output_gamma(0.8)_output_CLAHE_2_(8).png")
    img_output4 = cv2.imread("./../caso31/output_gamma(0.9)_output_CLAHE_2_(8).png")

    # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)

    m1, s1 = compare(gray0, gray1)
    m2, s2 = compare(gray0, gray2)
    m3, s3 = compare(gray0, gray3)
    m4, s4 = compare(gray0, gray4)

    print("m1: ", m1, " - s1: ", s1) #m1:  41.07766062796988  - s1:  0.39202123278281603
    print("m2: ", m2, " - s2: ", s2) #m2:  33.88394915984066  - s2:  0.45938044793929883
    print("m3: ", m3, " - s3: ", s3) #m3:  28.225963083657568  - s3:  0.527125886218865
    print("m4: ", m4, " - s4: ", s4) #m4:  23.681296360911777  - s4:  0.5901643957173279

def caso31_v3():
    img = cv2.imread("./../caso31/31.jpg")

    img_output1 = cv2.imread("./../caso31/output_gamma(0.9)_output_CLAHE_2_(4).png")
    img_output2 = cv2.imread("./../caso31/output_gamma(0.9)_output_CLAHE_2_(8).png")
    img_output3 = cv2.imread("./../caso31/output_gamma(0.9)_output_CLAHE_3_(4).png")
    img_output4 = cv2.imread("./../caso31/output_gamma(0.9)_output_CLAHE_3_(16).png")

    # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)

    m1, s1 = compare(gray0, gray1)
    m2, s2 = compare(gray0, gray2)
    m3, s3 = compare(gray0, gray3)
    m4, s4 = compare(gray0, gray4)

    print("m1: ", m1, " - s1: ", s1) #m1:  25.425139580082284  - s1:  0.587266032979283
    print("m2: ", m2, " - s2: ", s2) #m2:  23.681296360911777  - s2:  0.5901643957173279
    print("m3: ", m3, " - s3: ", s3) #m3:  34.61416157201173  - s3:  0.4640616236536807
    print("m4: ", m4, " - s4: ", s4) #m4:  30.189494949954586  - s4:  0.46361435806831996

def casoNovos_29():
    img = cv2.imread("./../../caso29/2015_04995.jpg")  # 11.350071185880978
    img_output1 = cv2.imread("./../../caso29/output_gamma(0.7)_output_CLAHE_2_(4).png")  # 35.0565473982559
    img_output2 = cv2.imread("./../../caso29/output_gamma(0.7)_output_CLAHE_2_(8).png")  # 35.089595250212
    img_output3 = cv2.imread("./../../caso29/output_gamma(0.7)_output_CLAHE_2_(12).png")  # 35.41938171158333
    img_output4 = cv2.imread("./../../caso29/output_gamma(0.7)_output_CLAHE_2_(16).png")  # 35.786805342542124
    img_output5 = cv2.imread("./../../caso29/output_gamma(0.7)_output_CLAHE_3_(4).png")  # 35.0565473982559
    img_output6 = cv2.imread("./../../caso29/output_gamma(0.7)_output_CLAHE_3_(8).png")  # 35.089595250212
    img_output7 = cv2.imread("./../../caso29/output_gamma(0.7)_output_CLAHE_3_(12).png")  # 35.41938171158333
    img_output8 = cv2.imread("./../../caso29/output_gamma(0.7)_output_CLAHE_3_(16).png")  # 35.786805342542124
    img_output9 = cv2.imread("./../../caso29/output_gamma(0.8)_output_CLAHE_2_(4).png")  # 35.0565473982559
    img_output10 = cv2.imread("./../../caso29/output_gamma(0.8)_output_CLAHE_2_(8).png")  # 35.089595250212
    img_output11 = cv2.imread("./../../caso29/output_gamma(0.8)_output_CLAHE_2_(12).png")  # 35.41938171158333
    img_output12 = cv2.imread("./../../caso29/output_gamma(0.8)_output_CLAHE_2_(16).png")  # 35.786805342542124
    img_output13 = cv2.imread("./../../caso29/output_gamma(0.8)_output_CLAHE_3_(4).png")  # 35.0565473982559
    img_output14 = cv2.imread("./../../caso29/output_gamma(0.8)_output_CLAHE_3_(8).png")  # 35.089595250212
    img_output15 = cv2.imread("./../../caso29/output_gamma(0.8)_output_CLAHE_3_(12).png")  # 35.41938171158333
    img_output16 = cv2.imread("./../../caso29/output_gamma(0.8)_output_CLAHE_3_(16).png")  # 35.786805342542124

    # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)
    gray5 = cv2.cvtColor(img_output5, cv2.COLOR_BGR2GRAY)
    gray6 = cv2.cvtColor(img_output6, cv2.COLOR_BGR2GRAY)
    gray7 = cv2.cvtColor(img_output7, cv2.COLOR_BGR2GRAY)
    gray8 = cv2.cvtColor(img_output8, cv2.COLOR_BGR2GRAY)
    gray9 = cv2.cvtColor(img_output9, cv2.COLOR_BGR2GRAY)
    gray10 = cv2.cvtColor(img_output10, cv2.COLOR_BGR2GRAY)
    gray11 = cv2.cvtColor(img_output11, cv2.COLOR_BGR2GRAY)
    gray12 = cv2.cvtColor(img_output12, cv2.COLOR_BGR2GRAY)
    gray13 = cv2.cvtColor(img_output13, cv2.COLOR_BGR2GRAY)
    gray14 = cv2.cvtColor(img_output14, cv2.COLOR_BGR2GRAY)
    gray15 = cv2.cvtColor(img_output15, cv2.COLOR_BGR2GRAY)
    gray16 = cv2.cvtColor(img_output16, cv2.COLOR_BGR2GRAY)


    m1, s1 = compare(gray0, gray1)
    m2, s2 = compare(gray0, gray2)
    m3, s3 = compare(gray0, gray3)
    m4, s4 = compare(gray0, gray4)

    m5, s5 = compare(gray0, gray5)
    m6, s6 = compare(gray0, gray6)
    m7, s7 = compare(gray0, gray7)
    m8, s8 = compare(gray0, gray8)
    m9, s9 = compare(gray0, gray9)
    m10, s10 = compare(gray0, gray10)
    m11, s11 = compare(gray0, gray11)
    m12, s12 = compare(gray0, gray12)
    m13, s13 = compare(gray0, gray13)
    m14, s14 = compare(gray0, gray14)
    m15, s15 = compare(gray0, gray15)
    m16, s16 = compare(gray0, gray16)



    print("m1: ", m1, " - s1: ", s1) #m1:  25.425139580082284  - s1:  0.587266032979283
    print("m2: ", m2, " - s2: ", s2) #m2:  23.681296360911777  - s2:  0.5901643957173279
    print("m3: ", m3, " - s3: ", s3) #m3:  34.61416157201173  - s3:  0.4640616236536807
    print("m4: ", m4, " - s4: ", s4) #m4:  30.189494949954586  - s4:  0.46361435806831996

    print("m5: ", m5, " - s5: ", s5)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m6: ", m6, " - s6: ", s6)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m7: ", m7, " - s7: ", s7)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m8: ", m8, " - s8: ", s8)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m9: ", m9, " - s9: ", s9)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m10: ", m10, " - s10: ", s10)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m11: ", m11, " - s11: ", s11)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m12: ", m12, " - s12: ", s12)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m13: ", m13, " - s13: ", s13)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m14: ", m14, " - s14: ", s14)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m15: ", m15, " - s15: ", s15)  # m1:  25.425139580082284  - s1:  0.587266032979283
    print("m16: ", m16, " - s16: ", s16)  # m1:  25.425139580082284  - s1:  0.587266032979283

    # m1: 47.1493330726113 - s1:  0.5680697773542968
    # m2: 44.988657211167514 - s2:  0.562523963164487
    # m3: 43.72512708816154 - s3:  0.5602523117001242
    # m4: 43.21885778768218 - s4:  0.5628629439155206
    # m5: 54.37107559393338 - s5:  0.4975651845084543
    # m6: 52.03373888579983 - s6:  0.48782427003180245
    # m7: 50.500838468646236 - s7:  0.48704813807737657
    # m8: 49.41053563673101 - s8:  0.49009804131512164
    # m9: 40.22227474164374 - s9:  0.6205558461202519
        # m10: 37.5760121014833 - s10:  0.6181401799953845
        # m11: 36.03355341350913 - s11:  0.6170609334146638
            # m12: 35.0405055844793 - s12:  0.6235571941390905
    # m13: 48.47679989514335 - s13:  0.5356347569378457
    # m14: 45.59425105123141 - s14:  0.5288439753538826
    # m15: 43.61470842819366 - s15:  0.5303048619783602
    # m16: 42.111775499081155 - s16:  0.5364081663921477

def casoNovos_30():
    img = cv2.imread("./../../caso30/30.jpg")  # 11.350071185880978
    # img_output1 = cv2.imread("./../../caso30/mse/output_gamma(0.6)_output_CLAHE_2_(8).png")  # 31.150071417839605
    # img_output2 = cv2.imread("./../../caso30/mse/output_gamma(0.7)_output_CLAHE_2_(8).png")  # 25.497424542692215
    # img_output3 = cv2.imread("./../../caso30/mse/output_gamma(0.8)_output_CLAHE_2_(8).png")  # 21.434178969664107
    # img_output4 = cv2.imread("./../../caso30/mse/output_gamma(0.65)_output_CLAHE_2_(8).png")  # 28.194410454527222
    # img_output5 = cv2.imread("./../../caso30/mse/output_gamma(0.75)_output_CLAHE_2_(8).png")  # 23.186085939390473

    img_output6 = cv2.imread("./../../caso30/output_gamma(0.7)_output_CLAHE_2_(4).png")  # 25.831000906311296
    img_output7 = cv2.imread("./../../caso30/output_gamma(0.7)_output_CLAHE_2_(8).png")  # 25.497424542692215
    img_output8 = cv2.imread("./../../caso30/output_gamma(0.7)_output_CLAHE_2_(12).png")  # 24.390605396249033
    img_output9 = cv2.imread("./../../caso30/output_gamma(0.7)_output_CLAHE_2_(16).png")  # 26.053858174690983

    img_output10 = cv2.imread("./../../caso30/output_gamma(0.7)_output_CLAHE_3_(8).png")  # 28.926300332521876
    img_output11 = cv2.imread("./../../caso30/output_gamma(0.7)_output_CLAHE_3_(12).png")  # 27.76392892252698
    img_output12 = cv2.imread("./../../caso30/output_gamma(0.7)_output_CLAHE_3_(16).png")  # 29.904288400823674
    img_output13 = cv2.imread("./../../caso30/output_gamma(0.7)_output_CLAHE_3_(18).png")  # 29.076105853576237

    # Convert the images to grayscale
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray1 = cv2.cvtColor(img_output1, cv2.COLOR_BGR2GRAY)
    # gray2 = cv2.cvtColor(img_output2, cv2.COLOR_BGR2GRAY)
    # gray3 = cv2.cvtColor(img_output3, cv2.COLOR_BGR2GRAY)
    # gray4 = cv2.cvtColor(img_output4, cv2.COLOR_BGR2GRAY)
    # gray5 = cv2.cvtColor(img_output5, cv2.COLOR_BGR2GRAY)

    gray6 = cv2.cvtColor(img_output6, cv2.COLOR_BGR2GRAY)
    gray7 = cv2.cvtColor(img_output7, cv2.COLOR_BGR2GRAY)
    gray8 = cv2.cvtColor(img_output8, cv2.COLOR_BGR2GRAY)
    gray9 = cv2.cvtColor(img_output9, cv2.COLOR_BGR2GRAY)
    gray10 = cv2.cvtColor(img_output10, cv2.COLOR_BGR2GRAY)
    gray11 = cv2.cvtColor(img_output11, cv2.COLOR_BGR2GRAY)
    gray12 = cv2.cvtColor(img_output12, cv2.COLOR_BGR2GRAY)
    gray13 = cv2.cvtColor(img_output13, cv2.COLOR_BGR2GRAY)
    # gray14 = cv2.cvtColor(img_output14, cv2.COLOR_BGR2GRAY)
    # gray15 = cv2.cvtColor(img_output15, cv2.COLOR_BGR2GRAY)
    # gray16 = cv2.cvtColor(img_output16, cv2.COLOR_BGR2GRAY)


    # m1, s1 = compare(gray0, gray1)
    # m2, s2 = compare(gray0, gray2)
    # m3, s3 = compare(gray0, gray3)
    # m4, s4 = compare(gray0, gray4)
    # m5, s5 = compare(gray0, gray5)

    m6, s6 = compare(gray0, gray6)
    m7, s7 = compare(gray0, gray7)
    m8, s8 = compare(gray0, gray8)
    m9, s9 = compare(gray0, gray9)
    m10, s10 = compare(gray0, gray10)
    m11, s11 = compare(gray0, gray11)
    m12, s12 = compare(gray0, gray12)
    m13, s13 = compare(gray0, gray13)
    # m14, s14 = compare(gray0, gray14)
    # m15, s15 = compare(gray0, gray15)
    # m16, s16 = compare(gray0, gray16)



    # print("m1: ", m1, " - s1: ", s1) #m1:  25.425139580082284  - s1:  0.
    # print("m2: ", m2, " - s2: ", s2) #m2:  23.681296360911777  - s2:  0.
    # print("m3: ", m3, " - s3: ", s3) #m3:  34.61416157201173  - s3:  0.
    # print("m4: ", m4, " - s4: ", s4) #m4:  30.189494949954586  - s4:  0.
    # print("m5: ", m5, " - s5: ", s5)  # m1:  25.425139580082284  - s1:  0.

    print("m6: ", m6, " - s6: ", s6)  # m6:  25.831000906311296  - s1:  0.587266032979283
    print("m7: ", m7, " - s7: ", s7)  # m7:  25.497424542692215  - s1:  0.587266032979283
    print("m8: ", m8, " - s8: ", s8)  # m8:  24.390605396249033  - s1:  0.587266032979283
    print("m9: ", m9, " - s9: ", s9)  # m9:  26.053858174690983  - s1:  0.587266032979283
    print("m10: ", m10, " - s10: ", s10)  # m10:  28.926300332521876  - s1:  0.587266032979283
    print("m11: ", m11, " - s11: ", s11)  # m11:  27.76392892252698  - s1:  0.587266032979283
    print("m12: ", m12, " - s12: ", s12)  # m12:  29.904288400823674  - s1:  0.587266032979283
    print("m13: ", m13, " - s13: ", s13)  # m13:  29.076105853576237  - s1:  0.587266032979283

    # print("m14: ", m14, " - s14: ", s14)  # m1:  25.425139580082284  - s1:  0.587266032979283
    # print("m15: ", m15, " - s15: ", s15)  # m1:  25.425139580082284  - s1:  0.587266032979283
    # print("m16: ", m16, " - s16: ", s16)  # m1:  25.425139580082284  - s1:  0.587266032979283


# caso01()
casoNovos_30()
# caso28()

#image = cv2.imread("./../caso01/01.jpg") #18.76060435910503
#image = cv2.imread("./../caso01/01.tiff") #18.76060435910503 - acho q processou mais rapido q o .jpg
#grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #137.38920851487123

#score1 = brisque.score(image)
#score2 = brisque.score(img2)

#print(score1)
#print(score2)


# obj = BRISQUE(img, url=False)
# obj.score()

# Mean Squared Error
# MSE1 = np.square(np.subtract(img,img_output1)).mean()
# MSE2 = np.square(np.subtract(img,img_output2)).mean()
# MSE3 = np.square(np.subtract(img,img_output3)).mean()
# MSE4 = np.square(np.subtract(img,img_output4)).mean()
#
#
# print("mse1: ", MSE1)
# print("mse2: ", MSE2)
# print("mse3: ", MSE3)
# print("mse4: ", MSE4)

# ssim_output1 = ssim(img, img_output1,data_range=img_output1.max() - img_output1.min())
# ssim_output2 = ssim(img, img_output2,data_range=img_output2.max() - img_output2.min())
# ssim_output3 = ssim(img, img_output3,data_range=img_output3.max() - img_output3.min())
# ssim_output4 = ssim(img, img_output4,data_range=img_output4.max() - img_output4.min())
#
# print("ssim1: ", ssim_output1)
# print("ssim2: ", ssim_output2)
# print("ssim3: ", ssim_output3)
# print("ssim4: ", ssim_output4)

# ======================gamma -> square -> equaliza
# parametroGamma = 0.6
# out_gamma = correcaoGamma(img, parametroGamma)
#
# parametroSquare = 0.004
# out_square = funcionSquare(out_gamma, parametroSquare)
#
# #out_equalize = functionEqualization(out_square)
#
# texto = "./../output_gamma("+str(parametroGamma)+")_Square("+str(parametroSquare)+").png"
# cv2.imwrite(texto, out_square)


