#######################################################################################################
# No terminal instale a lib pigpio_dht
# sudo apt update
# sudo apt install python3-pip -y
# pip3 install pigpio-dht --break-system-packages
# 
# Garante que o daemon esta rodando
# sudo systemctl start pigpiod
# sudo systemctl status pigpiod

import pigpio
import pigpio_dht
from time import sleep

GPIO = 4  # GPIO4 físico 7

pi = pigpio.pi()

if not pi.connected:
    print("Erro: pigpio não conectou")
    exit()

sensor = pigpio_dht.DHT11(GPIO, pi=pi)

while True:
    try:
        result = sensor.read()

        if result["valid"]:
            print(
                f"Temperatura: {result['temp_c']} C | "
                f"Umidade: {result['humidity']} %"
            )
        else:
            print("Leitura inválida")

    except Exception as e:
        print("Erro:", e)

    sleep(3)
