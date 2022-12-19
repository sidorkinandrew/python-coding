import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2021/day/5/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))
test = [
"0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2"
]


# Part I

import numpy as np

def parse_data(data):
  _res = []
  max_x, max_y = 0, 0
  for i in data:
    x1,y1,x2,y2 = map(int,i.replace(" -> ", ",").split(","))
    max_x, max_y = max([max_x, x1, x2]), max([max_y, y1, y2])
    _res.append(
        {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}
    )
  vmap = [[0 for i in range(max_x+50)] for j in range(max_y+50)]
  return _res, vmap

def fill_vmap(data, vmap, diagonals = False):
  for vector in data:
    if vector['x1'] == vector['x2']:
      vector['y1'], vector['y2'] = sorted([vector['y1'], vector['y2']])
      for j in range(vector['y1'], vector['y2']+1):
        vmap[vector['x1']][j] += 1
    elif vector['y1'] == vector['y2']:
      vector['x1'], vector['x2'] = sorted([vector['x1'], vector['x2']])
      for i in range(vector['x1'], vector['x2']+1):
        vmap[i][vector['y1']] += 1
    if diagonals:
      _before = get_crc(vmap)
      y_move, y_step = vector['y1'], 1 if vector['y1'] < vector['y2'] else -1 
      x_move, x_step = vector['x1'], 1 if vector['x1'] < vector['x2'] else -1 
      while x_move != vector['x2'] and y_move != vector['y2']:
        vmap[x_move][y_move] += 1
        x_move += x_step
        y_move += y_step
      vmap[x_move][y_move] += 1
  return vmap

def get_crc(vmap):
  return np.sum(np.sum(np.array(vmap),0))

def print_vmap(vmap):
  print("\n".join(["".join(map(str,i)) for i in list(map(list, zip(*vmap)))]).replace("0","."))
  


_res, vmap = parse_data(data)
vmap = fill_vmap(_res, vmap, diagonals=False)
a = np.array(np.concatenate(vmap).flat)
print(len(a[np.where(a>1)]))

# Part II

_res, vmap = parse_data(data)
vmap = fill_vmap(_res, vmap, diagonals=True)
a = np.array(np.concatenate(vmap).flat)
print(len(a[np.where(a>1)]))