# Advent of Code Template and Solutions

## About

This repo is my personal setup to participate in the [Advent of Code](https://adventofcode.com/)
programming challenges held every year December 1-25. It contains a solver template `template.py`
and a challenge preparation script `prepare.py`. I also published some of my challenge solutions.
They are all written in Python.


## Challenge preparation script

### Running the script

To prepare a challenge run

    (env) python prepare.py DAY [YEAR]  [--skip-input-download, -s]

where `YEAR` defaults to the current year if not provided.

e.g.

    (env) python prepare.py 7 2018

for challenge day 7 of 2018 or 

    $ (env) python prepare.py 16

for Challenge 16 of the current year,

### Notes

This will perform the following tasks:
1. Create a subfolder structure, e.g. `2018/07`
2. Copy the template `template.py` file to `solver.py`.
3. Create an empty `sample.txt` file which you will need to paste the sample input into. 
4. Download the challenge input to `input.txt`.

If any of the directories or files already exist they will _not_ get overwritten.

The last step will _not_ work if the challenge is not yet online.
You can add the `--skip-input-download` (or simply `-s`) argument to skip that step.

Also, for the last step to work you need to be logged into the
[Advent of Code](https://adventofcode.com/) website in order for the script to be
able to download the intput file using your browser cookies.

### Setup

To run the script you will need to install the following modules (ideally into a
virtual environment):

    (env) pip install requests browser-cookie3
