import random
import player_effects

healer_actions = ("approach", "listen", "speak", "heal", "leave")

healer_texts = {
    "action_prompt_far": "Will you approach or leave?",
    "action_prompt_close": "Will you listen, speak, or leave?",
    "invalid_action": "That choice was not recognized. Please try again.",
    "leave_text": "You leave the old healer behind and return to the ash-choked path."
}

def get_old_healer_intro_text():
    intro_texts = [
        "In the shelter of a broken wall, an old woman sits beside the ashes of a dead fire.",
        "A frail figure waits among the ruins, wrapped in worn cloth and silence.",
        "Near a collapsed doorway, an old healer remains where all others have fled."
    ]
    return random.choice(intro_texts)

def get_old_healer_dialog_text():
    dialog_texts = [
        (
            "The old healer studies your wounds in silence.\n"
            "\"You still carry warmth,\" she murmurs. \"That is rare.\""
        ),
        (
            "Her tired eyes rest on you for a long moment.\n"
            "\"Ash takes most things,\" she says quietly. \"Not all at once. Just enough.\""
        ),
        (
            "\"You walk like one who has not yet chosen to die,\" the old healer says.\n"
            "\"That still matters in a place like this.\""
        )
    ]
    return random.choice(dialog_texts)

def get_old_healer_approach_text():
    approach_texts = [
        (
            "The old healer raises a trembling hand and beckons you closer.\n"
            "\"Sit,\" she says. \"There is still a little strength left in these hands.\""
        ),
        (
            "She studies you without fear.\n"
            "\"You are not beyond saving,\" she murmurs. \"Not yet.\""
        ),
        (
            "With slow, careful motion, she gestures for you to come nearer.\n"
            "\"If you still intend to walk deeper into this ruin, then you should not do so broken.\""
        )
    ]
    return random.choice(approach_texts)

def get_old_healer_listen_text():
    listen_texts = [
        "\"The fire below never truly died,\" she whispers. \"It only learned to wait.\"",
        "\"Some still call this place a kingdom,\" she says. \"I only call it what remains.\"",
        "\"There are things beneath the stone that do not hate you,\" she murmurs. \"They simply do not care if you live.\""
    ]
    return random.choice(listen_texts)

def get_old_healer_heal_text():
    heal_texts = [
        (
            "The old healer tends to your wounds with trembling hands.\n"
            "Warmth returns to your body, and some of your strength follows."
        ),
        (
            "Her touch is light, but the ache begins to ease.\n"
            "You recover some health and regain some of your strength."
        ),
        (
            "She works in silence, as though repeating a rite older than memory.\n"
            "When she is done, your wounds trouble you less, and your strength has begun to return."
        )
    ]
    return random.choice(heal_texts)

warden_actions = ("speak", "listen", "leave")

warden_texts = {
    "action_prompt": "Will you speak, listen, or leave?",
    "invalid_action": "That choice was not recognized. Please try again.",
    "leave_text": "You leave the broken warden to his endless watch and return to the ruin."
}

def get_broken_warden_intro_text():
    intro_texts = [
        "A lone figure stands among the ash, clad in cracked armor darkened by age and fire.",
        "Near a shattered archway, a motionless warden keeps watch over a path long since abandoned.",
        "In the ruins ahead, a warrior remains at his post, though time and ash have nearly consumed him."
    ]
    return random.choice(intro_texts)

def get_broken_warden_speak_text():
    speak_texts = [
        (
            "The warden turns his helm toward you with slow, deliberate motion.\n"
            "\"You should not be here,\" he says. \"And yet... neither should I.\"\n"
            "\"If you walk deeper, do not mistake silence for mercy. Some things below do not sleep. They only wait.\""
        ),
        (
            "For a long moment, the warden says nothing.\n"
            "Then, from behind the ruined helm, a tired voice emerges.\n"
            "\"I have stood this watch so long that even the reason has begun to fade.\"\n"
            "He lowers his head for a moment.\n"
            "\"I was sworn to hold this path. I no longer know whether I keep danger out... or in.\""
        ),
        (
            "\"Another soul walks the ash,\" the warden murmurs.\n"
            "\"Tell me... has the kingdom fallen yet, or do I merely remember it dying?\"\n"
            "The ruined helm tilts ever so slightly.\n"
            "\"Beyond this ruin lies oath, fire, and failure. If you continue, you will meet all three.\""
        )
    ]
    return random.choice(speak_texts)

def get_broken_warden_listen_text():
    listen_texts = [
        "\"The flame was never meant to gutter,\" he whispers. \"Only to sleep.\"",
        "\"We were made to endure,\" the warden murmurs, as though reciting a vow half-lost to time.",
        "\"I remember the fire. I remember the oath. I do not remember when we began to fail.\""
    ]
    return random.choice(listen_texts)

def get_broken_warden_recognition_text():
    recognition_texts = [
        "\"You bear the look of one who has returned too late,\" the warden says.",
        "\"For a moment, I thought you were one of ours,\" the warden murmurs. \"But that line is ash now.\"",
        "\"You walk like the old blood remembers you,\" he says quietly. \"That troubles me.\""
    ]
    return random.choice(recognition_texts)

def encounter_warden():
    print(get_broken_warden_intro_text())
    print(get_broken_warden_recognition_text())

    while True:
        print(warden_texts["action_prompt"])
        action = input().lower()

        if action == "speak":
            print()
            print(get_broken_warden_speak_text())

        elif action == "listen":
            print()
            print(get_broken_warden_listen_text())

        elif action == "leave":
            print()
            print(warden_texts["leave_text"])
            return
        
        else:
            print()
            print(warden_texts["invalid_action"])

def encounter_healer(player):
    print()
    print(get_old_healer_intro_text())

    approached = False

    while True:
        if approached == False:
            print()
            print(healer_texts["action_prompt_far"])
            action = input().lower()

            if action == "approach":
                approached = True
                print()
                print(get_old_healer_approach_text())

            elif action == "leave":
                print()
                print(healer_texts["leave_text"])
                return False

            else:
                print()
                print(healer_texts["invalid_action"])

        else:
            print()
            print(healer_texts["action_prompt_close"])
            interaction = input().lower()

            if interaction == "listen":
                print()
                print(get_old_healer_listen_text())

            elif interaction == "speak":
                print()
                print(get_old_healer_dialog_text())

            elif interaction == "leave":
                print()
                print(healer_texts["leave_text"])
                return False

            else:
                print()
                print(healer_texts["invalid_action"])
                continue

            while True:
                print("Will you accept what help remains? (yes/no)")
                choice = input().lower()

                if choice == "yes":
                    print()
                    print(get_old_healer_heal_text())
                    player_effects.full_heal(player)
                    print("You are fully healed.")
                    return True

                elif choice == "no":
                    break

                else:
                    print()
                    print("Answer with yes or no.")