import logic

def main():
    logic.clear()
    print("Welcome to the DND Character Program")

    while True:
        try:
            print("what would you like to do?")
            print("1) Add Character Info    2) Display Character Info    3) Save Character    4) Load Character")
            print("5) Add Money    6) Display Money")
            print("7) Roll Dice    8) Exit")
            intChoice = int(input("Choice: "))
            logic.clear()

            if intChoice < 0 or intChoice > 8:
                print("Invalid choice!")
                continue
            elif intChoice == 1:
                character = logic.createCharacter()
            elif intChoice == 2:
                print(character)
            elif intChoice == 3:
                logic.saveCharacter(character)
            elif intChoice == 4:
                character = logic.loadCharacter()
            elif intChoice == 5:
                logic.addMoney(character)
            elif intChoice == 6:
                character.displayMoney()
            elif intChoice == 7:
                logic.rollDice()
            elif intChoice == 8:
                exit()

        except ValueError:
            logic.clear()
            print("Please input a number!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("\nCTRL+C")
