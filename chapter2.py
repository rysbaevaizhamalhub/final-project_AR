
# Chapter 2: The Corpse Encounter

# In this chapter, Wei Wuxian faces a powerful and vengeful corpse
# in the middle of the night. The player must make decisions on
# how to deal with this dangerous encounter

# Key Features:
# - The player can choose to fight the corpse, which will result
#   in a battle where they can win or lose.
# - The player can play the flute to summon an ally that calms
#   the corpse and provides important clues for the story.
# - The player can investigate the surroundings to uncover a
#   hidden path that leads to a secret route.


import chapter3
from utils import typing_effect
import time
import random


def chapter2(spiritual_energy):
    typing_effect("\n--- Chapter 2: The Corpse Encounter ---")
    typing_effect(
        "The moon casts eerie shadows as you face a vengeful corpse. You must act quickly.\n")

    typing_effect(f"Current Spiritual Energy: {spiritual_energy} jars\n")

    typing_effect("What will you do?")
    typing_effect("1. Fight the corpse.")
    typing_effect("2. Play the flute (demonic cultivation).")
    typing_effect("3. Investigate the surroundings.\n")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        spiritual_energy = fight_corpse(spiritual_energy)
        typing_effect("\nYou returned to the options menu of Chapter 2.")
        chapter2(spiritual_energy)
    elif choice == "2":
        spiritual_energy = play_flute(spiritual_energy)
        typing_effect("\nYou returned to the options menu of Chapter 2.")
        chapter2(spiritual_energy)
    elif choice == "3":
        spiritual_energy = investigate_surroundings(spiritual_energy)
        chapter3.chapter3(spiritual_energy)
    else:
        typing_effect("\nInvalid choice. Please select a valid option.\n")
        chapter2(spiritual_energy)


def fight_corpse(spiritual_energy):
    typing_effect(
        "\nYou engage the corpse in battle. Its strength is overwhelming, but you fight valiantly.")
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        typing_effect(
            "You defeat the corpse and gain 2 jars of spiritual energy!")
        spiritual_energy += 2
    else:
        typing_effect(
            "The corpse overpowers you. You lose 1 jar of spiritual energy.")
        spiritual_energy -= 1
        if spiritual_energy <= 0:
            typing_effect("You have run out of spiritual energy. Game Over.")
            exit()
    time.sleep(3)
    return spiritual_energy


def play_flute(spiritual_energy):
    typing_effect(
        "\nYou play the flute, summoning an ally. The music calms the corpse, and your ally gives you a valuable clue.")
    typing_effect(
        "You gain 1 jar of spiritual energy for your strategic choice.\n")
    spiritual_energy += 1
    time.sleep(3)
    return spiritual_energy


def investigate_surroundings(spiritual_energy):
    typing_effect("\nYou search the area carefully and find a hidden path.")
    typing_effect(
        "Unlocking a secret route earns you 1 jar of spiritual energy.\n")
    spiritual_energy += 1
    time.sleep(3)
    return spiritual_energy
