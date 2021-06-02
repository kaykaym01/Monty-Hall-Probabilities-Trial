import random
from collections import defaultdict

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

    # list of all doors
    all_doors = list(game.keys())

    # Remove chosen door and prize door from list of doors
    choice_doors = [x for x in all_doors if x != chosen_door and
        game[x] != 'prize']

    # Randomly select a door from choice_doors
    opened_door = random.choice(choice_doors)

    # Update dict with 'open' for chosen door
    game[opened_door] = 'open'

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

def play_game():
    # Simulates game play and returns result of game

    # Creates a new game
    game = newGame()

    # Simulates a guest choice
    choice = guestChoice()

    # Opens one door
    opened = openOneDoor(game, choice)

    # Changes the door to the other unopened door
    changed = guestChange(opened, choice)

    # checks the result for the changed choice
    result = checkResult(opened, changed)

    return result

def simulation(num_games=100):
    # Simulates num_games games and returns results of winning for switching
    # and not switching

    # Default dictionary for storing wins of switching and not switching
    results = defaultdict(int)

    # Loops through number of games
    for x in range(num_games):

        # Plays a game and gets the result
        result = play_game()

        # Updates dictionary with number of wins for switching vs not
        # switching (result='loss')
        if result == "win":
            results['switch_wins'] += 1
        else:
            results['not_switch_wins'] += 1

    return results

def print_results(results):
    # Receives results as input and prints results and graph

    # Gets the total number of games
    total_games = sum(list(results.values()))

    switch_wins = results['switch_wins']
    switch_percent = switch_wins / total_games

    not_switch_wins = results['not_switch_wins']
    not_switch_percent = not_switch_wins / total_games


    print(f"{'Switching Wins:':>20}{switch_percent:>10} ({switch_wins})")
    print(f"{'Not Switching Wins:':>20}{not_switch_percent:>10} ({not_switch_wins})")
    print(f"{'Total Games:':>20}{total_games:>17}")


if __name__ == '__main__':
    results = simulation(num_games=10000)
    print_results(results)
    print()
