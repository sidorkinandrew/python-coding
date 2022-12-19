import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2020/day/6/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))
test = [
"abc",
"",
"a",
"b",
"c",
"",
"ab",
"ac",
"",
"a",
"a",
"a",
"a",
"",
"b",
]


# Part I

def parse_list(data, sep=""):
  _result = []
  _current = []
  for i in data:
    if i == "":
      _result.append(sep.join(_current))
      _current = []
      continue
    _current.append(i)
  _result.append(sep.join(_current))
  return _result
  
print(sum([len(set(i)) for i in parse_list(data)]))

# Part II

count = 0
for i in parse_list(data, ";"):
  sets = list(map(set,i.split(";")))
  count += len(sets[0].intersection(*sets[1:]))
  
print(count)