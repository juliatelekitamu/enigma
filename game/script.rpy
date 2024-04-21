# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player")
# define p = Character("player_name", dynamic=True;)

define b = Character("Ben")

define j = Character("Joe")

define o = Character("Olivia")

define s = Character("Setting")

define e = Character("Eileen", image="eileen")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show e

    # These display lines of dialogue.

    """
    As the sun dipped below the horizon, casting long shadows over the eerie town of Whispering Hollow, a chill crept down player_name. They stood before what would be their new home, 657 Boulevard.

    A new job awaits in this small forsaken town, and the only available residence was this haunted house. Clutching their keys tightly, player_name couldn't shake the feeling of unease that settled on their shoulders.

    As Ben and player_name continued moving boxes into the house, Ben struck up a conversation to lighten the mood.
    """
    
    b "So are you excited for your new place and new job? This house looks awesome!"

    """ 
    player_name frowned slightly, not seeing what was so awesome about it.
    """
    
    p "The house is huge, and it was the only one that was available immediately, that's why I decided to buy it."

    b "It's going to be weird not seeing you around anymore. We have been best friends since we were in elementary school."

    o "Are you new in the neighborhood?"

    p "player_name turns to find a woman approaching with a friendly smile, her presence a welcome contrast to the foreboding atmosphere surrounding 657 Boulevard."

    b "Ben shot player_name an unsure look."

    # This ends the game.

    return