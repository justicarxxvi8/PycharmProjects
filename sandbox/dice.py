from random import randint

while True:
    user_choice = input("Do you want to role the dice? Y/N")
    if user_choice == "Y":
        print(randint(0,6))
        print("testa")
    elif user_choice == "N":
        print("End program")
        exit()
