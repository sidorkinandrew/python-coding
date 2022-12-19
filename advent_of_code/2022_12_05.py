import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2022/day/5/input"

data = r.get(task_url, cookies=cookies)

# Day 05 Part I / II

data = data.text.split("\n\n")

containers, instructions = data[0].split('\n'), data[1].split('\n')[:-1]

# containers = [
#     'ZN',
#     'MCD',
#     'P'
# ]

# instructions = [
#     'move 1 from 2 to 1',
#     'move 3 from 1 to 3',
#     'move 2 from 2 to 1',
#     'move 1 from 1 to 2'
# ]

for i, arow in enumerate(containers[:-1]):
  containers[i] = arow.replace("    "," [!]").split(" ")

containers[-1] = containers[-1].strip().replace('   ',' ').split(' ')
containers = list(map(list,zip(*containers)))

for i, arow in enumerate(containers):
  containers[i] = list(arow)[::-1]
  while '[!]' in containers[i]:
    containers[i].remove('[!]')
  containers[i] = "".join(containers[i]).replace('[','').replace(']','')[1:]
  
containers.insert(0,'dummy data')
print(containers)

def move_containers(data, _move, _from, _to, reverse_buffer = True):
  buffer = data[_from][-_move:]#[::-1]
  if reverse_buffer:
    buffer = buffer[::-1]
  # print(_move, _from, _to)
  # print('BEFORE:', data[_from], data[_to], _move, buffer)
  data[_from] = data[_from][:-_move]
  data[_to] += buffer
  # print('AFTER', data[_from], data[_to])

def process_instructions(data, moves):
  for arow in moves:  #  'move 14 from 4 to 6',
    print(arow)
    _move, _from, _to = map(int, arow.replace('move ','').replace('from ','').replace('to ','').split(' '))
    move_containers(data, _move, _from, _to, False)
    print(data)
    # input()

process_instructions(containers, instructions)

print(containers)
''.join([i[-1] for i in containers[1:]])
