import random as rdm

correct_letters = []
incorrect_letters = []
words = []


def getword():
    words = [line.strip().lower() for line in open('words.txt')]
    return rdm.choice(words)

global_word = getword()


def print_spaces(word):
    letters = str(len(word))
    print("The word has a total of " + letters + " letters" )
    return ["_" for word in word]


def userinput():
    print("------------------------------")
    one_letter_input = input("Please enter a letter!")
    return one_letter_input

index = ["_" for word in global_word]

def check_input_to_word(input, word):
    if input in word:
        print('\n' * 40)
        print("Letter found!")
        correct_letters.append(input)
        pos = global_word.find(input)

        if len(index) > 0:
            index[pos] = input

            print(index)

    elif input not in word:
        print('\n' * 40)
        print("Letter not found!")
        print(index)
        incorrect_letters.append(input)

    elif len(input) > 1:
        print("Too many letters!")

print("The rules are simple! You have a total of 9 tries to guess the word! Good luck!")
print_spaces(global_word)

while len(incorrect_letters) < 11:
    check_input_to_word(userinput(), global_word)
    print("------------------------------")
    print("These are the correct letters!")
    print(correct_letters)
    print("------------------------------")
    print("These are the incorrect letters!")
    print(incorrect_letters)
    if len(correct_letters) == len(global_word):
        print("You win!")
        break
    elif len(incorrect_letters) > 10:
        print("You lose!")
        break
