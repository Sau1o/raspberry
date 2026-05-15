#############################################################################################
# RoboCore - Kit Discovery para Raspberry Pi - Projeto Blink
# Faz o LED conectado ao GPIO 14 (localizado no pino 8 do barramento) piscar de 1 em 1 
# segundo.
#############################################################################################

#adicao das bibliotecas
from gpiozero import LED
from time import sleep

#configura o objeto "led" a GPIO 14 da placa
led = LED(14)

#executa infinitamente
while True:
    led.on() #acende o LED
    sleep(1) #aguarda 1 segundo
    led.off() #apaga o LED
    sleep(1) #aguarda 1 segundo
