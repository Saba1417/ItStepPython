import random


def random_number_generator(min_value: int, max_value: int) -> int:
    return random.randrange(min_value, max_value)

def main():
    print("Please enter range with 2 numbers")
    try:
        a = int(input().strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    try:
        b = int(input().strip())
    except ValueError:
        print("Please enter a valid number.")
        return

    if a == b:
        print("Range must contain two different numbers.")
        return

    if a > b:
        a, b = b, a  

    try:
        target = random_number_generator(a, b)
    except ValueError:
        print("Invalid range. Make sure the first number is less than the second.")
        return

    counter = 0
    print("Now try to guess number")
    while True:
        try:
            chosen = int(input().strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        counter += 1
        if chosen == target:
            print("Congratulations! You're right!")
            print(f"It took you {counter} tries.")
            break
        elif chosen > target:
            print("You need to try lower number")
        else:
            print("You need to try higher number")

if __name__ == "__main__":
    main()