import random

logo = """
  ________                            .__                   ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
        """
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 to 100.")
player = random.randint(1, 100)

user_answer = input("Choose a difficulty. Type 'easy' or 'hard': ")
game_level = user_answer
attempts = [5, 10]
if user_answer == "easy":
    print("You have {attempts[1]} attempts remaining to guess the number.")
elif user_answer == "hard":
    attempts -= 1
    print("You have {attempts[0]} attempts remaining to guess the number.")


user_guess = input("Make a guess: ")

def compare(player, num_input):
    if player > num_input:
        return "Too low."
    elif player < num_input:
        return "Too high."
    
print("Guess again")


    



