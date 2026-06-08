import cv2

reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read("trainer/trainer.yml")

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        cinza,
        1.2,
        5
    )

    for (x,y,w,h) in faces:

        id_, confianca = reconhecedor.predict(
            cinza[y:y+h,x:x+w]
        )

        if confianca < 70:
            nome = "name"  #troque pelo nome da pessoa
        else:
            nome = "DESCONHECIDO"

        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            nome,
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow("Reconhecimento", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()
