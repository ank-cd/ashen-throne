import random

# input action player
def read_battle_action_input():
    selection = ("attack", "flee", "status")
    while True:
        print()
        print("Make your choice: attack, flee, or status.")
        action = input().lower()
        if action in selection:
            return action
        else:
            print("Please enter a valid action.")

# action: attack
def player_attack(player, enemy, attack_set):
    if player["resource"] >= attack_set["cost"]:
        dmg_min, dmg_max = attack_set["dmg_range"]
        roll_dmg = random.randint(dmg_min, dmg_max)
        final_damage, is_crit = crit_calculator(roll_dmg, attack_set["crit_chance"], attack_set["crit_mult"])
        player["resource"] -= attack_set["cost"]
        enemy["hp"] = max(enemy["hp"] - final_damage, 0)
        return final_damage, is_crit, False
    else:
        enemy["hp"] = max(enemy["hp"] - attack_set["fallback_dmg"], 0)
        player["resource"] += 1
        return attack_set["fallback_dmg"], False, True

# action: flee
def try_flee(enemy):
    chance = enemy["flee_chance"]
    dice = random.randint(1,100)
    return dice <= chance

# action: status
def show_battle_status(player, enemy):
    print()
    print(f"Your HP: {player['hp']}/{player['max_hp']}")
    print(f"Your {player['resource_label']}: {player['resource']}/{player['max_resource']}")
    print(f"{enemy['name']} HP: {enemy['hp']}/{enemy['max_hp']}")
    print()

# crit
def crit_calculator(base_damage, crit_chance, crit_mult):
    dice = random.randint(1,100)
    if dice <= crit_chance:
        final_damage = round(crit_mult * base_damage)
        is_crit = True
    else:
        final_damage = base_damage
        is_crit = False
    return final_damage, is_crit

# enemy attack
def enemy_attack(enemy, player):
    dmg_min, dmg_max = enemy["dmg_range"]
    roll_dmg = random.randint(dmg_min, dmg_max)
    final_damage, is_crit = crit_calculator(roll_dmg, enemy["crit_chance"], enemy["crit_mult"])
    player["hp"] = max(player["hp"] - final_damage, 0)
    return final_damage, is_crit

def enemy_attack_log(enemy, counter_damage, counter_crit):
    if counter_crit:
        print(f"Critical hit! {enemy['name']} deals {counter_damage} damage to you.")
    else:
        print(f"{enemy['name']} deals {counter_damage} damage to you.")

# battle sequence
def battle_sequence(player, enemy, attack_set):
    print(f"You encounter {enemy['name']} with {enemy['hp']} HP.")
    print()

    while player["hp"] > 0 and enemy["hp"] > 0:
        action = read_battle_action_input()

        if action == "attack":
            battle_damage, battle_crit, used_fallback = player_attack(player, enemy, attack_set)
            if used_fallback:
                print()
                print(f"You are out of resources. You use a fallback attack and deal {battle_damage} damage.")
            elif battle_crit:
                print()
                print(f"Critical hit! You deal {battle_damage} damage to {enemy['name']}.")
            else:
                print()
                print(f"You deal {battle_damage} damage to {enemy['name']}.")
            if enemy["hp"] > 0:
                counter_damage, counter_crit = enemy_attack(enemy, player)
                enemy_attack_log(enemy, counter_damage, counter_crit)

        elif action == "flee":
            flee_result = try_flee(enemy)
            if flee_result:
                print()
                print("You successfully escaped.")
                return "flee"
            else:
                print()
                print("Your escape failed! The enemy attacks!")
                counter_damage, counter_crit = enemy_attack(enemy, player)
                enemy_attack_log(enemy, counter_damage, counter_crit)

        elif action == "status":
            show_battle_status(player, enemy)

    if player["hp"] > 0 and enemy["hp"] <= 0:
        print()
        print(f"{enemy['name']} has been defeated. The victory is yours.")
        print()
        return "win"
    else:
        return "lose"