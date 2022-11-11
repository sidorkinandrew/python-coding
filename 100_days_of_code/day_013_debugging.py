# 13.1 Even/Odd

number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# 13.2 Leap Year
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# 13.3 FizzBuzz
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
