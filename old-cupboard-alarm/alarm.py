#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

PHOTO_PIN=21
BUZZER_PIN=14


def setup():
    GPIO.setup(PHOTO_PIN, GPIO.IN)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

def cleanup():
    GPIO.cleanup(PHOTO_PIN)
    GPIO.cleanup(BUZZER_PIN)

def make_noise():
    print("Making noise.")
    runs = 100
    GPIO.output(BUZZER_PIN, True)
    time.sleep(.75)
    GPIO.output(BUZZER_PIN, False)

#    while runs > 0:
#        GPIO.output(BUZZER_PIN, not (runs % 2))
#        runs -= 1


def main():
    setup()
    make_noise()
    counter=0
    while 1:
        time.sleep(0.125)
        counter += 1
        is_dark = GPIO.input(PHOTO_PIN)
        if not is_dark:
            make_noise()
        print(f"{counter}: value is {is_dark}")
    cleanup()

if __name__ == '__main__':
    try:
        main()
    finally:
        print("clean up")
        cleanup()
