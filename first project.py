import random

print("Welcome to the Number Guessing Game!" \
"I'm thinking of a number between 1 and 100" \
"" \
"" \
"Please select the difficulty level:" \
"1. Easy (10 chances)" \
"2. Meduim (5 chances)" \
"3. Hard (3 chances)" \
"" \
"")

lvl=int(input("Enter your choice: "))
trr=0
cnt=1
while lvl!=1 and lvl!=2 and lvl!=3:
    lvl=int(input("Please try again : "))

if lvl==1:
    print("" \
    "" \
    "Great! You have selected the Easy difficulty level." \
    "Let's start the game!" \
    "" \
    "")
    trr=10
elif lvl==2:
    print("" \
    "" \
    "Great! You have selected the Medium difficulty level." \
    "Let's start the game!" \
    "" \
    "")
    trr=5
else:
    print("" \
    "" \
    "Great! You have selected the Hard difficulty level." \
    "Let's start the game!" \
    "" \
    "")
    trr=3

numb=random.randint(1,100)
print(numb)
ess=int(input("Enter your guess: "))

while cnt!=trr and ess!=numb:
    if ess<numb:
        cnt+=1
        print("Wrong! ,The number im thinking about is greater than "+str(ess))
        ess=int(input("" \
        "Enter your guess: "))
    elif ess>numb:
        cnt+=1
        print("Wrong! ,The number im thinking about is less than "+str(ess))
        ess=int(input("" \
        "Enter your guess: "))
    elif cnt!=trr and ess==numb:
        cnt+=1
        break
print("Congrations ! You have guessed the number in "+str(cnt)+" attempts.")

if cnt==trr and ess!=numb:
    print("Game over! The number that i was thinking about is "+str(numb))
