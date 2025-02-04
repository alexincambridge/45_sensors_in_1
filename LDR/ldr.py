import RPi.GPIO as GPIO
import time

# Configurar el pin GPIO
LDR_PIN = 18  # GPIO donde está el sensor

GPIO.setmode(GPIO.BCM)


def read_light() :
    """Mide el tiempo que tarda el LDR en descargarse."""
    GPIO.setup(LDR_PIN, GPIO.OUT)
    GPIO.output(LDR_PIN, True)
    time.sleep(0.1)  # Cargar el capacitor

    GPIO.setup(LDR_PIN, GPIO.IN)  # Cambiar a entrada
    start_time = time.time()

    while GPIO.input(LDR_PIN) == GPIO.HIGH :
        pass  # Esperar a que descargue

    return time.time() - start_time  # Tiempo de descarga


try :
    while True :
        light_level = read_light()
        print(f"Nivel de luz: {light_level:.5f} segundos")

        time.sleep(1)  # Esperar antes de la siguiente medición

except KeyboardInterrupt :
    print("\nSaliendo...")
finally :
    GPIO.cleanup()
