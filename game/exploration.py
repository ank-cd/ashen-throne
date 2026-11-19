import random
from text_exploration import exploration_texts

event_list = ["battle","nothing", "npc", "loot"]
event_weights = [50, 20, 15, 15]

def get_random_event():
    return random.choices(event_list, weights=event_weights)[0]

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