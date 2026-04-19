import random

import lore
import text_ui
import text_exploration
import text_npc
import text_boss

import exploration
import entity_sheet
import attack_sets
import battle
import player_effects

def start_menu():
    while True:
        print(text_ui.start_screen_text)
        print(text_ui.menu_texts["welcome"])
        print(text_ui.menu_texts["prompt"])
        command = input().lower()

        if command == "new":
            print()
            print(text_ui.menu_texts["new_game"])
            print()
            return "new"
        elif command == "quit":
            print(text_ui.menu_texts["quit"])
            return "quit"
        else:
            print(text_ui.menu_texts["invalid"])

def read_player_name():
    while True:
        print(text_ui.character_creation_texts["name_prompt"])
        player_name = input()

        print()
        while True:
            print("Will you bear this name? (yes/no)")
            answer = input().lower()

            if answer == "yes":
                return player_name
            elif answer == "no":
                print()
                print("So you do not know your own name?")
                break
            else:
                print("Answer with yes or no.")

def read_player_class():
    while True:
        print()
        print(text_ui.character_creation_texts["class_prompt"])
        player_class = input().lower()

        if player_class in text_ui.class_descriptions:
            print()
            print(text_ui.class_descriptions[player_class])

            while True:
                print()
                print("Is this what you are? (yes/no)")
                answer = input().lower()

                if answer == "yes":
                    return player_class
                elif answer == "no":
                    print()
                    print("Then what are you?")
                    break
                else:
                    print("Answer with yes or no.")
        else:
            print(text_ui.character_creation_texts["invalid_class"])
            
def read_set_choice(player_class):
    while True:
        class_sets = text_ui.set_descriptions[player_class]
        set_keys = list(class_sets.keys())

        print()
        print(text_ui.set_choice_texts[player_class])
        print("1:", class_sets[set_keys[0]]["title"])
        print("2:", class_sets[set_keys[1]]["title"])

        choice = input()
        if choice == "1":
            chosen_set = set_keys[0]
        elif choice == "2":
            chosen_set = set_keys[1]
        else:
            print("Please enter 1 or 2.")
            continue

        print()
        print(class_sets[chosen_set]["title"])
        print(class_sets[chosen_set]["description"])

        while True:
            print()
            print(text_ui.set_confirm_texts[player_class])
            answer = input().lower()

            if answer == "yes":
                return chosen_set
            elif answer == "no":
                print("Then choose better.")
                print()
                break
            else:
                print("Answer with yes or no.")        

def create_new_game():
    menu_result = start_menu()

    if menu_result == "new":
        player_name = read_player_name()
        player_class = read_player_class()
        selected_set = read_set_choice(player_class)
        player = entity_sheet.create_player(player_name, player_class)
        selected_attack = attack_sets.get_attack_set(player_class, selected_set)
        print()
        print(text_ui.get_intro_text(player_name))
        print()
        return player, selected_attack
    else:
        return None, None

def wait_for_boss_ready():
    while True:
        print("Type 'forward' when you are ready. Not that readiness will matter.")
        command = input().lower()

        if command == "forward":
            return
        else:
            print("There is only one way forward. Type 'forward'.")

# ----------------------------- GamePlay -----------------------------
player, selected_attack = create_new_game()

if player is not None:
    battle_count = 0
    healer_used = False
    boss_killed = False

    while player["hp"] > 0 and boss_killed == False:
        if battle_count == 5:
            select_boss = entity_sheet.roll_boss()
            print()
            print(text_boss.get_boss_intro_text(select_boss))

            enemy = entity_sheet.roll_enemy("boss")
            enemy["name"] = select_boss

            boss_result = battle.battle_sequence(player,enemy,selected_attack)

            if boss_result == "win":
                boss_killed = True
                print(text_boss.get_boss_victory_text(select_boss))
            elif boss_result == "lose":
                print(text_boss.get_defeat_text(player["name"]))
        else:
            movement, event = exploration.exploration()
            if event == "battle":
                enemy_tier = entity_sheet.roll_enemy_type()
                enemy = entity_sheet.roll_enemy(enemy_tier)

                print()
                print(text_exploration.get_enemy_encounter_text(enemy["name"], enemy_tier))

                battle_result = battle.battle_sequence(player, enemy, selected_attack)

                if battle_result == "win":
                    battle_count += 1
                    hp, resource = player_effects.post_battle_regeneration(player)
                    print()
                    print(f"You recover {hp} HP and {resource} {player['resource_label']}.")
                    print(f"Current HP: {player['hp']}/{player['max_hp']}")
                    print(f"Current {player['resource_label']}: {player['resource']}/{player['max_resource']}")
                    print()

                    if battle_count == 5:
                        print()
                        print(text_exploration.get_boss_warning_text())
                        wait_for_boss_ready()

                elif battle_result == "lose":
                    print(text_boss.get_defeat_text(player["name"]))

                elif battle_result == "flee":
                    continue

            elif event == "nothing":
                print()
                print(random.choice(text_exploration.nothing_texts))
                print()

            elif event == "npc":
                if battle_count < 3 or healer_used == True:
                    print()
                    text_npc.encounter_warden()

                else:
                    npc = entity_sheet.roll_npc()

                    if npc == "healer":
                        print()
                        healer_result = text_npc.encounter_healer(player)

                        if healer_result:
                            healer_used = True

                    else:
                        print()
                        text_npc.encounter_warden()

            elif event == "loot":
                print()
                print(random.choice(text_exploration.loot_texts))
                resource_gain = player_effects.loot_recovery(player)
                print(f"You recover {resource_gain} {player['resource_label']}.")
                print(f"Current {player['resource_label']}: {player['resource']}/{player['max_resource']}")

else:
    pass