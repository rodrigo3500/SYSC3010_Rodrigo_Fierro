'''
Using the temperature emulator used from the imported temperature_emu
The user can press any arrow key button on the sense hat to display the latest temperature reading
'''
import temperature_emu
from sense_emu import SenseHat

s = SenseHat()
s.clear()  # clear the screen


while True:
    for event in s.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":

            s.show_message(str(temperature_emu.update_temp()))












