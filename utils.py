import sys
import time


def typing_effect(text, delay=0.01):
    """
    Prints text one character at a time with a delay to simulate typing.

    Args:
        text (str): The text to display.
        delay (float): The delay between characters (default is 0.02 seconds).
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Print a newline at the end of the text
