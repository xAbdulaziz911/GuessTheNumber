import random
N = input("Choose The Difficulty(easy, normal, hard, veryhard, impossible): ")

if N == "easy":
  N = 10
  print("Guess from 1 to 10")

elif N == "normal":
  N = 50
  print("Guess from 1 to 50")

elif N == "hard":
  N = 200
  print("Guess from 1 to 200")

elif N == "veryhard":
  N = 10000
  print("Guess from 1 to 10000")

elif N == "impossible":
  N = 1000000000
  print("Guess from 1 to 1.000.000.000💀")

x = random.randint(1, N)
s = 0
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

    



   
   
