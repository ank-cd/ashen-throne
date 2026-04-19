import random
from lore import BOSS_NAME_DRAGON, BOSS_NAME_WARDEN

def get_vaelor_intro_text():
    intro_texts = [
        (
            "The ruin trembles.\n"
            "Ash falls like dead snow from the broken stone above.\n"
            f"Then, from the deep glow beneath the city, {BOSS_NAME_DRAGON} rises."
        ),
        (
            "A low, ancient roar rolls through the dark.\n"
            "The embers beneath the ruin flare once more.\n"
            f"Before you, a colossal shape stirs and breaks its slumber: {BOSS_NAME_DRAGON}."
        ),
        (
            "For a moment, all sound dies.\n"
            "Then the darkness parts around a vast, burning shape scarred by corruption and time.\n"
            f"{BOSS_NAME_DRAGON} has awakened."
        )
    ]
    return random.choice(intro_texts)

def get_last_warden_intro_text():
    intro_texts = [
        (
            "A lone figure stands in the ash before you, motionless beneath the ruined stone.\n"
            "The armor is cracked, the flame upon it long faded.\n"
            "At last, the figure lifts its head.\n"
            "The Last Warden still keeps watch."
        ),
        (
            "From the silence of the ruin, a warrior steps forth.\n"
            "Ancient armor hangs from a body not yet willing to fall.\n"
            "Though broken by time and grief, the Last Warden still bars the way."
        ),
        (
            "You are not greeted by a beast, but by duty that refused to die.\n"
            "Amid ash and shattered stone stands the final remnant of a sacred oath.\n"
            "The Last Warden draws near."
        )
    ]
    return random.choice(intro_texts)

def get_boss_intro_text(boss_name):
    if boss_name == BOSS_NAME_DRAGON:
        return get_vaelor_intro_text()
    if boss_name == BOSS_NAME_WARDEN:
        return get_last_warden_intro_text()
    return f"{boss_name} stands before you."

def get_vaelor_victory_text():
    victory_texts = [
        (
            "Vaelor lets out one final, broken roar.\n"
            "Then the great body collapses beneath ash and ruin.\n"
            "For the first time in ages, the flame beneath the city begins to dim.\n"
        ),
        (
            "The Blight-Bound falters.\n"
            "Corruption spills from the dragon’s ruined form like dying fire.\n"
            "At last, Vaelor falls.\n"
        ),
        (
            "With a final shudder, Vaelor crashes into the broken stone.\n"
            "The embers around you fade to a dull glow.\n"
            "What stood before you was no mere beast, but the ruin of a guardian.\n"
        )
    ]
    return random.choice(victory_texts)

def get_last_warden_victory_text():
    victory_texts = [
        (
            "The Last Warden sinks to one knee.\n"
            "For a moment, the ancient armor holds.\n"
            "Then it gives way, and the final watch comes to an end.\n"
        ),
        (
            "The broken warrior staggers, then falls in silence.\n"
            "No cry escapes the helm.\n"
            "Only ash moves where the last guardian stood.\n"
        ),
        (
            "The sacred blade slips from the Warden’s grasp.\n"
            "A duty carried beyond reason finally breaks.\n"
            "The Last Warden stands no more.\n"
        )
    ]
    return random.choice(victory_texts)

def get_victory_teaser_text():
    teaser_texts = [
        "But deeper in the ruin, something still endures.",
        "You are not alone in your victory. Something in the dark has been watching.",
        "Far below the dying stone, another presence stirs.",
        "This silence is no peace. Something older still remains.",
        "Beyond ash and flame, a darker will has taken notice."
    ]
    return random.choice(teaser_texts)

def get_boss_victory_text(boss_name):
    if boss_name == BOSS_NAME_DRAGON:
        return get_vaelor_victory_text()
    if boss_name == BOSS_NAME_WARDEN:
        return get_last_warden_victory_text()
    return f"{boss_name} falls before you."

def get_defeat_text(player_name):
    defeat_texts = [
        (
            f"{player_name} falls beneath the weight of ash, ruin, and flame.\n"
            f"Your journey ends here.\n\n"
            f"Game Over."
        ),
        (
            f"The darkness closes in around {player_name}.\n"
            f"No further step will be taken.\n\n"
            f"Game Over."
        ),
        (
            f"{player_name} can go no farther.\n"
            f"The dying kingdom claims another soul.\n\n"
            f"Game Over."
        )
    ]
    return random.choice(defeat_texts)

game_over_text = (
    "Game Over.\n"
    "The kingdom still dies, with or without you."
)