from random import randint
s = 0
modes = {"1": 10, "2": 50, "3": 200, "4": 10000, "5": 1000000000}

for i, mode in enumerate(["Easy","Normal","Hard","Very Hard","Impossible"], start=1):
    print(f"{i}- {mode}")
N = input("Choose The Difficulty (enter a number): ")

if N in modes:
  print(f"Guess from 1 to {modes[N]}")
  
  N = modes[N]
  x = randint(1, N)
  
else:
  print("Invalid choice. Please choose a valid number.")

while True:
  user = int(input(">>: "))
  s += 1
  if user == x:
    print("Correct!")
    print("Number of tries: ",s)
    break
  else:
    print("Missed it")
  if user > x:
     print("lower!")
  else:
    print("higher!")