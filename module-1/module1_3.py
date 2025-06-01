# Sylvester Brandon
# Sun Jun 1 2025
# Module: 1.3 - Countdown Song Assignment


def sing_bottles_song(starting_bottles):
    for bottles in range(starting_bottles, 0, -1):
        bottle_word = "bottle" if bottles == 1 else "bottles"
        next_bottles = bottles - 1
        next_bottle_word = "bottle" if next_bottles == 1 else "bottles"

        print(f"{bottles} {bottle_word} of beer on the wall, {bottles} {bottle_word} of beer.")
        if next_bottles > 0:
            print(f"Take one down and pass it around, {next_bottles} {next_bottle_word} of beer on the wall.\n")
        else:
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")

    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

def main():
    while True:
        try:
            user_input = input("How many bottles of beer are on the wall? ")
            starting_bottles = int(user_input)
            if starting_bottles <= 0:
                print("Please enter a positive integer.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.\n")

    sing_bottles_song(starting_bottles)

if __name__ == "__main__":
    main()
