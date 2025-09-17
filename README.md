## Idea board:
![idea.png](https://github.com/mich-gamedev/sphero-minigolf/blob/main/idea.png?raw=true)

## How to install:
### Prerequesites
- Python (>v3.7)
- Git
### Command line
- `sudo pip install spherov2`
- `sudo pip install bleak`
- `sudo pip install keyboard`
- `git clone https://github.com/mich-gamedev/sphero-minigolf.git` or `gh repo clone mich-gamedev/sphero-minigolf`

## How to run:
- `sudo python sphero_proj.py toyid=SM-#### team=#`
    - add -c to debug
    - replace `toyid=SM-####` with your toy'd ID / name
    - replace `team=#` with a number from 1-6, representing your team's color
        - 1 = `#ff0000`
        - 2 = `#ffff00`
        - 3 = `#00ff00`
        - 3 = `#00ffff`
        - 4 = `#0000ff`
        - 5 = `#ff00ff`


## How to play:
1. Sphero will start spinning, press **space** to stop it and decide the angle.
2. Sphero will start pulsing, press **enter** to decide the force of the hit and make it start moving.
3. Wait your turn.

## Problems:
- [ ] Sphero api has no collision normal exposed, so there's no option for proper "bouncing" off walls. Current fix is to just rotate it 180 degrees, may remove bouncing with more testing.
- [ ] BleakAdapter does not disconnect if the program is terminated, so it can disable a toy until the computer is shut off.
