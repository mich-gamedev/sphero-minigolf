#region USER SETTINGS
# How fast it rotates per second.
ROTATE_SPEED = 720.
# How much speed it loses when running into a wall. (CURRENTLY UNUSED)
BOUNCE_DECAY = .9
# How much it slows down per second
DECEL        = 255./2.
# How many seconds between each update.
TICK_DELTA   = 1./20.
#endregion









# ---- CODE BELOW ---- #
import time
import math
import asyncio
import sys
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
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
    state = States.CHOOSE_ROT


    async def run():
        global state
        exit_flag = False
        elapsed: float = 0.0
        speed: float
        while not exit_flag:
            if keyboard.is_pressed('esc'):
                bot.set_speed(0)
                exit_flag = True
            elif state == States.CHOOSE_ROT:
                bot.set_back_led(255)
                if keyboard.is_pressed('space'):
                    state = States.CHOOSE_SPEED
                else:
                    bot.spin(ROTATE_SPEED*TICK_DELTA, TICK_DELTA)
            elif state == States.CHOOSE_SPEED:
                speed = math.cos(elapsed * math.pi * 4) * 255
                bot.set_back_led(int(speed))
                bot.set_main_led(Color(int(speed), int(speed), int(speed)))
                elapsed += TICK_DELTA
                if keyboard.is_pressed('enter'):
                    state = States.MOVE
                    elapsed = 0
            elif state == States.MOVE:
                bot.set_back_led(int(speed))
                if speed > 0:
                    bot.set_speed(int(speed))
                    speed -= DECEL * TICK_DELTA
                else:
                    state = States.CHOOSE_ROT
                    speed = 0
            await asyncio.sleep(TICK_DELTA)

    asyncio.run(run())


