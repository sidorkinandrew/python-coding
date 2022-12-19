import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2021/day/3/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))

test = [
"00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"
]

# Part 1
def transform(data, k = 0):
  _res = {i:"" for i in range(len(data[0]))}
  for i in data:
    for j in range(len(i)):
      _res[j]+=i[j]
  return _res #{i:_res[i][k:] for i in _res}
  
fmt = transform(data)

length = len(fmt[0])
gamma, epsilon = "", ""
for i in fmt:
  singles = fmt[i].count("1")
  zeroes = length - singles
  gamma += "0" if zeroes > singles else "1"
  epsilon += "1" if zeroes > singles else "0"

print(int(gamma, 2) * int(epsilon, 2))

# Part II

import copy

def most_common(data, k):
  _tmp = "".join([i[k] for i in data])
  singles = _tmp.count("1")
  zeroes = len(_tmp) - singles
  criteria = "1" if singles >= zeroes else "0"
  return [j for j in data if j[k] == criteria]
  
def least_common(data, k):
  _tmp = "".join([i[k] for i in data])
  singles = _tmp.count("1")
  zeroes = len(_tmp) - singles
  criteria = "0" if singles >= zeroes else "1"
  return [j for j in data if j[k] == criteria]
  
oxygen = copy.copy(data)
i=0
while len(oxygen)!=1:
  oxygen = most_common(oxygen, i)
  i+=1

co2scrubber = copy.copy(data)
i=0
while len(co2scrubber)!=1:
  co2scrubber = least_common(co2scrubber, i)
  i+=1

print(int(oxygen[0], 2)*int(co2scrubber[0], 2))