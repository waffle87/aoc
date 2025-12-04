import subprocess
from datetime import datetime
from os import getenv
from pathlib import Path
from zoneinfo import ZoneInfo

import dotenv

dotenv.load_dotenv()

editor = getenv("EDITOR", "vi")
session_id = getenv("SESSION_ID")
if not session_id:
    raise ValueError("SESSION_ID not found")

aoc_tz = ZoneInfo("America/New_York")
aoc_time = datetime.now(aoc_tz)
year = aoc_time.year
day = aoc_time.day

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
data_file = data_dir / f"{day}_{year}.txt"

cmd = [
    "curl",
    f"https://adventofcode.com/{year}/day/{day}/input",
    "--cookie",
    f"session={session_id}",
    "-f",
    "-s",
]

try:
    output = subprocess.check_output(cmd, stderr=subprocess.PIPE)
    output = output.decode("utf-8")
    if "log in" in output:
        raise ValueError("failed to fetch input; check SESSION_ID")
    with open(data_file, "w") as f:
        f.write(output)

except subprocess.CalledProcessError as e:
    print(f"error fetching input: {e.stderr.decode('utf-8')}")
    exit(1)

source_file = Path(f"{day}_{year}.py")
if not source_file.exists():
    source_file.touch()

subprocess.run([editor, str(source_file), str(data_file)])
