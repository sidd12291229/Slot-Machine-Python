import random
import time

SLOT_VALUES = [1, 2]


def get_yes_or_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.\n")


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Enter again.")


def main():
    print("Welcome to Sidd's Slot Machine!")
    while True:
        money = get_integer_input("\nHow much money do you want to check in today? ")

        while True:
            spins = get_integer_input("How many times do you want to spin? ")
            if spins <= 0:
                print("\nNumber of spins must be greater than 0.\n")
                continue
            bet = get_integer_input("How much do you want to bet per spin? ")
            if bet > money:
                print("\nYour bet cannot be greater than your current money.\n")
                continue

            for i in range(spins):
                if money <= 0 or money - bet < 0:
                    break

                result, slot_values = randomizer()
                print(f"\nSlot machine: {', '.join(map(str, slot_values))}")

                if result:
                    money += bet
                    print("You have won the bet.")
                else:
                    money -= bet
                    print("You have lost the bet.")

                print(f"You have ${money} remaining.\n")
                time.sleep(2)

            if money <= 0 or money - bet < 0:
                print("\nYou do not have any more money left.")

                more = get_yes_or_no_input("Do you want to check in more money? (yes/no) ")
                if more:
                    add = get_integer_input("\nHow much more? ")
                    money += add
                    check_in = True
                else:
                    break

                if not check_in:
                    check_out = get_yes_or_no_input("Do you want to check out? (yes/no) ")

                    if check_out:
                        break
                    else:
                        check_in = False

        print("\nThank you for playing at Sidd's Slot Machine!")
        break


def randomizer():
    slot_values = [random.choice(SLOT_VALUES) for _ in range(2)]
    result = all(value == slot_values[0] for value in slot_values)
    return result, slot_values


if __name__ == '__main__':
    main()
