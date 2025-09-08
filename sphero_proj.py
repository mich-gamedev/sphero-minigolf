state = "waiting_turn"

colors = [0, 64, 128, 128 + 64, 255]
rotate_speed = 90

async def start_program():
    # Write code here
    return

def set_state(s):
    state = s
    if s == "waiting_turn":
        wait_turn()
    elif s == "rotate":
        rotate()
    
    

async def wait_turn():
    idx = 0
    while state != "waiting_turn":
        idx += 1
        if idx == colors.length:
            idx = 0
        set_back_led(colors[idx])
        await delay(.2)

async def rotate():
    while state != "rotate":
        await spin(rotate_speed, 1.)




async def on_collision():
    if state == "waiting_turn":
        set_state("rotate")
    elif state == "rotate":
        set_state("move")