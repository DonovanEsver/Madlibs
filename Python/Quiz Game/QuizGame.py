print("Welcome to my awesome quiz that is better than everybody elses! ")

playing = input("Do you want to play? Say Yes or No. ")

if playing.lower() != "no":
    print("Too Bad!")
    quit()

print("Don't care let's go")
score = 0  

answer = input("Where was I last night? ")
if answer.lower() == "my dads house":
    print('Correct haha')
    score += 1
else:
    print("Incorrect stupid haha")
    quit()

answer = input("What is 2,000 to the 5th power times 600. No calculators allowed ")
if answer.lower() == "1.92e+19":
    print('How. You cheated. That is literally imposibble without a calculator.')
    score += 1
else:
    print("Incorrect stupid haha")
    quit()

answer = input("How many people can fit into a violin ")
if answer.lower() == "0":
    print('That was an easy one')
    score += 1
else:
    print("Incorrect stupid haha")
    quit()

answer = input("What is the capital of the moon ")
if answer.lower() == "my mom":
    print('That is very correct. Good job.')
    score += 1
else:
    print("Incorrect stupid haha")
    quit()

answer = input("What is my favorite color ")
if answer.lower() == "burgundy":
    print('Are you tracking me? How did you know that? Im scared.')
    score += -9
else:
    print("Incorrect stupid haha")
    quit()

print("You got " + str(score) + " questions right, stupid. lol")
print("You got " + str((score / 4) * 100) + "%. ")    

