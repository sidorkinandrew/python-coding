import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2022/day/4/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

test = [
    '2-4,6-8',
'2-3,4-5',
'5-7,7-9',
'2-8,3-7',
'6-6,4-6',
'2-6,4-8'
]

# Day 04 Part I
def is_overlapping(left_a,right_a,left_b,right_b):
  a = list(range(int(left_a), int(right_a)+1))
  b = list(range(int(left_b), int(right_b)+1))
  return set(a).intersection(set(b)) == set(a) or set(a).intersection(set(b)) == set(b)

# Day 04 Part II
def is_overlapping(left_a,right_a,left_b,right_b, closed = 'both'):
  return pd.Interval(int(left_a),int(right_a),closed=closed).overlaps(pd.Interval(int(left_b),int(right_b),closed=closed))  


def count_overlapping(data):
  result = []
  count = 0
  for i in data:
    a, b = i.split(',')
    left_a,right_a,left_b,right_b = [*a.split('-'), *b.split('-')]
    if is_overlapping(left_a,right_a,left_b,right_b):
      count+=1
    result.append((i, is_overlapping(left_a,right_a,left_b,right_b)))
  return result, count

print(count_overlapping(data))
