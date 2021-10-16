import random
import webbrowser



num_easy = input("Enter number of easy questions (max 35): ")
while not num_easy.isnumeric() or (int(num_easy) < 0 or int(num_easy) > 35):
	num_easy = input("Please enter a valid number (0-35): ")

num_medium = input("Enter number of medium questions (max 105): ")
while not num_medium.isnumeric() or (int(num_medium) <0 or int(num_medium) > 105):
	num_medium = input("Please enter a valid number (0-105): ")

num_hard = input("Enter number of hard questions (max 30): ")
while not num_hard.isnumeric() or (int(num_hard) <0 or int(num_hard) > 30):
	num_hard = input("Please enter a valid number (0-30): ")

num_easy = int(num_easy)
num_medium = int(num_medium)
num_hard = int(num_hard)
print(num_easy)
print(num_medium)
print(num_hard)


easy_quest = random.choice(easy, k=num_easy)
medium_quest = random.choice(medium, k=num_medium)
hard_quest = random.choice(hard, k=num_hard)

for quest in easy_quest:
	webbrowser.open(quest)

for quest in medium_quest:
	webbrowser.open(quest)

for quest in hard_quest:
	webbrowser.open(quest)

print("Happy Studying :D")