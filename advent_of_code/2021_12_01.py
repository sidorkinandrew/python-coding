import pandas as pd
import numpy as np

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}

task_url = "https://adventofcode.com/2021/day/1/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))


# Part I
df1 = pd.DataFrame(list(map(int, data))).diff()
df1[df1 > 0].dropna().count()[0]

# Part II

test = [
  199,
  200,
  208,
  210,
  200,
  207,
  240,
  269,
  260,
  263
]

data = list(map(int, data))
def get_triplets(alist):
  _res = [sum([alist[i], alist[i+1], alist[i+2]]) for i in range(len(alist)-2)]
  #_res.append(alist[-1]+alist[-2])
  return _res


triplets = get_triplets(data)
df1 = pd.DataFrame(triplets).diff()

df1[df1 > 0].dropna().count()[0]

