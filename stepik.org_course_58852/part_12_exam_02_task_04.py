# https://stepik.org/lesson/327221/step/4?unit=310520
# put your python code here
a=input()
print("YES" if a.replace("-","").isnumeric() and \
   ((a.startswith("7-") and a.count("-")==3 and [len(i) for i in a.split("-")] == [1, 3, 3, 4] ) \
    or (a.count("-")==2 and [len(i) for i in a.split("-")] == [3, 3, 4] )) else "NO")
