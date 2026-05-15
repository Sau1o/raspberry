################################################################################
# RoboCore - Kit Discovery para Raspberry Pi - Projeto Visao Computacional
# Cria janela com a imagem captada pela camera e inverte a imagem.
################################################################################
  
import os
import cv2
from picamera2 import Picamera2 

# remove o debug da biblioteca picamera2
os.environ["LIBCAMERA_LOG_LEVELS"] = "4"

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size":(640,480)}))
picam2.start()
  
while True:
  frame = picam2.capture_array()
  imagemInvertida = cv2.flip(frame[:,:,:3], -1)
  cv2.imshow('Minha Camera', imagemInvertida)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
  	break

picam2.stop()
picam2.close()
cv2.destroyAllWindows()
