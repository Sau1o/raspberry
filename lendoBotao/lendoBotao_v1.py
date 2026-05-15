#############################################################################################
# RoboCore - Kit Discovery para Raspberry Pi - Projeto Lendo um Botao
# O codigo le o pino conectado ao botao, e entao acende o LED caso ele esteja pressionado.
#############################################################################################

#adicao da biblioteca ao codigo
from gpiozero import LED, Button

#criacao dos objetos conectados ao LED e ao botao, respectivamente
led = LED(14)
botao = Button(15)

while True:

    #quando o botao estiver pressionado
    botao.when_pressed = led.on #acende o LED

    #quando o botao estiver solto
    botao.when_released = led.off #apaga o LED
