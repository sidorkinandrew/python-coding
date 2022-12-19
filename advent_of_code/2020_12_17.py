import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2020/day/17/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))
test = [
".#.",
"..#",
"###"
]


#  Part I

from collections import defaultdict

def parse_data(data):
  _result = defaultdict(lambda: False)
  center = len(data) // 2
  for x, line in enumerate(data):
    for y, point in enumerate(line):
      coord = (x - center, y - center, 0)
      _result[coord] = True if "#" in point else False
  return _result
  
from itertools import product

neighbours = [c for c in product((-1, 0, +1), repeat=3)]
neighbours.pop(neighbours.index((0,0,0)))

def run_life(data, depth=4):
  for step in range(6):
    next_states = []
    for (x,y,z) in product(range(-step-depth, step+depth+1), repeat=3):
      _current = data[(x,y,z)]
      sum_neighbours = sum([data[x+dx, y+dy, z+dz] for (dx, dy, dz) in neighbours])
      if _current and sum_neighbours not in [2, 3]:
        next_states.append(((x,y,z), False))
      if not _current and sum_neighbours == 3:
        next_states.append(((x,y,z), True))
    for ((x,y,z), new_state) in next_states:
      data[(x,y,z)] = new_state
  return data
  
a = run_life(parse_data(data))
print(sum(a.values()))


#  Part II

from collections import defaultdict

def parse_data(data):
  _result = defaultdict(lambda: False)
  center = len(data) // 2
  for x, line in enumerate(data):
    for y, point in enumerate(line):
      coord = (x - center, y - center, 0, 0)
      _result[coord] = True if "#" in point else False
  return _result

neighbours = [c for c in product((-1, 0, +1), repeat=4)]
neighbours.pop(neighbours.index((0,0,0,0)))


def run_life(data, depth=4):
  for step in range(6):
    next_states = []
    for (x,y,z,w) in product(range(-step-depth, step+depth+1), repeat=4):
      _current = data[(x,y,z,w)]
      sum_neighbours = sum([data[x+dx, y+dy, z+dz, w+dw] for (dx, dy, dz, dw) in neighbours])
      if _current and sum_neighbours not in [2, 3]:
        next_states.append(((x,y,z,w), False))
      if not _current and sum_neighbours == 3:
        next_states.append(((x,y,z,w), True))
    for ((x,y,z,w), new_state) in next_states:
      data[(x,y,z,w)] = new_state
  return data


a = run_life(parse_data(data))
print(sum(a.values()))