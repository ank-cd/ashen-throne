import math

def post_battle_regeneration(player):
    old_hp = player["hp"]
    old_resource = player["resource"]

    regen_hp = math.ceil(player["max_hp"] * 0.10)
    regen_resource = math.ceil(player["max_resource"] * 0.20)

    player["hp"] = min(player["hp"] + regen_hp, player["max_hp"])
    player["resource"] = min(player["resource"] + regen_resource, player["max_resource"])

    actual_hp_regen = player["hp"] - old_hp
    actual_resource_regen = player["resource"] - old_resource

    return actual_hp_regen, actual_resource_regen

def full_heal(player):
    player["hp"] = player["max_hp"]
    player["resource"] = player["max_resource"]

def loot_recovery(player):
    old_resource = player["resource"]
    regen_resource = math.ceil(player["max_resource"] * 0.40)
    player["resource"] = min(player["resource"] + regen_resource, player["max_resource"])
    actual_resource_regen = player["resource"] - old_resource
    return actual_resource_regen