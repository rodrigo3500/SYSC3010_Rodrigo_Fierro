from sense_emu import SenseHat

s = SenseHat()


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


letters = [letter_r(), letter_f()]


s.clear()  # clear the screen

count = 0  # keep track of what letter to show next

while True:
    for event in s.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":

            s.set_pixels(letters[count % len(letters)])

            # increment count
            count += 1




