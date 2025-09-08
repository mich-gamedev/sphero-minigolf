import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
from enum import Enum

toy = scanner.find_toy()

#region const settings
FORCE_LIGHT_RANGE = {"min": 0, "max": 255}
FORCE_SPEED_RANGE = {"min": 0, "max": 255}

ROTATE_SPEED      = 180.

BOUNCE_DECAY      = .9

DECEL             = 255./8.

TICK_DELTA        = 1./20.
#endregion

class States(Enum):
    IDLE         = 0
    CHOOSE_ROT   = 1
    CHOOSE_SPEED = 2
    MOVE         = 3

state = States.IDLE


with SpheroEduAPI(toy) as bot:
    def set_state(s):
        state = s
        if s == States.IDLE:
            return
        elif s == States.CHOOSE_ROT:
            
    
    async def rotate():
        while state == States.CHOOSE_ROT:
            await bot.spin(ROTATE_SPEED*TICK_DELTA, TICK_DELTA)

    
    def on_collision(api):
        if state == States.CHOOSE_ROT:
            set_state(States.CHOOSE_SPEED)
        if state == States.CHOOSE_SPEED:
            set_state(States.MOVE)