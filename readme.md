## Advent of Code

This repository contains Python solutions for [AoC](https://adventofcode.com) for years 2020 - present.

Run from the top level by specifying the day. Most recent years set the input in the code itself:
```
$ python 2025/1_2025.py
1078
6412
```

The [`data.py`](data.py) script can be used to automatically fetch the daily input. This script depends on `python-dotenv` to read your cookie from a `.env` file:
```sh
# .env

SESSION_ID=371fe5f3a0bb53914c8f8e97adfe06a7
```

In Firefox (and probably similarly in mostly other browsers), this cookie can be found by...

1. After signing in, open any input page (eg. [adventofcode.com/2025/day/1/input](https://adventofcode.com/2025/day/1/input))
2. Right click -> Accessibility Properties -> Network -> Reload
3. Click on one of the network requests and under "Cookies" tab on right, copy `session` cookie

Running this script will fetch the input file (timezone agnostically) and open a Python file and the data file in `$EDITOR`.
