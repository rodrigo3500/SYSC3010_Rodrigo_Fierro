"""
Emulates a temperature
Current temp return a random temperature that fluctuates
"""
import random


temperature = 0


# First, the new direction of the temperature is decided.
# 20% chance it remains constant, 40% it increases, and 40% it decreases
# Once the direction is decided, it will increase/decrease by a value between 1-10 at a time
def update_temp():
    global temperature
    temp = int(random.random()*100)
    if temp < 20:
        return temperature
    elif temp < 60:
        temperature -= int(random.random()*10)
        return temperature
    else:
        temperature += int(random.random()*10)
        return temperature


