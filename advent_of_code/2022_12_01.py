import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2022/day/1/input"

data = r.get(task_url, cookies=cookies)

# Day 01 
for i in data.text.split('\n\n'):
  res.append(i.split('\n'))

del res[-1][-1]
summed = [sum(map(int,i)) for i in res]
print(max(summed))
print(sum(sorted(summed)[::-1][:3]))
