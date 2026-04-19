from lore import GAME_TITLE, ARTIFACT_NAME, DRAGON_NAME

start_screen_text = (
    "+ . * . + . * . + . * . +\n"
    f"       {GAME_TITLE.upper()}\n"
    "+ . * . + . * . + . * . +\n"
)

menu_texts = {
    "welcome": "Welcome, exile.",
    "prompt": "Type 'new' to begin your journey or 'quit' to leave.",
    "invalid": "Command not recognized. Please try again.",
    "new_game": "A new journey begins...",
    "quit": "You turn away from the dying kingdom."
}

character_creation_texts = {
    "name_prompt": "Speak your name, exile.",
    "class_prompt": "Ash leaves little choice. Still, choose: warrior, hunter, or mage.",
    "invalid_class": "The ash offers no such choice. Try again."
}

class_descriptions = {
    "warrior": "A hardened exile, tempered by blood and loss, who answers darkness with steel.",
    "mage": "A banished wielder of hidden arts, drawing power from a world already half-consumed.",
    "hunter": "A lone exile of ash and silence, striking with patience before the dark can close in."
}

set_choice_texts = {
    "warrior": "Now choose your discipline.",
    "hunter": "Now choose your path.",
    "mage": "Now choose your calling."
}

set_confirm_texts = {
    "warrior": "Will you commit to this discipline? (yes/no)",
    "hunter": "Will you follow this path? (yes/no)",
    "mage": "Will you answer this calling? (yes/no)"
}

set_descriptions = {
    "warrior": {
        "warrior_fast": {
            "title": "Duelist",
            "description": "You fight with discipline and precision, relying on timing, footwork, and control. Your blows are lighter, but they come with greater rhythm, allowing you to keep the pressure alive."
        },
        "warrior_heavy": {
            "title": "Reaver",
            "description": "You fight to crush, not to outlast, driving your strength into blows meant to break bone, armor, and will alike. Each strike carries greater weight, but demands far more in return."
        }
    },

    "hunter": {
        "hunter_bow": {
            "title": "Ranger",
            "description": "You fight with speed and flow, keeping distance while your arrows come in a steadier rhythm. Each shot is lighter, but easier to maintain as the battle wears on."
        },
        "hunter_crossbow": {
            "title": "Marksman",
            "description": "You favor the shot that ends doubt, placing weight and precision above speed. Each bolt strikes harder, but every attack carries the burden of greater commitment."
        }
    },

    "mage": {
        "mage_ice": {
            "title": "Frostbinder",
            "description": "You wield the cold with restraint, shaping your sorcery through focus and control. Your magic is steadier and less demanding, allowing you to endure through measured power."
        },
        "mage_fire": {
            "title": "Pyromancer",
            "description": "You call upon flame to consume rather than contain, giving shape to ruin with every cast. Your sorcery burns hotter and strikes harder, but its hunger is never without cost."
        }
    }
}

def get_intro_text(player_name):
    return (
        f"+ . * . + . * . + . * . +\n\n"
        f"The kingdom is dying.\n"
        f"Its streets lie buried beneath ash and fading embers, "
        f"and its halls have long since fallen silent.\n"
        f"You return now not as a child of hope, but as an exile — "
        f"one who was banished, for reasons now half-buried beneath time, silence, and ruin.\n"
        #f"Your name is {player_name}.\n\n"
        f"Beyond the broken city, the castle rises like a dying crown.\n"
        f"{ARTIFACT_NAME} remains bound to the one who gave everything to contain its darkness.\n"
        f"And below, where guardian and grave became one, rests {DRAGON_NAME}.\n"
    )