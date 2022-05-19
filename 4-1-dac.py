from RPi import GPIO as gpio


def dectobip(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]    


def cycle():
    num = input("Введите число от 0 до 255:\n")
    if num == 'q':
        return None
    if not num.isdigit():
        print('input error')
        return cycle()
    if abs(int(num)) != int(num):
        print('input error')
        return cycle()
    if int(num) > 255:
        print('input error')
        return cycle()
    return int(num)
    


dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

try:
    while __name__ == "__main__":
        num = cycle()
        if num or num == 0:
            asked = dectobip(num)
            gpio.output(dac, asked)
            print("approx. voltage: {:.4f}".format(num / 255 * 3.3))
        else:
            break
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
