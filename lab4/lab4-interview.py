from sense_emu import SenseHat

s = SenseHat()


g = (0, 255, 0)
y = (255, 255, 0)
b = (0, 0, 255)
r = (255, 0, 0)
w = (255,255,255)
o = (0,0,0)
p = (255,105, 180)


def letter_t():
    logo = [
    g, g, g, g, g, g, g, g,
    o, o, o, g, o, o, o, o,
    o, o, o, g, o, o, o, o,
    o, o, o, g, o, o, o, o,
    o, o, o, g, o, o, o, o,
    o, o, o, g, o, o, o, o,
    o, o, o, g, o, o, o, o,
    o, o, o, g, o, o, o, o,
    ]
    return logo


def letter_a():
    logo = [
    g, g, g, g, g, g, g, g,
    g, o, o, o, o, o, o, g,
    g, o, o, o, o, o, o, g,
    g, o, o, o, o, o, o, g,
    g, g, g, g, g, g, g, g,
    g, o, o, o, o, o, o, g,
    g, o, o, o, o, o, o, g,
    g, o, o, o, o, o, o, g,
    ]
    return logo


letters = [letter_t(), letter_a()]


s.clear()  # clear the screen

count = 0  # keep track of what letter to show next

increment_by_two = 0

while True:
    for event in s.stick.get_events():


        # Check if the joystick was pressed
        if event.action == "pressed":
            increment_by_two += 1
            if increment_by_two%2==0:
                s.set_pixels(letters[count % len(letters)])
                # increment count
                count += 1





"""
change letters to TA
only change every second time you change button
"""

