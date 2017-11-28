from random import randint


def generate_random_number():
    random_number = randint(0,25)
    return random_number


def random_number_guesser(number):
    while True:
        user_guess = input("Guess the number:")
        if int(user_guess) < number:
            print("Guess higher!")
        elif int(user_guess) > number:
            print("Guess lower!")
        elif int(user_guess) == number:
            print("You guessed correctly!")
            break

number = generate_random_number()
random_number_guesser(number)