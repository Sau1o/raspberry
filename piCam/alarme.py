###############################################################################
# RoboCore - Kit Discovery para Raspberry Pi - Projeto Alarme de Presenca 
# Cria janela com a imagem captada, analisa se ha movimento e notifica se houver.
################################################################################

import os
import cv2
import time
from picamera2 import Picamera2

# remove o debug da biblioteca picamera2
os.environ["LIBCAMERA_LOG_LEVELS"] = "4"

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size":(640,480)}))
picam2.start()

background = None

tempoInicial = time.time()

while True:
  frame = picam2.capture_array()
  imagemInvertida = cv2.flip(frame[:,:,:3], -1)
  roi = imagemInvertida[360:480, 160:320]

  roiCinza = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
  roiCinza = cv2.GaussianBlur(roiCinza, (5,5), 0)

  if background is None:
    background = roiCinza
    continue

  subtracao = cv2.absdiff(background, roiCinza)
  imagemPB = cv2.threshold(subtracao, 25, 255, cv2.THRESH_BINARY)[1]
  imagemPB = cv2.dilate(imagemPB, None, iterations=2)

  contornos = cv2.findContours(imagemPB.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

  try:
    contornos = max(contornos, key=cv2.contourArea)

    if len(contornos) > 400:
        cv2.drawContours(roi, [contornos], -1, (255,0,0), 1)
        tempoFinal = time.time()

        if tempoFinal - tempoInicial > 5:
            print("ALERTA: MOVIMENTO DETECTADO")
            tempoInicial = time.time()
  except:
    pass

  cv2.rectangle(imagemInvertida, (160,360), (320,480), (0,0,255), 1)

  cv2.imshow('Minha Camera', imagemInvertida)
  cv2.imshow('ROI', imagemPB)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

picam2.stop()
picam2.close()
cv2.destroyAllWindows()
