import random
best_score = None
while True:
    number = random.randint(1, 100)
    attempts = 7
    used_attempts = 0
    print("\nGuess the number between 1 and 100")
    print("You have 7 attempts.")
    while attempts > 0:
        try:
            guess = int(input("Enter your  guess:"))
            used_attempts += 1
            attempts -= 1
            if guess == number:
                print(f"Congratulations! You guessed correctly in{used_attempts}attempts.")
            
                if best_score is None or used_attempts < best_score:
                    best_score = used_attempts
                    print("New Best Score!")
                break
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
                if abs(guess - number) <= 5:
                    print("Hint: You are Very close!")
                    print(f"Attempts remaining: {attempts}")
        except ValueError:
            print(f"Invalid input! Please enter a number.")
            if attempts == 0 and guess != number:
               play_again = input(" Do you want to play again? (yes/no):").lower()
            if play_again != "yes":
                print("Thank you for playing! ")  
                     