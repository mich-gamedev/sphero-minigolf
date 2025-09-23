## Idea board:
![idea.png](https://github.com/mich-gamedev/sphero-minigolf/blob/main/idea.png?raw=true)

## How to install:
> [!NOTE]
> On windows 10, remove `sudo` from commands and instead run your CLI with admin permissions.
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
        - if empty, connects to first one found (usually the closest)
    - replace `team=#` with a number from 1-6, representing your team's color
        - 1 = `#ff0000` :aries: (default)
        - 2 = `#ffff00` :leo:
        - 3 = `#00ff00` :libra:
        - 4 = `#00ffff` :ophiuchus:
        - 5 = `#0000ff` :sagittarius:
        - 6 = `#ff00ff` :pisces:


## How to play:
1. Sphero will start spinning, press `space` to stop it and decide the angle.
2. Sphero will start pulsing, press `enter` to decide the force of the hit and make it start moving.
3. Wait your turn.

## Problems:
- [x] Sphero api has no collision normal exposed, so there's no option for proper "bouncing" off walls. Decided to remove bouncing.
- [x] BleakAdapter does not disconnect if the program is terminated, so it can disable a toy until the computer is shut off. Added an exit flag via pressing `esc` to fix this.
