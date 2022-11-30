
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
log_id = input("Enter your user ID: ")
log_pass = input("Enter password: ")

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    answer = input("What does ASP stand for? ")
if answer.lower() == " ACTIVE SERVER PAGES.":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    answer = input("What does DVD stand for? ")
if answer.lower() == " DIGITAL VIDEO DISK":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 6) * 100) + "%.")
print("THANK YOU HAVE A NICE DAY")