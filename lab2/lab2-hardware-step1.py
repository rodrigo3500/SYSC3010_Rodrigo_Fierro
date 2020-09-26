<<<<<<< HEAD
from sense_emu import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def trinket_logo():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus():
    W = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

images = [trinket_logo, trinket_logo, plus, raspi_logo, raspi_logo, equals, heart, heart]
count = 0


def r():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    O, W, O, O, W, O, O, O,
    O, W, O, O, W, O, O, O,
    O, W, W, W, O, O, O, O,
    O, W, W, O, O, O, O, O,
    O, W, O, W, O, O, O, O,
    O, W, O, O, W, O, O, O,
    ]
    return logo

def f():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, W, W, W, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    ]
    return logo

initials = [r,f]

while True:
    for event in s.stick.get_events():
        s.set_pixels(initials[count % len(initials)]())
        time.sleep(.75)
        count += 1
    
=======
from sense_emu import SenseHat
import time

s = SenseHat()

s.show_message("Astro Pi is awesome!!")

''' 
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
pink = (255, 105, 180)
'''


''' 
def r():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, O, O, O, O,
        O, W, O, O, W, O, O, O,
        O, W, O, O, W, O, O, O,
        O, W, W, W, O, O, O, O,
        O, W, W, O, O, O, O, O,
        O, W, O, W, O, O, O, O,
        O, W, O, O, W, O, O, O,
    ]
    return logo


def f():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, O, O, O,
        O, W, O, O, O, O, O, O,
        O, W, O, O, O, O, O, O,
        O, W, W, W, W, O, O, O,
        O, W, O, O, O, O, O, O,
        O, W, O, O, O, O, O, O,
        O, W, O, O, O, O, O, O,
    ]
    return logo


initials = [r, f]

while True:
    for event in s.stick.get_events():
        s.set_pixels(initials[count % len(initials)]())
        time.sleep(.75)
        count += 1
'''
>>>>>>> 8a5520e80051f57ffb1aa50c226b5ff25f08e971
