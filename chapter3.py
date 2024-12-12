
# Chapter 3: Mountain Journey

# In this chapter, Wei Wuxian travels through the mountains
# and faces new challenges. The player must make choices to
# determine the path ahead.

# Key Features:
# - The player can fight an enemy, which will result in a battle
#   with a possible victory or defeat.
# - The player can choose to climb the mountain and face a
#   challenging puzzle that will unlock a hidden path.
# - The player can investigate the area to find hidden clues
#   and gain spiritual energy.

import chapter4
from utils import typing_effect
import time
import random


def chapter3(spiritual_energy):
    typing_effect("\n--- Chapter 3: Mountain Journey ---")
    typing_effect(
        "The path ahead winds through the mountains, and strange sights and sounds fill the air.")
    typing_effect(
        "You sense both danger and opportunity as you continue your journey with Lan Wangji.\n")

    typing_effect(f"Current Spiritual Energy: {spiritual_energy} jars\n")

    typing_effect("What will you do?")
    typing_effect("1. Fight an enemy.")
    typing_effect("2. Climb the mountain and face a puzzle.")
    typing_effect("3. Investigate the area.\n")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        spiritual_energy = fight_enemy(spiritual_energy)
        chapter3(spiritual_energy)
    elif choice == "2":
        spiritual_energy = climb_mountain(spiritual_energy)
        chapter4.chapter4(spiritual_energy)
    elif choice == "3":
        spiritual_energy = investigate_area(spiritual_energy)
        chapter3(spiritual_energy)
    else:
        typing_effect("\nInvalid choice. Please select a valid option.\n")
        chapter3(spiritual_energy)


def fight_enemy(spiritual_energy):
    typing_effect("\nYou engage in battle with a powerful enemy.")
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        typing_effect(
            "You defeat the enemy, receive a special item, and gain 3 jars of spiritual energy!")
        spiritual_energy += 3
    else:
        typing_effect(
            "The enemy overpowers you. You lose 2 jars of spiritual energy.")
        spiritual_energy -= 2
        if spiritual_energy <= 0:
            typing_effect("You have run out of spiritual energy. Game Over.")
            exit()
    time.sleep(3)
    return spiritual_energy


def climb_mountain(spiritual_energy):
    typing_effect("\nYou climb the mountain and face a challenging puzzle.")
    choice = input("Will you solve the puzzle? (yes/no): ")
    if choice.lower() == "yes":
        typing_effect(
            "You solve the puzzle and unlock a hidden path, revealing important information for Chapter 4!")
        spiritual_energy += 1
    else:
        typing_effect(
            "You fail to solve the puzzle and must return to the choices.\n")
    time.sleep(3)
    return spiritual_energy


def investigate_area(spiritual_energy):
    typing_effect(
        "\nYou search the area carefully and discover hidden clues that help your progress.")
    typing_effect("Your efforts reward you with 1 jar of spiritual energy.\n")
    spiritual_energy += 1
    time.sleep(3)
    return spiritual_energy
