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

image ben carrying_boxes = "images/characters/ben/ben-carrying-boxes.png"
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




# The game starts here.

label start:
    $ povname = renpy.input("What is your name?", length=32)
    $ povname = povname.strip()
    play music "./gui/music/dopplerette.mp3" volume 1.5 loop 
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg house

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ben talking_mouth_open
    # These display lines of dialogue.

    """
    As the sun dipped below the horizon, casting long shadows over the eerie town of Whispering Hollow, a chill crept down [povname]'s back. They stood before what would be their new home, 657 Boulevard.

    A new job awaits in this small forsaken town, and the only available residence was this haunted house. Clutching their keys tightly, [povname] couldn't shake the feeling of unease that settled on their shoulders.

    As Ben and [povname] continued moving boxes into the house, Ben struck up a conversation to lighten the mood.
    """
    
    b "So are you excited for your new place and new job? This house looks awesome!"

    """ 
    [povname] frowned slightly, not seeing what was so awesome about it.
    """
    
    povname "The house is huge, and it was the only one that was available immediately, that's why I decided to buy it."

    b "It's going to be weird not seeing you around anymore. We have been best friends since we were in elementary school."

    stop music fadeout 2.0
    play music "./gui/music/SCP-x6x.mp3" loop

    o "Are you new in the neighborhood?"

    """
    [povname] turns to find a woman approaching with a friendly smile, her presence a welcome contrast to the foreboding atmosphere surrounding 657 Boulevard.
    Ben shoots [povname] an unsure look.
    """

    povname "Yeah! Just moved in."

    o "You must be [povname]! I'm Olivia! It's so nice to finally meet you in person!" 

    """
    Olivia smiles, her warm demeanor putting [povname] at ease. She presents a welcoming basket, and [povname] accepts it gratefully.
    """

    povname "Thank you! That's so sweet of you! It's so nice to finally talk in person!"

    o "If you ever need anything, don't hesitate to ask. This neighborhood can be a bit...unique, but we all look out for each other."

    """
    [povname] feels a wave of gratitude wash over them at Olivia's offer of support. 
    """

    povname "Thank you, Olivia. That means a lot. And it's good to know there are friendly faces nearby. I'll definitely keep that in mind."

    """
    As Olivia bids them farewell and continues on her way, [povname] can't help but feel a glimmer of hope. Perhaps, with the kindness of their new neighbor Olivia, they can find a sense of belonging in this strange and mysterious town after all.
    """
 
    b "Who was that?"

    """
    Ben's voice breaks the silence, pulling [povname] back to the present.
    [povname] laughed at Ben's worried expression.
    """

    povname "That was just Olivia, my coworker. I've been texting her for months! She's really nice. Why are you being so weird about her?"
    
    """
    Ben shrugged, avoiding [povname]'s gaze.
    """

    b "I don't know, just got a weird vibe, I guess. Nevermind."

    stop music fadeout 5.0
    play music "./gui/music/awkwardmeeting.mp3" fadein 2.0 loop
    """
    Before [povname] can probe further, a chilling figure emerges from the shadows.
    """

    j "So you're moving into 657 Boulevard?"

    b "AH!"

    """
    Ben cried out, jumping back in surprise.
    """

    povname "Yeah...Today is moving day."

    """
    [povname] said sheepishly, trying to mask their initial shock.
    """

    """
    The figure introduced himself, offering his hand.
    """

    j "Want an extra hand? I am Joe by the way, I live right across the street."

    """
    Joe's voice carried an unsettling undertone.
    """

    povname "Sure…" 
    
    """
    [povname] replied, mustering a smile despite the lingering unease.
    """
    
    povname "As much as you're, uh, willing to help. We could use all the assistance we can get. There are still plenty of boxes to carry inside and up the stairs."

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

        "[povname]":
            jump end_1

label ben_falls:
    povname "In my bedroom upstairs would be great."

    """
    [povname] replies, trying to maintain a sense of normalcy despite the ominous atmosphere.
    Ben nods, hoisting the boxes onto his shoulders and carefully making his way up the creaking stairs. 
    Each step seemed to groan beneath his weight, adding to the tension in the air.
    Joe and [povname] begin to unload the moving van, placing the boxes on the driveway.
    """

    j "You seem genuine."

    """
    Joe says looking deep into [povname]'s eyes.
    """

    j "I've seen a lot of good people come and go in this house, I hope you stick around."

    stop music
    """
    Before [povname] can even begin to ponder at what that might mean, a deafening crash reverberates through the house, causing them and Joe to freeze in their tracks.
    """

    """
    {b}{size=+20}BANG!{/size}{/b}
    """
    play music "./gui/music/nightvigil.mp3" loop
    j "What on earth was that?!"

    """
    Joe exclaims, his voice tinged with concern.

    """
    
    scene bg stairs

    """
    Heart pounding, [povname] and Joe rush inside the house, their minds racing with thoughts of what could have caused the disturbance. They find the boxes scattered at the bottom of the stairs, and to their horror, Ben lying unconscious beside them.
    Frantic, [povname] and Joe quickly assess the situation, their hands trembling as they check for signs of life. With adrenaline coursing through their veins, they realize the severity of the situation and waste no time in getting Ben to the hospital.
    Hours pass in agonizing uncertainty as [povname] paces the sterile halls of the hospital, their mind consumed with worry for their friend. Finally, the doctors emerge with grave expressions, delivering the devastating news—Ben is in a coma, his injuries severe and his prognosis uncertain.
    """

    """
    As [povname] returns to their house with the knowledge of their friend stuck in a coma, the air was filled with a suffocating sense of foreboding. The [povname] ventured deeper into the corridors, ready to retire for the night.
    With a nervous hand, [povname] flicked on a light, revealing their bedroom shrouded in shadows. And there, nestled in the corner, a pair of glowing eyes stared back at them—a solitary cat, its fur bristling with unease, as they too were sensing that there was something more to the house.
    As night descended upon Whispering Hollow, [povname] couldn't shake the feeling that their arrival at 657 Boulevard had set into motion a chain of events far beyond their understanding. Little did they know, the secrets of the house—and the town—were waiting to be unearthed, and the darkness that dwelled within would stop at nothing to claim its next victim.
    [povname] being new to the town, wants to get to know more about it and make some friends. 
    """

    menu:
        "Who should [povname] learn more about?"

        "Joe":
            jump team_joe

        "Olivia":
            jump team_olivia

label end_1:
    "You can leave them right there, I can move them upstairs to the bedroom."

    """
    [povname] reassures Ben, determined to handle the task alone.
    """
    scene bg stairs
    stop music
    play music "./gui/music/nightvigil.mp3" loop
    """
    As [povname] starts to ascend the stairs, the weight of the boxes pressing down on them with each step, a sudden loud crash echoes through the house. BANG!  Ben and Joe freeze in terror, their hearts pounding as they rush to investigate.
    Their worst fears are realized when they find [povname] lying at the foot of the stairs, blood pooling beneath their head from a severe injury. Panic sets in as Ben quickly dials 911, his hands shaking as he tries to keep [povname] awake, desperately praying for help to arrive in time.
    But before the paramedics can reach them, [povname] succumbs to their injuries, leaving Ben and Joe to grapple with the devastating loss of their friend. The haunted house on 657 Boulevard claims yet another victim, its malevolent presence leaving a trail of despair in its wake.
    """ 
    scene bg death

    """
    {b}{size=+25}[povname] has died{/size}{/b}
    """

    return

label team_joe:
    stop music
    """
    [povname] appreciates Olivia's note but does not pay much heed to it. [povname] recognizes that Joe is not your average neighbor. They soon realize that there are things that are strange about Joe but they still continue to trust him. They know he can use a helping hand while settling into their new life and having Joe right across the street is extremely convenient. [povname] decides to spend more time with Joe and continues to let him into his house to get it set up. 

    [povname] decided to keep the yellow eyed cat that appeared in the house when they moved in and named it Pepper, but they haven't shown Joe yet, since the cat hides anytime guests are over. 

    [povname] heard a rumor around the town that Joe killed Olivia's cat, but that couldn't be true, could it? Joe's mannerisms might be strange but he wouldn't kill a cat!

    The yellow eyed cat suddenly appears in the room while Joe is over. He leans down and picks up the cat, with a too-wide smile on his face.
    """

    scene bg room_cat

    menu:
        "Do you believe the rumors about Joe?"
        
        "[povname] wants to hear Joe out":
            jump nice_to_joe

        "[povname] doesn't trust Joe with their cat":
            jump mean_to_joe

label nice_to_joe:
    scene bg gamestable
    """
    [povname] and Joe chat for a few hours over a board game and some coffee. Joe suddenly stands up.
    """

    j "Thanks for giving me the chance to show you who I really am, most people are scared of me when they hear all the dumb stuff people say about me."

    povname "I'm sorry everyone tells you who to be, man. I know you'd never hurt a fly."

    j "That's not what Olivia tells everybody." 
    
    """
    Joe looks at the floor, sadness in his eyes.
    """

    povname "Why does she hate you so much?"

    j "Probably because I'm the only person who knows the real Olivia."

    povname "What do you mean by that?"

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
    povname "{b}{size=+25}Pepper!!{/size}{/b}"
    
    """
    [povname] screams at his cat to get away from Joe. 
    """

    scene bg closed_door

    """
    The [povname] was hesitant to have their cat around Joe but didn't want to be rude or mean about it. [povname] lifts Pepper from Joe's lap and takes him to the room, aggressively shutting the door behind him.
    """
    menu:
        "Do you feel bad for Joe?"  

        "[povname] doesn't feel bad for Joe":
            jump doesnt_feel_bad_joe
        
        "[povname] feels bad for Joe":
            jump feels_bad_joe

label doesnt_feel_bad_joe:


label feels_bad_joe:
    scene bg house_joe
    """
    A few weeks go by, and [povname] feels like maybe they overreacted about Joe and their cat. Maybe [povname] should go apologize and hear his side of the story with Olivia. 

    [povname] walks down the street to his yard, he only lives a few houses down. Maybe they could become friends and start hanging out, they are neighbors. [povname] puts their hands in their pockets sheepishly and follows the path to his front door. 

    [povname] feels their hands start to get clammy as they press the doorbell. They hear someone on the other side of the door.
    """
    

    j "Hey neighbor."

    """
    Joe opens the door and stares at [povname], unblinking.
    """

    povname "I just wanted to apologize for my overreaction the other day. I shouldn't have listened to rumors about you. It's so high school and immature. I should've talked to you and heard you out before making judgements about your character. I'm sorry Joe."

    j "Get off my lawn."

    """
    Joe stares at [povname] for a few beats too long before erupting into laughter.
    """

    j "I'm totally kidding. Oh! But you should've seen your face!"

    """
    [povname] laughs nervously, after having an adrenaline rush from Joe's wicked humor.
    """
    scene bg cookies

    j "A Neighbor dropped off some cookies and I just sat down to have some if you would like a bite? I can tell you what actually happened with me and Olivia."

    povname "Yeah...That would be great. Thanks, man."
    

    """
    They sit down at Joe's kitchen table where there are some beautiful sugar cookies on a white and red plate and a teapot. Joe pours them each a cup and they grab some cookies.
    """

    povname "Wow, these are SO good."

    j "I'm pretty sure it's from Sharon down the road, this is what she always brings to potlucks."

    povname "So what's the deal with you and Olivia?"

    """
    Joe takes a deep sigh.
    """

    j "She's had it out for me ever since I moved in. It only got worse after her divorce. She killed my cat. Then, because all she cares about is her reputation, she flipped the story and turned the neighborhood against me. I lost all my friends, my dignity, and my cat."

    povname "I am so sorry Joe, I'm sorry I ever doubted you."

    

    """
    The two chat for a while and snack on the cookies, when [povname] notices that the red and white plate is actually a white plate with red writing on it.
    """

    scene bg cookies_close

    povname "Hey Joe,"

    """
    [povname] moves some of the remaining cookies out of the way.
    """

    povname "What does this say?"

    """
    Joe slumps over in his chair, falling on the tile floor with a slap.
    
    [povname] looks at the plate.
    """

    scene bg cookies_olivia

    povname "Love, Olivia?!"

    scene bg death

    """
    [povname] dies from poison.
    """
    
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