import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2021/day/4/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))
test = [
"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
"",
"22 13 17 11  0",
" 8  2 23  4 24",
"21  9 14 16  7",
" 6 10  3 18  5",
" 1 12 20 15 19",
"",
" 3 15  0  2 22",
" 9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",
"",
"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
" 2  0 12  3  7"
]


# Part I

def parse_data(data):
  draws = data[0]
  boards = []
  _current = []
  for i in data[2:]:
    if i == "":
      boards.append(create_board(";".join(_current)))
      _current = []
      continue
    _current.append(i)
  boards.append(create_board(";".join(_current)))
  return draws, boards

def create_board(data):
  _result = {}
  _row = 0
  for i in data.split(";"):
    _result[_row] = {j:False for j in list(map(int,i.strip().replace("  ", " ").split(" ")))}
    _row += 1
  return _result
  
draws, boards = parse_data(test)

def run_bingo(draws, boards): # no column checks lol
  _draws = []
  for i in map(int, draws.split(",")):
    _draws.append(i)
    for aboard in boards:
      for arow in aboard:
        if i in aboard[arow].keys():
          aboard[arow][i] = True
          if sum(aboard[arow].values()) == 5:
            print("BINGO!")
            _sum = 0
            for j in aboard:
              _sum += sum([k for k,v in aboard[j].items() if not v])
            print(i, _draws)
            return aboard, _sum*i

board, _sum = run_bingo(draws, boards)
print(_sum)

# Part II

import numpy as np

def check_boards(boards):
  _res = {}
  for k in boards:
    list_of_lists = [[k[j][l] for l in k[j]] for j in k]
    rows = np.sum(np.array(list_of_lists), axis=1).tolist()
    columns = np.sum(np.array(list_of_lists).T, axis=1).tolist()
    _idx = boards.index(k)
    _res[_idx] = True if (rows.count(5) >= 1) or (columns.count(5) >= 1) else False
  return _res

def run_bingo_last(draws, boards):
  _res = []
  print("drawing:", end=" ")
  for i in map(int, draws.split(",")):
    print(i, end=" ")
    for aboard in boards:
      for arow in aboard:
        if i in aboard[arow].keys():
          aboard[arow][i] = True
    _res.append(check_boards(boards))
    if list(_res[-1].values()).count(False) == 0:
      print()
      _idx = list(_res[-2].values()).index(False)
      the_last_of_us = boards[_idx]
      _sum = 0
      for j in the_last_of_us:
        _sum += sum([k for k,v in the_last_of_us[j].items() if not v])
      print(i, _sum)
      return i * _sum

draws, boards = parse_data(data)

run_bingo_last(draws, boards)
