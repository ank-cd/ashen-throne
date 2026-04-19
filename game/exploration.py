import random
from text_exploration import exploration_texts

event_list = ["battle","nothing", "npc", "loot"]

def get_random_event():
    return random.choice(event_list)

def read_movement_input():
    directions = ("left", "right", "forward")
    while True:
        movement = input(exploration_texts["movement_prompt"] + " ").lower()
        if movement in directions:
            return movement
        else:
            print(exploration_texts["invalid_direction"])

def exploration():
    movement = read_movement_input()
    event = get_random_event()
    return movement, event