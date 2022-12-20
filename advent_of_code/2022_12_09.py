import requests as r
from copy import copy
import numpy as np
import pandas as pd

cookies = {
"_ga": "GA1.2.xx.xx",
"_gid": "GA1.2.xx.xx",
"session": "xx",
"_gat": "1"
}
task_url = "https://adventofcode.com/2022/day/9/input"
data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

test  = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
test = test.split('\n')

bridge = """......
......
......
......
H....."""
bridge = [list(i) for i in bridge.split('\n')]

test_part_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
test_part_2 = test_part_2.split('\n')

from dataclasses import astuple, dataclass

@dataclass
class Point():
  x: int = 0
  y: int = 0

  def __add__(self, other):
      x1, y1 = self
      x2, y2 = other
      return Point(x1+x2, y1+y2)

  def __sub__(self, other):
      x1, y1 = self
      x2, y2 = other
      return Point(x1-x2, y1-y2)

  def __iter__(self):
      return iter(astuple(self))   

directions = {'R': Point(0, 1), 'L': Point(0, -1), 'U': Point(-1, 0), 'D': Point(1, 0)}

class Rope():
  def __init__(self, bridge=None, bridge_len=10, tail_length=10):
    self.head = Point(0,0)
    self.tails = [Point(0,0) for i in range(tail_length)]
    self.tail_length = tail_length
    self.last_tail_visited = [Point(0,0)]
    self.bridge = [list('.'*bridge_len) for i in range(bridge_len)] if bridge is None else bridge
    self.debug = False

  def move_head(self, direction: Point):
    if self.debug:
      print('moving head to', self.head + direction, 'by', direction)
    self.head += direction
    self.tails[0].x, self.tails[0].y  = self.head.x, self.head.y

  def tail_step_to(self, tail_idx, to: Point):
      if tail_idx == self.tail_length-1 and self.tails[tail_idx] + to not in self.last_tail_visited:
        if self.debug:
          print(f'moving tail {tail_idx}: adding', self.tails[tail_idx] + to,'to the last tail visited list')
        self.last_tail_visited.append(self.tails[tail_idx] + to)
      self.tails[tail_idx] += to

  def move_tail(self, tail_idx):
    if self.debug:
      print(f'moving {tail_idx} tail to', self.tails[tail_idx-1])
    
    x,y = self.tails[tail_idx-1].x, self.tails[tail_idx-1].y
    tail_x, tail_y = self.tails[tail_idx].x, self.tails[tail_idx].y
    if tail_x == x and abs(y-tail_y)>1:
      self.tail_step_to(tail_idx, Point(0, np.sign(y - tail_y)))
    elif tail_y == y and abs(x-tail_x)>1:
      self.tail_step_to(tail_idx, Point(np.sign(x - tail_x), 0))
    elif abs(x-tail_x)>=2 or abs(y-tail_y)>=2:
      self.tail_step_to(tail_idx, Point(np.sign(x - tail_x), np.sign(y - tail_y)))

  def process_command(self, command, print_bridge=False):
    way, steps = command.split(' ')
    for i in range(int(steps)):
      rope.move_head(directions[way])
      for idx in range(1, self.tail_length):
        rope.move_tail(idx)

  def print_bridge(self, show_tails=True, show_tail_visited=False):
    max_x, max_y = max(x for x in map(lambda v: v.x, self.tails)), max(y for y in map(lambda v: v.y, self.tails))
    max_vx, max_vy = max(x for x in map(lambda v: v.x, self.last_tail_visited)), max(y for y in map(lambda v: v.y, self.last_tail_visited))
    max_len = max([abs(max_x), abs(max_y), abs(max_vx), abs(max_vy)])
    bridge = [list('.'*max_len*2) for i in range(max_len*2)]
    if show_tail_visited:
      print('Visited points by the last tail:', self.last_tail_visited)
      for i in self.last_tail_visited:
        bridge[i.x][i.y] = '#'
    if show_tails:
      for i in range(self.tail_length):
        tail = self.tails[i]
        bridge[tail.x][tail.y] = str(i-1) if i!=0 else 'H'
    print('\n'.join([''.join(i) for i in bridge]))

# Day 09 Part I

rope = Rope(bridge, tail_length=1) # (bridge_len=1)
for acommand in data:
  rope.process_command(acommand)

print(len(rope.last_tail_visited))


# Day 09 Part II

rope = Rope(bridge, tail_length=10) # (bridge_len=1)
for acommand in data:
  rope.process_command(acommand)

print(len(rope.last_tail_visited))
