import requests as r
from copy import copy
import numpy as np
import pandas as pd

cookies = {
"_ga": "GA1.2.x.x",
"_gid": "GA1.2.x.x",
"session": "xxx",
"_gat": "1"
}
task_url = "https://adventofcode.com/2022/day/7/input"
data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]


test =[
    """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
]

test = test[0].split('\n')

class FileSystem():
  def __init__(self):
    self.fs = {'/':{'files':[], 'dir_size':0}}
    self.current_folder = '/'  # '/a/b/c
  
  def navigate(self, command, calc_on_cd = True):
    # print(command)
    if 'cd ..' in command.strip():
      if calc_on_cd:
        current_dir_size = self.fs[self.current_folder]['dir_size']
      split_fs = self.current_folder.split('/')
      del split_fs[-2]  # going "up"
      self.current_folder = '/'.join(split_fs)
      # print('adding previous dir_size', current_dir_size, 'to the new current', self.fs[self.current_folder]['dir_size'])
      if calc_on_cd:
        self.fs[self.current_folder]['dir_size'] += current_dir_size
      # print('Command: ["', command, '"] current folder:', self.current_folder)
      return
    if ' cd ' in command.strip():
      new_folder = command.split(' cd ')[1]
      self.current_folder = self.current_folder + new_folder + '/'
      self.fs[self.current_folder] = {'files':[], 'dir_size':0}
      # print('Command: ["', command, '"] current folder:', self.current_folder)
      return
    if ' ls' in command.strip():
      # print('Command: ["', command, '"] current folder:', self.current_folder)
      return
    if command.strip().startswith('dir '):  # create a flat absolute path folder
      ls_folder = self.current_folder + command.split('dir ')[1] + '/'
      # print('Command: ["', command, '"] addin a new folder:', ls_folder)
      self.fs[ls_folder] = {'files':[], 'dir_size':0}
    else:  # append a file to the current directory
      # print(command.strip().split(" "))
      size, fname = command.strip().split(" ")
      self.fs[self.current_folder]['files'].append((int(size), fname))
      self.fs[self.current_folder]['dir_size'] += int(size)
      # print('Command: ["', command, '"] appending a file', self.fs[self.current_folder]['files'], 'current folder:', self.current_folder)

  def re_calc_root_size(self):
    root_size = self.fs['/']['dir_size']
    for adir in self.fs:
      if adir != '/':
         root_size += self.fs[adir]['dir_size']
    return root_size

  def sort_by_dirsize(self, folder_size_to_delete=None):
    result = {}
    for adir in self.fs:
      if adir != '/':
        result[adir] = self.fs[adir]['dir_size']
    if folder_size_to_delete is None:
      for adir in sorted(result, key=result.get, reverse=True):
        print(result[adir], ' | ', adir)
    else:
      for adir in sorted(result, key=result.get):
        if self.fs[adir]['dir_size'] >= folder_size_to_delete:
          print(result[adir], ' | ', adir)
          return self.fs[adir]['dir_size']
    return result

fs = FileSystem()



# Day 07 Part I

for i in data[1:]:
  fs.navigate(i)

total_sum = 0
for adir in fs.fs:
  if fs.fs[adir]['dir_size'] <= 100000:
    total_sum += fs.fs[adir]['dir_size']

print(total_sum)


# Day 07 part II

for i in data[1:]:
  fs.navigate(i, False)

drive_size = 70000000
target_free = 30000000

current_free = drive_size - fs.re_calc_root_size()
folder_size_to_delete = target_free - current_free


for i in data[1:]:
  fs.navigate(i)

a = fs.sort_by_dirsize(folder_size_to_delete)


