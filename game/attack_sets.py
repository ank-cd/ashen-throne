#Krieger-Set
warrior_set = {
    "warrior_fast": {"attack_name": "Blade Thrust", "dmg_range": (8,10), "crit_chance": 20, "crit_mult": 1.10, "cost": 6, "fallback_dmg": 6},
    "warrior_heavy": {"attack_name": "Axe Strike", "dmg_range": (11,13), "crit_chance": 20, "crit_mult": 1.10, "cost": 8, "fallback_dmg": 6}
}
#Jäger-Set
hunter_set = {
    "hunter_bow": {"attack_name": "Arrow Shot", "dmg_range": (7,9), "crit_chance": 30, "crit_mult": 1.20, "cost": 7, "fallback_dmg": 5},
    "hunter_crossbow": {"attack_name": "Bolt Shot", "dmg_range": (10,12), "crit_chance": 30, "crit_mult": 1.20, "cost": 9, "fallback_dmg": 5}
}
#Magier-Set
mage_set = {
    "mage_ice": {"attack_name": "Ice Shard", "dmg_range": (9,11), "crit_chance": 10, "crit_mult": 1.10, "cost": 8, "fallback_dmg": 4},
    "mage_fire": {"attack_name": "Fireball", "dmg_range": (12,14), "crit_chance": 10, "crit_mult": 1.10, "cost": 10, "fallback_dmg": 4}
}
#Alle Sets
all_attack_sets = {
    "warrior": warrior_set,
    "hunter": hunter_set,
    "mage": mage_set
}

def get_attack_set(player_class, set_name):
    if player_class not in all_attack_sets:
        raise ValueError("Unknown class.")
    allowed_sets = all_attack_sets[player_class]
    if set_name not in allowed_sets:
        raise ValueError("This attack set is not available for this class.")
    selected_set = allowed_sets[set_name]
    return selected_set