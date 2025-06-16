import random  # Importing the random module for rolling dice

# Introduction messages to the player
print("Welcome to Chohan!")
print("In this traditional Japanese gambling game, two dice are rolled.")
print("You must guess whether the dice total to an even (cho) or odd (han) number.")
print("NOTE: If the total of the dice roll is 2 or 7, you get a 10 mon bonus.\n")

# Initialize the player's starting money
purse = 5000  # Player starts with 5000 mon

# Main game loop
while True:
    print(f"\nYou have {purse} mon. How much do you bet? (or QUIT)")

    # Get and validate the player's bet amount
    while True:
        pot = input('sb: ')  # Input prompt with initials
        if pot.upper() == 'QUIT':  # Allow player to quit the game
            print("Thanks for playing!")
            exit()
        if not pot.isdecimal():  # Ensure input is a number
            print("Please enter a number.")
        else:
            pot = int(pot)  # Convert string to integer
            if pot > purse:  # Check if player has enough mon
                print(f"You don't have enough mon. Your purse: {purse}")
            else:
                break  # Valid bet

    # Get the player's bet choice (CHO for even, HAN for odd)
    print("Do you bet on even (CHO) or odd (HAN)?")
    while True:
        bet = input('sb: ').upper()  # Convert input to uppercase
        if bet in ['CHO', 'HAN']:  # Valid choices
            break
        print("Please enter either CHO or HAN.")  # Prompt again for invalid input

    # Roll two six-sided dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2  # Sum of dice

    # Check for bonus condition: total is 2 or 7
    if total == 2 or total == 7:
        print(f'The total was {total}. You get a 10 mon bonus!')
        purse += 10  # Add bonus to player's purse

    # Show the dice results and total
    print(f"The dealer rolls the dice: {die1}, {die2}")
    print(f"Total: {total}")

    # Determine if the total is even or odd
    if total % 2 == 0:
        result = 'CHO'  # Even number
    else:
        result = 'HAN'  # Odd number

    print(f"It is {result}.")  # Show actual result

    # Determine if player won or lost
    if bet == result:
        print(f"You won! You take the pot of {pot} mon.")
        purse += pot  # Add pot to purse
    else:
        print("You lost!")
        purse -= pot  # Subtract pot from purse

    # House takes a 12% cut of the pot (new requirement)
    house_cut = pot * 12 // 100  # Integer division for house cut
    purse -= house_cut  # Subtract house cut from purse
    print(f"The house takes a cut of {house_cut} mon.")

    # Check if player is out of money
    if purse <= 0:
        print("You're out of mon! Game over.")
        break  # End the game
