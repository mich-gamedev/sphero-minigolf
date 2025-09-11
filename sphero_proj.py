
#region USER SETTINGS
TOY_NAME     = ""

ROTATE_SPEED = 180.
BOUNCE_DECAY = .9
DECEL        = 255./8.
TICK_DELTA   = 1./20.
#endregion


# ---- CODE BELOW ---- #

import time
import math
import asyncio
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
from enum import Enum

# TODO: make this 1 program be able to control multiple spheros at once, ideally
toy = scanner.find_Mini(toy_name=(TOY_NAME if TOY_NAME else None))

class States(Enum):
    IDLE         = 0 # Before the game starts
    CHOOSE_ROT   = 1 # Slowly rotates, hit to choose rotation
    CHOOSE_SPEED = 2 # Slow oscillates light, hit to choose speed
    MOVE         = 3 # Performs movement

with SpheroEduAPI(toy) as bot:
    state = States.IDLE

    def set_state(s: int):
        state = s
        if s == States.IDLE:
            return
        elif s == States.CHOOSE_ROT:
            rotate()
        elif s == States.CHOOSE_SPEED:
            choose_speed()
        elif s == States.MOVE:
            move()

    async def rotate():
        bot.set_back_led(255)
        while state == States.CHOOSE_ROT:
            await bot.spin(ROTATE_SPEED*TICK_DELTA, TICK_DELTA)

    async def choose_speed():
        elapsed = 0.0
        power = 0.0
        while state == States.CHOOSE_SPEED:
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

    def on_collision(api):
        if state == States.IDLE:
            set_state(States.CHOOSE_ROT)
        if state == States.CHOOSE_ROT:
            set_state(States.CHOOSE_SPEED)
        if state == States.CHOOSE_SPEED:
            set_state(States.MOVE)
        if state == States.MOVE:
            bot.spin(180, 1)