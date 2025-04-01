# Application execution starts from this file

INSTRUCTIONS = """
>> USER INSTRUCTIONS <<
At any time type "exit" to exit the game.
"""

def main():
    print("Welcome to RPSLS!")
    print(INSTRUCTIONS)

    while True:
        user_input = input("Choose your action: ").lower()
        print(f"You chose: {user_input}\n")

        if user_input == "exit":
            print("Thanks for playing, bye!")
            break

if __name__ == "__main__":
    main()

