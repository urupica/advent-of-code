#!/usr/bin/env python

from argparse import ArgumentParser
from datetime import date
from pathlib import Path
import shutil

import browser_cookie3
import requests

current_year = date.today().year
parser = ArgumentParser()
parser.add_argument("day", choices=list(map(str, range(1, 25 + 1))))
parser.add_argument("year", nargs="?", choices=list(map(str, range(2015, current_year + 1))), default=str(current_year))
parser.add_argument("-s", "--skip_input_download", action="store_true")
args = parser.parse_args()

# create directory
path = Path(f"{args.year}/{args.day.zfill(2)}")
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
if not args.skip_input_download:
    input_path = path / "input.txt"
    if not Path(input_path).is_file():
        url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
        # you can also use another browser like .firefox(). Or try load the cookies of all browsers using .load()
        cookies = browser_cookie3.chrome(domain_name="adventofcode.com")
        response = requests.get(url, cookies=cookies)
        with open(input_path, "wb") as f:
            f.write(response.content)
