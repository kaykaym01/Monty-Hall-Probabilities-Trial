import random
def newGame():
    # Randomly assigns one of the doors to have the prize and the remaining
    # doors to have goats. Returns a dict with door number as the key and
    # whatever's behind it as the value.

    # randomly select integer between 1 and 3
    prize_door = random.randint(1, 3)

    # dictionary to hold door values
    doors = dict()

    # loop through 1-3
    for x in range(1, 4):
        # if x is the prize door, set value to prize
        if x == prize_door:
            doors[f'door{x}'] = 'prize'
        # else set value to goat
        else:
            doors[f'door{x}'] = 'goat'

    return doors


def guestChoice():
    # Randomly chooses one door, like the contestant on the game show. Returns
    # the chosen door

    # randomly select integer between 1 and 3
    door_number = random.randint(1, 3)
    door_chosen = f'door{door_number}'

    return door_chosen

def openOneDoor(game, chosen_door):
    # Receives as input the created game and door chosen by the contestant and
    # randomly 'opens' one of the doors - but not the door with the prize nor the
    # door that was chosen by the contestant. Returns a modified dict with the
    # value of the open door as 'open'

    # Remove chosen door and car door from list of doors
    choice_doors = [x for x in range(1, 4) if x != chosen_door and
        game[f'door{x}'] != 'prize']

    # Randomly select a door from choice_doors
    opened_door = random.choice(choice_doors)

    # Update dict with 'open' for chosen door
    game[f'door{opened_door}'] = 'open'

    return game

def guestChange(game, chosen_door):
    # Receives as input the created game and door chosen by the contestant and
    # switches the chosen door from the current door to the other closed door

    # list of doors
    doors = list(game.keys())

    # select new door that is not open and not already chosen
    new_door = [x for x in doors if game[x] != 'open'
        and x != chosen_door][0]

    return new_door

def checkResult(game, chosen_door):
    # Receives as input a created game and a door and returns 'win' if the
    # chosen door contains the prize. Otherwise, returns 'loss'.

    if game[chosen_door] == 'prize':
        return 'win'
    else:
        return 'loss'


doors = newGame()
choice = guestChoice()
opened = openOneDoor(doors, choice)
changed = guestChange(opened, choice)
result = checkResult(opened, changed)
print(doors)
print(choice)
print("Host has opened a door --> ", opened)
print("Contestant has switched doors --> ", changed)
print("Result --> ", result)
print()
