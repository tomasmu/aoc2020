import sys
import datetime
import time

#pip install requests
import requests

#cookies.py
from cookies import aoc_cookie

#take year/day from argument or today's date
if len(sys.argv) >= 1:
    day = datetime.date.today().strftime("%d")
    year = datetime.date.today().strftime("%Y")
if len(sys.argv) >= 2:
    day = sys.argv[1].zfill(2)
if len(sys.argv) == 3:
    year = sys.argv[2]

url = f"https://adventofcode.com/{year}/day/{int(day)}/input"

max_retries = 10
current_try = 1
while current_try <= 5:
    print(f"{datetime.datetime.today()} * {current_try}/{max_retries} GET {url}")
    response = requests.get(url=url, cookies=aoc_cookie)
    if not response.ok:
        print(f"{datetime.datetime.today()} * GET error {response.status_code}:\n'{response.text.strip()}'")
        pass
    else:
        first = "\n".join(response.text.strip().splitlines()[0:10])
        print(f"{datetime.datetime.today()} * GET OK {response.status_code}:\n{first}\n...")
        break
    time.sleep(10)
    current_try += 1
else:
    print("max attempts reached, exiting")
    sys.exit()

puzzle_input = response.text
input_file = f"./aoc{day}_input.txt"

#overwrite existing content
file = open(input_file, 'w')
file.write(puzzle_input)
