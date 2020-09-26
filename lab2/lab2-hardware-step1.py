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