import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2020/day/3/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))
test = [
"..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"
]


# Part I
def run_slope(data, dx, dy):
  run = copy(data)
  x,y = 0,0
  length = len(run)
  width = len(run[0])
  trees = 0
  while y < length-1:
    y += dy
    x = (x+dx) % width
    #print(x,y, run[y][x])
    if run[y][x] == "#":
      trees += 1
  return trees

print(run_slope(data, 3, 1))

# Part II
import numpy as np

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
result = [run_slope(data, i[0], i[1]) for i in slopes]

print(np.prod(result))