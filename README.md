## Idea board:
![idea.png](https://github.com/mich-gamedev/sphero-minigolf/blob/main/idea.png?raw=true)

## How to install:
### Prerequesites
- Python (>v3.7)
- Git
### Command line
- `pip install spherov2`
- `pip install bleak`
- `pip install keyboard`
- `git clone https://github.com/mich-gamedev/sphero-minigolf.git` or `gh repo clone mich-gamedev/sphero-minigolf`

## How to run:
- `cd sphero-minigolf`
- `python sphero_proj.py toyid=SM-####` (add -c to debug, replace toyid with your toy's ID)

## Problems:
- [ ] Sphero api has no collision normal exposed, so there's no option for proper "bouncing" off walls. Current fix is to just rotate it 180 degrees, may remove bouncing with more testing.
- [ ] BleakAdapter does not disconnect if the program is terminated, so it can disable a toy until the computer is shut off.