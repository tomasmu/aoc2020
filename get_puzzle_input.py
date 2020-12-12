import sys
import datetime
import time

#pip install requests
import requests

#cookies.py
from cookies import aoc_cookie

#take year/day from arguments or today's date
year, month, day = datetime.date.today().strftime("%Y-%m-%d").split("-")
if len(sys.argv) >= 2:
    day = sys.argv[1].zfill(2)
if len(sys.argv) >= 3:
    year = sys.argv[2]

#todo: validate date n stuff

url = f"https://adventofcode.com/{year}/day/{int(day)}/input"

max_retries = 10
backoff_seconds = 10
current_try = 1
while current_try <= max_retries:
    print(f"{datetime.datetime.today()} * {current_try}/{max_retries} GET {url}")
    response = requests.get(url=url, cookies=aoc_cookie)
    if not response.ok:
        print(f"{datetime.datetime.today()} * GET error {response.status_code}: '{response.text.strip()}'")
    else:
        lines = response.text.strip().splitlines()
        print(f"{datetime.datetime.today()} * GET OK {response.status_code}: {len(lines)} lines")
        break

    current_try += 1
    if current_try <= max_retries:
        print(f'will retry in {backoff_seconds} seconds')
        time.sleep(backoff_seconds)
else:
    print("max attempts reached, exiting")
    sys.exit()

puzzle_input = response.text

#overwrite existing content
input_file = f"./aoc{day}_input.txt"
file = open(input_file, 'w')
file.write(puzzle_input)
print(puzzle_input)
print(f"saved {len(lines)} lines to:", input_file)
