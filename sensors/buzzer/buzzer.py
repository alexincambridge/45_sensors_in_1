import RPi.GPIO as GPIO
import time

# Define GPIO pins for buzzers
BUZZER_1 = 17
BUZZER_2 = 27

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_1, GPIO.OUT)
GPIO.setup(BUZZER_2, GPIO.OUT)

# Create PWM objects (Control frequency)
buzzer1 = GPIO.PWM(BUZZER_1, 1000)  # 1kHz
buzzer2 = GPIO.PWM(BUZZER_2, 500)   # 500Hz

def beep_buzzer(buzzer, duration=0.5):
    """Turns the buzzer on and off"""
    buzzer.start(50)  # 50% duty cycle
    time.sleep(duration)
    buzzer.stop()

try:
    while True:
        print("Buzzer 1 (GPIO 17) Beep")
        beep_buzzer(buzzer1, 0.5)

        time.sleep(1)  # Pause between beeps

        print("Buzzer 2 (GPIO 27) Beep")
        beep_buzzer(buzzer2, 0.5)

        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    buzzer1.stop()
    buzzer2.stop()
    GPIO.cleanup()