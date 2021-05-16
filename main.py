from art import logo
import random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
trigger = False

def difficulty(level):

    if level == 'easy':
        attempt = 10
    elif level == 'hard':
        attempt = 5
    return attempt

def random_number():
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
          21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
          41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
          51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
          61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
          71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
          81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
          91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    random_number = random.choice(number)
    return random_number

def compare(check_number,guess):
    if check_number < guess:
        print("Too high")
    elif check_number > guess:
        print("Too low")
    elif check_number == guess:
        global trigger
        trigger = True
        print(f" You got it! The answer was {guess}.")
        

def total_attempt(attempt):
    return attempt - 1


random_num = random_number()
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print(f"the correct answer is {random_num}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
print(f"You have {difficulty(level)} attempts remaining to guess the number.")


attempt = difficulty(level)


while attempt != 0 :
    
    guess = int(input("make a guess : "))
    compare(check_number =random_num,guess = guess)
    attempt = attempt-1
    if attempt == 0:
        print("You've run out of guesses, you lose.")
    if trigger == True :
        attempt =0
    elif attempt != 0 :
        print(f"You have {attempt} attempts remaining to guess the number.")
    
    
