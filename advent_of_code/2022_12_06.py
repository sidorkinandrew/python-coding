import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2022/day/6/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]


# Day 06
test = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
    
test = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
]

from collections import deque

def find_marker(queue, buffer_lenght=14):
  buffer = deque(queue[:buffer_lenght-1])
  count = buffer_lenght-1
  for i in list(queue[buffer_lenght-1:]):
    count += 1
    buffer.append(i)
    if len(set(buffer)) == buffer_lenght:
      return count, buffer
    buffer.popleft()


# Day 06 Part I
find_marker(data[0], buffer_lenght=4)

# Day 06 Part II
find_marker(data[0], buffer_lenght=14)

