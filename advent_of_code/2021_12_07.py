import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2021/day/7/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))
test = [
"16,1,2,0,4,2,7,1,2,14"
]

#  Part I

import numpy as np
def parse_data(data):
  return list(map(int, data.split(",")))

def move_crabs(data):
    range_min, range_max = min(data), max(data)
    min_fuel = range_max**3

    for i in range(range_min, range_max + 1):
        fuels = np.abs(np.array(data) - i)
        total_fuels = sum(fuels)
        if total_fuels < min_fuel:
            min_fuel = total_fuels

    return min_fuel

print(move_crabs(parse_data(data[0]))

#  Part II


def move_crabs(data):
    range_min, range_max = min(data), max(data)
    min_fuel = range_max**3

    for i in range(range_min, range_max + 1):
        fuels = np.abs(np.array(data) - i)
        fuels = fuels * (fuels + 1) // 2
        total_fuels = sum(fuels)
        if total_fuels < min_fuel:
            min_fuel = total_fuels

    return min_fuel
    
    
print(move_crabs(parse_data(data[0]))
