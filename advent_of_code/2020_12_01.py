import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2020/day/1/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]
data = list(map(int, data))

print(len(data))

test = [
1721,
979,
366,
299,
675,
1456
]

# Part I
from itertools import combinations

_result = list(filter(lambda x: x[0]+x[1]==2020, list(combinations(data, 2))))[0]
print(_result[0] * _result[1])


# Part II
_result = list(filter(lambda x: x[0]+x[1]+x[2]==2020, list(combinations(data, 3))))[0]
print(_result[0] * _result[1] * _result[2])
