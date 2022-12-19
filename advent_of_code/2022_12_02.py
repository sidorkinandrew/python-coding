import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2022/day/2/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

# Day 02 part I
left_choices = 'ABC'
left_values = dict(zip(left_choices, range(1,len(left_choices)+1)))
# left_values = {
#     'A': 1,  # Rock 
#     'B': 2,  # Paper
#     'C': 3   # Scissors
# }

right_choices = 'XYZ'
right_values = dict(zip(right_choices, range(1,len(right_choices)+1)))
# right_values = {
#     'X': 1,  # Rock 
#     'Y': 2,  # Paper
#     'Z': 3   # Scissors
# }

def get_score(around):
  opponent_choice, my_choice = around.split(' ')
  if around in ['A X', 'B Y', 'C Z']:
    return 3
  if (my_choice == 'Z' and opponent_choice=='B') or (my_choice == 'Y' and opponent_choice=='A') \
     or (my_choice == 'X' and opponent_choice=='C'):
     return 6
  return 0

def calc_score(data):
  result = 0
  for around in data:
    print(around)
    my_choice = around.split(' ')[-1]
    result += right_values[my_choice]
    result += get_score(around)
    print(right_values[my_choice], get_score(around))
  return result

calc_score(data)


# Day 02 part II

def get_my_choice(opponent_choice, win = None):
  if win is None:
    the_idx = left_choices.index(opponent_choice)
  elif win:
    the_idx = (left_choices.index(opponent_choice) + 1) % 3
  else:
    the_idx = (left_choices.index(opponent_choice) - 1) % 3
  return right_choices[the_idx]
    

def apply_strategy(data):
  result = 0
  for around in data:
    opponent_choice, my_choice = around.split(' ')
    if my_choice == 'X':
      result += right_values[get_my_choice(opponent_choice, False)] + 0  # lose
    elif my_choice == 'Z':
      result += right_values[get_my_choice(opponent_choice, True)] + 6  # win
    else:
      result += right_values[get_my_choice(opponent_choice)] + 3  # draw
  return result


apply_strategy(data)
