import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2020/day/8/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))
test = [
"nop +0",
"acc +1",
"jmp +4",
"acc +3",
"jmp -3",
"acc -99",
"acc +1",
"jmp -4",
"acc +6"
]

# Part I

def run_loop(data):
  _exec = {}
  acc = 0
  i = 0
  while True:
    print(data[i])
    if data[i].startswith("nop"):
      i += 1
      _exec[i] = 1
      continue
    elif data[i].startswith("acc"):
      acc += int(data[i].split(" ")[1])
      _exec[i] = 1
      i += 1
      continue
    elif data[i].startswith("jmp"):
      i = i + int(data[i].split(" ")[1])
      if i in _exec.keys():
        return acc
      else:
        _exec[i] = 1


print(run_loop(data))

# Part II (not done)
