name = input("Enter your name: ")
mood = input("How are you feeling today? happy/sad/exicted/stressed: ")
energy = input("What is your energy levek on a scale of 1 to 10: ")

if energy < 3:
    print("Alert: your energy is low. Take some rest")


if energy >= 5:
    print("You have energy to do something productive today")
else:
    print("Take it slow and do something relaxing")


if mood == "happy":
   advice = "Keep spreading your positive energy!"
elif mood == "sad":
   advice = "Talk to someone you trust or do something that makes you feel better"
elif mood == "tired":
   advice = "Drink water, take a short break, and rest your mind."
elif mood == "stressed":
   advice = "Try deep breathing or make a small to-do list."
elif mood == "excited":
   advice = "Use your excitement to start something creatiive!"
else:
   advice = "Every mood is okay. Take care of yourself today."               


import datetime

today = datetime.datetime.now()

print("============")
print("DAILY MOOD ADVISOR REPORT")
print("============")
print("Name :", name)
print("Mood :", mood)
print("Energy Level :", energy)
print("Date and Time :", today)
print("Advice :", advice)
print("============")