import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2020/day/2/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))
test = [
"1-3 a: abcde",
"1-3 b: cdefg",
"2-9 c: ccccccccc",
]

# Part I
password_db = [
    {
        "min": int(data[i].split("-")[0]),
        "max": int(data[i].split(" ")[0].split("-")[1]),
        "key": data[i].split(" ")[1].replace(":",""),
        "password": data[i].split(" ")[2]
    }
    for i in range(len(data))
]

print(sum([1 for v in password_db if v['min']<= v['password'].count(v['key']) <= v['max']]))

# Part II

print(sum([1 for v in password_db if sum([v['password'][v['min']-1] == v['key'], v['password'][v['max']-1] == v['key']]) == 1]))
