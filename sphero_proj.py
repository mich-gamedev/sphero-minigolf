
#region USER SETTINGS
# How fast it rotates per second.
ROTATE_SPEED = 720.
# How much speed it loses when running into a wall. (CURRENTLY UNUSED)
BOUNCE_DECAY = .9
# How much it slows down per second
DECEL        = 255./8.
# How many seconds between each update.
TICK_DELTA   = 1./20.
#endregion










# ---- CODE BELOW ---- #
import math
import asyncio
import sys
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from enum import Enum
import keyboard

cli_args = sys.argv
toy_name = ""
for i in cli_args:
    if i.startswith("toyid="):
        toy_name = i.removeprefix("toyid=")

toy = scanner.find_Mini(toy_name=(toy_name if toy_name else None))

class States(Enum):
    IDLE         = 0 # Before the game starts
    CHOOSE_ROT   = 1 # Slowly rotates, hit to choose rotation
    CHOOSE_SPEED = 2 # Slowly oscillates light, hit to choose speed
    MOVE         = 3 # Performs movement

state = States.CHOOSE_ROT

with SpheroEduAPI(toy) as bot:


    def set_state(s):
        state = s
        print("new state:" + str(state))
        if s == States.IDLE:
            return
        elif s == States.CHOOSE_ROT:
            print("async running rotate")
            asyncio.run(rotate())
        elif s == States.CHOOSE_SPEED:
            asyncio.run(choose_speed())
        elif s == States.MOVE:
            asyncio.run(move())

#region STATE FUNCTIONS
    async def rotate():
        bot.set_back_led(255)
        print("state == states.CHOOSE_ROT: " + str(state == States.CHOOSE_ROT))
        print("current state: " + str(state))
        while state == States.CHOOSE_ROT:
            if keyboard.is_pressed('space'):
                set_state(States.CHOOSE_SPEED)
                break
            print("Spinning")
            bot.spin(ROTATE_SPEED*TICK_DELTA, TICK_DELTA)
            await asyncio.sleep(TICK_DELTA)

    async def choose_speed():
        elapsed = 0.0
        power = 0.0
        while state == States.CHOOSE_SPEED:
            if keyboard.is_pressed('enter'):
                set_state(States.MOVE)
                break
            power = math.cos(elapsed * math.pi / 2) * 255
            bot.set_back_led(power)
            elapsed += TICK_DELTA
            await asyncio.sleep(TICK_DELTA)
    
    async def move():
        bot.set_back_led(0)
        speed = 255.0
        while state == States.MOVE:
            bot.set_speed(speed)
            speed -= DECEL * TICK_DELTA
            await asyncio.sleep(TICK_DELTA)
            if speed <= 0:
                set_state(States.CHOOSE_ROT)
#endregion
    set_state(States.CHOOSE_ROT)