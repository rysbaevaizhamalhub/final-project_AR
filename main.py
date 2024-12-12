# Aizhamal Rysbaeva
# Nov 27th, 2024

# Milestone 3

# Game Overview:

# This is a text-based adventure game where the player controls
# Wei Wuxian, a character who has been brought back to life.
# The story is inspired by the Chinese fantasy novel, The Grandmaster
# of Demonic Cultivation (Mo Dao Zu Shi). The game follows Wei Wuxian
# as he tries to figure out what happened to him and uncover the
# mystery of his death.
#
# The player makes choices at different points in the game, and
# these choices affect what happens next in the story. The game is
# about finding out the truth, deciding between revenge and forgiveness,
# protecting friends, and dealing with dark forces.
#
# Key Features:
# - Multiple chapters with different paths and endings.
# - Choices that change the outcome of the game.
# - A "spiritual energy" system that affects gameplay.
# - A final choice between revenge or forgiveness, which determines
#   the end of the game.
#
# The game focuses on themes like morality, personal growth, and
# sacrifice, and it uses elements from Chinese fantasy like cultivation
# and spiritual powers.

import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

# Global variable to track spiritual energy
spiritual_energy = 3  # Start with 3 jars


def start_game():
    global spiritual_energy
    print("\n--- Welcome to the Adventure of Wei Wuxian ---")
    print("Your journey begins with 3 jars of spiritual energy. Make wise choices to keep your energy and uncover the truth!")
    print("\nEach action has consequences, and your spiritual energy is your lifeline.\n")

    # Start the game
    chapter1.chapter1(spiritual_energy)


if __name__ == "__main__":
    start_game()
