"""
Do not remove this file. Ensure your main function is in this file.

I will execute your game like this:

python3 game.py

Yes, you may add additional files to this folder.
"""
import random
import sys
import time
import story


def CHARACTER_CLASSES() -> tuple:
    """
    Return character classes as a tuple.

    Classes: ("Engineer", "Medic", "Soldier", "Scavenger").

    :return: a tuple.
    """
    return "Engineer", "Medic", "Soldier", "Scavenger"


def CHARACTER_RANKS() -> dict:
    """
    Return a dictionary of character classes, xp requirements, and rank titles.

    Each class (key) is assigned a nested dictionary as a value; within that nested dictionary are
    the xp requirements (key), and rank titles (values). The complete dictionary is as follows:

    {"Engineer": {0: "Novice", 10: "Intermediate", 20: "Expert"},
     "Medic": {0: "Intern", 10: "Resident", 20: "Attending"},
     "Soldier": {0: "Private", 10: "Sergeant", 20: "Corporal"},
     "Scavenger": {0: "Scrounger", 10: "Explorer", 20: "Master"}}

    :return: a dictionary.
    """
    return {
        "Engineer": {0: "Novice",
                     10: "Intermediate",
                     20: "Expert"},
        "Medic": {0: "Intern",
                  10: "Resident",
                  20: "Attending"},
        "Soldier": {0: "Private",
                    10: "Sergeant",
                    20: "Corporal"},
        "Scavenger": {0: "Scrounger",
                      10: "Explorer",
                      20: "Master"}}


def CHARACTER_STATS() -> dict:
    """
    Return a dictionary of ranks (keys) and tuples of stats (values).

    The complete dictionary is as follows:

    {"Novice": (13, 3, 6), "Intermediate": (17, 4, 7), "Expert": (20, 5, 8),
     "Intern": (15, 1, 6), "Resident": (18, 2, 7), "Attending": (23, 3, 8),
     "Private": (20, 4, 7), "Sergeant": (23, 5, 8), "Corporal": (23, 6, 9),
     "Scrounger": (13, 3, 6), "Explorer": (17, 4, 7), "Master": (19, 4, 8)}

    :return: a dictionary.
    """
    # Stats: Current / Max HP, Attack, Hit Chance.
    return {"Novice": (15, 2, 6),
            "Intermediate": (17, 3, 7),
            "Expert": (20, 4, 8),
            "Intern": (15, 2, 6),
            "Resident": (18, 3, 7),
            "Attending": (21, 4, 8),
            "Private": (17, 3, 7),
            "Sergeant": (20, 4, 8),
            "Corporal": (23, 5, 9),
            "Scrounger": (15, 3, 6),
            "Explorer": (17, 4, 7),
            "Master": (19, 4, 8)}


def CHARACTER_DIRECTIONS() -> dict:
    """
    Return dictionary of directions and movement values.

    The complete dictionary is as follows: {"North": -1, "East": 1, "South": 1, "West": -1}

    :return: a dictionary.
    """
    return {"North": -1, "East": 1, "South": 1, "West": -1}


def get_character_name() -> str:
    """
    Return capitalized name.

    This function asks the user to input a name. The name cannot contain spaces, digits,
    or special characters; it can contain only lowercase and uppercase letters.

    :return: a string.
    """
    while True:
        ask_player = input("\nWhat's your character's name? ")

        if not ask_player.isalpha():
            print("That won't work. Use uppercase or lowercase letters only.")

        else:
            return ask_player.capitalize()


def get_character_class(classes: list or tuple) -> str:
    """
    Return character class (string).

    This function asks the user to input an integer corresponding to a character class type.

    :precondition:  classes must be a non-empty list or tuple.
    :postcondition: class type (string) is returned.
    :return:        a string.
    """
    print("\nWhat's your character's class?")

    for num, class_type in enumerate(classes, start=1):
        print(f"{num}) {class_type}")

    while True:
        ask_player = input("Choose a number to select your character's class: ")

        if ask_player.isdigit() and 0 < int(ask_player) <= len(classes):
            return classes[int(ask_player) - 1]

        else:
            print("That won't work. Select a class number.")


def round_character_xp(character: dict) -> int:
    """
    Return rounded integer value for character["XP"].

    This function rounds a character's XP integer to either 0, 10, or 20,
    based on the original value of character["XP"].

    :param character: a dictionary.
    :precondition:    character must be a dictionary with a key called "XP" with an integer value.
    :postcondition:   a rounded integer is returned.
    :return:          an integer.

    >>> round_character_xp({"XP": 5})
    0
    >>> round_character_xp({"XP": 19})
    10
    """
    if character["XP"] < 10:
        return 0
    elif 10 <= character["XP"] <= 19:
        return 10
    else:
        return 20


def assign_character_rank(character: dict, ranks: dict) -> str:
    """
    Return a rank (string) based on "Rank" and "XP" values in character dictionary.

    The function first rounds the character to 0, 10, or 20. It then returns the rank value,
    a string, based on character's "Class" value and rounded character "XP" level, respectively.

    :param character: a dictionary.
    :param ranks:     a dictionary.
    :precondition:    character must contain the key "Class"; the value for "Class" must be a key
                      in the primary dictionary assigned to ranks. character must also contain the
                      key "XP"; the value for "XP" must be a key in the nested dictionary in ranks.
                      ranks must be a dictionary with string for keys and a nested dictionary as a
                      value; that nested dictionary must have 0, 10, and 20, respectively, as keys
                      and strings as values.
    :return:          a string.

    >>> player = {"Class": "Medic", "XP": 11}
    >>> player_ranks = {"Medic": {0: "Intern", 10: "Resident", 20: "Attending"}}
    >>> assign_character_rank(player, player_ranks)
    'Resident'
    """
    rounded_character_xp = round_character_xp(character)
    return ranks.get(character["Class"]).get(rounded_character_xp)


def assign_character_stats(character: dict, stats: dict):
    """
    Update character dictionary values based on character rank value.

    The values for the character keys "Max HP", "Current HP", "Attack", and  "Hit Chance" will
    be updated with integer values based on the character's rank. The values for these attributes
    are pulled from stats dictionary.

    :param character: a dictionary.
    :param stats:     a dictionary.
    :precondition:    character must have "Max HP", "Current HP", "Attack", "Hit Chance",
                      and "Rank" as keys; "Rank" must have a string value equal to a
                      key in the stats dictionary.
                      stats must have strings as keys; one of those keys must match the
                      value for the key "Rank" in the character dictionary.
    :postcondition:   character keys "Max HP", "Current HP", "Attack", and "Hit Chance"
                      are updated with integer values.

    >>> player = {'Rank': 'Sergeant', 'Max HP': '', 'Current HP': '', 'Attack': '', 'Hit Chance': ''}
    >>> available_stats = {"Private": (20, 4, 7), "Sergeant": (23, 5, 8), "Corporal": (23, 6, 9)}
    >>> assign_character_stats(player, available_stats)
    >>> print(player)
    {'Rank': 'Sergeant', 'Max HP': 23, 'Current HP': 23, 'Attack': 5, 'Hit Chance': 8}
    """
    character["Max HP"] = stats.get(character["Rank"])[0]
    character["Current HP"] = stats.get(character["Rank"])[0]
    character["Attack"] = stats.get(character["Rank"])[1]
    character["Hit Chance"] = stats.get(character["Rank"])[2]


def generate_character(classes: tuple or list, ranks: dict, stats: dict) -> dict:
    """
    Create a character dictionary.

    This function creates a character dictionary. The values for "Name" and "Class" are chosen by the user;
    the value for "XP" is given the integer 0; the value for "Location" is given the list [0, 0]; the value
    for "Ranks", a string, is updated based on the character "Class" value; and the integer values
    for "Max HP", "Current HP", "Attack", and "Hit Chance" are updated based on the "Rank" value.

    :param classes: a tuple or list.
    :param ranks:   a dictionary.
    :param stats:   a dictionary.
    :precondition:  classes must be a tuple or list of strings.
                    ranks must have at least one string key that's also found in classes.
                    stats must have at least one string key that's also a value in ranks.
    :postcondition: a character dictionary is created with complete attributes and values.
    :return:        a dictionary.
    """
    character = {"Name": get_character_name(),
                 "Class": get_character_class(classes),
                 "Rank": "",
                 "Max HP": "",
                 "Current HP": "",
                 "Attack": "",
                 "Hit Chance": "",
                 "XP": 0,
                 "Location": [0, 0]}

    character["Rank"] = assign_character_rank(character, ranks)
    assign_character_stats(character, stats)

    return character


def execute_user_choice(rows: int, columns: int, character: dict, boss: dict) -> str:
    """
    Print game information or return player move selection.

    This function allows the user to make one of five choices. They can quit the game; display the game board;
    display their character stats; print the coordinates of the room they're in; or select a direction they
    want to move, which returns a string. The user must select a direction to end the function.

    :param rows:      an integer.
    :param columns:   an integer.
    :param character: a dictionary.
    :param boss:      a dictionary.
    :precondition:    rows and columns must both be an integer greater than 0.
                      character and boss must each contain a "Location" key.
    :postcondition:   (1) quit the game, (2) print character stats, (3) print room location,
                      (4) print map, or (5) return the direction (string) the user wants to travel.
    :return:          a string.
    """
    directions = list(CHARACTER_DIRECTIONS().keys())

    while True:
        ask_user = input("-----------------------\n"
                         "|    Player Moves     |\n"
                         "-----------------------\n"
                         "| (1) North | (S)tats |\n"
                         "| (2) East  | (M)ap   |\n"
                         "| (3) South | (R)oom  |\n"
                         "| (4) West  | (Q)uit  |\n"
                         "-----------------------\n"
                         ">>> ")

        if ask_user.lower() == "q":
            quit("Thanks for playing!")

        elif ask_user.lower() == "m":
            display_game_board(rows, columns, character, boss)

        elif ask_user.lower() == "s":
            display_stats(character)

        elif ask_user.lower() == "r":
            print(f"You're currently in room {character['Location']}.")

        elif ask_user.isdigit() and 0 < int(ask_user) <= len(directions):
            return directions[int(ask_user) - 1]

        else:
            print("That won't work. Choose one of the available options.")


def display_game_board(rows: int, columns: int, character: dict, boss: dict):
    """
    Print game board, including character and boss locations.

    :param rows:      an integer.
    :param columns:   an integer.
    :param character: a dictionary.
    :param boss:      a dictionary.
    :precondition:    rows and columns must both be integers greater than 0.
                      character must contain string key called "Location" whose value is a list with two integers.
                      The first integer, representing the x-coordinate, must be 0 <= integer <= rows.
                      The second integer, representing the y-coordinate, must be 0 <= integer <= columns.

    >>> player = {"Location": [1, 2]}
    >>> main_boss = {"Location": [2, 1]}
    >>> display_game_board(3, 3, player, main_boss) # doctest: +NORMALIZE_WHITESPACE
    [ ][ ][ ]
    [ ][ ][B]
    [ ][@][ ]
    """
    for y_coord in range(columns):
        for x_coord in range(rows):
            if x_coord == character['Location'][0] and y_coord == character['Location'][1]:
                sys.stdout.write(f"[@]")
            elif x_coord == boss["Location"][0] and y_coord == boss["Location"][1]:
                sys.stdout.write(f"[B]")
            else:
                sys.stdout.write("[ ]")
        print("")


def display_stats(figure: dict):
    """
    Print contents of a dictionary.

    :param figure:  a dictionary.
    :precondition:  figure must be a non-empty dictionary.
    :postcondition: dictionary is printed in an easy-to-read format.

    >>> display_stats({"Name": "Bill", "Class": "Medic"}) # doctest: +NORMALIZE_WHITESPACE
    -----------------------
    Name        |  Bill
    Class       |  Medic
    -----------------------
    """
    print("-----------------------")
    for attribute, description in figure.items():
        print('{:<11} {:} {:<15}'.format(attribute, "| ", str(description)))
    print("-----------------------")


def validate_character_move(character: dict, direction: str, rows: int, columns: int) -> bool:
    """
    Determine if player can move in a given direction.

    :param character:   a dictionary.
    :param direction    a string.
    :param rows:        an integer.
    :param columns:     an integer.
    :precondition:      rows must be an integer greater than 1.
                        columns must be an integer greater than 1.
                        character dictionary must contain a key called "Location" with a list value
                        containing two integers representing x- and y-coordinates, respectively.
                        direction must be a string with one of four values: "North", "South", "East", or "West".
    :postcondition:     Determine if the character can (True) or cannot (False) move in the chosen direction.
    :return:            True or False.

    >>> validate_character_move({"Location": [0, 0]}, "North", 3, 3)
    You try moving North...
    False
    >>> validate_character_move({"Location": [0, 0]}, "East", 3, 3)
    You try moving East...
    True
    """
    print(f"You try moving {direction}...")

    if direction == "East" or direction == "West":

        #                        |     X-Coordinate     |           East = 1   OR   West = -1
        new_player_coordinates = character["Location"][0] + CHARACTER_DIRECTIONS()[direction]
        return 0 <= new_player_coordinates <= rows - 1

    else:                      # |     Y-Coordinate     |         North = -1   OR   South = 1
        new_player_coordinates = character["Location"][1] + CHARACTER_DIRECTIONS()[direction]
        return 0 <= new_player_coordinates <= columns - 1


def move_character_location(character: dict, direction: str):
    """
    Update value for character "Location" key.

    :param character:   a dictionary.
    :param direction:   a string
    :precondition:      character dictionary must contain a key called "Location" with a list value
                        containing two integers representing the x- and y-coordinates, respectively.
                        string must be one of four possible options: "North", "East", "South" or "West".
    :postcondition:     list value for character["Location"] key is updated.
    """
    if direction == "East" or direction == "West":

        #                                   East = 1   OR   West = -1
        character["Location"][0] += CHARACTER_DIRECTIONS()[direction]

    else:                               # North = -1   OR   South = 1
        character["Location"][1] += CHARACTER_DIRECTIONS()[direction]


def player_moves_character(rows: int, columns: int, character: dict, boss: dict):
    """
    Move character if the user-selected direction is valid.

    :param rows:        an integer.
    :param columns:     an integer.
    :param character:   a dictionary.
    :param boss:        a dictionary.
    :precondition:      rows and columns must both be integers greater than 0.
                        character must be a dictionary with a key called "Location".
                        boss must be a dictionary.
    :postcondition:     if character move is successful, prints out character["Location"]; else,
                        prints out a message telling the user they're as far as they can go.
    """
    user_choice = execute_user_choice(rows, columns, character, boss)
    move_is_valid = validate_character_move(character, user_choice, rows, columns)
    time.sleep(0.5)

    if move_is_valid:
        move_character_location(character, user_choice)
        print(f"You're now in {character['Location']}.")

    else:
        print(f"You're as far {user_choice} as you can go!")


def generate_enemy(character: dict) -> dict:
    """
    Generate enemy with stats based on character level.

    This function first determines the character's level, based on the value for character["XP"],
    the generates an enemy dictionary with the following key-values:

    Name       -> randomly selected string from a list of four strings.
    Current HP -> an integer.
    Attack     -> an integer.
    XP         -> an integer.
    Hit Chance -> an integer.

    :param character: a dictionary.
    :precondition:    character must contain an "XP" key with an integer value.
    :postcondition:   an enemy dictionary with attributes (keys) and stats (values).
    :return:          a dictionary.
    """
    character_level = round_character_xp(character)

    #                  |       Enemy HP       |   Enemy Attack   | XP  |  Enemy Hit Chance  |
    enemy_stats = {00: (random.randint(3, 4), random.randint(2, 3), 2, random.randint(7, 8)),
                   10: (random.randint(4, 5), random.randint(3, 4), 2, random.randint(7, 8)),
                   20: (random.randint(5, 6), random.randint(4, 5), 2, random.randint(7, 8))}

    enemy = {"Name": random.choice(["Drone", "Walker-Bot", "Ramoeba Ball", "Roller-Bot"]),
             "Current HP": enemy_stats.get(character_level)[0],
             "Attack": enemy_stats.get(character_level)[1],
             "XP": enemy_stats.get(character_level)[2],
             "Hit Chance": enemy_stats.get(character_level)[3]}

    print(f"\nA {enemy['Name']} appears...")
    time.sleep(0.5)
    return enemy


def character_may_or_may_not_engage_enemy(character: dict):
    """
    Determines if there's an enemy; if so, enemy is generated and
    player and enemy engage.

    :param character: a dictionary
    :precondition:    character must be a non-empty dictionary.
    :postcondition:   function runs until there is no longer an enemy.
    """
    there_is_an_enemy = random.randint(1, 5) == 1

    if there_is_an_enemy:
        enemy = generate_enemy(character)

        while there_is_an_enemy:
            there_is_an_enemy = character_fights_enemy(character, enemy)


def player_chooses_to_flee_or_fight(enemy: dict) -> bool:
    """
    Returns True if player fights, False if player runs.

    This function also allows the player to print out the enemy dictionary
    of attributes and attribute values.

    :param enemy:   a dictionary.
    :precondition:  enemy must be a non-empty dictionary.
    :postcondition: return True if player fights, False if player runs.
    :return:        True or False.
    """
    while True:
        ask_user = input("-----------------\n"
                         "|   Your move?  |\n"
                         "-----------------\n"
                         "| (F)ight       |\n"
                         "| (E)nemy stats |\n"
                         "| (R)un         |\n"
                         "-----------------\n"
                         ">>> ")

        if ask_user.lower() == "f":
            return True

        elif ask_user.lower() == "r":
            return False

        elif ask_user.lower() == "e":
            display_stats(enemy)

        else:
            print("Invalid command. Enter 'f' to fight or 'r' to run.")


def attack_hits_or_misses(attacker: dict, attackee: dict):
    """
    Determine if attacker hits attackee.

    This function determines whether the attacker successfully hits the attackee.
    If the attack lands, the attackee's "Current HP" integer value is reduced by
    the attacker's "Attack" integer value. If the attack misses, no changes.

    :param attacker: a dictionary.
    :param attackee: a dictionary.
    :precondition:   attacker must contain the keys "Name" and "Hit Chance"; "Hit Chance"
                     must have an integer value.
                     attackee must contain the keys "Name" and "Current HP"; "Current HP"
                     must have an integer value.
    :postcondition:  if attackee is hit, attackee "Current HP" value is updated.
    """
    print(f"{attacker['Name']} tries attacking {attackee['Name']}...")
    time.sleep(0.5)

    if random.randint(1, 10) <= attacker["Hit Chance"]:
        attackee["Current HP"] -= attacker["Attack"]
        print(f"... and succeeds!\n")

        time.sleep(0.5)

        print(f"{attackee['Name']} loses {attacker['Attack']}HP.")

        if attackee['Current HP'] <= 0:
            print(f"{attackee['Name']} has been defeated!")

        else:
            print(f"{attackee['Name']} has {attackee['Current HP']}HP remaining.\n")
    else:
        print(f"... and misses!")


def character_fights_enemy(character: dict, enemy: dict) -> bool:
    """
    Player and enemy engage in battle.

    This function runs through a battle scenario. The player can run, the enemy can run,
    or they can fight, with a chance that either the enemy or character dies. If the
    enemy dies, the player may or may not level up.

    :param character: a non-empty dictionary.
    :param enemy:     a non-empty dictionary.
    :precondition:
    :postcondition:
    :return:          True or False.
    """
    if not player_chooses_to_flee_or_fight(enemy):
        enemy_attacks_fleeing_player(enemy, character)
        return False

    if random.randint(1, 10) == 1:
        print("The enemy runs away...")
        return False

    attack_hits_or_misses(character, enemy)

    if not is_alive(enemy):
        level_up_character(character, enemy)
        return False

    attack_hits_or_misses(enemy, character)

    if is_alive(character):
        return True


def enemy_attacks_fleeing_player(enemy: dict, character: dict):
    """
    Determines if fleeing character is damaged or not.

    This function checks whether the character is damaged or not. If the character is damaged, the
    value for "Current HP" in the character dictionary is updated. If the character is not damaged,
    the character dictionary is not updated.

    :param enemy:       a dictionary.
    :param character:   a dictionary.
    :precondition:      character must contain a key called "Current HP" with an integer value greater than 0.
                        It must also contain a key called "Name" with a string value.
                        enemy must contain a key called "Name" with a string value. It must also contain a
                        key called "Attack" with an integer value.
    :postcondition:     If the character is hit, the character key "Current HP" is updated.
    """
    print(f"You try running away...\n"
          f"The {enemy['Name']} tries attacking you as you run...")
    time.sleep(0.5)

    if random.randint(1, 5) == 1:
        character["Current HP"] -= enemy["Attack"]
        print(f"... and, somehow, it manages to hit you!"
              f"You lose {enemy['Attack']}HP. You now have {character['Current HP']}HP remaining.\n")

    else:
        print("... and it misses.")


def level_up_character(character: dict, enemy: dict):
    """
    Print character XP increase; update character dictionary if 10 or 20 XP reached.

    :param character: a dictionary.
    :param enemy:     a dictionary.
    :precondition:    character must contain an "XP" key with an integer value; it must also
                      a "Rank" key with a string value.
                      enemy must contain an "XP" key with an integer value.
    :postcondition:   tells player how many XP they earned; if they hit 10 or 20 XP, character
                      dictionary is updated with new stat values; if player hits 20XP, in addition
                      to stats updates, they're told that they've hit the maximum level.
    """
    character["XP"] += enemy["XP"]
    print(f"You earned {enemy['XP']}XP!")

    if character["XP"] == 10 or character["XP"] == 20:
        print("\nYou leveled up!")
        character["Rank"] = assign_character_rank(character, CHARACTER_RANKS())
        assign_character_stats(character, CHARACTER_STATS())

    if character["XP"] == 20:
        print("You've hit the maximum level!")


def generate_boss(rows: int, columns: int) -> dict:
    """
    Return a dictionary of boss traits and values.

    This function creates a dictionary with the following keys and values:

    {"Name": "HAL 8500",
    "Description": "",
    "Current HP": random.randint(25, 28),
    "Attack": random.randint(6, 8),
    "Hit Chance": 8,
    "Location": [random.randint(1, rows - 1), random.randint(1, columns - 1)]}

    :return: a dictionary.
    """
    return {"Name": "HAL 8500",
            "Current HP": random.randint(22, 25),
            "Attack": random.randint(5, 7),
            "Hit Chance": 8,
            "Location": [random.randint(1, rows - 1), random.randint(1, columns - 1)]}


def character_fights_boss(character: dict, boss: dict) -> None:
    """
    Return out of function once player or boss has been defeated.

    This function begins the boss fight scenario. The player goes first, followed by the boss.
    After each turn, the function checks if the one attacked is still alive. If one of the figures
    die -- the character or the boss -- the function ends.

    :param character: a dictionary.
    :param boss:      a dictionary.
    :precondition:    boss must have a key called "Name".
                      character["XP"] and boss["XP"] integer values must be greater than 0.
    :postcondition:   return out of the function when either player or boss is defeated.
    :return:          None.
    """
    print(story.story["Boss Fight"])
    time.sleep(8)

    while is_alive(character) and is_alive(boss):

        if not player_chooses_to_flee_or_fight(boss):
            print("You can't run away! This is a fight to the death!")
            continue

        attack_hits_or_misses(character, boss)
        attack_hits_or_misses(boss, character)


def is_alive(figure: dict) -> bool:
    """
    Determine if value for "Current HP" is greater than 0.

    :param figure:  a dictionary.
    :precondition:  figure dictionary must contain a string key called "Current HP".
    :postcondition: if character has 1 or greater HP, True; else False.
    :return:        True or False.

    >>> is_alive({'Current HP': 1})
    True
    >>> is_alive({'Current HP': 0})
    False
    """
    return figure["Current HP"] > 0


def game():
    """
    Play the game.
    """
    print(story.story["Title Screen"])
    time.sleep(1)

    rows = 10
    columns = 10
    character = generate_character(CHARACTER_CLASSES(), CHARACTER_RANKS(), CHARACTER_STATS())
    boss = generate_boss(rows, columns)

    print(story.story["Intro"])
    time.sleep(15)

    while is_alive(character) and is_alive(boss):
        player_moves_character(rows, columns, character, boss)

        if character["Location"] == boss["Location"]:
            character_fights_boss(character, boss)
        else:
            character_may_or_may_not_engage_enemy(character)

    if not is_alive(character):
        time.sleep(0.5)
        quit("You were defeated! GAME OVER.")
    else:
        quit("You won the game!")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
