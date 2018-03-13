import random
import time

def run_game_1p():
    x = random.randint(1, 100)

    generated_number = random.randint((x), (x + 25))

    user_guess = int(input("\nLet's play a guessing game!\n\nTry to guess the number! (It's between " + str(x) + " and " + str(x + 25) + "): "))
    playing = True

    comp_guess_parameter_high = x + 25
    comp_guess_parameter_low = x

    while playing:
        if user_guess < generated_number:
            print("Oh No! That number is too low...\nMy Turn!\n")
            comp_guess_parameter_low = user_guess
        elif user_guess > generated_number:
            print("Oh No! That number is too high...\nMy Turn!\n")
            comp_guess_parameter_high = user_guess
        elif user_guess == generated_number:
            return "You guessed it right! The number is " + str(generated_number) + "... You Won!"

        time.sleep(.25)

        comp_rand_guess = random.randint((comp_guess_parameter_low), (comp_guess_parameter_high))

        if comp_rand_guess < generated_number:
            user_guess = int(input("Darnit! My guess (" + str(comp_rand_guess) + ") was too low...\nYour Turn: "))
            comp_guess_parameter_low = comp_rand_guess
        elif comp_rand_guess > generated_number:
            user_guess = int(input("Darnit! My guess (" + str(comp_rand_guess) + ") was too high...\nYour Turn: "))
            comp_guess_parameter_high = comp_rand_guess
        elif comp_rand_guess == generated_number:
            return "I guessed it right! The number is " + str(generated_number) + "... You lost!"

def main():
    result = run_game_1p()
    print(result)

    replay = input("Would you like to play again? (y/n): ")
    if replay == "y":
        main()

main()
