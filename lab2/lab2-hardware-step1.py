from sense_emu import SenseHat
import time

s = SenseHat()
s.low_light = True

g = (0, 255, 0)
y = (255, 255, 0)
b = (0, 0, 255)
r = (255, 0, 0)
w = (255,255,255)
o = (0,0,0)
p = (255,105, 180)


def letter_r():
    logo = [
    o, o, o, o, o, o, o, o,
    o, r, r, r, o, o, o, o,
    o, r, o, o, r, o, o, o,
    o, r, o, o, r, o, o, o,
    o, r, r, r, o, o, o, o,
    o, r, r, o, o, o, o, o,
    o, r, o, r, o, o, o, o,
    o, r, o, o, r, o, o, o,
    ]
    return logo


def letter_f():
    logo = [
    o, o, o, o, o, o, o, o,
    o, b, b, b, b, o, o, o,
    o, b, o, o, o, o, o, o,
    o, b, o, o, o, o, o, o,
    o, b, b, b, b, o, o, o,
    o, b, o, o, o, o, o, o,
    o, b, o, o, o, o, o, o,
    o, b, o, o, o, o, o, o,
    ]
    return logo

while True:
    time.sleep(.75)
    s.set_pixels(letter_r())
    time.sleep(.75)
    s.set_pixels(letter_f())


