# Quiz

QUESTION = [
    "A?",
    "B?",
    "C?",
]
ANS = ["aaa", "bbb", "ccc"]

for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == ANS[i]:
      print("correct")
    else:
      print("incorrect")
