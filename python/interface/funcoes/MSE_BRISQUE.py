# https://code.adonline.id.au/structural-similarity-index-ssim-in-python/

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from pylab import *
import time
from datetime import datetime
import imquality.brisque as brisque #pip install --upgrade --force-reinstall -U git+https://github.com/ocampor/image-quality@master

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

    return round(m,4), s

def get_mse(lst_imgs):
    lst_resultado = []
    lst_ordenada = []

    img0 = cv2.imread(lst_imgs[0])
    gray0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    lst_resultado.append(0)
    for i in range(1, len(lst_imgs)):
        img1 = cv2.imread(lst_imgs[i])
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        m1, s1 = compare(gray0, gray1)

        lst_resultado.append(m1)
    lst_ordenada = lst_resultado.copy()
    lst_ordenada.sort()

    return lst_resultado, lst_ordenada

def get_brisque(lst_imgs):
    lst_resultado = []

    named_tuplei = time.localtime()  # get struct_time
    time_stringi = time.strftime("%H:%M:%S", named_tuplei)
    ti = datetime.strptime(time_stringi, "%H:%M:%S")
    print(time_stringi)

    for i in range(0, len(lst_imgs)):
        print("execucao: ", i)
        img = cv2.imread(lst_imgs[i])
        score = brisque.score(img)
        lst_resultado.append(round(score, 4))

    named_tuplef = time.localtime()  # get struct_time
    time_stringf = time.strftime("%H:%M:%S", named_tuplef)
    tf = datetime.strptime(time_stringf, "%H:%M:%S")
    print(time_stringf)

    # get difference
    delta = tf - ti
    sec = delta.total_seconds()
    min = sec / 60
    hours = sec / (60 * 60)
    tempo_total = hours+ ":"+ min + ":"+sec
    print(tempo_total)

    return lst_resultado

