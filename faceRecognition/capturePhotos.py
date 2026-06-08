##################################
#sudo apt update
#sudo apt install python3-opencv
#pip install opencv-contrib-python
##################################

import cv2
import os

ID_USUARIO = 1
TOTAL_FOTOS = 200

camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

os.makedirs("dataset", exist_ok=True)

contador = 0

print("Olhando para a câmera...")
print("Pressione CTRL+C para interromper")

while True:

    ret, frame = camera.read()

    if not ret:
        continue

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        cinza,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        contador += 1

        rosto = cinza[y:y+h, x:x+w]

        nome_arquivo = f"dataset/User.{ID_USUARIO}.{contador}.jpg"

        cv2.imwrite(nome_arquivo, rosto)

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Fotos: {contador}/{TOTAL_FOTOS}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

    cv2.imshow('Capturando Faces', frame)

    tecla = cv2.waitKey(100)

    if tecla == 27:
        break

    if contador >= TOTAL_FOTOS:
        break

camera.release()
cv2.destroyAllWindows()

print(f"{contador} fotos capturadas!")
