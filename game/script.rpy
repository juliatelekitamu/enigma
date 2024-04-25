# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player")
# define p = Character("[povname]", dynamic=True;)

define b = Character("Ben", image = "ben")

define j = Character("Joe", image = "joe")

define o = Character("Olivia", image = "olivia")

define s = Character("Setting")

define u = Character("Unknown")

define e = Character("Eileen")

define pov = Character ("[povname]")

define blank = Character ("")

image ben carrying_boxes = "images/characters/ben/ben-boxes.png"
image ben mouth_closed = "images/characters/ben/ben-mouth-closed.png"
image ben talking_mouth_open = "images/characters/ben/ben-talking-mouth-open.png"
image ben talking_mouth_open_2 = "images/characters/ben/ben-talking-mouth-open-2.png"

image olivia smiling_talking = "images/characters/olivia/olivia-smiling-talking.png"
image olivia about_to_cry = "images/characters/olivia/olivia-about-to-cry.png"
image olivia concerned_1 = "images/characters/olivia/olivia-concerned-1.png"
image olivia concerned_2 = "images/characters/olivia/olivia-concerned-2.png"
image olivia concerned_3 = "images/characters/olivia/olivia-concerned-3.png"
image olivia crying = "images/characters/olivia/olivia-crying.png"
image olivia evil_smile_1 = "images/characters/olivia/olivia-evil-smile-1.png"
image olivia evil_smile_2 = "images/characters/olivia/olivia-evil-smile-2.png"
image olivia evil_smile_3 = "images/characters/olivia/olivia-evil-smile-3.png"
image olivia frown = "images/characters/olivia/olivia-frown.png"
image olivia frown_hands_together = "images/characters/olivia/olivia-frown-hands-together.png"
image olivia frustrated = "images/characters/olivia/olivia-frustrated.png"
image olivia losing_her_mind = "images/characters/olivia/olivia-losing-her-mind.png"
image olivia screaming = "images/characters/olivia/olivia-screaming.png"
image olivia slightly_concerned_talking = "images/characters/olivia/olivia-slightly-concerned-talking.png"
image olivia smile_mouth_closed = "images/characters/olivia/olivia-smile-mouth-closed.png"
image olivia smile_mouth_open = "images/characters/olivia/olivia-smile-mouth-open.png"
image olivia surprised = "images/characters/olivia/olivia-surprised.png"
image olivia surprised_concerned = "images/characters/olivia/olivia-surprised-concerned.png"


image joe frown_1 = "images/characters/joe/joe-frown-1.png"
image joe smile = "images/characters/joe/joe-smile.png"
image joe talking = "images/characters/joe/joe-talking.png"
image joe talking_smiling = "images/characters/joe/joe-talking-smiling.png"
image joe startled = "images/characters/joe/joe-startled.png"


default page_pieces = 9 # Amount of pieces for this puzzle.
default full_page_size = (711, 996)
default piece_coordinates = [
    (216 + 300, 137 + 40),
    (539 + 300, 146 + 40),
    (155 + 300, 423 + 40),
    (399 + 300, 419 + 40),
    (602 + 300, 539 + 40),
    (121 + 300, 778 + 40),
    (407 + 300, 686 + 40),
    (269 + 300, 887 + 40),
    (548 + 300, 828 + 40)
]

default initial_piece_coordinates = [] # Will be filled with random initial locations of the pieces.
default finished_pieces = 0 # Keeps track of the amount of pieces that have been placed correctly.


screen reassemble_puzzle:
    image "images/minigame/background.png"
    add DynamicDisplayable(countdown, length=120.0)
    frame:
        background "images/minigame/puzzle-frame.png"
        xysize full_page_size
        anchor(0.5, 0.5)
        pos(650, 535)

    draggroup:
        # Group of draggable pieces, and the spots they can be dragged to.
        # Paper pieces
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise True
                image "images/minigame/Pieces/piece-%s.png" % (i + 1)

        # Snappable spots to drag to.
        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                image "images/minigame/Pieces/piece-%s.png" % (i + 1) alpha 0.0 # Have the alpha at a higher value when first placing the pieces to make sure it looks correct.

init python:
    def setup_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc) # Add the random locations to a list so we can use them to place each piece.

    def piece_drop(dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to its location.
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to be dragged.
            finished_pieces += 1

            if finished_pieces == page_pieces:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("solved_puzzle")
    
    def countdown(st, at, length=0.0):

        remaining = length - st
        minutes = (int) (length - st) / 60
        seconds = (int) (length - st) % 60


        if remaining > 2.0:
            return Text("%02d:" % minutes + "%02d" % seconds, color="#fff", size=48), .1
        elif remaining > 0.0:
            return Text("%02d:" % minutes + "%02d" % seconds, color="#f00", size=48), .1
        else:
            renpy.jump("not_solved_puzzle")
            return anim.Blink(Text("00:00", color="#f00", size=48)), None


# The game starts here.

label start:
    $ povname = renpy.input("What is your name?", length=32)
    $ povname = povname.strip()
    play music "./gui/music/dopplerette.mp3" volume 1.5 loop 
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg house

    transform midleft:
        xalign 0.33 yalign 1.00
    transform midright:
        xalign 0.66 yalign 1.05

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    blank "As the sun dipped below the horizon, casting long shadows over the eerie town of Whispering Hollow, a chill crept down [povname]'s back." 
    
    play sound "wind_sounds.mp3" volume 0.3

    blank "They stood before what would be their new home, 657 Boulevard."

    blank "A new job awaits in this small forsaken town, and the only available residence was this haunted house."
 
    show ben talking_mouth_open at midleft with dissolve
 
    blank "Clutching their keys tightly, [povname] couldn't shake the feeling of unease that settled on their shoulders."

    stop sound fadeout 2.0

    blank "As Ben and [povname] continued moving boxes into the house, Ben struck up a conversation to lighten the mood."

    hide ben
    show ben mouth_closed at midleft

    b "So are you excited for your new place and new job? This house looks awesome!"

    show ben talking_mouth_open at midleft 

    blank "[povname] frowned slightly, not seeing what was so awesome about it."

    hide ben
    show ben mouth_closed at midleft
    
    povname "The house is huge, and it was the only one that was available immediately, that's why I decided to buy it."

    b "It's going to be weird not seeing you around anymore. We have been best friends since we were in elementary school."

    stop music fadeout 2.0
    play music "./gui/music/SCP-x6x.mp3" loop

    show olivia smiling_talking at midright with dissolve

    o "Are you new in the neighborhood?"

    hide olivia
    show olivia smile_mouth_closed at midright

    blank "[povname] turns to find a woman approaching with a friendly smile, her presence a welcome contrast to the foreboding atmosphere surrounding 657 Boulevard."

    blank "Ben shoots [povname] an unsure look."

    povname "Yeah! Just moved in."

    show olivia smiling_talking at midright

    o "You must be [povname]! I'm Olivia! It's so nice to finally meet you in person!" 

    hide olivia
    show olivia smile_mouth_closed at midright

    blank "Olivia smiles, her warm demeanor putting [povname] at ease. She presents a welcoming basket, and [povname] accepts it gratefully."

    show olivia smile_mouth_open at midright

    povname "Thank you! That's so sweet of you! It's so nice to finally talk in person!"

    show olivia smiling_talking at midright

    o "If you ever need anything, don't hesitate to ask. This neighborhood can be a bit...unique, but we all look out for each other."

    hide olivia
    show olivia smile_mouth_closed at midright

    blank "[povname] feels a wave of gratitude wash over them at Olivia's offer of support." 

    povname "Thank you, Olivia. That means a lot. And it's good to know there are friendly faces nearby. I'll definitely keep that in mind."

    blank "As Olivia bids them farewell and continues on her way, [povname] can't help but feel a glimmer of hope."
    
    blank "Perhaps, with the kindness of their new neighbor Olivia, they can find a sense of belonging in this strange and mysterious town after all."
    
    hide olivia with dissolve

    hide ben
    show ben talking_mouth_open at midleft

    b "Who was that?"

    blank "Ben's voice breaks the silence, pulling [povname] back to the present."

    blank "[povname] laughed at Ben's worried expression."


    povname "That was just Olivia, my coworker. I've been texting her for months! She's really nice. Why are you being so weird about her?"
    
    hide ben 
    show ben mouth_closed at midleft

    blank "Ben shrugged, avoiding [povname]'s gaze."

    show ben talking_mouth_open_2 at midleft

    b "I don't know, just got a weird vibe, I guess. Nevermind."

    hide ben
    show ben mouth_closed at midleft

    show joe frown_1 at midright with dissolve
    stop music fadeout 5.0
    play music "./gui/music/awkwardmeeting.mp3" fadein 2.0 loop

    blank "Before [povname] can probe further, a chilling figure emerges from the shadows."

    hide joe
    show joe talking at midright

    j "So you're moving into 657 Boulevard?"

    hide ben 
    show ben talking_mouth_open_2 at midleft

    b "AH!"

    blank "Ben cried out, jumping back in surprise."

    povname "Yeah...Today is moving day."


    blank "[povname] said sheepishly, trying to mask their initial shock."

    blank "The figure introduced himself."

    hide joe
    show joe talking_smiling at midright

    j "Want an extra hand? I am Joe by the way, I live right across the street."

    blank "Joe's voice carried an unsettling undertone."

    hide joe
    show joe smile at midright

    povname "Sure…" 
    
    blank "[povname] replied, mustering a smile despite the lingering unease."
    
    povname "As much as you're, uh, willing to help. We could use all the assistance we can get. There are still plenty of boxes to carry inside and up the stairs."

    blank "Ben, eager to divert his attention from the eerie encounter, asked,"

    hide ben 
    show ben talking_mouth_open at midleft

    b "Where should I put these boxes?"

    blank "His voice betraying a hint of apprehension as he glanced around the dimly lit entryway of the house."

    menu:
        "Who carries the boxes?"

        "Ben":
            jump ben_falls

        "[povname]":
            jump end_1

label ben_falls:
    povname "In my bedroom upstairs would be great."

    transform benwithboxes:
        xalign 0.4 yalign 0.7

    hide ben with dissolve
    show ben carrying_boxes at benwithboxes with dissolve
    blank "[povname] replies, trying to maintain a sense of normalcy despite the ominous atmosphere."

    blank "Ben nods, hoisting the boxes onto his shoulders and carefully making his way up the creaking stairs."

    blank "Each step seemed to groan beneath his weight, adding to the tension in the air."

    blank "Joe and [povname] begin to unload the moving van, placing the boxes on the driveway."

    hide ben with dissolve

    hide joe
    show joe talking_smiling at midright

    j "You seem genuine."

    hide joe
    show joe smile at midright

    blank "Joe says looking deep into [povname]'s eyes."

    hide joe
    show joe talking_smiling at midright

    j "I've seen a lot of good people come and go in this house, I hope you stick around."

    hide joe
    show joe smile at midright

    stop music

    play sound "falling_stairs.flac" volume 1.0

    blank "Before [povname] can even begin to ponder at what that might mean, a deafening crash reverberates through the house, causing them and Joe to freeze in their tracks."

    """
    {b}{size=+20}BANG!{/size}{/b}
    """

    play music "./gui/music/nightvigil.mp3" loop    
    hide joe
    show joe startled at midright

    j "What on earth was that?!"

    blank "Joe exclaims, his voice tinged with concern."
    
    scene bg stairs

    show joe startled at midright

    blank "Heart pounding, [povname] and Joe rush inside the house, their minds racing with thoughts of what could have caused the disturbance."
    
    blank "They find the boxes scattered at the bottom of the stairs, and to their horror, Ben lying unconscious beside them."

    blank "Frantic, [povname] and Joe quickly assess the situation, their hands trembling as they check for signs of life. With adrenaline coursing through their veins, they realize the severity of the situation and waste no time in getting Ben to the hospital."

    blank "Hours pass in agonizing uncertainty as [povname] paces the sterile halls of the hospital, their mind consumed with worry for their friend."
    
    blank "Finally, the doctors emerge with grave expressions, delivering the devastating news — Ben is in a coma, his injuries severe and his prognosis uncertain."

    hide joe with dissolve

    blank "As [povname] returns to their house with the knowledge of their friend stuck in a coma, the air was filled with a suffocating sense of foreboding."
    
    blank "The [povname] ventured deeper into the corridors, ready to retire for the night."

    blank "With a nervous hand, [povname] flicked on a light, revealing their bedroom shrouded in shadows."
    
    blank "And there, nestled in the corner, a pair of glowing eyes stared back at them—a solitary cat, its fur bristling with unease, as they too were sensing that there was something more to the house."

    blank "As night descended upon Whispering Hollow, [povname] couldn't shake the feeling that their arrival at 657 Boulevard had set into motion a chain of events far beyond their understanding."
    
    blank "Little did they know, the secrets of the house—and the town—were waiting to be unearthed, and the darkness that dwelled within would stop at nothing to claim its next victim."

    blank "[povname] being new to the town, wants to get to know more about it and make some friends."

    menu:
        "Who should [povname] learn more about?"

        "Joe":
            jump team_joe

        "Olivia":
            jump team_olivia

label end_1:
    povname "You can leave them right there, I can move them upstairs to the bedroom."

    blank "[povname] reassures Ben, determined to handle the task alone."
    show ben mouth_closed at midleft
    show joe smile at midright

    scene bg stairs
    hide ben 
    hide joe
    stop music
    play music "./gui/music/nightvigil.mp3" loop

    blank "As [povname] starts to ascend the stairs, the weight of the boxes pressing down on them with each step, a sudden loud crash echoes through the house."
    
    play sound "falling_stairs.flac" volume 1.0

    """
    {b}{size=+20}BANG!{/size}{/b}
    """
    
    blank "Ben and Joe freeze in terror, their hearts pounding as they rush to investigate."

    blank "Their worst fears are realized when they find [povname] lying at the foot of the stairs, blood pooling beneath their head from a severe injury."
    
    blank "Panic sets in as Ben quickly dials 911, his hands shaking as he tries to keep [povname] awake, desperately praying for help to arrive in time."
    
    blank "But before the paramedics can reach them, [povname] succumbs to their injuries, leaving Ben and Joe to grapple with the devastating loss of their friend."
    
    blank "The haunted house on 657 Boulevard claims yet another victim, its malevolent presence leaving a trail of despair in its wake."

    scene bg death

    """
    {b}{size=+25}[povname] has died{/size}{/b}
    """

    return

label team_joe:
    stop music

    blank "[povname] appreciates Olivia's note but does not pay much heed to it. [povname] recognizes that Joe is not your average neighbor. They soon realize that there are things that are strange about Joe but they still continue to trust him."
    
    blank "They know he can use a helping hand while settling into their new life and having Joe right across the street is extremely convenient."
    
    blank "[povname] decides to spend more time with Joe and continues to let him into his house to get it set up."

    scene bg room_cat

    blank "[povname] decided to keep the yellow eyed cat that appeared in the house when they moved in and named it Pepper, but they haven't shown Joe yet, since the cat hides anytime guests are over."

    blank "[povname] heard a rumor around the town that Joe killed Olivia's cat, but that couldn't be true, could it? Joe's mannerisms might be strange but he wouldn't kill a cat!"

    transform double_size_midleft: 
        xalign 0.33 yalign 1.8 zoom 1.5

    show joe smile at double_size_midleft with dissolve

    blank "The yellow eyed cat suddenly appears in the room while Joe is over. He leans down and picks up the cat, with a too-wide smile on his face."

    scene bg room_cat

    menu:
        "Do you believe the rumors about Joe?"
        
        "[povname] wants to hear Joe out":
            jump nice_to_joe

        "[povname] doesn't trust Joe with their cat":
            jump mean_to_joe

label nice_to_joe:

    transform double_size_midleft1:
        xalign 0.2 yalign 1.8 zoom 1.5

    scene bg gamestable
    show joe smile at double_size_midleft1

    blank "[povname] and Joe chat for a few hours over a board game and some coffee. Joe suddenly stands up."

    hide joe
    show joe talking_smiling at double_size_midleft1

    j "Thanks for giving me the chance to show you who I really am, most people are scared of me when they hear all the dumb stuff people say about me."

    hide joe
    show joe smile at double_size_midleft1

    povname "I'm sorry everyone tells you who to be, man. I know you'd never hurt a fly."

    hide joe 
    show joe frown_1 at double_size_midleft1

    j "That's not what Olivia tells everybody." 
    

    blank "Joe looks at the floor, sadness in his eyes."

    povname "Why does she hate you so much?"

    hide joe
    show joe talking_smiling at double_size_midleft1

    j "Probably because I'm the only person who knows the real Olivia."

    povname "What do you mean by that?"

    hide joe
    show joe startled at double_size_midleft1

    j "She actually killed MY cat. Olivia has never even HAD a cat! But because I dress a bit alternatively, have a special interst in frogs, and keep to myself, everyone would rather believe Miss Queen Bee Sorority Girly Olivia."

    povname "Wow. I am SO sorry Joe." 

    menu:
        "How do you feel now that you know the truth?"

        "[povname] believes Joe":
            jump believes_joe

        "[povname] doesn't know who to believe":
            jump doesnt_know

        "[povname] thinks Joe is lying":
            jump joe_lying

label mean_to_joe:

    show joe smile at double_size_midleft1

    povname "{b}{size=+25}Pepper!!{/size}{/b}"
    
    hide joe 
    show joe frown_1 at double_size_midleft1

    blank "[povname] screams at his cat to get away from Joe."

    scene bg closed_door

    blank "The [povname] was hesitant to have their cat around Joe but didn't want to be rude or mean about it. [povname] lifts Pepper from Joe's lap and takes him to the room, aggressively shutting the door behind him."

    menu:
        "Do you feel bad for Joe?"  

        "[povname] doesn't feel bad for Joe":
            jump doesnt_feel_bad_joe
        
        "[povname] feels bad for Joe":
            jump feels_bad_joe

label doesnt_feel_bad_joe:


label feels_bad_joe:
    scene bg house_joe
    blank "A few weeks go by, and [povname] feels like maybe they overreacted about Joe and their cat. Maybe [povname] should go apologize and hear his side of the story with Olivia."

    blank "[povname] walks down the street to his yard, he only lives a few houses down. Maybe they could become friends and start hanging out, they are neighbors."
    
    blank "[povname] puts their hands in their pockets sheepishly and follows the path to his front door."

    blank "[povname] feels their hands start to get clammy as they press the doorbell. They hear someone on the other side of the door."
    p "Hey neighbor."

    show joe talking_smiling at midright with dissolve

    blank "Joe opens the door and stares at [povname], unblinking."
    
    hide joe
    show joe frown_1 at midright

    povname "I just wanted to apologize for my overreaction the other day. I shouldn't have listened to rumors about you."
    
    povname "It's so high school and immature. I should've talked to you and heard you out before making judgements about your character. I'm sorry Joe."

    hide joe
    show joe startled at midright

    j "Get off my lawn."

    blank "Joe stares at [povname] for a few beats too long before erupting into laughter."

    j "I'm totally kidding. Oh! But you should've seen your face!"

    blank "[povname] laughs nervously, after having an adrenaline rush from Joe's wicked humor."

    scene bg cookies

    j "A Neighbor dropped off some cookies and I just sat down to have some if you would like a bite? I can tell you what actually happened with me and Olivia."

    povname "Yeah...That would be great. Thanks, man."
    
    blank "They sit down at Joe's kitchen table where there are some beautiful sugar cookies on a white and red plate and a teapot. Joe pours them each a cup and they grab some cookies."

    povname "Wow, these are SO good."

    j "I'm pretty sure it's from Sharon down the road, this is what she always brings to potlucks."

    povname "So what's the deal with you and Olivia?"

    blank "Joe takes a deep sigh."

    j "She's had it out for me ever since I moved in. It only got worse after her divorce. She killed my cat. Then, because all she cares about is her reputation, she flipped the story and turned the neighborhood against me."
    
    j "I lost all my friends, my dignity, and my cat."

    povname "I am so sorry Joe, I'm sorry I ever doubted you."

    blank "The two chat for a while and snack on the cookies, when [povname] notices that the red and white plate is actually a white plate with red writing on it."

    scene bg cookies_close

    povname "Hey Joe,"

    blank "[povname] moves some of the remaining cookies out of the way."

    povname "What does this say?"

    blank "Joe slumps over in his chair, falling on the tile floor with a slap."
    
    blank "[povname] looks at the plate."

    scene bg cookies_olivia

    povname "Love, Olivia?!"

    scene bg death

    blank "[povname] dies from poison."
    
    """
    {b}{size=+25}END - OLIVA KILLS PLAYER{/size}{/b}
    """

    return

label believes_joe:


label doesnt_know:


label joe_lying:


label team_olivia:
    blank "[povname] decides to befriend Olivia, and begins to hang out with her routinely."
    
    blank "They walk together at night around the neighborhood, and for a while, it seems that everything is fine."

    blank "Although there haven’t been any more accidents, [povname] can’t shake the feeling that there is something much older, and darker lurking in the shadows."

    blank "[povname] decides to confide in Olivia of their concerns about the situation."

    menu:
        "They decides to ask Olivia about:"  

        "Ask Olivia about Joe":
            jump ask_about_joe
        
        "Ask Olivia about the house and town":
            jump ask_about_house


label ask_about_joe:
    blank "[povname] decides to ask Olivia about Joe, hoping to quell the eerie feeling [povname] gets whenever Joe is around."
    
    povname "Olivia, can I ask you about Joe?"

    blank "Olivia turns to [povname] with a slight frown on her face." 
    
    o "Joe, what about him?"

    povname "Well, I’ve noticed he seems a bit off. Do you know anything about him?"

    blank "A hint of anger appears in her eyes."

    o "I would be careful around him if I were you."

    blank "It seems that Olivia is not keen on responding to questions about Joe. [povname], however, grows more curious and wants to uncover the truth about Joe."

    blank "[povname] hesitates, but decides to press further."

    povname "I’ve heard some rumors… that he might have caused some trouble?"

    blank "Suddenly, Olivia’s calm demeanor breaks, and with an uncharacteristic burst of emotion, she exclaims."

    o "Trouble? You have no idea! He killed my cat!"

    blank "Following this shocking revelation, [povname] sees Joe in a much darker light."
    
    blank "But, alongside this suspicion towards Joe, [povname] can’t help but feel shocked at Olivia’s sudden outburst, and a sense of doubt regarding Olivia’s accusation creeps in."

    menu:

        "Believe Olivia":
            jump believe_olivia
        
        "Doubt Olivia":
            jump doubt_olivia


label ask_about_house:
    blank "Olivia sighs and settles down on the chair."

    o "The house has a long and unforgiving history."

    blank "This change in her tone unsettles [povname]. [povname] is eager to hear more so Olivia continues."

    o "There have been incidents…"
    
    o "A family who lived there before you, their child died. After that, they just disappeared. Some say they were taken by the darkness that resides within those walls. "

    blank "[povname]'s heart sinks and a heavy feeling takes over. The weight of Olivia’s words sink in, sending a shiver down [povname]'s spine."

    menu:

        "Ask Olivia to stay":
            jump stay_olivia
        
        "Say nothing":
            jump say_nothing


label believe_olivia:
    blank "[povname] believes Olivia and thanks her for sharing the story."

    blank "After their talk, [povname] heads back home to finish setting up their new home."

    blank "[povname] is cleaning their home and notices an antique dresser at the corner of the room."

    blank "Curious, [povname] wants to explore, however, [povname] is also exhausted and has a whole house to clean up like the dusty bookshelf or sorting through the attic."

    menu:
        "What should the [povname] focus on?"  

        "Attic":
            jump not_dresser
        
        "Dresser":
            jump dresser

        "Bookshelf":
            jump not_dresser


label doubt_olivia:
    blank "[povname] decides not to trust Olivia and gets up to confront her."

    blank "[povname] doubts Olivia because of her sudden outburst."

    povname "I’m not sure if I can trust the fact that Joe just killed your cat. He seems like a nice guy, I don’t think he would do something like that."

    blank "Olivia sighs and speaks calmly."

    o "Well, he did. Why wouldn’t you trust me? I wouldn’t make something up for no reason."

    povname "Well, I would like to get to hear both sides of the story and ask Joe…"

    blank "[povname] suddenly feels a sharp pain on their abdomen."

    blank "They look down and see a knife piercing through the skin."

    povname "I knew I shouldn’t have trusted you…"

    scene black with dissolve

    blank "[povname] breathes out before falling to the ground, everything fading to black..."

    blank "OLIVIA BAD END 1"

    return


label stay_olivia:
    blank "[povname] is terrified by the idea of their house being haunted, possibly by ghosts."

    blank "Olivia eagerly offers to let [povname] live in her spare bedroom."

    o "Oh I just realized, my old roommate recently left, and I guess her bedroom is now open. Since we’re good friends, I’ll gladly let you live there for free!"

    povname "Great, thanks so much! I’ll start packing my bags…"

    blank "On a chilly Thursday evening, [povname] is moving her boxes one by one into the house."
    
    blank "Olivia then points to an empty room, directing them to check out the space."

    o "Hey the room is right over here, wanna check it out real quick? There’s no bedbugs I promise :)"

    blank "[povname] enters the room, and notices that something is a bit off."

    blank "First, the door seemed awfully thick, and it was a struggle to even open it. The walls were gray and blank, and the window had bars over them."

    blank "Before [povname] even has time to process the situation, the door slams shut behind them and a click of the lock sounds."

    povname "Ha Olivia thats funny, you can let me out now."

    blank "..."

    povname "Hello? Let me out now!"

    blank "A couple hours later, Joe arrives at the window."

    j "Hmm what do we have here?"

    menu:

        "Ask Joe for help":
            jump joe_help
        
        "Tell Joe to go away":
            jump joe_go_away


label say_nothing:
    blank "[povname] decides to keep living in the house after being told about the house background."

    jump believe_olivia


label not_dresser:

    blank "[povname] decides to ignore the dresser and continue cleaning the rest of the house."

    blank "[povname] continues on with life, staying friends with Olivia."
    
    blank "Nothing bad happens to the [povname], however spooky things continue to occur in the house."

    blank "OLIVIA FRIEND END"

    return


label joe_help:
    povname "Help me, Joe! Olivia locked me in here, and I’m trapped."

    blank "Joe leaves and comes back with an angle grinder and cuts through the window bars, letting [povname] out."

    j "Stay away from Olivia, and get back home ASAP!"

    blank "[povname] runs home and is frantically packing up all their belongings wanting to get far away from this town."
    
    blank "As they are packing, they notice something in the dresser."

    jump dresser


label joe_go_away:
    povname "Go away, creepy man!"

    blank "Joe mutters under his breath that you’re making the wrong choice and shuffles away."

    blank "[povname] continues to pound on the door, screaming at Olivia to let them out. Hours pass, and Olivia finally responds."

    o "Heyyy [povname], I’m so sorry, but I had to do this. The truth is, your house isn’t really haunted."

    o "I used to live there, and had to move out when my boyfriend died of, uh, natural causes…"

    o "Anyway, now that you’re locked in here, I can finally move back in again! Don’t worry, I’m sure you’ll be fine living here, you can get water from the bathroom sink!"

    povname "LET ME OUT! Wait, what am I going to eat?"

    o "I’m sure you’ll be able to, like photosynthesize or something. Bye!"

    blank "After a few weeks pass, player dies of starvation."

    blank "STARVATION END"

    return


label dresser: 
    blank "[povname] finds scraps of torn paper behind the dresser. Curious, [povname] attempts to arrange the pieces together to see what it says."

    povname "Hmm, interesting. It seems like someone wrote something and then tore it all up. I wonder what it says."

    #### PUT MINI GAME HERE ####
    #### jump to solved_puzzle or not_solved_puzzle ####
    $setup_puzzle()
    call screen reassemble_puzzle


label solved_puzzle:
    blank "Once the puzzle is solved, it reveals a confession note written by Olivia, revealing all the crimes she committed, including killing the cat, her boyfriend, and causing the house to seem haunted."

    blank "Player immediately calls 911, alerting the police who then arrest Olivia."

    blank "GOOD END ([povname] wins game)"

    return

label not_solved_puzzle:
    blank "[povname] does not solve the puzzle in time, and Olivia walks in on the [povname] arranging the puzzle."

    o "Hey! What are you doing?"

    blank "[povname] hesitates for a second to let Olivia know what's going on."

    povname "Oh, I just found these torn pieces of paper, and I was trying to put them back together to see what it says."

    o "I would suggest throwing them away, I’m sure it's nothing important! I’m sure your time is valuable and doubt you should be wasting your efforts on something like this…"

    povname "Its ok, I have nothing better to do"

    o "This is your last warning…"

    povname "Olivia, stop it, you’re acting weird."

    blank "Before [povname] can even think, [povname] suddenly feels a sharp pain on their abdomen."

    blank "They look down and see a knife piercing through the skin."

    scene black with dissolve

    blank "Falling to the ground, everything fades to black."

    blank "OLIVIA BAD END 2"

    return

# This ends the game.
return
