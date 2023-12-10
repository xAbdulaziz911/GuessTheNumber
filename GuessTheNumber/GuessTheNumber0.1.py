from random import randint
modes = {"1": 10, "2": 50, "3": 200, "4": 10000, "5": 1000000000}
user = 0
x = 0
s = 0
while True:
  for i, mode in enumerate(["Easy","Normal","Hard","Very Hard","Impossible"], start=1):
    print(f"{i}- {mode}") 
  N = input("Choose The Difficulty (enter a number): ")
  if N in modes:
    print(f"Guess from 1 to {modes[N]}")
    N = modes[N]
    x = randint(1, N)
    break
  else:
    print("Invalid choice. Please choose a valid number.")
while True:
  try:
    user = int(input(">>: "))
    s += 1
    if user == x:
      print("Correct!")
      print(f"Number of tries: {s}")
      break
    else:
      print("Missed it")
  except:ValueError
  if user > x:
    print("lower!")
  else:
    print("higher!")