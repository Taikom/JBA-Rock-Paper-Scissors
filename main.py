# Rock, paper, scissors
import random

rating_f = open('rating.txt', 'r')
scores = rating_f.readlines()
rating_f.close()

option_user = None
player = input("Enter your name: ")
score = 0
print(f"Hello, {player}")
for line in scores:
    p, s = line.split()
    if player == p:
        score = int(s)
options = input()
if options == '':
    variates = ['rock', 'paper', 'scissors']
else:
    variates = options.split(",")
print("Okay, let's start")
var_f = []
var_w = []

while True:
    option_pc = random.choice(variates)
    option_user = input()
    for i in range(len(variates)):
        if variates[i] == option_user:
            var_w = variates[i+1:]
            var_f = variates[:max(0,i)]
    while len(var_f) != len(var_w):
        if len(var_f) > len(var_w):
            var_w.append(var_f[0])
            del var_f[0]
        else:
            var_f.append(var_w[-1])
            del var_w[-1]

    if option_user == "!rating":
        print(score)
    elif option_user == "!exit":
        print("Bye!")
        break
    elif option_user in variates:
        if option_user == option_pc:
            print(f"There is a draw ({option_pc})")
            score += 50
        elif option_pc in var_w:
            print(f"Sorry, but the computer chose {option_pc}")
        elif option_pc in var_f:
            print(f"Well done. The computer chose {option_pc} and failed")
            score += 100
    else:
        print("Invalid input")
rating_f = open('rating.txt', 'w')
for line in scores:
    if player == p:
        rating_f.write(player + " " + score + "\n")
    else:
        rating_f.write(line)
rating_f.close()
