# Chapter 5: Final Confrontation

# This is the final chapter where Wei Wuxian faces his ultimate
# enemy—the one responsible for his death. The player must make
# the final decision: whether to choose revenge or forgiveness,
# which will determine the outcome of the game.

# Key Features:
# - The player can choose to defend allies and protect them from
#   the enemy’s attacks.
# - The player can uncover hidden truths about Wei Wuxian’s past
#   and gain valuable spiritual energy.
# - The player will confront the final enemy and make the ultimate
#   decision between revenge or forgiveness.

from utils import typing_effect
import time


def chapter5(spiritual_energy):
    typing_effect("\n--- Chapter 5: Final Confrontation ---")
    typing_effect(
        "The air is heavy with dark energy as you approach the crumbling temple. The final piece of the puzzle lies here.")
    typing_effect("You must decide how to confront the ultimate enemy.\n")

    typing_effect(f"Current Spiritual Energy: {spiritual_energy} jars\n")

    typing_effect("What will you do?")
    typing_effect("1. Defend Lan Wangji and allies.")
    typing_effect("2. Discover a hidden truth.")
    typing_effect("3. Confront the final enemy.\n")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        spiritual_energy = defend_allies(spiritual_energy)
        typing_effect("\nYou returned to the options menu of Chapter 5.")
        chapter5(spiritual_energy)  # Return to options menu
    elif choice == "2":
        spiritual_energy = discover_truth(spiritual_energy)
        typing_effect("\nYou returned to the options menu of Chapter 5.")
        chapter5(spiritual_energy)  # Return to options menu
    elif choice == "3":
        spiritual_energy = confront_enemy(spiritual_energy)
    else:
        typing_effect("\nInvalid choice. Please select a valid option.\n")
        chapter5(spiritual_energy)


def defend_allies(spiritual_energy):
    typing_effect(
        "\nYou protect Lan Wangji and your allies from the enemy's attacks.")
    typing_effect(
        "Your efforts consume 1 jar of spiritual energy but ensure everyone's safety.\n")
    spiritual_energy -= 1
    if spiritual_energy <= 0:
        typing_effect("You have run out of spiritual energy. Game Over.")
        exit()
    time.sleep(3)
    return spiritual_energy


def discover_truth(spiritual_energy):
    typing_effect(
        "\nYou uncover a hidden truth about Wei Wuxian's past, gaining 2 jars of spiritual energy.\n")
    spiritual_energy += 2
    time.sleep(3)
    return spiritual_energy


def confront_enemy(spiritual_energy):
    typing_effect(
        "\nYou face the final enemy, the one responsible for your death.")
    choice = input(
        "Will you choose revenge or forgiveness? (revenge/forgiveness): ")

    if choice.lower() == "revenge":
        typing_effect(
            "\nYou defeat the betrayer, but the triumph comes at a heavy cost to your soul.")
        typing_effect("The game ends with a dark victory. Game Over.")
        exit()
    elif choice.lower() == "forgiveness":
        typing_effect(
            "\nYou offer forgiveness, gaining peace and 10 jars of spiritual energy.")
        typing_effect("Wei Wuxian moves on with a brighter future. Victory!")

        # Ending Message
        typing_effect(
            "\nCongratulations, brave soul! You've chosen the path of peace.")
        typing_effect(
            "Your choice will echo through the ages as a testament to the power of forgiveness.")
        typing_effect(
            "The world is a better place because of you, and Wei Wuxian can now rest in peace.")

        typing_effect(
            "\nThank you for playing! Your adventure has come to a satisfying conclusion.")
        typing_effect(
            "The path ahead is brighter, and though this journey ends, new possibilities await in the future.")

        typing_effect("\nEnd of Game. Press any key to exit...")
        input()  # Pauses to allow player to read final message
        exit()
    else:
        typing_effect("\nInvalid choice. Returning to the confrontation.\n")
        chapter5(spiritual_energy)
    return spiritual_energy
