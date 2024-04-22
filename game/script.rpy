# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player")
# define p = Character("player_name", dynamic=True;)

define b = Character("Ben")

define j = Character("Joe")

define o = Character("Olivia")

define s = Character("Setting")

define u = Character("Unknown")

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

    """
    player_name turns to find a woman approaching with a friendly smile, her presence a welcome contrast to the foreboding atmosphere surrounding 657 Boulevard.
    Ben shoots player_name an unsure look.
    """

    p "Yeah! Just moved in."

    o "You must be player_name! I'm Olivia! It's so nice to finally meet you in person!" 

    """
    Olivia smiles, her warm demeanor putting player_name at ease. She presents a welcoming basket, and player_name accepts it gratefully.
    """

    p "Thank you! That's so sweet of you! It's so nice to finally talk in person!"

    o "If you ever need anything, don't hesitate to ask. This neighborhood can be a bit...unique, but we all look out for each other."

    """
    player_name feels a wave of gratitude wash over them at Olivia's offer of support. 
    """

    p "Thank you, Olivia. That means a lot. And it's good to know there are friendly faces nearby. I'll definitely keep that in mind."

    """
    As Olivia bids them farewell and continues on her way, player_name can't help but feel a glimmer of hope. Perhaps, with the kindness of their new neighbor Olivia, they can find a sense of belonging in this strange and mysterious town after all.
    """

    b "Who was that?"

    """
    Ben's voice breaks the silence, pulling player_name back to the present.
    player_name laughed at Ben's worried expression.
    """

    p "That was just Olivia, my coworker. I've been texting her for months! She's really nice. Why are you being so weird about her?"
    
    """
    Ben shrugged, avoiding player_name's gaze.
    """

    b "I don't know, just got a weird vibe, I guess. Nevermind."

    """
    Before player_name can probe further, a chilling figure emerges from the shadows.
    """

    u "So you're moving into 657 Boulevard?"

    b "AH!"

    """
    Ben cried out, jumping back in surprise.
    """

    p "Yeah...Today is moving day."

    """
    player_name said sheepishly, trying to mask their initial shock.
    """

    """
    The figure introduced himself, offering his hand.
    """

    j "Want an extra hand? I am Joe by the way, I live right across the street."

    """
    Joe's voice carried an unsettling undertone.
    """

    p "Sure…" 
    
    """
    player_name replied, mustering a smile despite the lingering unease.
    """
    
    p "As much as you're, uh, willing to help. We could use all the assistance we can get. There are still plenty of boxes to carry inside and up the stairs."

    """
    Ben, eager to divert his attention from the eerie encounter, asked,
    """

    b "Where should I put these boxes?"

    """
    His voice betraying a hint of apprehension as he glanced around the dimly lit entryway of the house.
    """

    menu:
        "Who carries the boxes?"

        "Ben":
            jump ben_falls

        "player_name":
            jump end_1

label ben_falls:
    p "In my bedroom upstairs would be great."

    """
    player_name replies, trying to maintain a sense of normalcy despite the ominous atmosphere.
    Ben nods, hoisting the boxes onto his shoulders and carefully making his way up the creaking stairs. 
    Each step seemed to groan beneath his weight, adding to the tension in the air.
    Joe and player_name begin to unload the moving van, placing the boxes on the driveway.
    """

    j "You seem genuine."

    """
    Joe says looking deep into player_name's eyes.
    """

    j "I've seen a lot of good people come and go in this house, I hope you stick around."

    """
    Before player_name can even begin to ponder at what that might mean, a deafening crash reverberates through the house, causing them and Joe to freeze in their tracks.
    """

    """
    {b}BANG!{/b}
    """



    return

label end_1:
    return


# This ends the game.

return