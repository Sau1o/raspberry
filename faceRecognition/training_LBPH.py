import cv2
import os
import numpy as np
from PIL import Image

caminho_dataset = "dataset"

reconhecedor = cv2.face.LBPHFaceRecognizer_create()

detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

def carregar_imagens(caminho):

    imagens = [
        os.path.join(caminho, f)
        for f in os.listdir(caminho)
    ]

    faces = []
    ids = []

    for imagem in imagens:

        img = Image.open(imagem).convert('L')

        img_numpy = np.array(img, 'uint8')

        id_usuario = int(
            os.path.split(imagem)[-1].split(".")[1]
        )

        faces_detectadas = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces_detectadas:
            faces.append(img_numpy[y:y+h,x:x+w])
            ids.append(id_usuario)

    return faces, ids

print("Treinando...")

faces, ids = carregar_imagens(caminho_dataset)

reconhecedor.train(
    faces,
    np.array(ids)
)

os.makedirs("trainer", exist_ok=True)

reconhecedor.write(
    "trainer/trainer.yml"
)

print("Treinamento concluído!")
print("Arquivo salvo em trainer/trainer.yml")
