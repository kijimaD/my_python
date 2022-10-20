import random
import datetime

ALP = ["A", "B", "C", "D", "E", "F", "G"]
r = random.choice(ALP)
alp = ""

for ch in ALP:
    if ch != r:
        alp = alp + ch

print(alp)
start = datetime.datetime.now()

ans = input("excluded alphabet?")
if ans == r:
    print("correct")
    now = datetime.datetime.now()
    print((now-start).seconds)
else:
    print("incorrect")
