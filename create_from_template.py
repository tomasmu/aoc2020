import datetime
import os
import shutil
import sys

if len(sys.argv) == 1:
    #no argument given, take today's day
    day = datetime.date.today().strftime("%d")
else:
    day = sys.argv[1].zfill(2)

script_file = f"./aoc{day}.py"
example_file = f"./aoc{day}_example.txt"
input_file = f"./aoc{day}_input.txt"

if os.path.exists(script_file):
    print(f'file already exists for day {day}')
    sys.exit()

#copy template
shutil.copy('template.py', script_file)

#create if not exists
open(example_file, 'a')
open(input_file, 'a')
