import yaml
import os, subprocess
import argparse
import shutil

from bs4 import BeautifulSoup
import requests

########### LOAD CONFIG ###########
if not os.path.exists('config.yml'):
    raise FileNotFoundError('Missing config file "config.yml" with infos for url/year/session')
try:
    with open('config.yml') as file:
        config = yaml.safe_load(file)
except:
    raise ImportError('Unable to load "config.yaml" file, please check for correct format of the file')
for key in ['url','year','session']:
    if key not in config:
        raise KeyError(f'Missing key in "config.yml" : {key}')
    if not isinstance(key, str):
        raise TypeError(f'Key "{key}" in "config.yml" not of type str')
url = config['url']
year = config['year']
session = config['session']

########### COLLECT ARGUMENTS ###########
try:
    parser = argparse.ArgumentParser(description='Collect input for Advent of Code')
    parser.add_argument('-d',type=str,required=True,help='Day to collect')
    args = parser.parse_args()
except:
    raise KeyError('Missing entry for day (-d)')

########### CREATE DIRECTORY ###########
dest = os.path.join(year,f'day_{args.d}')
if os.path.isdir(dest):
    raise FileExistsError(f'Destination directory "{dest}" already exists')
os.makedirs(dest)

########### PARSE DAY PROBLEM ###########
line_size = 120
day_url = f'{url}/{year}/day/{args.d}'
response = requests.get(day_url)
soup = BeautifulSoup(response.text)

########### COLLECT INSTRUCTIONS AND TEST INPUT ###########
instructions = soup.find('article',attrs={'class':'day-desc'})

instructions_path = os.path.join(dest, 'instructions.txt')
with open(instructions_path,'w') as file:
    for line in range(len(instructions.text)%line_size):
        file.write(f"{instructions.text[line*line_size:(line+1)*line_size]} \n")
    file.close()
    
test_input_path = os.path.join(dest, 'test_input.txt')
with open(test_input_path,'w') as file:
    file.write(instructions.find('pre').text)
    file.close()

########### COLLECT REAL INPUT ###########
real_input_path = os.path.join(dest, 'real_input.txt')
with open(real_input_path,"w") as file:
    output = subprocess.check_output(f'curl {day_url}/input --cookie "session={session}"', shell=True)
    output = output.decode('utf-8')
    file.write(output)
    file.close()

########### CLONE SOLUTION TEMPLATE ###########
template_solution = os.path.join('templates','solution.py')
shutil.copyfile(template_solution, os.path.join(dest,'solution.py'))
