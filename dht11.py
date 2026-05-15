#############################################################################################
# RoboCore - Kit Discovery para Raspberry Pi - Leitura de Temperatura e Umidade
# Utiliza o DHT11 para ler a temperatura e umidade ambiente de 2 em 2 segundos

# lembre-se de instalar a lib: pip3 install adafruit-circuitpython-dht
#############################################################################################
      
# adicao das bibliotecas ao codigo
import board
import subprocess
import adafruit_dht
from time import sleep
      
# garante que o pino estara disponivel para uso
subprocess.run("pgrep -f 'gpiochip[04] 14' | xargs kill", shell=True, stderr=subprocess.PIPE)
      
# cria o objeto "sensor" com o modelo DHT11 a GPIO 14 da placa
sensor = adafruit_dht.DHT11(board.D14)
      
# adicao das variaveis auxiliares
temperatura = 20
umidade = 50
peso = 0.8
      
while True:

    sleep(2) #aguarda 2 segundos para nova leitura
      
    #verifica se a leitura do sensor e valida
    try:
        temperatura = temperatura*(1-peso) + sensor.temperature*peso
      	umidade = umidade*(1-peso) + sensor.humidity*peso
      
      	#exibe os valores lidos no terminal
      	print("Temperatura: {} C | Umidade: {} %".format(round(temperatura,2),round(umidade,2)))
    except:
      	print("Leitura invalida")
