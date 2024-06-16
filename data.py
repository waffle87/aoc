#!/bin/python3
import time
import subprocess
from pathlib import Path

# [firefox]
# from https://adventofcode.com/2022/day/12/input or any input page
# right click > inspect accessibility properties > network > reload
# under "file", click "input" request > cookies > copy 'session' id
id = "53616c7465645f5f0aeeefb39c77e9a10d29c3d1b6cc63e4f846aa1c0f8fffa5034ab3c12ac0522e1f540dc394e379ad5a6a5a91874f0bbaca4eb7699a00b3c6"
year = time.strftime("%Y")
hour = time.strftime("%H")
day = int(time.strftime("%d"))
cmd = f'curl https://adventofcode.com/{year}/day/{day}/input --cookie "session={id}"'
output = subprocess.check_output(cmd, shell=True)
output = output.decode("utf-8")
with open(f"data/{day}_{year}.txt", "w") as f:
    f.write(output)
Path(f"{day}_{year}.py").touch()
