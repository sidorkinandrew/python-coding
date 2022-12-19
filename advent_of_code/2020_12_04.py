import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2020/day/4/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

print(len(data))
test = [
"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
"byr:1937 iyr:2017 cid:147 hgt:183cm",
"",
"iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
"hcl:#cfa07d byr:1929",
"",
"hcl:#ae17e1 iyr:2013",
"eyr:2024",
"ecl:brn pid:760753108 byr:1931",
"hgt:179cm",
"",
"hcl:#cfa07d eyr:2025 pid:166559648",
"iyr:2011 ecl:brn hgt:59in"
]

# Path I
def parse_db(data):
  passport_db = []
  _current = []
  for i in data:
    print(i)
    if i == "":
      passport_db.append(" ".join(_current))
      _current = []
      continue
    _current.append(i)
  passport_db.append(" ".join(_current))
  return passport_db

def parse_passport(data):
  elems = data.split(" ")
  return {i.split(":")[0]:i.split(":")[1] for i in elems}

print(sum([len(set(parse_passport(i).keys())-set(['cid']))==7 for i in passport_db]))

# Path II

invalid_passports = [
"eyr:1972 cid:100",
"hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
"",
"iyr:2019",
"hcl:#602927 eyr:1967 hgt:170cm",
"ecl:grn pid:012533040 byr:1946",
"",
"hcl:dab227 iyr:2012",
"ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
"",
"hgt:59cm ecl:zzz",
"eyr:2038 hcl:74454a iyr:2023",
"pid:3556412378 byr:2007",
]

valid_passports = [
"pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
"hcl:#623a2f",
"",
"eyr:2029 ecl:blu cid:129 byr:1989",
"iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
"",
"hcl:#888785",
"hgt:164cm byr:2001 iyr:2015 cid:88",
"pid:545766238 ecl:hzl",
"eyr:2022",
"",
"iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
]


def validate_passport(data):
  # byr (Birth Year) - four digits; at least 1920 and at most 2002.
  if int(data['byr']) < 1920 or int(data['byr']) > 2002:
    return 0
  # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
  if int(data['iyr']) < 2010 or int(data['iyr']) > 2020:
    return 0
  # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
  if int(data['eyr']) < 2020 or int(data['eyr']) > 2030:
    return 0
  # hgt (Height) - a number followed by either cm or in:
  if (not data['hgt'].endswith("cm")) and (not data['hgt'].endswith("in")):
    return 0
  # If cm, the number must be at least 150 and at most 193.
  if data['hgt'].endswith("cm"):
    _hgt = int(data['hgt'].replace("cm", ""))
    if _hgt < 150 or _hgt > 193:
      return 0
  # If in, the number must be at least 59 and at most 76.
  if data['hgt'].endswith("in"):
    _hgt = int(data['hgt'].replace("in", ""))
    if _hgt < 59 or _hgt > 76:
      return 0
  # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
  if not data['hcl'].startswith("#"):
    return 0
  if sum([1 for i in data['hcl'][1:] if i in '0123456789abcdef'])!=6:
    return 0
  # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
  if data['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
    return 0
  # pid (Passport ID) - a nine-digit number, including leading zeroes.
  if sum([1 for i in data['pid'] if i in '1234567890'])!=9:
    return 0
  return 1
  
  
passport_db = parse_db(data) #(test + [""] + valid_passports + [""] + invalid_passports)
print(len(passport_db))

count = 0
for i in passport_db:
  _res = parse_passport(i)
  if len(set(parse_passport(i).keys())-set(['cid']))!=7:
    continue
  count += validate_passport(_res)

print(count)