import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2021/day/6/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))
test = [
"3,4,3,1,2"
]


# Part I

def parse_data(data):
  return list(map(int, data[0].split(",")))
  
def breed_fish(data, period = 80):
  data = np.array(data)
  for i in range(period):
    data = data-1
    data = np.append(data, [8] * len(data[data==-1]))
    data[data==-1] = 6
  return data


import numpy as np

result = breed_fish(parse_data(data), period=80)

print(len(result))

# Part II

from collections import defaultdict

def heavy_fish(data, period=256):
  fish = defaultdict(int)
  fish = {i:0 for i in range(9)}
  for k in data:  # count fish
    fish[k] += 1
  for _ in range(period): # move left (decreases lifespan by 1)
    fish[0], fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7], fish[8] = \
      fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7], fish[8], fish[0]
    fish[6] += fish[8]  # 0 ([8] after the move above) becomes a 6
  return fish

result = heavy_fish(parse_data(data))

print(sum(result.values()))

