#!/bin/python3
import time
import subprocess
from pathlib import Path

# [firefox]
# from https://adventofcode.com/2022/day/12/input or any input page
# right click > inspect accessibility properties > network > reload
# under "file", click "input" request > cookies > copy 'session' id
id = "53616c7465645f5fcd5b9a18a69a4ab874f367b422884a975cddb33dac42401df30be8e602ce986d28fe2502209d2d106254b106339e93608711d228ff22176d"
year = time.strftime("%Y")
hour = time.strftime("%H")
day = int(time.strftime("%d")) + 1
cmd = f'curl https://adventofcode.com/{year}/day/{day}/input --cookie "session={id}"'
output = subprocess.check_output(cmd, shell=True)
output = output.decode("utf-8")
with open(f"data/{day}_{year}.txt", "w") as f:
    f.write(output)
Path(f"{day}_{year}.py").touch()
