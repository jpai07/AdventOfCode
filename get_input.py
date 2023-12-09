import os, subprocess
import argparse
from bs4 import BeautifulSoup
import requests

MAIN = "https://adventofcode.com"
YEAR = "2023"
# In order to collect input file, need to be authentified
# For this we will need to fill a SESSION argument 
# 1. Log in/ create account to "https://adventofcode.com"
# 2. Go to "https://adventofcode.com/2023/day/1/input"
# 3. On chrome, inspect page and go to Application>Cookies section
# 4. Copy and paste the 'session' Value that you see just below 
SESSION = "***** FILL SESSION HERE ******"

parser = argparse.ArgumentParser(description="Collect input for Advent of Code")
parser.add_argument("-d",type=int,required=True,help="Day to collect")
args = parser.parse_args()

DAY = args.d
URL = f"{MAIN}/{YEAR}/day/{DAY}"
DEST = f"./day_{DAY}/"

assert not os.path.isdir(DEST), "Destination directory already exists"
os.mkdir(DEST)

########################### GET INSTRUCTIONS FILE ###########################
LINE_SIZE = 120
response = requests.get(URL)
soup = BeautifulSoup(response.text, features="lxml")
instructions = soup.find("article",attrs={"class":"day-desc"}).text
with open(f"{DEST}/instructions.txt","w") as file:
    for line in range(len(instructions)%LINE_SIZE):
        file.write(
            f"{instructions[line*LINE_SIZE:(line+1)*LINE_SIZE]} \n"
            )
    file.close()

########################### GET INPUT FILE ###########################
with open(f"{DEST}/input.txt","w") as file:
    output = subprocess.check_output(
        f'curl {URL}/input --cookie "session={SESSION}"',
        shell=True
        )
    output = output.decode("utf-8")
    file.write(output)
    file.close()
