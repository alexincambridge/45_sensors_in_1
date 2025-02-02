
# Wiring Diagram
# Mercury Tilt Sensor
#
# One pin → GPIO 38 (Input)
# Other pin → GND
# (Optional: Use a 10K pull-down resistor between GPIO 38 and GND to prevent floating values)
# LED
#
# Positive (Anode) → GPIO 40 (Output)
# Negative (Cathode) → GND
# (Use a 330Ω resistor in series with the LED for current limiting)

import RPi.GPIO as GPIO
import time

# Pin configuration
SENSOR_PIN = 38  # Mercury switch input
LED_PIN = 40  # LED output

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Enable internal pull-down resistor

try:
    while True:
        sensor_state = GPIO.input(SENSOR_PIN)

        # Print state only when it changes (debouncing)
        if sensor_state:
            print("Tilt detected!")
            GPIO.output(LED_PIN, True)
        else:
            print("No tilt.")
            GPIO.output(LED_PIN, False)

        time.sleep(0.1)  # Small delay to avoid excessive CPU usage

except KeyboardInterrupt:
    print("\nExiting gracefully...")
finally:
    GPIO.cleanup()