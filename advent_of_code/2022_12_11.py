import requests as r
from copy import copy
import numpy as np
import pandas as pd
import math
from functools import reduce
from operator import mul

cookies = {
"_ga": "GA1.2.xx.xx",
"_gid": "GA1.2.xx.xx",
"session": "xx",
"_gat": "1"
}
task_url = "https://adventofcode.com/2022/day/11/input"
data = r.get(task_url, cookies=cookies)
data = data.text.split("\n\n")
data = [i.strip().split('\n') for i in data]

test = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

test = test.split('\n\n')
test = [i.strip().split('\n') for i in test]



class Monkey:
  classmethod
  def operation(text):
    _ = text.split('= old ')[1].strip()
    if '+' in _:
      value = int(_.replace('+ ',''))
      return lambda x: x + value
    if 'old' in _:
      return lambda x: x * x
    if '*' in _:
      value = int(_.replace('* ',''))
      return lambda x: x * value

  def __init__(self, text):
    self.name = text[0]
    self.items = list(map(int,text[1].strip().split(': ')[1].split(', ')))
    self.operation = Monkey.operation(text[2])
    self.operation_text = text[2].strip().split('Operation: ')[1]
    self.test = lambda x: x % int(text[3].split('divisible by ')[1]) == 0
    self.test_value = int(text[3].split('divisible by ')[1])
    self.test_text = text[3].strip().split('Test: ')[1]
    self.test_true = 'Monkey ' + text[4].split('to monkey ')[1]
    self.test_false = 'Monkey ' + text[5].split('to monkey ')[1]
    self.items_inspected = 0

  def __repr__(self):
    return f"{self.name} has the following items {self.items},\n" + \
        f"trowing items to [{self.test_true}] if true and to [{self.test_false}] otherwise;\n" + \
        f"the operation is [{self.operation_text}] with the following test [{self.test_text}]"

class KeepAway:
  def __init__(self, data, debug = False):
    self.monkeys = {}
    for i in data:
      _ = Monkey(i)
      self.monkeys[_.name[:-1]] = _
    self.worry_level = None
    self.debug = debug
    self.worry_level_function = lambda x: math.floor(x/3)

  def print_monkeys(self):
    print('\n\n'.join([str(i) for i in self.monkeys]))

  def print_monkeys_items(self):
    print('\n\n'.join([f"{self.monkeys[i].name}: {self.monkeys[i].items}"  for i in self.monkeys]))

  def process_round(self):
    for mnky_idx in self.monkeys:
      if self.debug:
        print(mnky_idx)
      for _ in range(len(self.monkeys[mnky_idx].items)):
        item = self.monkeys[mnky_idx].items.pop(0)
        self.monkeys[mnky_idx].items_inspected += 1
        if self.debug:
          print(f'Monkey inspects an item with a worry level of {str(item)}.')
        self.worry_level = self.monkeys[mnky_idx].operation(item)
        if self.debug:
          print(f'Worry level is multiplied by {item} to {self.worry_level}.')
        self.worry_level = self.worry_level_function(self.worry_level)
        if self.debug:
          print(f'Monkey gets bored with item {item}. Worry level is divided by 3 to {self.worry_level}.')
        test_result = self.monkeys[mnky_idx].test(self.worry_level)
        if self.debug:
          print(f'Current worry level ({self.worry_level}) is{"" if test_result else " not"} {self.monkeys[mnky_idx].test_text}.')
        recipient = self.monkeys[mnky_idx].test_true if test_result else self.monkeys[mnky_idx].test_false
        self.monkeys[recipient].items.append(self.worry_level)
        if self.debug:
          print(f'Item with worry level {self.worry_level} is thrown to {recipient}.')
    if self.debug:
      self.print_monkeys_items()
  
  def get_monkey_business(self):
    result = []
    for mnky in self.monkeys:
      print(mnky, self.monkeys[mnky].items_inspected)
      result.append(self.monkeys[mnky].items_inspected)
    top = sorted(result)[-2:]
    print(top)
    print("Monkey business level:", top[0]*top[1])

def lcm(alist):
  lcm = 1
  for i in alist:
    lcm = lcm*i//math.gcd(lcm, i)
  return lcm

# Day 11 Part I
game = KeepAway(data)
for i in range(20):
  game.process_round()

  game.get_monkey_business()

# Day 11 Part II
game = KeepAway(data)
monkey_test_values = [game.monkeys[monkey].test_value for monkey in game.monkeys]
print(monkey_test_values)
print(reduce(mul, monkey_test_values, 1))
print(lcm(monkey_test_values))
game.worry_level_function = lambda x: x % lcm(monkey_test_values) # reduce(mul, monkey_test_values, 1)

for i in range(10000):
  game.process_round()
  
game.get_monkey_business()
