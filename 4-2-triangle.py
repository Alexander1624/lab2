from RPi import GPIO as gpio
import time


def dectobip(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]


dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
period = int(input("период:\n"))

try:
    temp = 0
    while __name__ == '__main__':
        gpio.output(dac, dectobip(temp % 256))
        temp += 1
        time.sleep(period/512)
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
