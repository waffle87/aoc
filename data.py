import os
import subprocess
import time
from pathlib import Path

import dotenv

dotenv.load_dotenv()
id = os.getenv("SESSION_ID")
year = time.strftime("%Y")
hour = time.strftime("%H")
day = int(time.strftime("%d"))
cmd = f'curl https://adventofcode.com/{year}/day/{day}/input --cookie "session={id}"'
output = subprocess.check_output(cmd, shell=True)
output = output.decode("utf-8")
with open(f"data/{day}_{year}.txt", "w") as f:
    f.write(output)
Path(f"{day}_{year}.py").touch()
