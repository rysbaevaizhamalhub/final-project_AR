# Chapter 1: Rebirth

# In this chapter, Wei Wuxian wakes up in a new body and starts
# to realize that he has been brought back to life. The player
# helps Wei Wuxian figure out what happened to him and learns
# about the curse that brought him back.

# Key Features:
# - The player can read mysterious talismans to understand more
#   about the curse.
# - The player can investigate the body Wei Wuxian now inhabits
#   to find clues about his past.
# - The player must decide whether to escape the mansion or
#   confront the people who mistreated the body.

import chapter2
import chapter3
from utils import typing_effect
import time


def chapter1(spiritual_energy):
    typing_effect("\n--- Chapter 1: Rebirth ---")
    typing_effect(
        "The early morning light filters through the dark room, where talismans written with human blood hang on the walls.")
    typing_effect(
        "Wei Wuxian wakes up, disoriented, realizing he is inhabiting someone else's body.\n")

    typing_effect(f"Current Spiritual Energy: {spiritual_energy} jars\n")

    typing_effect("What will you do?")
    typing_effect("1. Read the talismans.")
    typing_effect("2. Investigate the body.")
    typing_effect("3. Plan an escape from the mansion.")
    typing_effect("4. Confront the abusers using dark energy.\n")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        spiritual_energy = read_talismans(spiritual_energy)
        typing_effect("\nYou returned to the options menu of Chapter 1.")
        chapter1(spiritual_energy)
    elif choice == "2":
        spiritual_energy = investigate_body(spiritual_energy)
        typing_effect("\nYou returned to the options menu of Chapter 1.")
        chapter1(spiritual_energy)
    elif choice == "3":
        plan_escape(spiritual_energy)
    elif choice == "4":
        spiritual_energy = confront_abusers(spiritual_energy)
        chapter2.chapter2(spiritual_energy)
    else:
        typing_effect("\nInvalid choice. Please select a valid option.\n")
        chapter1(spiritual_energy)


def read_talismans(spiritual_energy):
    typing_effect(
        "\nYou study the talismans written in blood, deciphering the dark symbols.")
    typing_effect("Will you break the curse to reveal hidden truths?\n")
    choice = input("Break the curse? (yes/no): ")

    if choice.lower() == "yes":
        typing_effect(
            "You break the curse and gain 1 jar of spiritual energy for your bravery!\n")
        spiritual_energy += 1
    else:
        typing_effect(
            "The curse remains, and no further clues are revealed.\n")
    time.sleep(3)
    return spiritual_energy


def investigate_body(spiritual_energy):
    typing_effect(
        "\nYou examine the frail body you now inhabit. Searching the room, you find a weapon hidden under the bed.")
    typing_effect(
        "This weapon may prove useful later, but it takes a toll on your spiritual energy.")
    spiritual_energy -= 1
    typing_effect(
        "You lose 1 jar of spiritual energy but gain a new tool for your journey.\n")
    time.sleep(3)
    return spiritual_energy


def plan_escape(spiritual_energy):
    typing_effect(
        "\nThe mansion feels oppressive, and you decide to plan your escape.")
    typing_effect(
        "Using a hidden passage, you successfully escape and skip to Chapter 3!")
    time.sleep(3)
    chapter3.chapter3(spiritual_energy)


def confront_abusers(spiritual_energy):
    typing_effect(
        "\nYou confront the Mo family, unleashing a surge of dark energy.")
    typing_effect(
        "The abusers are intimidated, and you retrieve a map and gain 1 jar of spiritual energy.")
    spiritual_energy += 1
    time.sleep(3)
    return spiritual_energy
