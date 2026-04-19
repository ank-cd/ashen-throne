import random

exploration_texts = {
    "movement_prompt": "Which way will you go? (left, right, forward)\n",
    "invalid_direction": "That direction was not recognized. Please try again.",

    "city_intro": (
        "You step into the ruined city beneath a sky of ash. "
        "Blackened stone, drifting cinder, and the weight of old fire greet your return."
    ),

    "toward_castle": (
        "Far beyond the scorched streets, the old castle rises through ash and ruin, "
        "watching the city like a dying crown."
    ),

    "boss_hint": (
        "The ash grows thicker with every step. "
        "Somewhere ahead, something ancient stirs beneath the ruin."
    )
}

city_texts = [
    "You move through a street choked with ash, where blackened stone still remembers the fire.",
    "A dim red glow lingers beneath the ruins, as if the city never truly stopped burning.",
    "Ash drifts slowly through the air as you step between shattered walls and charred doorways.",
    "The remains of the city smolder in silence, their heat long faded, but never fully gone.",
    "You pass beneath a cracked archway, its stones darkened by old flame and ruin.",
    "Burned banners hang in tatters above the street, stirring weakly in the ashen wind.",
    "The road ahead is lined with scorched homes, hollow and still beneath a sky of cinder.",
    "Each step sends ash whispering across the broken ground.",
    "A ruined square opens before you, its statues blackened, its fountain dry and filled with soot.",
    "The city lies in ruin, yet somewhere beneath the stone, an ancient fire still breathes."
]

nothing_texts = [
    "The path remains empty. For a moment, only silence walks beside you.",
    "You find nothing here but blackened stone and fading echoes.",
    "No enemy appears. No treasure waits. Only ruin surrounds you.",
    "The street lies still, as though the city itself is holding its breath.",
    "Nothing stirs in the darkness ahead."
]

loot_texts = [
    "Something glints among the rubble.",
    "You notice a small cache hidden beneath broken stone.",
    "Among the ruins, you find something of use left behind by the fallen.",
    "A forgotten supply rests in the shadows, untouched by time.",
    "Your eyes catch the faint shine of something valuable in the dust."
]

def get_lesser_encounter_text(enemy_name):
    encounter_texts = [
        f"From the drifting ash, {enemy_name} emerges.",
        f"{enemy_name} stumbles into your path through the ruined street.",
        f"A ragged shape moves through the cinder-stained dark — {enemy_name}."
    ]
    return random.choice(encounter_texts)

def get_normal_encounter_text(enemy_name):
    encounter_texts = [
        f"{enemy_name} steps from the scorched shadows and blocks your way.",
        f"Through the falling ash, {enemy_name} comes into view.",
        f"The silence breaks as {enemy_name} rises before you."
    ]
    return random.choice(encounter_texts)

def get_elite_encounter_text(enemy_name):
    encounter_texts = [
        f"A heavy presence gathers in the ruin as {enemy_name} appears.",
        f"From the ash and silence, {enemy_name} emerges with grim purpose.",
        f"The air grows still as {enemy_name} steps into the dying light."
    ]
    return random.choice(encounter_texts)

def get_enemy_encounter_text(enemy_name, enemy_tier):
    if enemy_tier == "lesser":
        return get_lesser_encounter_text(enemy_name)
    if enemy_tier == "normal":
        return get_normal_encounter_text(enemy_name)
    if enemy_tier == "elite":
        return get_elite_encounter_text(enemy_name)
    return f"{enemy_name} appears before you."

def get_boss_warning_text():
    warning_texts = [
        "The ash grows thicker with every step. Even the silence feels watchful now.",
        "A heavy stillness settles over the ruin, as though the city itself is holding its breath.",
        "The air burns faintly in your lungs. Something ancient waits ahead."
    ]
    return random.choice(warning_texts)