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


def trinket_logo():
    logo = [
    o, o, o, o, o, o, o, o,
    o, y, y, y, b, g, o, o,
    y, y, y, y, y, b, g, o,
    y, y, y, y, y, b, g, o,
    y, y, y, y, y, b, g, o,
    y, y, y, y, y, b, g, o,
    o, y, y, y, b, g, o, o,
    o, o, o, o, o, o, o, o,
    ]
    return logo


def raspi_logo():
    logo = [
    o, g, g, o, o, g, g, o,
    o, o, g, g, g, g, o, o,
    o, o, r, r, r, r, o, o,
    o, r, r, r, r, r, r, o,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    o, r, r, r, r, r, r, o,
    o, o, r, r, r, r, o, o,
    ]
    return logo


def plus():
    logo = [
    o, o, o, o, o, o, o, o,
    o, o, o, w, w, o, o, o,
    o, o, o, w, w, o, o, o,
    o, w, w, w, w, w, w, o,
    o, w, w, w, w, w, w, o,
    o, o, o, w, w, o, o, o,
    o, o, o, w, w, o, o, o,
    o, o, o, o, o, o, o, o,
    ]
    return logo


def equals():
    logo = [
    o, o, o, o, o, o, o, o,
    o, w, w, w, w, w, w, o,
    o, w, w, w, w, w, w, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, w, w, w, w, w, w, o,
    o, w, w, w, w, w, w, o,
    o, o, o, o, o, o, o, o,
    ]
    return logo


def heart():
    logo = [
    o, o, o, o, o, o, o, o,
    o, p, p, o, p, p, o, o,
    p, p, p, p, p, p, p, o,
    p, p, p, p, p, p, p, o,
    o, p, p, p, p, p, o, o,
    o, o, p, p, p, o, o, o,
    o, o, o, p, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ]
    return logo


images = [trinket_logo, trinket_logo, plus, raspi_logo, raspi_logo, equals, heart, heart]
count = 0

while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1

