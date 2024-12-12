
# Chapter 4: The Mysterious Figure

# In this chapter, Wei Wuxian encounters a mysterious figure
# that may hold important information about his past. The player
# has to decide how to handle the situation and what to learn
# from the encounter.

# Key Features:
# - The player can choose to learn more about Wei Wuxian’s past
#   through a vision, but it costs some spiritual energy.
# - The player can choose to fight the figure, which will lead
#   to a battle where they can win or lose.

import chapter5
from utils import typing_effect
import time
import random


def chapter4(spiritual_energy):
    typing_effect("\n--- Chapter 4: The Mysterious Figure ---")
    typing_effect(
        "The road ahead leads to an abandoned village. Strange noises echo, and a shadowy figure emerges.")
    typing_effect(
        "You sense this encounter could reveal vital truths about your past.\n")

    typing_effect(f"Current Spiritual Energy: {spiritual_energy} jars\n")

    typing_effect("What will you do?")
    typing_effect("1. Learn about Wei Wuxian's past.")
    typing_effect("2. Fight the figure.\n")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        spiritual_energy = learn_past(spiritual_energy)
        typing_effect("\nYou returned to the options menu of Chapter 4.")
        chapter4(spiritual_energy)
    elif choice == "2":
        spiritual_energy = fight_figure(spiritual_energy)
        chapter5.chapter5(spiritual_energy)
    else:
        typing_effect("\nInvalid choice. Please select a valid option.\n")
        chapter4(spiritual_energy)


def learn_past(spiritual_energy):
    typing_effect(
        "\nYou watch a vision of Wei Wuxian's past, learning crucial details about his life and death.")
    typing_effect(
        "The revelation gives you clarity but consumes 1 jar of spiritual energy.")
    spiritual_energy -= 1
    if spiritual_energy <= 0:
        typing_effect("You have run out of spiritual energy. Game Over.")
        exit()
    time.sleep(3)
    return spiritual_energy


def fight_figure(spiritual_energy):
    typing_effect("\nYou engage in a fierce battle with the shadowy figure.")
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        typing_effect(
            "The figure is defeated, revealing a hidden truth. You gain 4 jars of spiritual energy!")
        spiritual_energy += 4
    else:
        typing_effect(
            "You lack the strength to defeat the figure. You lose 1 jar of spiritual energy.")
        spiritual_energy -= 1
        if spiritual_energy <= 0:
            typing_effect("You have run out of spiritual energy. Game Over.")
            exit()
    time.sleep(3)
    return spiritual_energy
