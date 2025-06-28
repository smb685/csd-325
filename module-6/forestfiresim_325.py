"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # Added constant for water

# Try changing these settings:
INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01

PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    while True:
        displayForest(forest)
        nextForest = {'width': WIDTH, 'height': HEIGHT}
        for x in range(WIDTH):
            for y in range(HEIGHT):
                cell = forest[(x, y)]

                # Skip water: it never changes
                if cell == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                if cell == EMPTY:
                    if random.random() <= GROW_CHANCE:
                        nextForest[(x, y)] = TREE
                    else:
                        nextForest[(x, y)] = EMPTY
                elif cell == TREE:
                    if isNextToFire(forest, x, y) or random.random() <= FIRE_CHANCE:
                        nextForest[(x, y)] = FIRE
                    else:
                        nextForest[(x, y)] = TREE
                elif cell == FIRE:
                    nextForest[(x, y)] = EMPTY
        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Add lake in center region
            if 30 <= x <= 49 and 8 <= y <= 13:
                forest[(x, y)] = WATER
            elif random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest


def displayForest(forest):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
            elif cell == FIRE:
                bext.fg('red')
            elif cell == WATER:
                bext.fg('blue')
            else:
                bext.fg('reset')
            print(cell, end='')
        print()
    bext.fg('reset')
    print()


def isNextToFire(forest, x, y):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            if (x + dx, y + dy) in forest and forest[(x + dx, y + dy)] == FIRE:
                return True
    return False


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
