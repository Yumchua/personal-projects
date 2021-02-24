# Brian's Basic Python RPG
# Anti-spoiler buffer
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# imports
import math
import random
from threading import Timer
import time
from operator import itemgetter


# messages
def contin():
    input("Press enter to continue...")
    print("")


def action_sel():
    selection = input("Please select...")
    print("")
    return selection


def max_health():
    print("You are already at full health!")


def max_mana():
    print("You are already at full mana!")


def no_mp():
    print("You don't have enough MP remaining!")


def no_items():
    print("You don't have any items currently!")


def no_pot():
    print("You don't have any more potions!")


def mon_encounter():
    image_dispatcher[str(current_mon.num)]()
    if current_mon.name[0].lower() in "aeiou":
        print("An \"" + current_mon.name + "\" appeared!")
    else:
        print("A \"" + current_mon.name + "\" appeared!")


def action_err():
    print("Please select a valid action.")


def num_err():
    print("A nice whole number, PLEASE!")


def game_over():
    print("Your health was reduced to zero! Sorry, that means your story ends here...")
    contin()
    print("GAME OVER.")
    exit()


# classes
class Character:
    def __init__(self, name, age, lvl, max_hp, hp, max_mp, mp, strg, intl, defn, spd, exp, weapon, status, duration,
                 status_initial):
        self.name = name
        self.age = age
        self.lvl = lvl
        self.max_hp = max_hp
        self.hp = hp
        self.max_mp = max_mp
        self.mp = mp
        self.strg = strg
        self.intl = intl
        self.defn = defn
        self.spd = spd
        self.exp = exp
        self.weapon = weapon
        self.status = status
        self.duration = duration
        self.status_initial = status_initial


class LevelUp:
    def __init__(self, lvl, threshold, hp_gain, mp_gain, strg_gain, intl_gain, defn_gain, spd_gain):
        self.lvl = lvl
        self.threshold = threshold
        self.hp_gain = hp_gain
        self.mp_gain = mp_gain
        self.strg_gain = strg_gain
        self.intl_gain = intl_gain
        self.defn_gain = defn_gain
        self.spd_gain = spd_gain


class Enemy:
    def __init__(self, name, max_hp, hp, atk, spd, exp, wep_res, fire_res, ice_res, poison_chance, status, boss, num):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.atk = atk
        self.spd = spd
        self.exp = exp
        self.wep_res = wep_res
        self.fire_res = fire_res
        self.ice_res = ice_res
        self.poison_chance = poison_chance
        self.status = status
        self.boss = boss
        self.num = num

    def mon_attack(self):
        low_value = self.atk - 2
        high_value = self.atk + 2
        low_value = max(low_value - math.ceil(protag.defn * defn_multiplier), 0)
        high_value = max(high_value - math.ceil(protag.defn * defn_multiplier), 0)
        damage_dealt = random.randint(low_value, high_value)
        protag.hp = protag.hp - damage_dealt
        print("The " + current_mon.name + " attacks and deals " + str(damage_dealt) + " damage!")
        contin()
        if protag.hp <= 0:
            game_over()
        if random.random() < current_mon.poison_chance and protag.status is None:
            protag.status = psn
            print("You were poisoned!")
            contin()
        return protag.hp, protag.status


class Items:
    def __init__(self, hp70_pot, mp50_pot, cursed_doll, used_doll):
        self.hp70_pot = hp70_pot
        self.mp50_pot = mp50_pot
        self.cursed_doll = cursed_doll
        self.used_doll = used_doll


class Weapons:
    def __init__(self, name, wep_range):
        self.name = name
        self.wep_range = wep_range


class Spells:
    def __init__(self, name, mp_cost, dmg_range, status_name, status_chance):
        self.name = name
        self.mp_cost = mp_cost
        self.dmg_range = dmg_range
        self.status_name = status_name
        self.status_chance = status_chance


class Status:
    def __init__(self, name, damage, immobile, duration):
        self.name = name
        self.damage = damage
        self.immobile = immobile
        self.duration = duration


# protagonist
protag = Character("The Protagonist", 20, 1, 100, 100, 50, 50, 10, 8, 5, 5, 0, None, None, 0, True)
run_result = False

lvl_1 = LevelUp(1, 100, 10, 5, 2, 1, 1, 1)
lvl_2 = LevelUp(2, 150, 10, 5, 2, 2, 2, 2)
lvl_3 = LevelUp(3, 200, 10, 5, 2, 2, 1, 1)

level_dict = {
    "1": lvl_1,
    "2": lvl_2,
    "3": lvl_3
}

# items
items_1 = Items(0, 0, 0, False)

# weapon stats
wooden_sword = Weapons("Wooden Sword", range(6, 9))

# spell stats
fireball = Spells("Fireball", 8, range(10, 16), "BRN_LV1", .15)
frost_bolt = Spells("Frost bolt", 8, range(10, 12), "FRZ", .3)

# statuses
brn_lv1 = Status("BRN_LV1", 3, False, True)
frz = Status("FRZ", 0, True, 1)
psn = Status("PSN", 3, False, 3)
un_frz = Status("UN_FRZ", 0, False, 0)


# monster images
def mon_0_image():
    print("          /\\             ")
    print("         /   \\           ")
    print("        /      \\         ")
    print("      /          \\       ")
    print("     /             \\     ")
    print("    / ( @ )  ( @ )  \\    ")
    print("   |                /     ")
    print("    \\              /     ")
    print("       - - - - - -        ")


def mon_1_image():
    print("          =====           ")
    print("        //     \\\\       ")
    print("       || @   @ ||        ")
    print("       ||       ||        ")
    print("        \\\\     //       ")
    print("          =====           ")
    print("       // I   I \\\\      ")
    print("      --  I---I  --       ")
    print("     //   I   I   \\\\    ")
    print("    UU    I---I    UU     ")


def mon_2_image():
    print("          /\\             ")
    print("         /   \\           ")
    print("        /  \\/  \\        ")
    print("      /    /\\    \\      ")
    print("     /             \\     ")
    print("    / ( X )  ( X )  \\    ")
    print("   |                /     ")
    print("    \\              /     ")
    print("       - - - - - -        ")


def mon_3_image():
    print("           +++++          ")
    print("          /  {} \\        ")
    print("    <>   [  |  | ]    <>  ")
    print("    <>   [       ]    <>  ")
    print("          +++++++         ")
    print("           V V V          ")


def mon_4_image():
    print("             /\\          ")
    print("    ^      /\\  /\\   ^ ^ ")
    print("          /      \\       ")
    print("         [  |  |  ]    ^  ")
    print("  ^  ^   [        ]      ^")
    print("           ------         ")


def mon_5_image():
    print("        /\\\\            </\\>             </\\>        /\\\\       ")
    print("       /   \\\\          /  \\             /  \\       /  \\\\      ")
    print("      /     \\\\       </    \\>^       ^</    \\>    /    \\\\     ")
    print("     /        \\\\     ^      ^         ^      ^   /       \\\\     ")
    print("    /     V    \\\\   |   / \\    ^        / \\   | /    V    \\\\  ")
    print("   /   V    V    \\\\|     =          ^    =     |   V    V  \\\\   ")
    print("    V        V  V  |    \\ /   ^         \\ /    |V         VV      ")
    print("                    \\                          /                   ")
    print("                     \\                        /                    ")
    print("                      \\                      /                     ")
    print("                       --=--=--=---=---=--=-                        ")


def mon_6_image():
    print("           /\\^^>                                                   ")
    print("          /  \\                                                     ")
    print("         /    \\                                                    ")
    print("        /   _  \\                                                   ")
    print("       / __     \\                                                  ")
    print("      /          \\                                                 ")
    print("    || vvvvvvvvvv |||                                               ")
    print("   |||  --\\   /--  |||                                             ")
    print("  ||||  (O)   (O)  |||                                              ")
    print("   ||       ^       ||                                              ")
    print("   ||\\      -      /||                                             ")
    print("         -------     |                                              ")


image_dispatcher = {
    "0": mon_0_image,
    "1": mon_1_image,
    "2": mon_2_image,
    "3": mon_3_image,
    "4": mon_4_image,
    "5": mon_5_image,
    "6": mon_6_image
}

# monster stats
slime = Enemy("Slime", 40, 40, 8, 4, 40, 0, 0, 0, 0, None, "Tutorial", 0)
skeleton = Enemy("Skeleton", 80, 80, 11, 5, 60, 0, 0, 0, 0, None, False, 1)
toxic_slime = Enemy("Toxic Slime", 60, 60, 10, 9, 60, -5, 5, 5, 0.3, None, False, 2)
ice_elemental = Enemy("Ice Elemental", 90, 90, 12, 7, 80, 5, -20, 10, 0, None, False, 3)
fire_elemental = Enemy("Fire Elemental", 70, 70, 14, 7, 80, 0, 10, -20, 0, None, False, 4)
ancient_bat = Enemy("Ancient Bat", 120, 120, 20, 12, 150, 0, -10, -5, 0, None, True, 5)
great_witch = Enemy("Great Witch", 90, 90, 17, 15, 150, -5, 10, 10, 0.2, None, True, 6)

# monster dictionary
monster_dictionary = {
    "mon_0": slime,
    "mon_1": skeleton,
    "mon_2": toxic_slime,
    "mon_3": ice_elemental,
    "mon_4": fire_elemental,
    "mon_5": ancient_bat,
    "mon_6": great_witch
}

# multipliers
strg_multiplier = 0.35
intl_multiplier = 0.35
wep_res_multiplier = 0.5
fire_res_multiplier = 0.5
ice_res_multiplier = 0.5
defn_multiplier = 0.3
run_multiplier = 3
run_base = 0.5
run_min = 0.2


# menus
def menu_1():
    print(
        "(1) Attack\n"
        "(2) Spell\n"
        "(3) Item\n"
        "(4) Run\n"
        "(5) COMBAT INFO"
    )


def menu_2():
    print(
        "(1) " + fireball.name + "         MP: 8\n"
        "(2) " + frost_bolt.name + "       MP: 8\n"
        "(3) CANCEL"
    )


def menu_3():
    print(
        "(1) HP 70 Potion   x " + str(items_1.hp70_pot) + "\n"
        "(2) CANCEL"
    )


def menu_4():
    print(
        "(1) Cursed Doll    x " + str(items_1.cursed_doll) + "\n"
        "(2) CANCEL"
    )


def menu_5():
    print(
        "(1) HP 70 Potion   x " + str(items_1.hp70_pot) + "\n"
        "(2) Cursed Doll    x " + str(items_1.cursed_doll) + "\n"
        "(3) CANCEL"
    )


def menu_6():
    print(
        "(1) MP 50 Potion   x " + str(items_1.mp50_pot) + "\n"
        "(2) CANCEL"
    )


def menu_7():
    print(
        "(1) HP 70 Potion   x " + str(items_1.hp70_pot) + "\n"
        "(2) MP 50 Potion   x " + str(items_1.mp50_pot) + "\n"
        "(3) CANCEL"
    )


def menu_8():
    print(
        "(1) MP 50 Potion   x " + str(items_1.mp50_pot) + "\n"
        "(2) Cursed Doll    x " + str(items_1.cursed_doll) + "\n"
        "(3) CANCEL"
    )


def menu_9():
    print(
        "(1) HP 70 Potion   x " + str(items_1.hp70_pot) + "\n"
        "(2) MP 50 Potion   x " + str(items_1.mp50_pot) + "\n"
        "(3) Cursed Doll    x " + str(items_1.cursed_doll) + "\n"
        "(4) CANCEL"
    )


# intro
game_start = time.time()
print(
    "Welcome Adventurer!\n"
    "You are about to embark on an exciting journey where you will be able to fight fantastical monsters\n"
    "and solve crunchy puzzles. But first... Let's get to know a bit about you.")
contin()

# name
while True:
    protag.name = input("What is your name, traveller? ")
    if protag.name == "":
        print("No name? Then you shall be known as \"The Protagonist.\"")
        protag.name = "The Protagonist"
        break
    elif len(protag.name) <= 24:
        break
    else:
        print("That's a bit too long for my old ears to remember. Again!\n")
        continue

loop_num = 1
for i in protag.name:
    if i in "1234567890" and loop_num == 1:
        print("Your name has numbers in it?! Amazing!\n")
        loop_num += 1
# age
loop_num = 1
while True:
    try:
        if loop_num == 1:
            protag.age = int(input("And how old might you be? "))
            if protag.age < 1:
                print("Haha, something's not right here. Try again!")
                loop_num += 1
                continue
            elif protag.age > 1000000:
                print("That's too old, impossible! Try again.")
                loop_num += 1
                continue
            break
        else:
            protag.age = int(input())
            if protag.age < 1:
                print("Haha, something's not right here. Try again!")
                loop_num += 1
                continue
            elif protag.age > 1000000:
                print("That's too old! Try again.")
                loop_num += 1
                continue
            break
    except ValueError:
        num_err()
        loop_num += 1
        continue

# stats
print(
    "Now for the fun part. Your character will have the chance to fight enemies and your \"stats\" will determine\n"
    "how much damage you do to enemies and how tenacious you are in battle.")
contin()
print(
    "\"Strength\" determines how much your physical attacks do. \"Intelligence\" is for your magical attacks.\n"
    "\"Defence\" will make you take less damage from enemy attacks. And \"Speed\" will decide who acts first\n"
    "and your chances of running from battle.")
contin()
print("Here are your starting stats.")

stats = [
    ['lvl', protag.lvl],
    ['max hp', protag.max_hp],
    ['max mp', protag.max_mp],
    ['strg', protag.strg],
    ['intl', protag.intl],
    ['defn', protag.defn],
    ['spd', protag.spd]
]


def stats_update():
    stats[0][1] = protag.lvl
    stats[1][1] = protag.max_hp
    stats[2][1] = protag.max_mp
    stats[3][1] = protag.strg
    stats[4][1] = protag.intl
    stats[5][1] = protag.defn
    stats[6][1] = protag.spd


for i in stats:
    print(i)
contin()

stats_left = 15

print(
    "I will give you " + str(stats_left) + " extra stats to distribute between strength, intelligence,\n"
    "defence, and speed. The choice is yours!")

add_strg = 0
add_intl = 0
add_defn = 0
add_spd = 0
add_list = [add_strg, add_intl, add_defn, add_spd]

stats_dummy = [
    ["strg", protag.strg],
    ["intl", protag.intl],
    ["defn", protag.defn],
    ["spd", protag.spd]
]

stats_names = ["strength", "intelligence", "defence", "speed"]

y_n = "n"
while True:
    stats_left = 15
    try:
        for i in range(len(add_list)):
            if stats_left == 0 and y_n == "n":
                stats_dummy = [
                    ["strg", protag.strg],
                    ["intl", protag.intl],
                    ["defn", protag.defn],
                    ["spd", protag.spd]
                ]
                add_strg = 0
                add_intl = 0
                add_defn = 0
                add_spd = 0
                add_list = [add_strg, add_intl, add_defn, add_spd]
                continue
            elif stats_left == 0 and y_n == "y":
                break
            while True:
                try:
                    if stats_left == 1:
                        print("\nYou have " + str(stats_left) + " point remaining.")
                    else:
                        print("\nYou have " + str(stats_left) + " points remaining.")
                    add_list[i] = int(input("How many points into " + stats_names[i] + "? "))
                    if add_list[i] < 0:
                        print("No negative numbers!")
                        continue
                    elif add_list[i] <= stats_left:
                        stats_dummy[i][1] += add_list[i]
                        stats_left -= add_list[i]
                        if stats_left == 0:
                            print("\nThis is your current distribution.")
                            for h in stats_dummy:
                                print(h)
                            contin()
                            while True:
                                y_n = input("Would you like to keep this? (y/n) ").lower()
                                if y_n != "y" and y_n != "n":
                                    print("Please type \"y\" or \"n\".\n")
                                    continue
                                else:
                                    break
                        break
                    else:
                        print("You don't have enough points remaining!")
                        continue
                except ValueError:
                    num_err()
                    continue
        if stats_left != 0:
            print("You did not use up all your points! Try again.")
            continue
        elif stats_left == 0 and y_n == "n":
            stats_dummy = [
                ["strg", protag.strg],
                ["intl", protag.intl],
                ["defn", protag.defn],
                ["spd", protag.spd]
            ]
            add_strg = 0
            add_intl = 0
            add_defn = 0
            add_spd = 0
            add_list = [add_strg, add_intl, add_defn, add_spd]
            continue
        elif stats_left == 0 and y_n == "y":
            break
        else:
            break
    except ValueError:
        num_err()
        continue

protag.strg += add_list[0]
protag.intl += add_list[1]
protag.defn += add_list[2]
protag.spd += add_list[3]
stats_update()

added_stats = [
    ["strength", add_list[0]],
    ["intelligence", add_list[1]],
    ["defence", add_list[2]],
    ["speed", add_list[3]]
]

added_stats = sorted(added_stats, key=itemgetter(1), reverse=True)
stat_max = added_stats[0][1]
indices = [stat for stat in range(len(added_stats)) if added_stats[stat][1] == stat_max]
best_stats = []
for index in indices:
    best_stats.append(added_stats[index][0])

# combat tutorial
print("\nNow you are ready to begin your adventure...")
contin()
print(
    "You awake in a tranquil forest as you see light gently shining its way through the trees. There doesn't seem\n"
    "to be any signs of another human around and you are ill with a classic case of protagonist amnesia. You seem\n"
    "to be dressed in thin, ragged clothing and your only equipment is a wooden sword laying beside you.")
protag.weapon = wooden_sword
contin()
print("With no specific direction in mind, you brush yourself off and begin walking on the path in front of you.")
contin()
print("*SHRRRTT*")
contin()
print("The bushes in front of you begin rustling as you immediately ready your sword...")
contin()

current_mon = monster_dictionary.get("mon_0")
mon_encounter()
contin()

print(
    "Looks like you've just encountered your first enemy. Don't worry, I'll step you through how combat works in\n"
    "this game. Throughout your journey, you may experience \"random enemy encounters\". These encounters will\n"
    "usually serve as small roadblocks to your path, but they are handy in conditioning you to fight and giving\n"
    "you much needed experience points to level up your character."
)
contin()
print(
    "Battle works in a turn-based fashion. That is, you and the enemy will take turns doing actions until the battle\n"
    "concludes either with you or the enemy losing the battle, or you successfully running away\n"
    "(only for the cowardly!)."
)
contin()
print(
    "You have 4 main actions available to you: \"Attack\", \"Spell\", \"Item\", and \"Run\".\n"
    "\"Attack\" serves as your normal physical attack.\n"
    "\"Spell\" lets you access a range of magical spells to use.\n"
    "\"Item\" allows you to use any appropriate items you have in battle.\n"
    "\"Run\" gives you a chance to end the encounter."
)
contin()
print(
    "You will be able to access these options by inputting the corresponding number listed next to the action.\n"
    "Try using either \"Attack\" or \"Spell\"."
)
contin()


# combat functions
def dmg_delta_phys():
    damage_delta_phys = list(protag.weapon.wep_range)
    damage_delta_new = []
    for d in damage_delta_phys:
        damage_delta_new.append(
            max(d + math.ceil(protag.strg * strg_multiplier) - math.ceil(current_mon.wep_res * wep_res_multiplier), 0)
        )
    damage_delta_new.sort()
    return damage_delta_new


def attack():
    damage_dealt = random.randint(damage_range[0], damage_range[len(damage_range)-1])
    current_mon.hp -= damage_dealt
    print("You strike with your " + wooden_sword.name + ".")
    print("You did " + str(damage_dealt) + " damage!")
    return current_mon.hp


def spell_1():
    damage_delta_mag = list(fireball.dmg_range)
    damage_delta_new = []
    for d in damage_delta_mag:
        damage_delta_new.append(
            max(d + math.ceil(protag.intl * intl_multiplier) - math.ceil(current_mon.fire_res * fire_res_multiplier), 0)
        )
    damage_delta_new.sort()
    damage_dealt = random.randint(damage_delta_new[0], damage_delta_new[len(damage_delta_new)-1])
    current_mon.hp -= damage_dealt
    print("You cast a mighty fireball.")
    print("You did " + str(damage_dealt) + " damage!")
    protag.mp -= fireball.mp_cost
    if random.random() < fireball.status_chance and current_mon.status is None and current_mon.hp > 0:
        current_mon.status = brn_lv1
        print("The " + current_mon.name + " was burned!")
    return current_mon.hp, protag.mp, current_mon.status


def spell_2():
    damage_delta_mag = list(frost_bolt.dmg_range)
    damage_delta_new = []
    for d in damage_delta_mag:
        damage_delta_new.append(
            max(d + math.ceil(protag.intl * intl_multiplier) - math.ceil(current_mon.ice_res * ice_res_multiplier), 0)
        )
    damage_delta_new.sort()
    damage_dealt = random.randint(damage_delta_new[0], damage_delta_new[len(damage_delta_new) - 1])
    current_mon.hp -= damage_dealt
    print("You cast a chilling blast of ice.")
    print("You did " + str(damage_dealt) + " damage!")
    protag.mp -= frost_bolt.mp_cost
    if random.random() < frost_bolt.status_chance and current_mon.status is None and current_mon.hp > 0:
        current_mon.status = frz
        print("The " + current_mon.name + " was frozen!")
    return current_mon.hp, protag.mp, current_mon.status


def use_hp_pot():
    items_1.hp70_pot -= 1
    new_hp = min(protag.hp + 70, protag.max_hp)
    print("You used the potion and healed " + str(new_hp - protag.hp) + " HP!")
    protag.hp = new_hp
    return items_1.hp70_pot, protag.hp


def use_mp_pot():
    items_1.mp50_pot -= 1
    new_mp = min(protag.mp + 50, protag.max_mp)
    print("You used the potion and healed " + str(new_mp - protag.mp) + " MP!")
    protag.mp = new_mp
    return items_1.mp50_pot, protag.mp


def use_doll():
    if current_mon is not great_witch:
        print("It doesn't seem like you can use this here...")
    elif current_mon is great_witch and current_mon.hp > 0.5 * current_mon.max_hp:
        print("The " + current_mon.name + " seems too enraged to listen. You'll have to fight for now...")
    elif current_mon is great_witch and current_mon.hp <= 0.5 * current_mon.max_hp:
        print("\"Could it be? Is that my daughter you hold in your hands?\"")
        items_1.used_doll = True
        return items_1.used_doll


def run():
    if current_mon.boss is True:
        print("You can't run away from a boss!")
        run_success = False
    elif current_mon.boss == "Tutorial":
        print("This is the tutorial. No running!")
        run_success = False
    elif random.random() < max(run_base + (protag.spd - current_mon.spd) * run_multiplier * 0.01, run_min):
        print("You ran away successfully!")
        run_success = True
    else:
        print("You tried but couldn't escape from battle...")
        run_success = False
    return run_success


def combat_info():
    print(
        "The enemy " + current_mon.name + " has " + str(current_mon.hp) +
        "/" + str(current_mon.max_hp) + " HP remaining.\n"
        "You have " + str(protag.hp) + "/" + str(protag.max_hp) + " HP and "
        + str(protag.mp) + "/" + str(protag.max_mp) + " MP remaining."
    )


def battle_end():
    print("The enemy's health was reduced to zero! You win the battle!")
    print("You gained " + str(current_mon.exp) + " EXP!")
    contin()
    protag.exp += current_mon.exp
    while True:
        if protag.exp >= level_dict[str(protag.lvl)].threshold:
            level_dummy = [
                ['lvl     ', protag.lvl, '  >', protag.lvl],
                ["max_hp  ", protag.max_hp, '>', protag.max_hp],
                ["max_mp  ", protag.max_mp, ' >', protag.max_mp],
                ["strg    ", protag.strg, ' >', protag.strg],
                ["intl    ", protag.intl, '  >', protag.intl],
                ["defn    ", protag.defn, '  >', protag.defn],
                ["spd     ", protag.spd, '  >', protag.spd],
            ]
            protag.exp -= level_dict[str(protag.lvl)].threshold
            protag.max_hp += level_dict[str(protag.lvl)].hp_gain
            protag.hp += level_dict[str(protag.lvl)].hp_gain
            protag.max_mp += level_dict[str(protag.lvl)].mp_gain
            protag.mp += level_dict[str(protag.lvl)].mp_gain
            protag.strg += level_dict[str(protag.lvl)].strg_gain
            protag.intl += level_dict[str(protag.lvl)].intl_gain
            protag.defn += level_dict[str(protag.lvl)].defn_gain
            protag.spd += level_dict[str(protag.lvl)].spd_gain
            protag.lvl += 1
            print("You leveled up!")
            level_dummy_2 = [protag.lvl, protag.max_hp, protag.max_mp,
                             protag.strg, protag.intl, protag.defn, protag.spd]
            for le in range(len(level_dummy)):
                level_dummy[le][3] = level_dummy_2[le]
                print(level_dummy[le])
            contin()
            if protag.exp >= level_dict[str(protag.lvl)].threshold:
                continue
        else:
            break
    protag.status = None
    protag.status_initial = True
    return protag.lvl, protag.exp, protag.max_hp, protag.hp, protag.max_mp, protag.mp, \
        protag.strg, protag.intl, protag.defn, protag.spd, protag.status, protag.status_initial


def status_effect_hero():
    if protag.status == psn and protag.status_initial is True:
        protag.duration = 3
        protag.status_initial = False
    if protag.status == psn:
        print("You are poisoned and take " + str(psn.damage) + " damage.")
        contin()
        protag.hp -= psn.damage
        protag.duration -= 1
        if protag.duration == 0:
            protag.status = None
            protag.status_initial = True
            if protag.hp >= 0:
                print("The poison has worn off.")
                contin()
    if protag.hp <= 0:
        game_over()
    return protag.hp, protag.status, protag.duration, protag.status_initial


def status_effect_mon():
    if current_mon.status == brn_lv1:
        print("The enemy is burned and takes " + str(brn_lv1.damage) + " damage.")
        contin()
        current_mon.hp -= brn_lv1.damage
    return current_mon.hp, current_mon.status


def status_effect_start_turn():
    if current_mon.status == frz:
        print("The enemy is frozen solid and can't move!")
        contin()
        current_mon.status = un_frz
    elif current_mon.status == un_frz:
        print("The enemy thaws out and can act again!")
        contin()
        current_mon.status = None
    return current_mon.hp, current_mon.status


# action sequence
while True:
    if current_mon.spd > protag.spd:
        print("The enemy was faster than you and acts first!")
        contin()
        status_effect_start_turn()
        if current_mon.status == un_frz:
            break
        current_mon.mon_attack()
        status_effect_mon()
        if current_mon.hp <= 0:
            battle_end()
            break
    break
while True:
    if current_mon.hp <= 0:
        battle_end()
        break
    while True:
        menu_1()
        action_1 = action_sel()
        if action_1 == "1":
            damage_range = dmg_delta_phys()
            attack()
            contin()
            break
        elif action_1 == "2":
            while True:
                menu_2()
                action_2 = action_sel()
                if action_2 == "1":
                    if fireball.mp_cost > protag.mp:
                        no_mp()
                        contin()
                        continue
                    spell_1()
                    contin()
                    break
                elif action_2 == "2":
                    if frost_bolt.mp_cost > protag.mp:
                        no_mp()
                        contin()
                        continue
                    spell_2()
                    contin()
                    break
                elif action_2 == "3":
                    break
                else:
                    action_err()
                    continue
            if action_2 == "3":
                continue
            else:
                break
        elif action_1 == "3":
            if items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                no_items()
                contin()
                continue
            elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                while True:
                    menu_3()
                    action_3 = action_sel()
                    if action_3 == "1":
                        if protag.hp == protag.max_hp:
                            max_health()
                            contin()
                            continue
                        use_hp_pot()
                        contin()
                        break
                    elif action_3 == "2":
                        break
                    else:
                        action_err()
                        continue
                if action_3 == "2":
                    continue
                else:
                    break
            elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                while True:
                    menu_4()
                    action_4 = action_sel()
                    if action_4 == "1":
                        if current_mon is not great_witch:
                            use_doll()
                            contin()
                            continue
                        elif current_mon is great_witch:
                            use_doll()
                            contin()
                            break
                    elif action_4 == "2":
                        break
                    else:
                        action_err()
                        continue
                if action_4 == "2":
                    continue
                else:
                    break
            elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                while True:
                    menu_5()
                    action_5 = action_sel()
                    if action_5 == "1":
                        if protag.hp == protag.max_hp:
                            max_health()
                            contin()
                            continue
                        use_hp_pot()
                        contin()
                        break
                    elif action_5 == "2":
                        if current_mon is not great_witch:
                            use_doll()
                            contin()
                            continue
                        elif current_mon is great_witch:
                            use_doll()
                            contin()
                            break
                    elif action_5 == "3":
                        break
                    else:
                        action_err()
                        continue
                if action_5 == "3":
                    continue
                else:
                    break
            elif items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                while True:
                    menu_6()
                    action_6 = action_sel()
                    if action_6 == "1":
                        if protag.mp == protag.max_mp:
                            max_mana()
                            contin()
                            continue
                        use_mp_pot()
                        contin()
                        break
                    elif action_6 == "2":
                        break
                    else:
                        action_err()
                        continue
                if action_6 == "2":
                    continue
                else:
                    break
            elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                while True:
                    menu_7()
                    action_7 = action_sel()
                    if action_7 == "1":
                        if protag.hp == protag.max_hp:
                            max_health()
                            contin()
                            continue
                        use_hp_pot()
                        contin()
                        break
                    elif action_7 == "2":
                        if protag.mp == protag.max_mp:
                            max_mana()
                            contin()
                            continue
                        use_mp_pot()
                        contin()
                        break
                    elif action_7 == "3":
                        break
                    else:
                        action_err()
                        continue
                if action_7 == "3":
                    continue
                else:
                    break
            elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                while True:
                    menu_8()
                    action_8 = action_sel()
                    if action_8 == "1":
                        if protag.mp == protag.max_mp:
                            max_mana()
                            contin()
                            continue
                        use_mp_pot()
                        contin()
                        break
                    elif action_8 == "2":
                        if current_mon is not great_witch:
                            use_doll()
                            contin()
                            continue
                        elif current_mon is great_witch:
                            use_doll()
                            contin()
                            break
                    elif action_8 == "3":
                        break
                    else:
                        action_err()
                        continue
                if action_8 == "3":
                    continue
                else:
                    break
            elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                while True:
                    menu_9()
                    action_9 = action_sel()
                    if action_9 == "1":
                        if protag.hp == protag.max_hp:
                            max_health()
                            contin()
                            continue
                        use_hp_pot()
                        contin()
                        break
                    elif action_9 == "2":
                        if protag.mp == protag.max_mp:
                            max_mana()
                            contin()
                            continue
                        use_mp_pot()
                        contin()
                        break
                    elif action_9 == "3":
                        if current_mon is not great_witch:
                            use_doll()
                            contin()
                            continue
                        elif current_mon is great_witch:
                            use_doll()
                            contin()
                            break
                    elif action_9 == "4":
                        break
                    else:
                        action_err()
                        continue
                if action_9 == "4":
                    continue
                else:
                    break
        elif action_1 == "4":
            run_result = run()
            contin()
            if current_mon.boss == "Tutorial":
                continue
            else:
                break
        elif action_1 == "5":
            combat_info()
            contin()
            continue
        else:
            action_err()
            continue
    if run_result is True:
        protag.status = None
        protag.status_initial = True
        run_result = False
        break
    if current_mon.hp <= 0:
        battle_end()
        break
    status_effect_hero()
    status_effect_start_turn()
    if current_mon.status == un_frz:
        continue
    current_mon.mon_attack()
    status_effect_mon()
    if current_mon.hp <= 0:
        battle_end()
        break
    continue

# npc encounter 1

print("Congratulations! You've taken down your first enemy! Whether you triumph or fail in the rest of your\n"
      "journey is now up to you. Farewell, and I hope to see you on the other side...")
contin()
print("After fighting off the " + current_mon.name + ", you catch your breath and continue walking on the path\n"
      "in front of you. You make it out of the shade of the forest and reach a three-pronged fork in the road.")
contin()
print(
    "To your left, you see a desolate road ahead filled with nothing but rocks and dirt. In the far distance\n"
    "there seems to be a craggy mountain.\n"
    "Directly in front, another forest not unlike the one you just stepped out of. Except this one seems to\n"
    "emit a slight haze and foreboding presence.\n"
    "As you consider your options, you realise a woman on the path to the right begins to approach you.\n"
    "She seems to be wheeling cabbages."
)
contin()
print("\"Hey! You look like you're in a daze.\"")
contin()
print(
    "Without wanting to involve a stranger into your amnesiac troubles you quickly come up with a line.\n"
    "\"I'm an adventurer from a far away town. Just looking for some direction if you could spare some.\""
)
contin()
print(
    "\"Ahh... Well I saw you eyeing the paths in front of you. The mountain to your left wouldn't be too\n"
    "too difficult to reach. There are reports of a beast that lives inside the cave there that terrorises\n"
    "the townsfolk on the other side. You'd be doing them a great service if you investigated that problem.\"\n"
    "\"For the forest in front of you, well there isn't much to see but bugs and trees. Lots of them! I sometimes\n"
    "gather mushrooms from the outskirts. It's rumoured that a mother who once lost their daughter in that\n"
    "very forest now haunts it. She ran into the forest looking for her daughter that hadn't come back\n"
    "after being told to gather ingredients. Neither of them were ever seen to return.\""
)
contin()
print("\"But that's just a rumour! Ha Ha Ha!!\"")
contin()

# significant choice

print(
    "After listening to who might very well be a mad woman, you make your choice.\n"
    "WARNING: Your decision will significantly affect the rest of your journey."
)
while True:
    choice = input("(1) Mountainous path to the left.\n"
                   "(2) Suspicious forest straight ahead.\n")
    if choice != "1" and choice != "2":
        action_err()
        continue
    else:
        break

# game path 1

if choice == "1":
    print("\"I think I'll see what's going on inside that cave.\"")
    contin()
    print("\"In that case, let me give you these to aid you on your journey.\"\n"
          "The woman hands you some glass containers holding red and blue liquids.")
    contin()
    items_1.hp70_pot += 2
    items_1.mp50_pot += 1
    print(
        "You received:\n"
        "2 x HP 70 Potion\n"
        "1 x MP 50 Potion"
    )
    contin()
    print("\"Now I'll get back to where I was going and leave you on your way.\"\n"
          "The woman wheels her cart past you as you put away the potions that she gave you.\n"
          "You begin to set out on the rocky path ahead.")
    contin()
    print("After walking for what seems like an eternity, you finally reach the bottom of the mountain at the\n"
          "end of the path. \"Well, only one way up.\"")
    contin()
    print("As you prepare to climb up, a monster appears from behind the rocks!")
    contin()

    # random encounter 1

    monster_roll = random.random()
    if 0 <= monster_roll < 0.5:
        current_mon = monster_dictionary.get("mon_1")
        mon_encounter()
        contin()
    elif 0.5 <= monster_roll < 1:
        current_mon = monster_dictionary.get("mon_2")
        mon_encounter()
        contin()
    while True:
        if current_mon.spd > protag.spd:
            print("The enemy was faster than you and acts first!")
            contin()
            status_effect_start_turn()
            if current_mon.status == un_frz:
                break
            current_mon.mon_attack()
            status_effect_mon()
            if current_mon.hp <= 0:
                battle_end()
                break
        break
    while True:
        if current_mon.hp <= 0:
            battle_end()
            break
        while True:
            menu_1()
            action_1 = action_sel()
            if action_1 == "1":
                damage_range = dmg_delta_phys()
                attack()
                contin()
                break
            elif action_1 == "2":
                while True:
                    menu_2()
                    action_2 = action_sel()
                    if action_2 == "1":
                        if fireball.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_1()
                        contin()
                        break
                    elif action_2 == "2":
                        if frost_bolt.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_2()
                        contin()
                        break
                    elif action_2 == "3":
                        break
                    else:
                        action_err()
                        continue
                if action_2 == "3":
                    continue
                else:
                    break
            elif action_1 == "3":
                if items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    no_items()
                    contin()
                    continue
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    while True:
                        menu_3()
                        action_3 = action_sel()
                        if action_3 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_3 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_3 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_4()
                        action_4 = action_sel()
                        if action_4 == "1":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_4 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_4 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_5()
                        action_5 = action_sel()
                        if action_5 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_5 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_5 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_5 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_6()
                        action_6 = action_sel()
                        if action_6 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_6 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_6 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_7()
                        action_7 = action_sel()
                        if action_7 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_7 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_7 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_7 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_8()
                        action_8 = action_sel()
                        if action_8 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_8 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_8 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_8 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_9()
                        action_9 = action_sel()
                        if action_9 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_9 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_9 == "3":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_9 == "4":
                            break
                        else:
                            action_err()
                            continue
                    if action_9 == "4":
                        continue
                    else:
                        break
            elif action_1 == "4":
                run_result = run()
                contin()
                if current_mon.boss == "Tutorial":
                    continue
                else:
                    break
            elif action_1 == "5":
                combat_info()
                contin()
                continue
            else:
                action_err()
                continue
        if run_result is True:
            protag.status = None
            protag.status_initial = True
            run_result = False
            break
        if current_mon.hp <= 0:
            battle_end()
            break
        status_effect_hero()
        status_effect_start_turn()
        if current_mon.status == un_frz:
            continue
        current_mon.mon_attack()
        status_effect_mon()
        if current_mon.hp <= 0:
            battle_end()
            break
        continue
    print("After attending to the monster, you begin your ascent.")
    contin()

    # quick-time event

    print("You grab the ledge above you with your right hand. The one above that with your left.\n"
          "Right. Left. Right. Left.")
    contin()
    print("The sun beats down on you.")
    contin()
    print("You reach out to grab the next ledge...")
    contin()

    timeout = 1.2
    t = Timer(timeout, print, ["You couldn't grab the ledge in time and fell down!"])
    t.start()
    start_time = time.time()
    prompt = "...your hand slips! Quick! Press \"ENTER\" to re-grab the ledge!\n"
    answer = input(prompt)
    t.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if reaction_time > timeout:
        print("You take 20 damage from the fall.")
        qte1 = False
        if protag.hp > 20:
            protag.hp -= 20
        elif protag.hp <= 20:
            protag.hp = 1
    else:
        print("Your hand grabs the ledge in time!")
        qte1 = True
    contin()

    print("With a final burst of energy, you quickly scale the rest of the cliff face.\n"
          "You aren't at the top yet, but you arrive at an entrance leading into the mountain.\n"
          "Feeling exhausted, you camp out for the night...")
    contin()
    print("...")
    contin()
    print("As you wake up to a new day, you steel yourself and head into the cave.\n"
          "There are several torches at the entrance and you take one and light it up with a bit of magic.\n"
          "You press on into the darkness...")
    contin()

    # puzzle 1

    print("You come up to what seems like a magically-infused door unalike the rest of your surroundings.\n"
          "Upon closer inspection, you are faced with a riddle...")
    contin()
    print("A Jewish rock star has a very busy schedule as an entertainer. Throughout the week, they are\n"
          "constantly filling the world with awesomeness.\n"
          "On the first day, they rocked. On the second, they rolled. The third, rocked. Fourth, rolled.\n"
          "And so on and so forth.\n"
          "What did they do on the seventh day?")

    secret_word = "RESTED"
    guess = ""
    guess_count = 0
    guess_limit = 3
    guess_remaining = guess_limit - guess_count
    out_of_guesses = False

    while guess.upper() != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input(f"Enter your answer (Guesses left: {guess_remaining}): ")
            print("")
            guess_count += 1
            guess_remaining = guess_limit - guess_count
        else:
            out_of_guesses = True
        if guess_count == 1 and guess.upper() != secret_word:
            print("HINT: The answer starts with the letter \"r\".")
        elif guess_count == 2 and guess.upper() != secret_word:
            print("HINT: They neither rocked, nor rolled.")

    if out_of_guesses:
        puzzle1 = False
        print("Unable to solve the riddle, the door stays shut.")
        contin()
        print("You give it another look-over and the integrity of the door seems compromised and\n"
              "weathered through the curse of time.")
        contin()
        print("...")
        contin()
        print("You take a step back and crash yourself through the door!\n"
              "*BANG*\n"
              "The foundation gives way behind you and crumbles, leaving the path behind blocked off and \n"
              "a mysterious red and blue liquid on the floor.")
        contin()
        print("Being left a little worse for wear, you continue forward.\n"
              "Out of the corner of your eye, you spot something ready to jump out at you as you ready your sword...")
        contin()
    else:
        puzzle1 = True
        print("Using your superior wit, the door gives way to you and opens.")
        contin()
        print("A red and blue potion are presented to you on the other side of the door.")
        contin()
        items_1.hp70_pot += 1
        items_1.mp50_pot += 1
        print(
            "You received:\n"
            "1 x HP 70 Potion\n"
            "1 x MP 50 Potion"
        )
        contin()
        print("You press on but not before another monster jumps out at you...")
        contin()

    # random encounter 2

    monster_roll = random.random()
    if 0 <= monster_roll < 0.5:
        current_mon = monster_dictionary.get("mon_3")
        mon_encounter()
        contin()
    elif 0.5 <= monster_roll < 1:
        current_mon = monster_dictionary.get("mon_4")
        mon_encounter()
        contin()
    while True:
        if current_mon.spd > protag.spd:
            print("The enemy was faster than you and acts first!")
            contin()
            status_effect_start_turn()
            if current_mon.status == un_frz:
                break
            current_mon.mon_attack()
            status_effect_mon()
            if current_mon.hp <= 0:
                battle_end()
                break
        break
    while True:
        if current_mon.hp <= 0:
            battle_end()
            break
        while True:
            menu_1()
            action_1 = action_sel()
            if action_1 == "1":
                damage_range = dmg_delta_phys()
                attack()
                contin()
                break
            elif action_1 == "2":
                while True:
                    menu_2()
                    action_2 = action_sel()
                    if action_2 == "1":
                        if fireball.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_1()
                        contin()
                        break
                    elif action_2 == "2":
                        if frost_bolt.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_2()
                        contin()
                        break
                    elif action_2 == "3":
                        break
                    else:
                        action_err()
                        continue
                if action_2 == "3":
                    continue
                else:
                    break
            elif action_1 == "3":
                if items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    no_items()
                    contin()
                    continue
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    while True:
                        menu_3()
                        action_3 = action_sel()
                        if action_3 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_3 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_3 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_4()
                        action_4 = action_sel()
                        if action_4 == "1":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_4 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_4 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_5()
                        action_5 = action_sel()
                        if action_5 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_5 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_5 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_5 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_6()
                        action_6 = action_sel()
                        if action_6 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_6 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_6 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_7()
                        action_7 = action_sel()
                        if action_7 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_7 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_7 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_7 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_8()
                        action_8 = action_sel()
                        if action_8 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_8 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_8 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_8 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_9()
                        action_9 = action_sel()
                        if action_9 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_9 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_9 == "3":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_9 == "4":
                            break
                        else:
                            action_err()
                            continue
                    if action_9 == "4":
                        continue
                    else:
                        break
            elif action_1 == "4":
                run_result = run()
                contin()
                if current_mon.boss == "Tutorial":
                    continue
                else:
                    break
            elif action_1 == "5":
                combat_info()
                contin()
                continue
            else:
                action_err()
                continue
        if run_result is True:
            protag.status = None
            protag.status_initial = True
            run_result = False
            break
        if current_mon.hp <= 0:
            battle_end()
            break
        status_effect_hero()
        status_effect_start_turn()
        if current_mon.status == un_frz:
            continue
        current_mon.mon_attack()
        status_effect_mon()
        if current_mon.hp <= 0:
            battle_end()
            break
        continue
    print("You push farther into the cave and reach what seems to be the darkest recesses.")
    contin()
    print("You wave your torch in front of you to get a better view of the room when suddenly, two crimson eyes\n"
          "light up and stare directly into your being...")
    contin()
    print("A ginormous winged beast rears above you and blows you back with a great gust.\n"
          "Your torch gets blown out and the whole room lights up with fire.\n"
          "Seemingly unable to catch a break, you know this is the beast that has been terrorising the villagers.")
    contin()
    print("Only one way out of here alive, you prepare yourself to fight...")
    contin()

    # boss encounter 1

    current_mon = monster_dictionary.get("mon_5")
    mon_encounter()
    contin()
    while True:
        if current_mon.spd > protag.spd:
            print("The enemy was faster than you and acts first!")
            contin()
            status_effect_start_turn()
            if current_mon.status == un_frz:
                break
            current_mon.mon_attack()
            status_effect_mon()
            if current_mon.hp <= 0:
                battle_end()
                break
        break
    while True:
        if current_mon.hp <= 0:
            battle_end()
            break
        while True:
            menu_1()
            action_1 = action_sel()
            if action_1 == "1":
                damage_range = dmg_delta_phys()
                attack()
                contin()
                break
            elif action_1 == "2":
                while True:
                    menu_2()
                    action_2 = action_sel()
                    if action_2 == "1":
                        if fireball.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_1()
                        contin()
                        break
                    elif action_2 == "2":
                        if frost_bolt.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_2()
                        contin()
                        break
                    elif action_2 == "3":
                        break
                    else:
                        action_err()
                        continue
                if action_2 == "3":
                    continue
                else:
                    break
            elif action_1 == "3":
                if items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    no_items()
                    contin()
                    continue
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    while True:
                        menu_3()
                        action_3 = action_sel()
                        if action_3 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_3 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_3 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_4()
                        action_4 = action_sel()
                        if action_4 == "1":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_4 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_4 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_5()
                        action_5 = action_sel()
                        if action_5 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_5 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_5 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_5 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_6()
                        action_6 = action_sel()
                        if action_6 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_6 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_6 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_7()
                        action_7 = action_sel()
                        if action_7 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_7 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_7 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_7 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_8()
                        action_8 = action_sel()
                        if action_8 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_8 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_8 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_8 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_9()
                        action_9 = action_sel()
                        if action_9 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_9 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_9 == "3":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_9 == "4":
                            break
                        else:
                            action_err()
                            continue
                    if action_9 == "4":
                        continue
                    else:
                        break
            elif action_1 == "4":
                run_result = run()
                contin()
                if current_mon.boss == "Tutorial":
                    continue
                else:
                    break
            elif action_1 == "5":
                combat_info()
                contin()
                continue
            else:
                action_err()
                continue
        if run_result is True:
            protag.status = None
            protag.status_initial = True
            run_result = False
            break
        if current_mon.hp <= 0:
            battle_end()
            break
        status_effect_hero()
        status_effect_start_turn()
        if current_mon.status == un_frz:
            continue
        current_mon.mon_attack()
        status_effect_mon()
        if current_mon.hp <= 0:
            battle_end()
            break
        continue

    print("After a long and hard fought battle, you emerge victorious over the big bat.\n"
          "You stand tired, but triumphant that you managed to fell such a creature.\n"
          "Hopefully the villagers will reward you handsomely for your efforts.")
    contin()
    print("Completely bone-tired, you are barely able to drag yourself out of the cave on the other side.\n"
          "After being in the cave for so long, the light blinds you as you step out.\n"
          "You fall onto the ground in utter fatigue.")
    contin()
    print("You see people running towards you and you let them cart you away, unable to move. They seem pleasant.")
    contin()
    print("The last thing you see is the sun setting over the horizon as you pass out...")
    contin()
    game_end = time.time()
    game_duration = game_end - game_start
    print("CONGRATULATIONS! You've completed this short text-based role-playing game in "
          f"{time.strftime('%M:%S', time.gmtime(game_duration))}.\n"
          "This is just 1 of 3 possible endings so feel free to replay the game if you enjoyed it!\n"
          "The following paragraph details your accomplishments in the run, share it\n"
          "(highlight > right click > copy > paste) with the creator or others who have played the game (:")
    contin()

    if protag.age <= 12:
        age_description = "irresponsibly young"
    elif 12 < protag.age <= 18:
        age_description = "youthful"
    elif 18 < protag.age <= 29:
        age_description = "energetic"
    elif 29 < protag.age <= 69:
        age_description = "mature"
    elif 69 < protag.age <= 100:
        age_description = "ripe old"
    else:
        age_description = "wickedly old"

    if len(best_stats) > 1:
        stat_description = "a balance in stats"
    else:
        stat_description = best_stats[0]

    if qte1 is False:
        qte1_description = "Unfortunately they sustained damage on the way as their reaction time wasn't the best."
    else:
        qte1_description = "Their quick thinking allowed them to surmount great heights."
    if puzzle1 is False:
        puzzle1_description = "Lacking a sharp mind, they blew through obstacles rather than using thinking."
    else:
        puzzle1_description = "Being a learned scholar, they gracefully made their way through riddles."

    print(
        "The Protagonist's Journey:\n"
        f"{protag.name} was an adventurer that favoured {stat_description} above all else.\n"
        f"At the {age_description} age of {protag.age}, they managed to fell a great beast in the caves.\n"
        f"{qte1_description}\n"
        f"{puzzle1_description}\n"
        f"The villagers of the land celebrated in {protag.name}'s endeavours and all was well in the land."
    )
    contin()
    print("Thanks for playing!")

# game path 2

if choice == "2":
    print("\"Hmm... the forest intrigues me.\"")
    contin()
    print("\"Well I can't stop you! Let me give you these.\"\n"
          "The woman hands you some glass containers holding red and blue liquids.")
    contin()
    items_1.hp70_pot += 2
    items_1.mp50_pot += 1
    print(
        "You received:\n"
        "2 x HP 70 Potion\n"
        "1 x MP 50 Potion"
    )
    contin()
    print("\"Now I should hurry along now. Safe travels!\"\n"
          "The woman pushes her cart past you as you bag the potions that you received.\n"
          "You start walking into the misty forest.")
    contin()
    print("As you get closer, the fog begins to clear and the forest transforms into a beautiful night scene.\n"
          "Unique plants glow in the darkness and ferns sprout from the sides inviting you in.")
    contin()
    print("Before you can make any more progress, a creature appears from behind the grasses.")
    contin()

    # random encounter 1

    monster_roll = random.random()
    if 0 <= monster_roll < 0.5:
        current_mon = monster_dictionary.get("mon_1")
        mon_encounter()
        contin()
    elif 0.5 <= monster_roll < 1:
        current_mon = monster_dictionary.get("mon_2")
        mon_encounter()
        contin()
    while True:
        if current_mon.spd > protag.spd:
            print("The enemy was faster than you and acts first!")
            contin()
            status_effect_start_turn()
            if current_mon.status == un_frz:
                break
            current_mon.mon_attack()
            status_effect_mon()
            if current_mon.hp <= 0:
                battle_end()
                break
        break
    while True:
        if current_mon.hp <= 0:
            battle_end()
            break
        while True:
            menu_1()
            action_1 = action_sel()
            if action_1 == "1":
                damage_range = dmg_delta_phys()
                attack()
                contin()
                break
            elif action_1 == "2":
                while True:
                    menu_2()
                    action_2 = action_sel()
                    if action_2 == "1":
                        if fireball.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_1()
                        contin()
                        break
                    elif action_2 == "2":
                        if frost_bolt.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_2()
                        contin()
                        break
                    elif action_2 == "3":
                        break
                    else:
                        action_err()
                        continue
                if action_2 == "3":
                    continue
                else:
                    break
            elif action_1 == "3":
                if items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    no_items()
                    contin()
                    continue
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    while True:
                        menu_3()
                        action_3 = action_sel()
                        if action_3 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_3 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_3 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_4()
                        action_4 = action_sel()
                        if action_4 == "1":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_4 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_4 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_5()
                        action_5 = action_sel()
                        if action_5 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_5 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_5 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_5 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_6()
                        action_6 = action_sel()
                        if action_6 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_6 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_6 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_7()
                        action_7 = action_sel()
                        if action_7 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_7 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_7 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_7 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_8()
                        action_8 = action_sel()
                        if action_8 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_8 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_8 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_8 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_9()
                        action_9 = action_sel()
                        if action_9 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_9 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_9 == "3":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_9 == "4":
                            break
                        else:
                            action_err()
                            continue
                    if action_9 == "4":
                        continue
                    else:
                        break
            elif action_1 == "4":
                run_result = run()
                contin()
                if current_mon.boss == "Tutorial":
                    continue
                else:
                    break
            elif action_1 == "5":
                combat_info()
                contin()
                continue
            else:
                action_err()
                continue
        if run_result is True:
            protag.status = None
            protag.status_initial = True
            run_result = False
            break
        if current_mon.hp <= 0:
            battle_end()
            break
        status_effect_hero()
        status_effect_start_turn()
        if current_mon.status == un_frz:
            continue
        current_mon.mon_attack()
        status_effect_mon()
        if current_mon.hp <= 0:
            battle_end()
            break
        continue
    print("You continue deeper into the forest.")
    contin()

    # quick-time event

    print("As you wander deeper, your surroundings seem to creep in on you and you notice the light\n"
          "become ever so slightly dimmer.")
    contin()
    print("\"HEY YOU!\"")
    contin()
    print("A fairy flits into view and catches your attention.\n"
          "\"I don't know what brought you into this forest, but I think you're the one I've been looking for!\"")
    contin()
    print("\"Answer this question for me! You'll have to be quick though...\"")
    contin()

    fairy_answer = ["MUSHROOM", "MUSHROOMS"]
    timeout = 10
    t = Timer(timeout, print, ["\"AHH! YOU'RE TOO SLOW!!\""])
    t.start()
    start_time = time.time()
    prompt = "\"What can be gathered on the edge of the forest?? You have 10 seconds to answer!\"\n"
    answer = input(prompt)
    t.cancel()
    end_time = time.time()
    reaction_time = end_time - start_time
    if answer.upper() not in fairy_answer and reaction_time < timeout:
        print("\"That's not right at all!\"\n"
              "The fairy looks visibly angry and casts a hurtful enchantment on you.")
        contin()
        protag.status = psn
        print("You were poisoned!")
        contin()
        qte2 = False
    elif answer.upper() in fairy_answer and reaction_time < timeout:
        print("\"CORRECT-O-MUNDO! Let me give you a little of my magic.\"")
        contin()
        protag.hp = protag.max_hp
        protag.mp = protag.max_mp
        print("You were fully healed!")
        contin()
        qte2 = True
    else:
        print("The fairy looks visibly angry and casts a hurtful enchantment on you.")
        contin()
        protag.status = psn
        print("You were poisoned!")
        contin()
        qte2 = False

    print("Completely astonished by how this fairy is stealing the show, you dumbly follow along.\n"
          "\"Here... I'll give you another puzzle!\"\n"
          "\"Don't worry, there's no time limit on this one. But you only get one shot!\"")
    contin()

    # puzzle 2

    secret_word = "1"
    print("Five people are forcibly brought to the town centre for questioning. Here are their statements.\n"
          "A: \"Only one out of the five of us is lying.\"\n"
          "B: \"Two of the five of us are lying.\"\n"
          "C: \"Don't listen to these guys, three of the five of us are lying.\"\n"
          "D: \"Listen here, out of the five of us, four are lying.\"\n"
          "E: \"HA HA HA! All five of us are filthy liars!\"")
    guess = input("How many people are telling the truth? (input a number): ")
    print("")

    if guess == secret_word:
        puzzle2 = True
        print("\"That's right! They should let \"D\" go for sure!\"")
        contin()
        print("\"I think you've proved you're worthy of having this!\"\n"
              "The fairy hands you a ragged-looking doll. You're not quite sure its purpose, but its eyes\n"
              "incite a feeling of sadness.")
        contin()
        items_1.cursed_doll += 1
        print(
            "You received:\n"
            "1 x Cursed Doll"
        )
        contin()
        print("\"I should go now. Good luck with everything! GOODBYE!!\"\n"
              "You watch as the fairy flicks back into the darkness of the forest leaving you by yourself.")
        contin()
    else:
        puzzle2 = False
        print("\"Tsk tsk... I'm not impressed at all. Don't worry, I won't bother you anymore.\"\n"
              "And just like that, the fairy darts away leaving you alone in the forest again.")
        contin()
    print("With that out of the way, you continue on your way through the forest but not before something\n"
          "jumps out at you...")
    contin()

    # random encounter 2

    monster_roll = random.random()
    if 0 <= monster_roll < 0.5:
        current_mon = monster_dictionary.get("mon_3")
        mon_encounter()
        contin()
    elif 0.5 <= monster_roll < 1:
        current_mon = monster_dictionary.get("mon_4")
        mon_encounter()
        contin()
    while True:
        if current_mon.spd > protag.spd:
            print("The enemy was faster than you and acts first!")
            contin()
            status_effect_start_turn()
            if current_mon.status == un_frz:
                break
            current_mon.mon_attack()
            status_effect_mon()
            if current_mon.hp <= 0:
                battle_end()
                break
        break
    while True:
        if current_mon.hp <= 0:
            battle_end()
            break
        while True:
            menu_1()
            action_1 = action_sel()
            if action_1 == "1":
                damage_range = dmg_delta_phys()
                attack()
                contin()
                break
            elif action_1 == "2":
                while True:
                    menu_2()
                    action_2 = action_sel()
                    if action_2 == "1":
                        if fireball.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_1()
                        contin()
                        break
                    elif action_2 == "2":
                        if frost_bolt.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_2()
                        contin()
                        break
                    elif action_2 == "3":
                        break
                    else:
                        action_err()
                        continue
                if action_2 == "3":
                    continue
                else:
                    break
            elif action_1 == "3":
                if items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    no_items()
                    contin()
                    continue
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    while True:
                        menu_3()
                        action_3 = action_sel()
                        if action_3 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_3 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_3 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_4()
                        action_4 = action_sel()
                        if action_4 == "1":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_4 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_4 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_5()
                        action_5 = action_sel()
                        if action_5 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_5 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_5 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_5 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_6()
                        action_6 = action_sel()
                        if action_6 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_6 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_6 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_7()
                        action_7 = action_sel()
                        if action_7 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_7 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_7 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_7 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_8()
                        action_8 = action_sel()
                        if action_8 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_8 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_8 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_8 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_9()
                        action_9 = action_sel()
                        if action_9 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_9 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_9 == "3":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_9 == "4":
                            break
                        else:
                            action_err()
                            continue
                    if action_9 == "4":
                        continue
                    else:
                        break
            elif action_1 == "4":
                run_result = run()
                contin()
                if current_mon.boss == "Tutorial":
                    continue
                else:
                    break
            elif action_1 == "5":
                combat_info()
                contin()
                continue
            else:
                action_err()
                continue
        if run_result is True:
            protag.status = None
            protag.status_initial = True
            run_result = False
            break
        if current_mon.hp <= 0:
            battle_end()
            break
        status_effect_hero()
        status_effect_start_turn()
        if current_mon.status == un_frz:
            continue
        current_mon.mon_attack()
        status_effect_mon()
        if current_mon.hp <= 0:
            battle_end()
            break
        continue
    print("You reach what seems to be a clearing in the forest. Overgrown plants prevent you from travelling\n"
          "any further in this direction.")
    contin()
    print("Right before you turn back, a voice calls out from around you.\n"
          "\"WHO has come to disturb me?!\"")
    contin()
    print("A great stream of wind and dust attacks you and forces you to close your eyes.\n"
          "When you look back, a terribly large, intimidating figure stands in front of you.\n"
          "Her figure is humanoid but her physical traits resemble that of a witch.")
    contin()
    print("\"Why have you come into this part of the forest?\"")
    contin()
    print("You stumble for an answer as her mere presence pushes down on you.\n"
          "\"I'm a lost traveller. Just looking for a way out to the other side of this forest.\"")
    contin()
    print("\"Like I'm going to believe that! This forest has taken enough away, I won't let you do the same!\"\n"
          "Unable to reason with her, you brace yourself to fight instead...")
    contin()

    # boss encounter 2

    current_mon = monster_dictionary.get("mon_6")
    mon_encounter()
    contin()
    hp_trigger = False
    while True:
        if current_mon.spd > protag.spd:
            print("The enemy was faster than you and acts first!")
            contin()
            status_effect_start_turn()
            if current_mon.status == un_frz:
                break
            current_mon.mon_attack()
            status_effect_mon()
            if current_mon.hp <= 0:
                battle_end()
                break
        break
    while True:
        if current_mon.hp <= 0:
            battle_end()
            break
        if hp_trigger is False and current_mon.hp <= 0.5 * current_mon.max_hp:
            hp_trigger = True
            print("The witch seems to have calmed down a bit...")
            contin()
        if items_1.used_doll is True:
            break
        while True:
            menu_1()
            action_1 = action_sel()
            if action_1 == "1":
                damage_range = dmg_delta_phys()
                attack()
                contin()
                break
            elif action_1 == "2":
                while True:
                    menu_2()
                    action_2 = action_sel()
                    if action_2 == "1":
                        if fireball.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_1()
                        contin()
                        break
                    elif action_2 == "2":
                        if frost_bolt.mp_cost > protag.mp:
                            no_mp()
                            contin()
                            continue
                        spell_2()
                        contin()
                        break
                    elif action_2 == "3":
                        break
                    else:
                        action_err()
                        continue
                if action_2 == "3":
                    continue
                else:
                    break
            elif action_1 == "3":
                if items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    no_items()
                    contin()
                    continue
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot == 0:
                    while True:
                        menu_3()
                        action_3 = action_sel()
                        if action_3 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_3 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_3 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_4()
                        action_4 = action_sel()
                        if action_4 == "1":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_4 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_4 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot == 0:
                    while True:
                        menu_5()
                        action_5 = action_sel()
                        if action_5 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_5 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_5 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_5 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_6()
                        action_6 = action_sel()
                        if action_6 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_6 == "2":
                            break
                        else:
                            action_err()
                            continue
                    if action_6 == "2":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll == 0 and items_1.mp50_pot >= 1:
                    while True:
                        menu_7()
                        action_7 = action_sel()
                        if action_7 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_7 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_7 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_7 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot == 0 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_8()
                        action_8 = action_sel()
                        if action_8 == "1":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_8 == "2":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_8 == "3":
                            break
                        else:
                            action_err()
                            continue
                    if action_8 == "3":
                        continue
                    else:
                        break
                elif items_1.hp70_pot >= 1 and items_1.cursed_doll >= 1 and items_1.mp50_pot >= 1:
                    while True:
                        menu_9()
                        action_9 = action_sel()
                        if action_9 == "1":
                            if protag.hp == protag.max_hp:
                                max_health()
                                contin()
                                continue
                            use_hp_pot()
                            contin()
                            break
                        elif action_9 == "2":
                            if protag.mp == protag.max_mp:
                                max_mana()
                                contin()
                                continue
                            use_mp_pot()
                            contin()
                            break
                        elif action_9 == "3":
                            if current_mon is not great_witch:
                                use_doll()
                                contin()
                                continue
                            elif current_mon is great_witch:
                                use_doll()
                                contin()
                                break
                        elif action_9 == "4":
                            break
                        else:
                            action_err()
                            continue
                    if action_9 == "4":
                        continue
                    else:
                        break
            elif action_1 == "4":
                run_result = run()
                contin()
                if current_mon.boss == "Tutorial":
                    continue
                else:
                    break
            elif action_1 == "5":
                combat_info()
                contin()
                continue
            else:
                action_err()
                continue
        if run_result is True:
            protag.status = None
            protag.status_initial = True
            run_result = False
            break
        if items_1.used_doll is True:
            break
        if current_mon.hp <= 0:
            battle_end()
            break
        status_effect_hero()
        status_effect_start_turn()
        if current_mon.status == un_frz:
            continue
        current_mon.mon_attack()
        status_effect_mon()
        if current_mon.hp <= 0:
            battle_end()
            break
        continue

    # ending 2

    if items_1.used_doll is True:
        print("You hold the doll out in front of you hoping to come through to the witch.\n"
              "\"It really is! You've brought my daughter back to me!\"")
        contin()
        print("\"You see... I once had a cherished daughter that lived with me in the fields outside this forest.\n"
              "One day, I told her to go to the edge of this forest to help me gather some ingredients.\n"
              "I was foolish and didn't consider how free-willed children could be.\"")
        contin()
        print("\"It was too late when I came looking for Lily...\"")
        contin()
        print("\"I ran into the forest looking high and low for her but couldn't find any trace of her.\n"
              "Right when I had reached my limit, a being flowing with radiant energy appeared in front of me.\"")
        contin()
        print("\"I am the spirit of this forest. Do you not know that terrible monsters lurk inside here?\n"
              "I do all that I can to push them back but my efforts are not enough. Why did you not take\n"
              "greater care in looking over your daughter?\"")
        contin()
        print("\"I will imprison you within this forest until such a time a person with good heart looks\n"
              "fairly upon you.\"")
        contin()
        print("Just as the woman finishes her story, a brilliant light shines out of the doll and in a flash,\n"
              "it transforms into a small girl. The girl immediately runs into the arms of her mother with\n"
              "tears flowing.")
        contin()
        print("A comforting feeling sweeps through your body as you feel you can rest easy after today...")
        contin()
        game_end = time.time()
        game_duration = game_end - game_start
        print("CONGRATULATIONS! You've completed this short text-based role-playing game in "
              f"{time.strftime('%M:%S', time.gmtime(game_duration))}.\n"
              "This is just 1 of 3 possible endings so feel free to replay the game if you enjoyed it!\n"
              "The following paragraph details your accomplishments in the run, share it\n"
              "(highlight > right click > copy > paste) with the creator or others who have played the game (:")
        contin()

        if protag.age <= 12:
            age_description = "irresponsibly young"
        elif 12 < protag.age <= 18:
            age_description = "youthful"
        elif 18 < protag.age <= 29:
            age_description = "energetic"
        elif 29 < protag.age <= 69:
            age_description = "mature"
        elif 69 < protag.age <= 100:
            age_description = "ripe old"
        else:
            age_description = "wickedly old"

        if len(best_stats) > 1:
            stat_description = "a balance in stats"
        else:
            stat_description = best_stats[0]

        if qte2 is False:
            qte2_description = "Their subpar memory led them to being accosted by a fairy."
        else:
            qte2_description = "Their attention to detail is worthy of praise."
        if puzzle2 is False:
            puzzle2_description = "Although courageous, thinking logically is not always their strong suit."
        else:
            puzzle2_description = "Unable to be tricked, their deduction skills could solve mysteries."

        print(
            "The Protagonist's Journey:\n"
            f"{protag.name} was an adventurer that favoured {stat_description} above all else.\n"
            f"At the {age_description} age of {protag.age}, they managed to bring peace to a sorrowful heart.\n"
            f"{qte2_description}\n"
            f"{puzzle2_description}\n"
            f"No one will stop {protag.name} from taking on the rest of the challenges this world has to offer."
        )
        contin()
        print("Thanks for playing!")

    # ending 2

    else:
        print("You breathe a sigh of relief as you finally manage to overcome the witch.\n"
              "She falls down and slowly vanishes into the air...")
        contin()
        print("The overgrown vegetation pulls away and light spills into the clearing where you stand.\n"
              "The whole spectrum of colours bloom around you in flowers and plants.\n"
              "You spot a path leading outside the forest on the other side of the clearing.")
        contin()
        print("Not quite knowing what you got out of this venture, you step out into the light and look\n"
              "forward to what else is on the horizon...")
        contin()
        game_end = time.time()
        game_duration = game_end - game_start
        print("CONGRATULATIONS! You've completed this short text-based role-playing game in "
              f"{time.strftime('%M:%S', time.gmtime(game_duration))}.\n"
              "This is just 1 of 3 possible endings so feel free to replay the game if you enjoyed it!\n"
              "The following paragraph details your accomplishments in the run, share it\n"
              "(highlight > right click > copy > paste) with the creator or others who have played the game (:")
        contin()

        if protag.age <= 12:
            age_description = "irresponsibly young"
        elif 12 < protag.age <= 18:
            age_description = "youthful"
        elif 18 < protag.age <= 29:
            age_description = "energetic"
        elif 29 < protag.age <= 69:
            age_description = "mature"
        elif 69 < protag.age <= 100:
            age_description = "ripe old"
        else:
            age_description = "wickedly old"

        if len(best_stats) > 1:
            stat_description = "a balance in stats"
        else:
            stat_description = best_stats[0]

        if qte2 is False:
            qte2_description = "Their subpar memory led them to being accosted by a fairy."
        else:
            qte2_description = "Their attention to detail is worthy of praise."
        if puzzle2 is False:
            puzzle2_description = "Although courageous, thinking logically is not always their strong suit."
        else:
            puzzle2_description = "Unable to be tricked, their deduction skills could solve mysteries."

        print(
            "The Protagonist's Journey:\n"
            f"{protag.name} was an adventurer that favoured {stat_description} above all else.\n"
            f"At the {age_description} age of {protag.age}, they battled a being of great magic.\n"
            f"{qte2_description}\n"
            f"{puzzle2_description}\n"
            f"{protag.name} will, without doubt, overcome many more obstacles on their journey."
        )
        contin()
        print("Thanks for playing!")
