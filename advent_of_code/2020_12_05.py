import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2020/day/5/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))

test = [
"FBFBBFFRLR",
"BFFFBBFRRR",
"FFFBBBFRRR",
"BBFFBBFRLL"
]

# Part I

def get_row(ticket):
  low = 0
  high = 127
  mid = 0
  for i in range(8):
      mid = (high + low) // 2
      if ticket[i] == "B":
          low = mid + 1  # print("B", low, mid, high)
      elif ticket[i] == "F":
          high = mid     # print("F", low, mid, high)
  return  (high + low) // 2
  
def get_seat(ticket):
  low = 0
  high = 7
  mid = 0
  for i in range(3):
      mid = (high + low) // 2
      if ticket[7+i] == "R":
          low = mid + 1  # print("R", low, mid, high)
      elif ticket[7+i] == "L":
          high = mid     # print("L", low, mid, high)
  return  (high + low) // 2
  
ticket_ids = {}
for i in data:
  a = get_row(i)
  b = get_seat(i)
  ticket_ids[i] = a*8 + b 

print(sorted(ticket_ids.values())[-1])

# Part II

_prev = sorted(ticket_ids.values())[0]
for i in sorted(ticket_ids.values())[1:]:
  if i - _prev != 1:
    print(i, _prev)
  _prev = i
