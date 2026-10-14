inp = int(input("Enter any number from 0 to 9 : "))

match inp:
    case 1:
        print("you won car")
    case 5:
        print("you won a house")
    case _:
        print("Better luck next time")