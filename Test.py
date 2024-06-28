import random

# Values that remain the same for both classes
physical_multiplier = 1
magic_multiplier = 1
guard = 1.00
enemy_choice = 0


# The base options of skills available
def skill_options():
    print("1. Heal (20 mp)")
    print("2. Fireball (20 mp)")
    print("3. Charge (30 mp)")
    print("4. Concentrate (30 mp)")


# Tells the player their health points, magic points, and their enemies health
def indicator():
    print("Health: " + str(player_health))
    print("Magic Power: " + str(magic_power))
    print(monster_name + " Health: " + str(enemy_health))


# __________________________________________________________________________
# An explanation on why the text appears under the question instead of next to it
print("To make the lines easier to read, the answer to inputs ")
print("will apear under the question instead of beside them as usual.")
print("")
# Tells the player that they don't need to use capitals for any choices
print("Capitals are not required to play this game.")
print("____________________________________________________")
print("")
print("Welcome to Heros of Illisia! (A Fantasy RPG)")
print("")
print("-------------------------------------------------")
print("Do you need a tutorial? (Yes/No)")
tutorial = str(input(""))
if tutorial == "yes" or tutorial == "Yes":
    # Intructions for those who need help and are new to fantasy RPG
    print("")
    print("In this game you are to fight a monster as a chosen class,")
    print("Depending on that class you will have different options to choose from on your turn.")
    print("")
    print("If your health reaches 0 you will lose, to win you must bring the monsters health to 0.")
    print("")
    print("you can choose your action by typing it out or entering its number.")
    print("")
    print("The skills Concentrate and Charge boost your magic and physical multiplier respectivly")
    print("After using your skill or attack, the multiplier will reset to 1.")
    print("")
    print("Guard will make you take less damage against enemies hits for one turn. (Knight only)")
    print("")
    print("Running away is possible but has a chance to fail.")
else:
    print("Then Embark on this quest to save the land!")
print("__________________________________________________________________________________________")
# Has the player pick a class that will effect their health, magic and skills
while True:
    print("Please pick a class:")
    print("1. Wizard")
    print("2. Knight")
    class_choice = str(input(""))
    if class_choice == "Wizard" or class_choice == "wizard" or class_choice == "1":
        player_health = 250
        magic_power = 400


        # Wizards cannont guard
        def print_options():
            print("1. Attack")
            print("2. Skill")
            print("3. Run")


        break
    elif class_choice == "Knight" or class_choice == "knight" or class_choice == "2":
        player_health = 400
        magic_power = 250


        # Knights can't use magic but can do a strong cut instead
        def skill_options():
            print("1. Heal (20 mp)")
            print("2. Strong Cut (25 hp)")
            print("3. Charge (30 mp)")
            print("4. Concentrate (30 mp)")


        # Allows the knight to Guard
        def print_options():
            print("1. Attack")
            print("2. Skill")
            print("3. Guard")
            print("4. Run")


        break
    else:
        print("You seemed panicked, are you alright?")
print("____________________________________________________")
# Has the player pick a monster/ difficulty to fight
print("Pick a difficulty")
print("1. Goblin (Easy)")
print("2. Demon (Medium)")
print("3. Dragon (Hard)")
difficulty = str(input(""))
if difficulty == "goblin" or difficulty == "Goblin" or difficulty == "easy" or difficulty == "Easy" or difficulty == "1":
    monster_name = "Goblin"
    monster_attack = 15
    monster_heal = 50
    monster_curse = 40
    enemy_health = 200
    enemy_health_max = 200
elif difficulty == "demon" or difficulty == "Demon" or difficulty == "medium" or difficulty == "Medium" or difficulty == "2":
    monster_name = "Demon"
    monster_attack = 20
    monster_heal = 60
    monster_curse = 80
    enemy_health = 400
    enemy_health_max = 400
elif difficulty == "dragon" or difficulty == "Dragon" or difficulty == "Hard" or difficulty == "hard" or difficulty == "3":
    monster_name = "Dragon"
    monster_attack = 50
    monster_heal = 110
    monster_curse = 70
    enemy_health = 800
    enemy_health_max = 800
print("____________________________________________________")
# Quick introduction to the story before the game starts
print("Welcome to the capital city of Illisia!")
print("Unfortunatly, monsters have recently started terrorizing the whole continent!")
print("Could you help take some down for us? (Yes/No) ")
start = str(input(""))

if start == "no" or start == "No":
    # Ends game
    print("Fine! Stay in the fort to avoid getting hurt!")
elif start == "yes" or start == "Yes":
    # start fight
    print("____________________________________________________")
    print("A " + monster_name + " approaches!")
    while True:
        print("____________________________________________________")
        if player_health <= 0:
            print("You have perished in battle.")
            break
        elif enemy_health <= 0:
            print("You have slain the enemy!")
            break
        else:
            indicator()
            print("-------------------------------------------------")
            print_options()
            action = str(input(""))
            if class_choice == "knight" or class_choice == "Knight" or class_choice == "2":
                if action == "Attack" or action == "attack" or action == "1":
                    # Attacks the enemy with their weapon
                    enemy_health = enemy_health - (60 * physical_multiplier)
                    physical_multiplier = 1
                    print("You attacked the " + monster_name + "!")
                elif action == "Skill" or action == "skill" or action == "2":
                    # Shows the Skills the player can use
                    print("-------------------------------------------------")
                    skill_options()
                    print("-------------------------------------------------")
                    skill_action = str(input(""))
                    if magic_power >= 15 and skill_action == "Heal" or magic_power >= 15 and skill_action == "heal" or magic_power >= 15 and skill_action == "1":
                        # Heals the player
                        player_health += (75 * magic_multiplier)
                        magic_multiplier = 1
                        magic_power -= 15
                        print("You healed yourself!")
                        while player_health > 200:
                            player_health = player_health - 1
                    elif skill_action == "Strong cut" or skill_action == "strong cut" or skill_action == "2":
                        # Lots of damage using a strong cut
                        enemy_health = enemy_health - (100 * physical_multiplier)
                        player_health -= 25
                        physical_multiplier = 1
                        print("You cut with Percision!")
                    elif magic_power >= 30 and skill_action == "Charge" or magic_power >= 30 and skill_action == "charge" or magic_power >= 30 and skill_action == "3":
                        # Charges their next punch/slash
                        magic_power -= 30
                        physical_multiplier += .5
                        if physical_multiplier > 6:
                            print("You are unable to be more focused!")
                            physical_multiplier = - .5
                        else:
                            print("You charged " + str(physical_multiplier) + " times your power of physical strength!")
                    elif magic_power >= 30 and skill_action == "Concentrate" or magic_power >= 30 and skill_action == "concentrate" or magic_power >= 30 and skill_action == "4":
                        # Charges their next magic attack
                        magic_power -= 30
                        magic_multiplier += .5
                        if magic_multiplier > 6:
                            print("You are unable to be more focused!")
                            magic_multiplier = - .5
                        else:
                            print("You concentrated " + str(magic_multiplier) + " times your power of magic!")
                    else:
                        print("Not enough magic")
                elif action == "Guard" or action == "guard" or action == "3":
                    # Makes the player take less damage
                    guard -= 0.5
                    print("You guarded yourself")
                elif action == "Run" or action == "run" or action == "4":
                    # Lets the player get away and end the game
                    chance = random.randint(1, 4)
                    if chance >= 2:
                        print("You got away")
                        break
                    else:
                        # The player is unable to escape and took damage
                        print("But you couldn't get away!")
                        player_health -= 20
                else:
                    print("You panicked and missed your turn")

            # If the class chosen is wizard:
            elif class_choice == "Wizard" or class_choice == "wizard" or class_choice == "1":
                if action == "Attack" or action == "attack" or action == "1":
                    # Attacks the enemy with their wand
                    enemy_health = enemy_health - (30 * physical_multiplier)
                    physical_multiplier = 1
                    print("You attacked the " + monster_name + "!")
                elif action == "Skill" or action == "skill" or action == "2":
                    # Shows the Skills the player can use
                    print("-------------------------------------------------")
                    skill_options()
                    print("-------------------------------------------------")
                    skill_action = str(input(""))
                    if magic_power >= 15 and skill_action == "Heal" or magic_power >= 15 and skill_action == "heal" or magic_power >= 15 and skill_action == "1":
                        # Heals the player
                        player_health += (75 * magic_multiplier)
                        magic_multiplier = 1
                        magic_power -= 15
                        print("You healed yourself!")
                        while player_health > 200:
                            player_health = player_health - 1
                    elif magic_power >= 20 and skill_action == "Fireball" or magic_power >= 20 and skill_action == "fireball" or magic_power >= 20 and skill_action == "2":
                        # Lots of damage using fireball
                        enemy_health = enemy_health - (110 * magic_multiplier)
                        magic_power -= 20
                        magic_multiplier = 1
                        print("You cast fireball!")
                    elif magic_power >= 30 and skill_action == "Charge" or magic_power >= 30 and skill_action == "charge" or magic_power >= 30 and skill_action == "3":
                        # Charges their next punch/slash
                        magic_power -= 30
                        physical_multiplier += .5
                        if physical_multiplier > 6:
                            print("You are unable to be more focused!")
                            physical_multiplier = - .5
                        else:
                            print("You charged " + str(physical_multiplier) + " times your power of physical strength!")
                    elif magic_power >= 30 and skill_action == "Concentrate" or magic_power >= 30 and skill_action == "concentrate" or magic_power >= 30 and skill_action == "4":
                        # Charges their next magic attack
                        magic_power -= 30
                        magic_multiplier += .5
                        if magic_multiplier > 6:
                            print("You are unable to be more focused!")
                            magic_multiplier = - .5
                        else:
                            print("You concentrated " + str(magic_multiplier) + " times your power of magic!")
                    else:
                        print("Not enough Magic Power")

                elif action == "Run" or action == "run" or action == "3":
                    # Lets the player get away and end the game
                    chance = random.randint(1, 4)
                    if chance >= 2:
                        print("You got away")
                        break
                    else:
                        # The player is unable to escape and took damage
                        print("But you couldn't get away!")
                        player_health -= 20
                else:
                    print("You panicked and missed your turn")
        print("____________________________________________________")
        # Which type of random the enemy will pick
        if enemy_health <= 100 and difficulty != "Dragon" or enemy_health <= 100 and difficulty != "dragon" or enemy_health <= 100 and difficulty != "3":
            enemy_choice = random.randint(1, 10)
        elif difficulty == "Dragon" or difficulty == "dragon" or difficulty == "3":
            enemy_choice = random.randint(1, 12)
        elif difficulty == "Demon" or difficulty == "demon" or difficulty == "2":
            enemy_choice = random.randint(2, 11)
        else:
            enemy_choice = random.randint(2, 10)
            # The action the monster will take based of the random number generated
        if enemy_choice == 1 or enemy_choice == 2 or enemy_choice == 3 or enemy_choice == 4:
            # The monster heals itself
            print("The " + monster_name + " Healed itself!")
            enemy_health += monster_heal
            while enemy_health > enemy_health_max:
                enemy_health = enemy_health - 1
        elif enemy_choice == 5 or enemy_choice == 6 or enemy_choice == 7:
            # The monster attacks the player with its claws or sword
            player_health -= (monster_attack * guard)
            guard = 1
            print("The " + monster_name + " attacked you!")
        elif enemy_choice == 8 or enemy_choice == 9 or enemy_choice == 10 or enemy_choice == 11:
            # The Monster uses a strong curse
            player_health -= monster_curse
            print("The " + monster_name + " used a curse!")
        elif enemy_choice == 12:
            # Dragon Breath
            player_health -= 125
            print("THE DRAGON BREATHED FIRE!!!!")
        # Makes the enemy say something so its still engaging after a while
        enemy_boast = random.randint(1, 100)
        if enemy_boast < 70 and enemy_boast <= 40:
            print(monster_name + ": You are weak!")
        elif enemy_boast < 50 and enemy_boast <= 69:
            print(monster_name + ": You " + class_choice + "s are so annoying!")
        elif enemy_boast < 90 and enemy_boast <= 70:
            print(monster_name + ": Why won't you just die!")
        elif enemy_boast == 100:
            print(monster_name + ": I want my Mommy!!!!")
else:
    print("It seems you are panicked!")
    print("Stay in the fort to avoid getting hurt!")