import random
from lore import BOSS_NAME_DRAGON, BOSS_NAME_WARDEN

#Player
class_templates = {
    "warrior": {"max_hp": 110, "resource_label": "Rage", "max_resource": 70},
    "hunter": {"max_hp": 100, "resource_label": "Endurance", "max_resource": 80},
    "mage": {"max_hp": 90, "resource_label": "Mana", "max_resource": 90}
}

def create_player(player_name, player_class):
    if player_class not in class_templates:
        raise ValueError("Invalid player class.")
    selected_class = class_templates[player_class]
    player = {
        "name": player_name, #player_name = input() main.py
        "class": player_class,
        "max_hp": selected_class["max_hp"],
        "hp": selected_class["max_hp"],
        "resource_label": selected_class["resource_label"],
        "max_resource": selected_class["max_resource"],
        "resource": selected_class["max_resource"],
    }
    return player

enemy_names_lesser = ["Starved Hound", "Hollow Servant", "Scorched Drifter"]
enemy_names_normal = ["Blighted Hound", "Fallen Guard", "Ashen Lunatic"]
enemy_names_elite = ["Shadow Beast", "Ashen Knight", "Broken Warden"]
enemy_names_boss = [BOSS_NAME_DRAGON, BOSS_NAME_WARDEN]

enemy_name_pool = {
    "lesser": enemy_names_lesser,
    "normal": enemy_names_normal,
    "elite": enemy_names_elite,
    "boss": enemy_names_boss
}

enemy_templates = {
    "lesser": {"hp_range": (30, 50), "dmg_range": (5, 6), "crit_chance": 0, "crit_mult": 0.0, "flee_chance": 70},
    "normal": {"hp_range": (55, 75), "dmg_range": (6, 8), "crit_chance": 0, "crit_mult": 0.0, "flee_chance": 50},
    "elite": {"hp_range": (80, 110), "dmg_range": (9, 13), "crit_chance": 10, "crit_mult": 1.10, "flee_chance": 20},
    "boss": {"hp_range": (150, 180), "dmg_range": (11, 15), "crit_chance": 5, "crit_mult": 1.20, "flee_chance": 0}
}

def roll_enemy_type():
    dice = random.randint(1,100)
    if dice <=10:
        return "elite"
    elif dice <=45:
        return "normal"
    else:
        return "lesser"

def roll_boss():
    dice = random.randint(1,100)
    if dice <= 10:
        return BOSS_NAME_WARDEN
    else:
        return BOSS_NAME_DRAGON

def roll_npc():
    dice = random.randint(1,100)
    if dice <= 70:
        return "healer"
    else:
        return "warden"

def roll_enemy(enemy_type):
    if enemy_type not in enemy_templates:
        raise ValueError("Unknown enemy type.")
    spawned_enemy = enemy_templates[enemy_type]
    hp_min, hp_max = spawned_enemy["hp_range"]
    roll_enemy_hp = random.randint(hp_min, hp_max)
    name_pool = enemy_name_pool[enemy_type]
    enemy_name = random.choice(name_pool)
    enemy = {
        "name": enemy_name,
        "enemy_type": enemy_type,
        "max_hp": roll_enemy_hp,
        "hp": roll_enemy_hp,
        "dmg_range": spawned_enemy["dmg_range"],
        "crit_chance": spawned_enemy["crit_chance"],
        "crit_mult": spawned_enemy["crit_mult"],
        "flee_chance": spawned_enemy["flee_chance"],
    }
    return enemy