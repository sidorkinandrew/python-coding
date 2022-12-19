import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2022/day/3/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

test = [
'vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw'
]

# Day 03 Part I
priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_left(rucksack):
  return rucksack[:len(rucksack)//2]

def get_right(rucksack):
  return rucksack[len(rucksack)//2:]

def get_priorities(data):
  result = []
  for rucksack in data:
    same_item = list(set(get_left(rucksack)).intersection(set(get_right(rucksack))))
    print(rucksack, same_item)
    result.append(priority.index(same_item[0])+1)
  return result

print(sum(get_priorities(data)))


# Day 03 Part II

def get_groups(data, group_lenght = 3):
  return [data[i:i + group_lenght] for i in range(0, len(data), group_lenght)]


def get_group_tag(data):
  result = []
  for agroup in get_groups(data):
    same_tag = list(set(agroup[0]).intersection(set(agroup[1])).intersection(set(agroup[2])))
    print(agroup,'\n', same_tag)
    result.append(priority.index(same_tag[0])+1)    
  return result

print(sum(get_group_tag(data)))
