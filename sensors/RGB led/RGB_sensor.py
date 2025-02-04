# Wiring the RGB LED:
# Connect the RGB LED pins to the Raspberry Pi GPIO pins (e.g., GPIO17, GPIO27, GPIO22 in the script).
# Use appropriate current-limiting resistors for each pin.
# Connect the cathode of the LED to a ground pin on the Raspberry Pi.

import time
import random
from gpiozero import RGBLED

# Initialize RGB LED with corresponding GPIO pins
# Replace these values with the GPIO pins you've used
led = RGBLED(red=17, green=27, blue=22)


def random_color() :
    """Generate a random RGB color."""
    return random.random(), random.random(), random.random()


def main() :
    try :
        while True :
            # Generate a random color
            r, g, b = random_color()

            # Set the RGB LED to the random color
            led.color = (r, g, b)  # Values must be floats between 0 and 1

            print(f"Setting color to R: {r:.2f}, G: {g:.2f}, B: {b:.2f}")

            # Pause before changing to the next random color
            time.sleep(1)
    except KeyboardInterrupt :
        # Turn off LED when script is stopped
        led.off()
        print("\nScript terminated. RGB LED turned off.")


if __name__ == "__main__" :
    main()