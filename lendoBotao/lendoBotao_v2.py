import RPi.GPIO as GPIO
GPIO.setup(12,GPIO.IN)

while True:
  input_value = GPIO.input(12)
  if input_value == False:
    print("Botão pressionado..")
    while input_value == False:
      input_value = GPIO.input(12)
