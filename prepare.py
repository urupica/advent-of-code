#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path
import shutil

import browser_cookie3
import requests


parser = ArgumentParser()
parser.add_argument("year", choices=list(map(str, range(2015, 2023 + 1))))
parser.add_argument("day", choices=list(map(str, range(1, 25 + 1))))

args = parser.parse_args()
year = args.year
day = args.day

# create directory
path = Path(f"{year}/{day.zfill(2)}")
path.mkdir(parents=True, exist_ok=True)

# copy template
solver_path = path / "solver.py"
if not solver_path.is_file():
    shutil.copyfile("template.py", solver_path)

# create empty sample input file
sample_path = path / "sample.txt"
if not sample_path.is_file():
    open(sample_path, 'w').close()

# download input file
input_path = path / "input.txt"
if not Path(input_path).is_file():
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = browser_cookie3.chrome()
    response = requests.get(url, cookies=cookies)
    with open(input_path, "wb") as f:
        f.write(response.content)
