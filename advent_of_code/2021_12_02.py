import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
data = r.get("https://adventofcode.com/2021/day/2/input", cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))

test = [
  "forward 5",
  "down 5",
  "forward 8",
  "up 3",
  "down 8",
  "forward 2"
]
# part I
depth, position = 0, 0
for i in data:
  command, step = i.split(" ")
  if command.startswith("forward"):
    position += int(step)
  elif command.startswith("up"):
    depth -= int(step)
  elif command.startswith("down"):
    depth += int(step)
  print(f"{command} / {step}: {position} {depth}")
  
print(depth*position)

# part II
depth, position, aim = 0, 0, 0
for i in data: #data
  command, step = i.split(" ")
  if command.startswith("forward"):
    position += int(step)
    depth += aim*int(step)
  elif command.startswith("up"):
    aim -= int(step)
  elif command.startswith("down"):
    aim += int(step)
  print(f"{command} / {step}: {position} {depth} {aim}")

print(depth*position)