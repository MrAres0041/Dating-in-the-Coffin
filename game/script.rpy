# Other stuff
init python:
    def V1(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/sfx/voices/V1.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def V2(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/sfx/voices/V2.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def V3(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/sfx/voices/V3.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def V4(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/sfx/voices/V4.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def V5(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/sfx/voices/V5.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def V6(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/sfx/voices/V6.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def V7(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/sfx/voices/V7.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def V8(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/sfx/voices/V8.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def text_sound(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("audio/sfx/voices/writting.wav")
        elif event == "slow_done":
            renpy.sound.stop()

# Variables

default AshleyAff = 0
default AndrewAff = 0
default DualAff = 0
default JuliaAff = 0

# Backgrounds
image advertising = "gui/advertising.png"
image advertising2 = "gui/advertising2.png"
image main = "gui/main_menu.png"

image cabin_front = "images/bgs/cabin.png"
image cabin_side = "images/bgs/cabin2.png"
image office = "images/bgs/office.png"
image cabin_inside1 = "images/bgs/cabin_inside1.png"
image drive = "images/bgs/I drive.png"
image motel1 = "images/bgs/motel1.png"
image motel2 = "images/bgs/motel2.png"
image crime1 = "images/bgs/crime1.png"
image crime2 = "images/bgs/crime2.png"
image eat food = "images/bgs/eat food.png"
image park = "images/bgs/park.png"
image malaga = "images/bgs/Malaga.png"
image driving = "images/bgs/Driving.png"
image passion = "images/bgs/club passion.png"
image club1 = "images/bgs/club f1.png"
image club2 = "images/bgs/club f2.png"
image car = "images/bgs/car.png"
image table = "images/bgs/table.png"
image JohnnyF1 = "images/bgs/Johnny1.png"
image end1 = "images/bgs/TGC.png"
image club_in = "images/bgs/club in.png"
image club_night = "images/bgs/cabin night.png"
image M_Room = "images/bgs/Motel_room.png"
image dream1 = "images/bgs/dream1.png"
image Forest1 = "images/bgs/Forest1.png"
image Forest2 = "images/bgs/Forest2.png"
image Forest3 = "images/bgs/Forest3.png"
image Forest4 = "images/bgs/Forest4.png"
image LabOut = "images/bgs/LabOut.png"
image Lab1 = "images/bgs/Lab1.png"
image CarsonEntrance = "images/bgs/Carson.png"
image car0 = "images/bgs/car0.png"
image car1 = "images/bgs/car1.png"
image car2 = "images/bgs/car2.png"
image car3 = "images/bgs/car3.png"
image JvC = "images/bgs/Johnny vs Carson.png"
image city1 = "images/bgs/ciity1.png"
image Jul = "images/bgs/Jul.png"
image HouseOut = "images/bgs/HouseOut.png"
image DoorOpening = "images/bgs/DoorOpening.png"
image FrontDoor = "images/bgs/FrontDoor.png"
image OpenFrontDoor = "images/bgs/OpenFrontDoor.png"
image HouseIn1 = "images/bgs/HouseIn1.png"
image HouseIn2 = "images/bgs/HouseIn2.png"





image start1 = "images/bgs/Encounter Zero.png"
image start2 = "images/bgs/First Encounter.png"



# Polaroids

image Pol1 = "images/polaroids/Pol1.png"
image Pol2 = "images/polaroids/Pol2.png"
image Pol3 = "images/polaroids/Pol3.png"
image Pol4 = "images/polaroids/Pol4.png"
image Pol5 = "images/polaroids/Pol5.png"
image Pol6 = "images/polaroids/Pol6.png"
image Pol7 = "images/polaroids/Pol7.png"
image Pol8 = "images/polaroids/Pol8.png"
image Pol9 = "images/polaroids/Pol9.png"


# Items
image shovel ="images/objects/Shovel.png"
image butcher ="images/objects/butcher.png"
image sodas = "images/objects/soda.png"
image notepad = "images/objects/notepad.png"
image keys = "images/objects/keys.png"
image HF = "images/objects/HF.png"


# Characters
define items = Character(what_prefix='{i}"', what_suffix='"')
define narrator = Character(callback=text_sound)
define Johnny = Character("Jonathan", what_prefix='{i}"', what_suffix='"',  color="#bd0d1f", callback=V2)
define UnJohnny = Character("???", what_prefix='{i}"', what_suffix='"',  color="#bd0d1f", callback=V2)
define Andrew = Character("Andrew", what_prefix='{i}"', what_suffix='"',  color="#389438", callback=V3)
define Ashley = Character("Ashley", what_prefix='{i}"', what_suffix='"', color="#cf55ae", callback=V5)
define Officer = Character("Officer", what_prefix='{i}"', what_suffix='"', color="#1417b5", callback=V4)
define Lars = Character("Lars", what_prefix='{i}"', what_suffix='"', color="#0080ff", callback=V6)
define UnCarson = Character("???", what_prefix='{i}"', what_suffix='"', color="#ffff66", callback=V7)
define Carson = Character("Carson", what_prefix='{i}"', what_suffix='"', color="#ffff66", callback=V7)
define UnJulia = Character("???", what_prefix='{i}"', what_suffix='"', color="#ffff99", callback=V8)
define Julia = Character("Julia", what_prefix='{i}"', what_suffix='"', color="#ffff99", callback=V8)


# Sprites

image Johnny = "images/sprites/Johnny/JP_1.png"
image Johnny R = "images/sprites/Johnny/JP_1R.png"
image Johnny smug1 = "images/sprites/Johnny/JP_2.png"
image Johnny smug1 R = "images/sprites/Johnny/JP_2R.png"
image Johnny serious1 = "images/sprites/Johnny/JP_3.png"
image Johnny serious1 R = "images/sprites/Johnny/JP_3R.png"
image Johnny chat1 = "images/sprites/Johnny/JP_4.png"
image Johnny chat1 R = "images/sprites/Johnny/JP_4R.png"
image Johnny smile1 = "images/sprites/Johnny/JP_5.png"
image Johnny smile1 R = "images/sprites/Johnny/JP_5R.png"
image Johnny smile2 = "images/sprites/Johnny/JP_6.png"
image Johnny smile2 R = "images/sprites/Johnny/JP_6R.png"
image Johnny smug2 = "images/sprites/Johnny/JP_7.png"
image Johnny smug2 R = "images/sprites/Johnny/JP_7R.png"
image Johnny serious2= "images/sprites/Johnny/JP_8.png"
image Johnny serious2 R = "images/sprites/Johnny/JP_8R.png"
image Johnny serious3= "images/sprites/Johnny/JP_9.png"
image Johnny serious3 R = "images/sprites/Johnny/JP_9R.png"
image Johnny sigh= "images/sprites/Johnny/JP_10.png"
image Johnny sigh R= "images/sprites/Johnny/JP_10R.png"
image Johnny P= "images/sprites/Johnny/JP_11.png"
image Johnny P R= "images/sprites/Johnny/JP_11R.png"
image Johnny P2= "images/sprites/Johnny/JP_12.png"
image Johnny P2 R= "images/sprites/Johnny/JP_12R.png"
image Johnny confused= "images/sprites/Johnny/JP_13.png"
image Johnny confused R= "images/sprites/Johnny/JP_13R.png"
image Johnny angry1= "images/sprites/Johnny/JP_14.png"
image Johnny angry1 R= "images/sprites/Johnny/JP_14R.png"
image Johnny angry2= "images/sprites/Johnny/JP_15.png"
image Johnny angry2 R= "images/sprites/Johnny/JP_15R.png"
image Johnny shovel = "images/sprites/Johnny/JP_S.png"

image Ashley angry1 = "images/sprites/Ashley/A_1.png"
#image Ashley angry1 R = "images/sprites/Ashley/A_1R.png"
image Ashley pout1 = "images/sprites/Ashley/A_2.png"
#image Ashley pout1 R = "images/sprites/Ashley/A_2R.png"
image Ashley smug2 = "images/sprites/Ashley/A_3.png"
#image Ashley smug2 R = "images/sprites/Ashley/A_3R.png"
image Ashley smug1 = "images/sprites/Ashley/A_4.png"
#image Ashley smug1 R = "images/sprites/Ashley/A_4R.png"
image Ashley angry2 = "images/sprites/Ashley/A_5.png"
#image Ashley angry2 R = "images/sprites/Ashley/A_5R.png"
image Ashley smug3 = "images/sprites/Ashley/A_6.png"
image Ashley smug3 R = "images/sprites/Ashley/A_6R.png"
image Ashley giggle1 = "images/sprites/Ashley/A_7.png"
#image Ashley giggle1 R = "images/sprites/Ashley/A_7R.png"
image Ashley mad = "images/sprites/Ashley/A_8.png"
#image Ashley mad R = "images/sprites/Ashley/A_8R.png"
image Ashley = "images/sprites/Ashley/A_9.png"
#image Ashley R = "images/sprites/Ashley/A_9R.png"
image Ashley think = "images/sprites/Ashley/A_10.png"
image Ashley ewww = "images/sprites/Ashley/A_11.png"
image Ashley mad2 = "images/sprites/Ashley/A_12.png"
image Ashley mad3 = "images/sprites/Ashley/A_13.png"
image Ashley mocking1 = "images/sprites/Ashley/A_14.png"
image Ashley worried1 = "images/sprites/Ashley/A_15.png"
image Ashley worried2 = "images/sprites/Ashley/A_16.png"

image Andrew sigh = "images/sprites/Andrew/An_1.png"
#image Andrew sigh R = "images/sprites/Andrew/An_1R.png"
image Andrew serious1 = "images/sprites/Andrew/An_2.png"
#image Andrew serious1 R = "images/sprites/Andrew/An_2R.png"
image Andrew nervous1 = "images/sprites/Andrew/An_3.png"
#image Andrew nervous1 R = "images/sprites/Andrew/An_3R.png"
image Andrew smug1 = "images/sprites/Andrew/An_4.png"
#image Andrew smug1 R = "images/sprites/Andrew/An_4R.png"
image Andrew chat1 = "images/sprites/Andrew/An_5.png"
#image Andrew chat1 R = "images/sprites/Andrew/An_5R.png"
image Andrew facepalm = "images/sprites/Andrew/An_6.png"
#image Andrew facepalm R = "images/sprites/Andrew/An_6R.png"
image Andrew smug2 = "images/sprites/Andrew/An_7.png"
#image Andrew smug2 R = "images/sprites/Andrew/An_7R.png"
image Andrew superangry = "images/sprites/Andrew/An_8.png"
#image Andrew superangry R = "images/sprites/Andrew/An_8R.png"
image Andrew nervous2 = "images/sprites/Andrew/An_9.png"
#image Andrew nervous2 R = "images/sprites/Andrew/An_9R.png"
image Andrew confused = "images/sprites/Andrew/An_10.png"
image Andrew worried1 = "images/sprites/Andrew/An_11.png"
image Andrew angry1 = "images/sprites/Andrew/An_12.png"
image Andrew sigh2 = "images/sprites/Andrew/An_13.png"
image Andrew angry2 = "images/sprites/Andrew/An_14.png"
image Andrew = "images/sprites/Andrew/An_15.png"
image Andrew what = "images/sprites/Andrew/An_16.png"

image Julia chat1 = "images/sprites/Julia/J1.png"
image Julia = "images/sprites/Julia/J2.png"
image Julia serious1 = "images/sprites/Julia/J3.png"
image Julia chat2 = "images/sprites/Julia/J4.png"
image Julia down = "images/sprites/Julia/J5.png"
image Julia nervous = "images/sprites/Julia/J6.png"
image Julia sad = "images/sprites/Julia/J7.png"
image Julia happy = "images/sprites/Julia/J8.png"
image Julia giggle = "images/sprites/Julia/J9.png"
image Julia smile = "images/sprites/Julia/J10.png"
image Julia ewww = "images/sprites/Julia/J11.png"
#image Julia angry = "images/sprites/Julia/J12.png"
image Julia scream = "images/sprites/Julia/J13.png"
image Julia chat1 R = "images/sprites/Julia/J1_R.png"
image Julia R = "images/sprites/Julia/J2_R.png"
image Julia serious1 R = "images/sprites/Julia/J3_R.png"
image Julia chat2 R = "images/sprites/Julia/J4_R.png"
image Julia down R = "images/sprites/Julia/J5_R.png"
image Julia nervous R = "images/sprites/Julia/J6_R.png"
image Julia sad R = "images/sprites/Julia/J7_R.png"
image Julia happy R = "images/sprites/Julia/J8_R.png"
image Julia giggle R = "images/sprites/Julia/J9_R.png"
image Julia smile R = "images/sprites/Julia/J10_R.png"
image Julia ewww R = "images/sprites/Julia/J11_R.png"
image Julia angry R = "images/sprites/Julia/J12_R.png"
image Julia scream R = "images/sprites/Julia/J13_R.png"


image Officer scared = "images/sprites/Others/P1.png"
image Officer serious = "images/sprites/Others/P2.png"
image Officer nervous1 = "images/sprites/Others/P3.png"
image Officer nervous2 = "images/sprites/Others/P4.png"
image Officer indifferent = "images/sprites/Others/P5.png"
image Officer chat = "images/sprites/Others/P6.png"
image Officer = "images/sprites/Others/P7.png"
image Officer sigh1 = "images/sprites/Others/P8.png"
image Officer sigh2 = "images/sprites/Others/P9.png"
image Lars 1 = "images/sprites/Others/L1.png"
image Lars 1 right = "images/sprites/Others/L1_R.png"
image Lars 2 = "images/sprites/Others/L2.png"
image Lars 2 right = "images/sprites/Others/L2_R.png"
image Lars 3 = "images/sprites/Others/L3.png"
image Lars 4 = "images/sprites/Others/L4.png"
image Lars 4 right = "images/sprites/Others/L4_R.png"
image Lars 5 = "images/sprites/Others/L5.png"
image Lars 5 right = "images/sprites/Others/L5_R.png"
image Lars 6 = "images/sprites/Others/L6.png"
image Lars 6 right = "images/sprites/Others/L6_R.png"

image Carson 1 = "images/sprites/Others/C1.png"
image Carson 2 = "images/sprites/Others/C2.png"
image Carson 3 = "images/sprites/Others/C3.png"
image Carson 4 = "images/sprites/Others/C4.png"
image Carson 5 = "images/sprites/Others/C5.png"


# The game starts here.

label splashscreen:
    scene black
    pause 1.0
    show advertising with fade
    pause 2.0
    scene black with fade
    scene advertising2 with dissolve
    pause 2.0
    scene black with fade
    pause 3.0
    hide advertising with dissolve
    show main with fade
    return


label start:
    stop music fadeout 2.0
    with Dissolve(2.0)
    scene black with fade
    pause 3.0
    play sound "audio/sfx/typing.wav"
    scene start1 with fade
    pause 3.0
    scene black with fade
    pause 3.0
    window hide
    play sound "audio/sfx/phone ring.wav"
    pause 9.0
    stop sound
    UnJohnny "Hello?"
    Johnny "Jonathan Paddle speaking."
    Johnny "P.I."
    window hide
    play music "audio/music/Bananarama - Cruel Summer.wav"
    scene cabin_front with fade
    pause 1.5
    "All started with a stolen car."
    "A gray Seat Málaga with one of the rear lights broken,{w} patent number [[REDACTED]."
    scene office with fade
    "Nothing special at first instance.{w} People get their vehicles stolen every day and those corrupt pigs of the department always find excuses to keep them for themselves."
    "This,{w} in case they find them in the first place, off course..."
    "That’s why, instead of going straight to the police as would be logical anywhere else,{w} they better call someone special…{w} Someone…"
    show Johnny P
    play sound "audio/sfx/Whip.wav"
    pause 1.0
    "...like me."
    play sound "audio/sfx/Whip.wav"
    hide Johnny P
    show Johnny P2
    "If there's a problem,{w} better call me~"
    play sound "audio/sfx/Whip.wav"
    hide Johnny P2
    show Johnny smile2
    "A strong...{w} intelligent...{w} seductive man."
    "A more than capable detective who’s also..."
    hide Johnny smile2
    show Johnny sigh
    stop music
    play sound "audio/sfx/scratch.wav"
    items "Broke as fuck..."
    stop sound
    scene black with fade
    "B-But let's not entertain ourselves with trivialities."
    Johnny "All right…{w} Time to go to work."
    Johnny "But…{w} Let’s not forget this."
    hide window
    play sound "audio/sfx/item_got.ogg"
    show shovel
    pause 1.0
    "{i}Jonathan has picked up Human Resources! (his shovel){/i}"
    Johnny "Just in case things get dirty…"
    hide shovel
    pause 0.5
    play sound "audio/sfx/car turning on.wav"
    pause 0.5
    play music "audio/music/Bananarama - Cruel Summer sing.wav" fadein 1.0
    "Gotta admit one thing,{w} things have gotten easier lately."
    "A lot of calls,{w} a lot of works,{w} a lot of things that keep me going."
    "Bad for the people,{w} but good for me."
    "And to be honest,{w} that’s all that I care about for now."
    "I’ve been living in that old, rotten cabin since… the incident with my parents."
    "I totally need to get out of that bloody mouse hole."
    "Still,{w} not everything is bad in there."
    scene drive with fade
    pause 1.0
    "Looking through the window, I met with the silhouette of the city drawing over the horizon."
    "The rumble of the cars and the echo of people yelling at each other’s started to filled my ears."
    "The disgusting,{w} putrid smell of men and their filth is something that torments me every time I put a step on this circus."
    "I saw their faces..."
    "Those fake expressions pretending a mediocre happiness with smiles as empty as their heads."
    Johnny "Repulsive…"
    pause 1.0
    "But that’s ok."
    "It shouldn't even bother me."
    "After all... I'm not like them."
    "I'm smarter,{w} more attractive,{w} and way happier then all of them."
    Johnny "I'm better... Better than those."
    "Once I get enough money for a new apartment,{w} I’ll be as far away as I can be from this hell-hole."
    "And so I'll be able to live the life I deserve."
    scene black with fade
    pause 0.3
    Johnny "Sadly… {w} this case surely won't be the one to make my dream come true..."
    stop music fadeout 2.0
    pause 2.0
    scene motel1 with fade
    "I parked right in the crime zone."
    play music "audio/music/Delay.wav" fadein 2.0
    play sound "audio/sfx/car door.wav"
    show Johnny R at left
    with moveinleft
    "The vision of a seedy motel received me with its dungy pestilence as I stood out of the car."
    hide Johnny
    show Johnny serious1 R at left
    "With a simple look, I could tell what kind of activities my client was carrying out."
    "Not like… it’s out of place for one of my regulars but anyway."
    "The first thing to do as part of the protocol is examine the area."
    hide Johnny
    show Johnny serious2 R at left
    "Due to the time difference between my arrival and the crime, it was very unlikely to find any meaningful clues."
    "So I thought the best would be to just look for witnesses."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "A location like this usually has a good number of amblers.{w} It wouldn’t be hard to find someone who could have seen something."
    "With this in mind, I started moving."
    play sound "audio/sfx/Steps stone.wav"
    hide Johnny smile1 R
    show Johnny R at left
    with moveinleft
    hide Johnny R
    show Johnny R at center
    with moveinleft
    hide Johnny R
    show Johnny R at right
    with moveinleft
    hide Johnny R
    show Johnny R at offscreenright
    with moveinleft
    scene eat food with fade
    "At my left was a restaurant followed by an ugly clothes shopping."
    "Taking into account that the theft happened between the night and early morning, it would be strange if someone would have seen something in there."
    "In the best scenario, the owners would be weirdos who have their alarms set for everything that happens in the neighborhood. "
    "(It happens way more often than you would expect)"
    "That’s left as an option for now."
    scene park with fade
    "At my right was the entrance to a public park."
    "A very frequented place."
    "Horny teenagers,{w} lurking perverts,{w} and lots of vagabonds {w}(the worst of them)."
    "There’s always someone watching on these kinds of sites, so it was a clear choice."
    "However, what I found in there wasn’t exactly what I was thinking...{w} nor expecting at all."
    scene crime1 with fade
    "Behind a very remarkable police tape,{w} hide by the bushes and surrounded by men in blue uniforms,{w} was the cold and fetid corpse of a poor bastard."
    "A cloud of flies flew around the white blanket covering it.{w} They tried kept looking around in a vague attempt to penetrate the thin fabric."
    "It wasn't by any means something recent."
    scene black with fade
    stop music fadeout 1.0
    pause 1.0
    play music "audio/music/Magnum Force.wav" fadein 1.0
    "And off course,{w} this called my attention."
    scene crime2 with fade
    play sound "audio/sfx/Steps grass.wav"
    show Johnny at right
    with moveinright
    "Naturally, I edged the marking border to have a clearer view of the inside."
    "However, my intentions would be immediately stopped by the annoyed gaze of one of the man in charge."
    Officer "Hey!!!"
    show Officer serious at left
    with moveinleft
    hide Johnny
    show Johnny sigh at right
    Johnny "Always a problem…"
    Officer "Far away from here, opportunist."
    Officer "This is a closed area,{w} and even more for people of your kind."
    hide Johnny
    show Johnny serious1 at right
    Johnny "Of... my {b}kind{/b}?"
    "I know it wasn't, but still took that as a compliment."
    hide Johnny
    show Johnny chat1 at right
    Johnny "Let me explain this to you, officer.{w} I'm not here to cause any trouble."
    hide Officer
    show Officer at left
    "I gave him one of my presentation cards."
    hide Johnny
    show Johnny P at right
    play sound "audio/sfx/whip.wav"
    Johnny "Jonathan Paddle, PI."
    hide Johnny
    show Johnny P2 at right
    play sound "audio/sfx/whip.wav"
    Johnny "If there’s a problem,{w} better call me~"
    hide Johnny
    show Johnny confused at right
    hide Officer
    show Officer sigh1 at left
    Officer "Yeah, I know you well, freak…"
    hide Officer
    show Officer indifferent at left
    Officer"You're the one who covered the agency's signs with those stupid advertising pamphlets."
    hide Johnny
    show Johnny smile1 at right
    "Ups... thought nobody saw me..."
    hide Johnny
    show Johnny chat1 at right
    Johnny "Ehem… yeah.{w} No hard vibes anyway, right?"
    hide Johnny
    show Johnny at right
    hide Officer
    show Officer serious at left
    Officer "Whatever…{w} Just get out of here."
    Officer "We're already too busy to deal with any more troubles."
    "My alerts went off when I heard that statement."
    hide Johnny
    show Johnny serious1 at right
    Johnny "Busy?{w} Doing what?{w} It's not like people never get killed in this city."
    Johnny "Why is this particular guy so special?"
    hide Johnny
    show Johnny chat1 at right
    Johnny "Oh! Don’t tell me...{w} He was the owner of a donut’s restaurant."
    hide Johnny
    show Johnny smug2 at right
    hide Officer
    show Officer sigh1 at left
    "Judging by his breathing, I could assume that he didn't find my little joke to be amusing."
    Officer "Whatever we're doing here is none of your business."
    Officer "I have a better idea,{w} why don't you go investigate the {b}who cares about your opinion{/b} case?"
    hide Johnny
    show Johnny chat1 at right
    Johnny "There’s no need to get angry, officer.{w} I’m just doing my job the same way you’re doing yours."
    Johnny "The difference is,{w} I {b}do{/b} like mine."
    hide Johnny
    show Johnny smug1 at right
    hide Officer
    show Officer sigh2 at left
    "I heard a resigned sigh coming from him, to which I couldn't help but smile mischievously."
    "Sadly, as much as I would like to keep messing with him, that wasn't the reason to be there."
    hide Johnny
    show Johnny chat1 at right
    Johnny "All right, now if you don’t mind,{w} I’ll just take a quick look and—{nw}"
    hide Johnny
    show Johnny at right
    hide Officer
    show Officer sigh1 at left
    Officer "Are you deaf?{w} I said this is a closed area."
    Officer "You can’t be here,{w} which is the part you don't understand?"
    hide Johnny
    show Johnny serious1 at right
    Johnny "Yes, I heard that before,{w} but I’m standing in the allowed zone.{w} I don't see why I wouldn't be able to stay."
    Officer "Because I’m saying that you {b}CAN’T{/b} be here."
    hide Officer
    show Officer at left
    Officer "We have strict orders to not letting anyone come closer.{w} Especially a fucking Larry Zito wanna be like you."
    Officer "Now piss off, or I'll put you in a cage with the weirdos we caught last night."

    ################################### Police choice

    menu:
        "He was pretty serious about this so... I decided to answer with—"

        "Disdain":
            jump Disdain1
        "Demureness":
            jump Demureness1
        "Indifference":
            jump Indifference1


    label Disdain1:
        $ PoliDisdain = True
        stop music fadeout 2.0
        hide Johnny
        show Johnny angry1 at right
        Johnny "So…{w} the bigger men have spoken, didn’t?{w} Yeah… I know how it is."
        hide Johnny
        show Johnny serious1 at right
        play music "audio/music/Ennio Morricone - The Thing.wav" fadein 2.0
        "I looked at the excuse of a man up and down."
        scene black with fade
        "His body language said everything I needed to know."
        play sound "audio/sfx/paper.wav"
        show Pol3 with dissolve
        "An awkward posture..."
        play sound "audio/sfx/paper.wav"
        show Pol2 with dissolve
        "A neglected physique..."
        play sound "audio/sfx/paper.wav"
        show Pol1 with dissolve
        "Eyes filled with doubt,{w} unable to even keep his gaze locked on mine."
        "The pestilence of the mediocrity was strong on him,{w} enough to make my lungs sting and my blood boil."
        "But what’s the point on even bother for someone like this?"
        "Someone weak…{w} Someone who can’t even stand for himself."
        "He probably just wanted to go back home,{w} to get enough money to live just another fucking month and that’s it."
        "It’s even…{w} sad,{w} if you stop to think about it."
        "Being someone so pathetic,{w} with such lack of ambition."
        scene crime2 with fade
        show Officer sigh1 at left
        show Johnny serious1 at right
        Officer "Excuse me?{w} What did you just—{nw}"
        Johnny "It’s always the same with the people like you."
        Johnny "One is here,{w} trying to do their best,{w} making a living to follow a dream,{w} and you just want to to sit down on that nasty couch of yours and jerk off with the cheap pornography you bought at the Chinese"
        hide Officer
        show Officer scared at left
        Officer "W-What did you just said?"
        hide Johnny
        show Johnny angry1 at right
        Officer "What could you know about me, freak?"
        Officer "You are just a parasite that lives from the misery of the people."
        "A...{w} {b}parasite{/b},{w} huh? "
        Johnny "Maybe…{w} yeah, that could be."
        hide Officer
        show Officer sigh2 at left
        Johnny "I'm a lot of things, I would say..."
        hide Johnny
        show Johnny chat1 at right
        Johnny "Still, why don't you tell me?"
        Johnny "Who was this time?{w} The Fat Tony?{w} Vito Corleone?{w} Antonio Montana?{w} Some poor wanna be with full pockets?"
        scene black with fade
        "Of course, that response was the last straw."
        play sound "audio/sfx/Safery.wav"
        pause 0.5
        "I heard him releasing the safety of his gun moments before the barrel was pointed at me."
        "Again, the calls of the anger appeared on his face,{w} but they were just lies compared to the reflection on his eyes."
        "I saw nerves,{w} doubt,{w} the fear of a small man who hides behind of a gun bigger than himself."
        Officer "Get out..."
        Officer "Run the fuck out of here or I'll send you straight to the obituary."
        "Maybe I would have taken that threat seriously if his voice hadn't wavered."
        pause 0.3
        Johnny "Oh, I’ll go... you don’t need to worry about that."
        Johnny "Just…{w} I hope you look at me with the same eagerness next time we see."
        pause 1.0
        play sound "audio/sfx/Steps grass.wav"
        Johnny "Have a nice day, officer~"
        stop music fadeout 2.0
        scene black with fade
        jump main_route

    label Demureness1:
        $ PoliDemureness = True

        "Ignoring the warnings of the little man in blue, I took a look at the corpse over his shoulder."
        scene black with fade
        "There was very little I could get with a view like this."
        "However, something particular caught my sight."
        play sound "audio/sfx/paper.wav"
        show Pol4 with fade
        "His shoes looked like normal ones at naked eyes, but their soles were completely plane."
        "In principle,{w} this is not incriminating evidence."
        "I mean, a lot of people have their shoes with plane sole,{w} but they also come very handy on cases where the victimizer don’t want to leave any clues of the crime."
        "To keep it simple,{w} there's a small chance that this person did't come with good intentions."
        "Things like shoe size and sole shape are often a big help when it comes to locating people."
        "But of course they're not a reliable clue."
        "A small help, however..."
        hide Pol4
        stop music fadeout 2.0
        Officer "HEEEEEEY!!! {w} ASSHOLE!!!"
        "Off course, my thoughts were stopped by the cop yelling at my ear..."
        scene crime2
        show Officer sigh2 at left
        show Johnny serious1 at right
        Officer "You didn’t hear me? I said you better piss of before I send you to resolve the case of the fallen soup in the bathroom."
        Officer "I'm not repeating it..."
        Officer "GET OUT."
        "His tone was so annoying..."
        "Just the voice of a poor thing who tried desperately to sound intimidating."
        play music "audio/music/Ennio Morricone - The Thing.wav" fadein 2.0
        pause 0.5
        hide Johnny
        show Johnny angry1 at right
        pause 0.5
        hide Officer
        show Officer scared at left
        "The moment I turned to look over him, he shivered like a scared little sheep."
        "He thought I wouldn’t notice…"
        hide Officer
        show Officer serious at left
        "...but I did.{w} Oh hell I did..."
        "There was no need to lower myself to his level."
        hide Johnny smug1
        show Johnny chat1 at right
        Johnny "I’ll have that on mind.{w} We’ll be in contact soon enough, officer."
        hide Johnny chat1
        show Johnny smug1 R at right
        pause 0.2
        hide Johnny
        show Johnny smug1 R at offscreenright
        with moveinleft
        pause 0.5
        hide Officer scared
        show Officer at left
        Officer "Yeah, that’s it!"
        hide Officer
        show Officer indifferent at left
        Officer "You better move on... {w} Fucking... weird..."
        stop music fadeout 2.0
        scene black with fade

        jump main_route

    label Indifference1:
        $ PoliIndifference = True
        stop music fadeout 2.0
        pause 2.0
        play music "audio/music/Ennio Morricone - The Thing.wav" fadein 2.0
        hide Johnny
        show Johnny angry1 at right
        "I stared at his eyes."
        "A man like this...{w} with the rights to impose himself over others."
        "Someone weak and influenceable,{w} with a fragile body and a brain atrophied like a walnut."
        scene black with fade
        "It was disgusting,{w} repulsive to even think about it."
        "But why even bother?{w} What power do mud people like him really have?"
        hide Officer
        show Officer nervous1 with dissolve
        "Even at that moment, just by the touching our gazes,{w} I could feel his heart racing."
        "He felt nervous,{w} self-conscious,{w} {b}unsafe{/b}."
        "But why?{w} Why someone on his position would let himself to be intimidated by others?"
        "The answer is simple...{w} Because he's small.{w} He just pretends to be brave,{w} tries to look strong just to keep his appearance."
        "But deep down... {w} Well, statements are unnecessary"
        hide Officer nervous1
        show Officer nervous2
        "Questions started to sprout on his mind."
        "“What is he doing?”{w} “Why does he keep staring at me?”"
        "“What should I do?”{w} “Is he gonna hurt me?”{w} “I don’t wanna get hurt, should I yell at him?”{w} “Maybe threaten him?”{w} “Hurt him?”{w} “Perhaps…”"
        "“Perhaps {b}shoot{/b} him?”"
        hide Officer nervous1 with fade
        "My thoughts were confirmed as I see his hand moving slowly towards the gun on his belt,{w} and a little grin started to creep on my face as a result of that."
        "Now his pupils dilated,{w} small beads of sweat began to emanate from his skin, and his pulse faltered as his fingers wound around the weapon."
        "But before he could even pull it out…"
        stop music
        scene crime2
        show Officer nervous2 at left
        show Johnny chat1 at right
        Johnny "All right."
        Johnny "Until we see each other’s again,{w} officer~"
        hide Johnny chat1
        show Johnny serious3 at right
        "I spoke."
        scene black with fade
        "And so I did."
        "I moved on, leaving the little man alone with his thoughts."
        play sound "audio/sfx/Steps grass.wav"
        "And as I walked away, I heard an almost inaudible sigh of tranquility.{w} The sound of his soul reentering his body."
        "And then,{w} the distant voice of that poor man prayed..."
        Officer "For fuck sake…{w} What were those eyes?"

        jump main_route


    ############################# End Police choice

label main_route:
    pause 0.5
    play music "audio/music/Delay.wav"
    pause 0.5
    scene motel2 with fade
    show Johnny at right
    with moveinright
    hide Johnny
    show Johnny at center
    with moveinright
    "That was fishy..."
    "The cartels could to be moving around this, but it’s too clean to be one of their scenes."
    "Usually when they leave a body in sight it is to send a message, but they used to be... {b}less complete{/b},{w} at least in most cases."
    "It’s likely to be an amateur work."
    hide Johnny
    show Johnny serious1 at center
    "But then again, my question would be if this is somehow related with the stolen car."
    "Could have been a reckoning between gangs."
    "A guy jumps out of the bushes,{w} attacks,{w} the other dude falls death and the attacker escapes."
    hide Johnny
    show Johnny sigh at center
    "Still, that has very little sense…{w} Why stealing someone’s car being an easier way to get caught?"
    "Why not using your own car instead or searching for a escape route?"
    "There’s also the possibility for them to be separate events,{w} which would make this an incredible and unfortunate coincidence."
    "The place...{w} the circumstance...{w} the time between events...{w} everything is so strange."
    scene black with fade
    Johnny "Strange..."
    stop music fadeout 2.0
    "And as this thought crossed my mind, something appeared on my field of view."
    scene malaga
    play sound "audio/sfx/static.wav" loop volume 0.6
    pause 1.5
    "At a speed above the allowed, a gray Seat Málaga with one of the rear lights broken crossed the street."
    stop sound fadeout 2.0
    scene black with fade
    "For a moment, I thought I imagined it."
    "Who would be so unaware as to pass right in front of their own crime scene?"
    scene motel2 with fade
    show Johnny sigh at center
    "It took me a few moments to process what I’ve just seen,{w} and when I came back to reality there was only one thing I could think about."
    hide Johnny
    show Johnny smug1 at center
    Johnny "Let’s drive!"
    play music "audio/music/Cruel Summer ost.wav"
    scene black with fade
    play sound "audio/sfx/car turning on.wav"
    pause 0.5
    scene driving with fade
    "I followed the silhouette of the car, keeping a safe distance to avoid being noticed."
    "The driver clearly wasn’t an expert.{w} Reckless maneuvers,{w} overly-accelerated speed,{w} little control over the vehicle,{w} seemed to be the profile of someone nervous or upset."
    "I like that kind of people.{w} They usually oppose some resistance."
    "It make things more interesting (at least for me)."
    scene black with fade
    "However, those who came out of that car were quite far from what I had in mind."
    pause 3.0
    scene passion with fade
    "The sun was starting to set when they stopped in front of a nightclub."
    "In my case, I parked on the opposite side of the road and dedicated myself to observe."
    "Two young adults emerged from the vehicle."
    play sound "audio/sfx/paper.wav"
    show pol6 with fade
    "A guy with green eyes,{w} slender,{w} disheveled,{w} looking like he haven't slept in days."
    play sound "audio/sfx/paper.wav"
    show pol5 with fade
    "And a girl with pink eyes,{w} of relative short stature,{w} confident,{w} with a pretty but also messy hairstyle."
    "A particular duet, but nothing flashy."
    "They seemed to have a heated argument."
    "They yell at each other before their expressions changed from the anger to the calm, {w}and as if nothing had happened,{w} they walked straight into the building with two prominent smiles on their faces."
    Johnny "Possible bipolar disorder…"
    play sound "audio/sfx/paper.wav"
    hide pol6 with dissolve
    pause 0.5
    play sound "audio/sfx/paper.wav"
    hide pol5 with dissolve
    pause 1.0
    "With my first two suspects on the board, I decided to investigate."
    "First of all,{w} checking the car."
    scene black with fade
    play sound "audio/sfx/car door.wav"
    pause 1.5
    "And for my not so big surprise,{w} the doors weren’t locked."
    scene car with fade
    "The keys weren’t there neither, sadly."
    "However, I do found a couple of interesting items there..."
    pause 1.0
    play sound "audio/sfx/item_got.ogg"
    show butcher
    pause 1.0
    "{i}Jonathan has picked up a butcher blade.{/i}"
    "Quite good to chop some meat.{w} And I was just needing one of these."
    hide butcher
    play sound "audio/sfx/item_got.ogg"
    show sodas
    pause 1.0
    "{i}Jonathan has picked up a couple of empty soda cans.{/i}"
    "Caramelized Apple and Cinnamon…{w} I heard people use this stuff to remove rust from engines."
    "You must have a really strong stomach to drink this thing…"
    hide sodas
    play sound "audio/sfx/item_got.ogg"
    show notepad
    pause 1.0
    "{i}Jonathan has picked up a folder full of documents...{/i}"
    "{i}...defunction documents.{/i}"
    "Now this…{w} this was something else."
    play sound "audio/sfx/paper.wav"
    hide notepad with dissolve
    pause 1.0
    Johnny "Andrew and Ashley Graves, huh?"
    Johnny "Siblings…"
    Johnny "Day of decease: [[REDACTED]"
    Johnny "Cause: Fire/Smoke suffocation."
    "This was a couple of weeks ago.{w} If I'm not mistaken, it happened the same day that quarantined apartment was burnt to ashes."
    "Should I assume some kind of connection?"
    "It's already quite the event by its own, but with this?"
    "We can say that..."
    stop music
    extend" {i}it fanned the flames of my interest.{/i}"
    pause 2.0
    "..."
    "Good thing nobody is gonna read this notes."
    pause 2.0
    play music "audio/music/Cruel Summer ost.wav"
    "Anyway..."
    "Most likely, these documents are fake.{w} These little siblings tried to fake their deaths."
    "Why to do such a thing in that way?{w} Why taking an entire apartment with them?{w} And most importantly, why {b}that{/b} apartment in particular?"
    "I had more questions than answers…{w} and luckily, my two suspects were just a couple of meters of distance."
    "The thing is..."
    scene black with fade
    "This wasn’t just a stolen car case anymore.{w} Which also means that, the danger involved was bigger than I could imagine."
    "Considering all the factors on board, I had no reasons to keep going.{w} Could have just walked away, presented the information to my client and let him deal with the rest."
    "Work finished."
    stop music fadeout 1.5
    "But then again…{w} Where would be the fun on that?"
    play sound "audio/sfx/static.wav" fadein 1.5 loop volume 0.4
    "I’m gonna be honest,{w} I do wanted to talk with these two {b}grave-walkers{/b}, {w}and it would've been a total waste not to take advantage of the situation."
    "I mean...{w} they were over there.{w} Why not doing it?"
    "And besides all that,{w} I would get a nice recommendation if I return the car instead of just bringing some dirty information."
    Johnny "You always have to pamper your client, no matter how idiotic they are~"
    stop sound fadeout 1.5
    pause 1.0
    play sound "audio/sfx/car door.wav"
    "So, I got out of the car, closed the door and fixed my clothes before walking into the club."
    Johnny "Show time~"
    play music "audio/music/ALEX - AKUMA.wav"
    scene club_in with fade
    "The night was falling, so the place was still a little empty."
    show pol8 with dissolve
    show pol7 with dissolve
    "The girl was sitting on a table at the bottom of the place while the emo guy was leaning against the railing of the balcony in the second floor."
    "Usually, women doesn’t give me much troubles."
    "It’s just a matter of pulling out the {i}Paddle’s style{/i}, and they tell me what I want to hear…{w} or they attack me.{w} One of those options."
    scene club1 with fade
    show Ashley at right
    pause 0.5
    play sound "audio/sfx/Steps stone.wav"
    "I walked into her with airs of calm."
    show Johnny R at left with moveinleft
    "Those eyes felt over me without much interest, {nw}"
    hide Ashley
    show Ashley smug1 at right
    extend "but at the moment I sat on the chair, {nw}"
    hide Johnny
    show Johnny smile2 R at left
    extend"a mocking smirk crept on that face."
    hide Ashley
    show Ashley smug2 at right
    Ashley "You’re totally not a cop, right?"
    hide Ashley
    show Ashley smug1 at right
    hide Johnny
    show Johnny chat1 R at left
    Johnny "Actually, I’m not.{w} I applied for the position, but they expelled me from the academy before graduating."
    hide Johnny
    show Johnny smile1 R at left
    Johnny "Sad, I really wanted to use a taser..."
    hide Ashley
    show Ashley think at right
    "She inspected me from top to bottom with very little modesty just before her eyes lit up on realization."
    hide Ashley
    show Ashley smug2 at right
    Ashley "Oh!{w} You're that guy from the ads."
    Ashley "The one who looks like…"
    hide Ashley
    show Ashley smug1 at right
    hide Johnny
    show Johnny chat1 R at left
    Johnny "A lady-killer?"
    hide Ashley
    show Ashley at right
    hide Johnny
    show Johnny confused R at left
    play sound "audio/sfx/scratch.wav"
    Ashley "…a clown."
    hide Johnny
    show Johnny sigh R at left
    "Bitch..."
    hide Johnny
    show Johnny chat1 R at left
    Johnny "Y-Yeah... that one..."
    hide Johnny
    show Johnny P R at left
    play sound "audio/sfx/whip.wav"
    Johnny "Johnny Paddle, P.I."
    hide Johnny P R
    show Johnny P2 R at left
    play sound "audio/sfx/whip.wav"
    hide Ashley
    show Ashley smug1 at right
    Johnny "If there’s a problem…{w} Better call me~"
    hide Ashley
    show Ashley giggle1 at right
    "I received a playful laugh from her part as an answer.{w} The tone, however, wasn’t natural at all."
    hide Ashley
    hide Johnny
    show Ashley smug1 at right
    show Johnny serious1 R at left
    "Her face kept on a expression of constant smugness,{w} her eyes remained free of any nerves, regardless of disown my intentions."
    "It was easy to tell that she was playing.{w} I wasn't consider a threat, not at all.{w} Or at least... she didn't show it."
    hide Ashley
    show Ashley smug3 at right
    "That's a good thing, but I still couldn’t be completely sure of that..."
    "No matter how much I tried to see through her, I wasn’t able to distinguish any trace of sincere emotions."
    "It felt…{w} particularly strange."
    "As if her whole figure wasn't but a lie trying to fool me at every moment."
    hide Ashley
    show Ashley smug2 at right
    Ashley "So, a detective talking to a pretty lady on a club.{w} It sounds like something out of those cheap 60's movies when you say it loud."
    hide Ashley
    show Ashley smug1 at right
    hide Johnny
    show Johnny chat1 R at left
    Johnny "A little, yeah, but I'm still incognito,{w} so don’t tell anybody you saw a handsome detective stealing the tips bottle."
    hide Ashley
    show Ashley smug2 at right
    hide Johnny
    show Johnny serious2 R at left
    Ashley "First of all,{w} those tips are mine, mister."
    hide Ashley
    show Ashley at right
    Ashley "And second, you’re not fooling anybody with that old costume of yours."
    Ashley "Why don’t you better tell me why your interest on this sweet-innocent girl in front of you?"
    hide Johnny
    show Johnny serious1 R at left
    "I haven’t seen a sweet and innocent person in years."
    "And frankly, with the little evidence I had till that moment, I could tell she was a lot of things but sweet nor innocent."
    "Hot and dangerous maybe,{w} but not sweet or innocent."
    hide Johnny
    show Johnny R at left
    Johnny "I was hired to find the whereabouts of a car stolen a few days ago."
    Johnny "A gray Seat Málaga with one of the rear lights broken.{w} Does it sounds familiar to you?"
    hide Ashley
    show Ashley pout1 at right
    "She took the information and thought about it for a considerably long moment."
    hide Ashley
    show Ashley smug1 at right
    "The mischievous smile on her lips confirmed that she indeed knew exactly what I was talking about."
    "Off course, she wasn't about to tell me that easy."
    hide Ashley
    show Ashley smug3 at right
    hide Johnny
    show Johnny confused R at left
    Ashley "Nope. Haven’t seen a car like that in my life."
    "The confidence with which she said those words managed to surprise me...{w} a little."
    "A good liar…{w} one of the kind I would even say."
    hide Johnny
    show Johnny smug1 R at left
    "That made me a little more excited."
    "However my next few words would be fundamental, so I was forced to swallow those feelings and concentrate..."

    #################################### Ashley 1 choice

    menu:
        "I continued with..."

        "Sharpness":
            $ AshleyAff -=1
            jump Sharpness1

        "Subtlety":
            $ AshleyAff +=1
            jump Subtlety1

        "Straightness":
            $ DualAff +=1
            jump Straightness1

    label Sharpness1:
        hide Johnny
        show Johnny smug2 R at left
        hide Ashley
        show Ashley smug1 at right
        "Even trying my best, I couldn’t help to laugh at her smoothness."
        hide Johnny
        show Johnny chat1 R at left
        Johnny "You’re good.{w} I give you some points."
        hide Johnny
        show Johnny smug2 R at left
        hide Ashley
        show Ashley smug2 at right
        Ashley "Thank you~"
        Ashley "My brother always say I have a gift with words."
        hide Ashley
        show Ashley mad at right
        Ashley "Just…{w} not with those specific words."
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny R at left
        Johnny "I can imagine, yeah…"
        hide Johnny
        show Johnny serious1 R at left
        Johnny "By the way, I'm feeling an extra pair of eyes on me right now."
        Johnny "I suppose they’re from him."
        hide Ashley
        show Ashley giggle1 at right
        Ashley "hahahaha, yeah..."
        hide Ashley
        show Ashley smug3 at right
        Ashley "He’s very protective with his little sister,{w} ever since we were children."
        hide Ashley
        show Ashley pout1 at right
        Ashley "Truly a sweetheart."
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Indeed.{w} What kind of brother wouldn't ensure the safety of his sister?"
        Johnny "Much more, if we consider how attractive this one turns to be..."
        hide Johnny
        show Johnny serious3 R at left
        hide Ashley
        show Ashley giggle1 at right
        "I received a mocking laugh in return, and her brow went down with a pitiful meaning."
        Ashley "Oh, please."
        hide Ashley
        show Ashley smug3 R at right
        Ashley "Don't pull out the womanizing detective's card. You’re trying it so hard."
        hide Johnny
        show Johnny chat1 R at left
        Johnny "I’m not pulling out any card, miss…"
        hide Ashley
        show Ashley smug2 at right
        hide Johnny
        show Johnny smile2 R at left
        Ashley "Ashley.{w} Ashley Graves."
        Ashley "But I suppose you already knew it, right?"
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny serious3 R at left
        Johnny "You got me,{w} but I wanted to hear it from you."
        hide Ashley
        show Ashley at right
        Johnny "After all...{w} a name like that should be said by lips just as beautiful~"
        hide Ashley
        show Ashley mad at right
        "This time, the smile on her face was vanished."
        hide Johnny
        show Johnny serious1 R at left
        "Maybe… I overdid with the praises…{w} She clearly wasn't comfortable with it anymore."
        hide Ashley
        show Ashley mad at right
        "So, at the risk of ruining the conversation, I assumed I'd better get straight to the point."
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Anyway…{w} Now that we introduced ourselves, would you mind telling me a little about the car outside?"
        Johnny "That’s why I’m here after all."
        hide Johnny
        show Johnny smile2 R at left
        hide Ashley
        show Ashley think at right
        Ashley "And why would I do that?"
        Johnny "Because it’s better for you two, as simple as that."
        hide Johnny
        show Johnny chat1 R at left
        Johnny "We can say I’m just an employ."
        Johnny "I was hired to find it, and If I don’t,{w} then there’s a big chance that my client will send someone who will."
        hide Johnny
        show Johnny smug2 R at left
        Johnny "Probably someone not as reasonable as me."
        hide Johnny
        show Johnny serious3 R at left
        hide Ashley
        show Ashley at right
        Ashley "Was that…{w} a threat?{w} Because that sounded like a threat..."
        hide Johnny
        show Johnny smug2 R at left
        Johnny "I would prefer the term {b}bargain{/b}.{w} In essence is the same, but it sounds way more elegant."
        pause 1.0
        hide Johnny
        show Johnny serious2 R at left
        Johnny"Look, I’m telling you how things are.{w} I could just walk away and you’ll never see me again, OR…{w} you can give me the keys, I return the vehicle, and nothing ever happened here."
        hide Johnny
        show Johnny chat1 R at left
        Johnny"Sounds good? I think it sounds pretty good."
        "It did sound good…"
        hide Johnny
        show Johnny smile1 R at left
        hide Ashley
        show Ashley mad2 at right
        extend " but she didn't like it.{w} Not at all I would say."
        "I could feel the air change around us,{w} the tension raising up as she kept hiding behind that emotion wall."
        "Still, hard to read, but it was evident that she was pissed now."
        hide Johnny
        show Johnny serious1 R at left
        hide Ashley
        show Ashley ewww at right
        Ashley "And just when I was starting to like you, detective…"
        Ashley "Fine,{w} you want that piece of scrap? Is yours. {w} It’s out of gas anyway."
        hide Ashley
        show Ashley mad3 at right
        Ashley "But unfortunately for you, I don’t have the keys."
        Ashley "Go talk with Andy up there…"
        scene black with fade
        "I woke from the chair and looked at her one last time."
        Johnny "Thank you for…{nw}"
        Ashley "Piss off..."
        "All right…{w} That could have gone better, I have to admit."
        jump main_route2

    label Subtlety1:
        hide Ashley
        show Ashley smug1 at right
        "I nodded and turned towards the guy at the second floor."
        hide Johnny
        show Johnny serious1 R at left
        Johnny "So, a girl and her brother went to a bar in a stolen car and she doesn’t know anything about it…"
        Johnny "It even seems like the number of some half-time comedian."
        hide Ashley
        show Ashley smug2 at right
        Ashley "It easily could be.{w} And the punchline would be the underpaid detective trying to get a confession out of the girl."
        hide Johnny
        show Johnny smug1 R at left
        Ashley "I would say that it’s a fun joke but…"
        hide Ashley
        show Ashley at right
        extend " I’m not into comedies."
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Yeah, me neither to be honest.{w} Too much chatter to come up with something dumb."
        Johnny "I’m more of a drama enjoyer, you see?{w} We create a tense environment, make the people go into suspense, and then slowly but surely reveal the plot."
        hide Johnny
        show Johnny smug1 R at left
        hide Ashley
        show Ashley smug1 at right
        Ashley "Is this by any meaning the suspense part?{w} Should I be worried?"
        hide Johnny
        show Johnny serious3 R at left
        Johnny "I don’t know. {w} Maybe you should be..."
        extend " Maybe we both should be…"
        hide Johnny
        show Johnny chat1 R at left
        extend " Or maybe just the guy up there, who knows?"
        hide Johnny
        show Johnny smile2 R at left
        hide Ashley
        show Ashley giggle1 at right
        Ashley "Hah!"
        hide Ashley
        show Ashley mocking1 at right
        Ashley "Andrew is worried on main.{w} I swear, that guy hasn’t known tranquility in his whole life."
        hide Ashley
        show Ashley smug3 at right
        Ashley "My bad, actually."
        hide Ashley
        show Ashley giggle1 at right
        hide Johnny
        show Johnny smug2 R at left
        "I couldn’t avoid to giggle a little after such declaration."
        "There was something odd and sinister on those words,{w} a strange ambiguity located between sincerity and jokes."
        "I couldn't really tell if she was being honest,{w} but rather than scare or disrupt me..."
        hide Ashley
        show Ashley smug1 at right
        extend " I found myself actually wanting to know more about that."
        "It was… amusing,{w} actually amusing."
        hide Johnny
        show Johnny serious3 R at left
        Johnny "I got the feeling that you weren't joking.{w} Am I right?"
        hide Ashley
        show Ashley smug2 at right
        Ashley "Will it matter for you?"
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Touché, touché..."
        Johnny "But still...{w} Throw me a stick."
        hide Johnny
        show Johnny smug1 R at left
        "She didn't said anything.{w} But her silence...{w} that smile, those guiltless eyes, said enough."
        hide Johnny
        show Johnny smug2 R at left
        Johnny "I see..."
        hide Ashley
        show Ashley smug2 at right
        Ashley "You have good eyes, detective. {w} And I don't like people who can see through me, you know?"
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Well that's bad.{w} Because It's been a while since the last time I found myself really invested in a conversation."
        hide Johnny
        show Johnny smile2 R at left
        Johnny "Congratulations!{w} You caught my interest."
        hide Ashley
        show Ashley smug2 at right
        Ashley "Don’t get to conclusions so quick, Mr. Detective-man."
        hide Ashley
        show Ashley smug3 at right
        Ashley "You may be confusing the signs."
        hide Johnny
        show Johnny smug2 R at left
        Johnny "Yeah… That’s probable,{w} but maybe it’s a good thing.{w} I don’t get surprised too often."
        hide Ashley
        show Ashley at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Tell you what, if you give me the keys of the car I’ll tell my client that I found them somewhere in the middle of nowhere."
        hide Ashley
        show Ashley giggle1 at right
        hide Johnny
        show Johnny smile2 R at left
        "She chuckled at my proposal,{w} but not for the reasons I would had like."
        hide Ashley
        show Ashley smug2 at right
        Ashley "Yeah... There’s a little problem with that."
        hide Johnny
        show Johnny smile1 R at left
        extend " I don’t have the keys."
        hide Ashley
        show Ashley mad at right
        Ashley "Andy doesn't trust me enough for that…{w} but whatever."
        hide Ashley
        show Ashley worried2 at right
        hide Johnny
        show Johnny sigh R at left
        Ashley "Oh, and it’s out of gas by the way."
        hide Ashley
        show Ashley smug1 at right
        "Well, that was disappointing."
        hide Johnny
        show Johnny confused R at left
        Johnny "I guess I’ll have to talk with your brother then.{w} Any recommendation?"
        hide Ashley
        show Ashley smug2 at right
        Ashley "Don’t mention that you’re a detective."
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny smile2 R at left
        Johnny "Tell him that I'm gonna put him in a cell with a six-foot black guy named Ramón.{w} Got it!"
        scene black with fade
        "Welp,{w} gotta admit,{w} that ended up better than expected."
        jump main_route2

    label Straightness1:
        hide Johnny
        show Johnny serious1 R at left
        "Without waiting for a call, I took the documents out of my pocket."
        Johnny "So…{w} Mr. and Miss Graves."
        hide Ashley
        show Ashley smug1 at right
        Johnny "Deceased on [[REDACTED].{w} And now founded in a crappy nightclub with a stolen vehicle."
        Johnny "That should be quite the story, am I right?"
        hide Ashley
        show Ashley mocking1 at right
        hide Johnny
        show Johnny confused R at left
        "Ashley giggled as she saw the documents."
        "She didn't seem surprised at all by the fact that I had her death's papers."
        hide Ashley
        show Ashley smug2 at right
        Ashley "Oh… you found that.{w} I wasn’t expecting you to break into the car."
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "My methods may be {b}unorthodox{/b}, but my results are unquestionable."
        hide Johnny
        show Johnny smile1 R at left
        Johnny "And barely legal..."
        hide Johnny
        show Johnny serious1 R at left
        hide Ashley
        show Ashley smug2 at right
        Ashley "Good, I like that.{w} It means you know how to get what you want."
        hide Ashley
        show Ashley mocking1 at right
        Ashley "And yes, as you said it's quite the story."
        hide Ashley
        show Ashley smug3 at right
        extend " But how interested are you on hearing this girl's familiar anecdotes?"
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Not much, to be honest.{w} I have my own couple of stories about broken families."
        hide Johnny
        show Johnny smile1 R at left
        Johnny "Still, I want to guess..."
        pause 1.5
        hide Johnny
        show Johnny serious3 R at left
        Johnny "Parents?"
        hide Ashley
        show Ashley at right
        Ashley "Parents."
        "Yeah, it wasn't that hard."
        hide Ashley
        show Ashley worried2 at right
        Ashley "Will you believe me if I say that it was Andy's idea?{w} He may not look like, but he can be quite impulsive sometimes..."
        hide Ashley
        show Ashley at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Well, now that you mention it,{w} he definitely looks like the kind of guy who would drive the night out with phonk music in the background."
        pause 0.5
        hide Johnny
        show Johnny smile2 R at left
        hide Ashley
        show Ashley think at right
        Ashley "We had... an {b}altercation{/b} with mom and dad..."
        hide Ashley
        show Ashley smug2 at right
        extend " But that's in the past."
        hide Ashley
        show Ashley smug1 at right
        Ashley "Now everything we want is to began our new life {b}far away{/b} from them."
        hide Johnny
        show Johnny smug1 R at left
        Johnny "You know what, miss Graves?{w} Every word you say makes me like you even more~"
        hide Ashley
        show Ashley pout1 at right
        Ashley "Awwww, you flatter me, detective.{w} Too bad you're here to put us some incommode handcuffs."
        hide Ashley
        show Ashley think at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "And who said such a thing?"
        extend " I'm not here to put handcuffs on anyone, dear."
        hide Johnny
        show Johnny smug1 R at left
        Johnny "Unless you want me to, of course~"
        hide Ashley
        show Ashley mad at right
        Ashley "So… You aren't here for us?{w} Don't tell me you just want the stupid car..."
        hide Johnny
        show Johnny R at left
        Johnny "Well yes, that assumption is correct, ma'am."
        hide Johnny
        show Johnny smug2 R at left
        extend " Now, if you want to confess any kind of crime I could…"
        hide Ashley
        show Ashley worried2 at right
        Ashley "No, no, no… I think I’m good like this."
        hide Ashley
        show Ashley at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Great!{w} So, do we have a deal?{w} The car in exchange of silence."
        hide Johnny
        show Johnny serious1 R at left
        hide Ashley
        show Ashley smug2 at right
        Ashley "To be honest, you can take that piece of scrap if you want."
        hide Ashley
        show Ashley smug3 at right
        Ashley "We almost ran out of gasoline{nw}"
        hide Ashley
        show Ashley smug1 at right
        extend " and I'm not in the mood for pushing it, so..."
        hide Ashley
        show Ashley at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "So you're gonna give it to me for good.{w} What a collaborator, wish all of my jobs were like this."
        hide Ashley
        show Ashley smug2 at right
        hide Johnny
        show Johnny smile1 R at left
        Ashley "Not so fast, detective.{w} If you really want the keys you’ll have to go ask Andrew for them."
        hide Ashley
        show Ashley mocking1 at right
        Ashley "Maybe I should've mention it before."
        hide Ashley
        show Ashley worried2 at right
        Ashley "He's the one who have them."
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny sigh R at left
        Johnny "Always... {w} Always a problem..."
        hide Ashley
        show Ashley giggle1 at right
        play sound "audio/sfx/blingy_sp.ogg"
        Ashley "Hahahaha~"
        hide Ashley
        show Ashley smug3 at right
        Ashley "Whatever,{w} just try not to scare him too much."
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny confused R at left
        Ashley "May even cry a little,{w} he likes to do that sometimes."
        hide Johnny
        show Johnny smile1 R at left
        Johnny "As fun as that sounds, I think I’ll try to make things quick."
        show Johnny smile2 R at left
        Johnny "But thanks anyway, miss Graves.{w} And of course…"
        "I slid one of my business cards on the table."
        play sound "audio/sfx/whip.wav"
        hide Johnny
        show Johnny P2 R at left
        pause 0.5
        Johnny "If there’s a problem…"
        play sound "audio/sfx/whip.wav"
        hide Johnny
        show Johnny P R at left
        pause 0.5
        extend " better call me~"
        hide Ashley
        show Ashley giggle1 at right
        play sound "audio/sfx/blingy_sp.ogg"
        Ashley "Hahahahaha, yeah yeah I get it…"
        hide Ashley
        show Ashley smug2 at right
        Ashley "I’ll have it on mind."
        scene black with fade
        "Zero problem here."
        jump main_route2

    ############################### End Ashley's choices

label main_route2:
    stop music fadeout 2.0
    pause 2.0
    play music "audio/music/See You After Babe (HTML Remix).wav" fadein 1.0
    "After this encounter, I made my way into the stairway to find the guy leaning against the railing."
    scene club2 with fade
    show Andrew confused at left
    "His gaze passed over me discreetly, perhaps trying not to be noticed."
    pause 0.5
    play sound "audio/sfx/Steps stone.wav"
    show Johnny at right
    with moveinright
    "I took my place aside him and, trying to get a good first impression, {nw}"
    hide Johnny
    show Johnny smile2 at right
    extend " I gift a friendly smile."
    hide Andrew
    show Andrew worried1 at left
    "And his answer wasn't but a dense silence."
    "He didn't even try to look at me until, just kept himself isolated hoping that I would eventually get away from there."
    hide Johnny
    show Johnny smug1 at right
    "But of course, I wasn't going anywhere."
    hide Andrew
    show Andrew sigh at left
    "He snorted and addressed me with a tired tone after a while."
    hide Andrew
    show Andrew serious1 at left
    Andrew "What is it?"
    hide Andrew
    show Andrew nervous1 at left
    hide Johnny
    show Johnny chat1 at right
    Johnny "Mr. Graves, am I right?{w} I had the pleasure to talk with your little sister."
    hide Johnny
    show Johnny smug1 at right
    Johnny "Think you two have a dirty little secret.{w} Am I right?"
    hide Andrew
    show Andrew confused at left
    Andrew "Pleasure?{w} That’s not the word I would use..."
    hide Andrew
    show Andrew chat1 at left
    Andrew "Look, whatever she told you it’s probably a lie."
    hide Andrew
    show Andrew sigh at left
    Andrew "She’s very good at it and...{w} to be honest she's kinda insane…"
    hide Andrew
    show Andrew angry1 at left
    Andrew "...and adopted.{w} Specially adopted."
    hide Johnny
    show Johnny chat1 at right
    hide Andrew
    show Andrew confused at left
    Johnny "Well, that’s quite the revelation, Mr. Graves.{w} Let me introduce myself."
    hide Johnny
    show Johnny smile2 at right
    "I extended a presentation card."
    Johnny "If there’s a problem…"
    play sound "audio/sfx/whip.wav"
    hide Johnny
    show Johnny P at right
    extend " better—{nw}"
    play sound "audio/sfx/scratch.wav"
    Andrew "Quit that, I know you."
    hide Johnny
    show Johnny smile1 at right
    extend " You’re the clown from those posters."
    hide Johnny
    show Johnny sigh at right
    "Yeah, I don’t think she's adopted."
    Johnny "You’re not funny, man.{w} Where’s your spirit?"
    hide Andrew
    show Andrew sigh2 at left
    Andrew "Dead, just like your 80s detective role."
    hide Andrew
    show Andrew angry2 at left
    hide Johnny
    show Johnny smile1 at right
    Andrew "Now would you mind to fuck off?{w} We have no business with you, and I really need a moment alone..."
    hide Johnny
    show Johnny serious1 at right
    hide Andrew
    show Andrew angry1 at left
    Johnny "I'm afraid I can't do that, brother."
    "He turned out to be way less chatty than his sister."
    "His expressions, however, turned to be quite clearer than hers.{w} He was anxious,{w} the tickle on his hand left that on sight.{w} His sight escaped the eye contact, and his right leg moved with a certain nervous tic."
    hide Andrew
    show Andrew nervous1 at left
    "I had a feeling that,{w} at the slightest chance,{w} he would try to run away in an attempt to escape."

    ################################### Andrew choice

    menu:
        "It was better to think my next move."

        "Straightness":
            $ DualAff +=1
            jump Straightness2

        "Sharpness":
            $ AndrewAff -=1
            jump Sharpness2

        "Subtlety":
            $ AndrewAff +=1
            jump Subtlety2

    label Straightness2:
        pause 0.5
        Johnny "Look, I’m not against you nor your sis, all right?"
        "I took one step backwards just to give him some space."
        hide Johnny
        show Johnny chat1 at right
        Johnny "You can relax. {w} Breathe deeply, enjoy the music, take a second to flavor the moment."
        hide Andrew
        show Andrew nervous2 at left
        hide Johnny
        show Johnny smile2 at right
        Johnny "I understand that you may think I'm just trying to get a confession,{w} or that may be looking for more reasons to screw you up,{w} but the reality couldn't be further from that."
        hide Andrew
        show Andrew confused at left
        "His expression softened a little."
        "For an instant, I thought I may had passed through him."
        hide Johnny
        show Johnny serious1 at right
        hide Andrew
        show Andrew angry1 at left
        "But sadly, he frowned and closed himself before I could even be sure of that."
        Johnny "The point is that I just want the car back, ok?{w} That’s what I’m here for."
        hide Johnny
        show Johnny chat1 at right
        Johnny "The fact that you or the goth girl had rob a bank, killed a guy or maybe sold some meth isn’t my business at all."
        hide Johnny
        show Johnny smug1 at right
        "Like I wouldn't have skeletons in my closet anyway..."
        hide Andrew
        show Andrew chat1 at left
        Andrew "Oh, yeah? You don’t care?{w} Well, that’s exactly what a cop would say."
        hide Johnny
        show Johnny chat1 at right
        Johnny "And to be honest with you,{w} I was on the academy for a season."
        hide Andrew
        show Andrew confused at left
        hide Johnny
        show Johnny angry1 at right
        Johnny "They didn’t appreciate my…{w} talents..."
        hide Andrew
        show Andrew facepalm at left
        "The poor guy sigh and looked down at the lower floor."
        hide Andrew
        show Andrew confused at left
        hide Johnny
        show Johnny serious2 at right
        "For moments, his eyes locked over his sister while she kept trying to steal from the flask of tips."
        hide Johnny
        show Johnny smile2 at right
        "I found that pretty funny, got to admit,{w} but he didn’t react at all."
        hide Johnny
        show Johnny serious2 at right
        "It was as if he had been lost in thought, and for an instant, forgotten about the rest of the world."
        "Quite ominous...{w} I even thought about giving him a slap on the nape."
        hide Andrew
        show Andrew chat1 at left
        Andrew "Let’s say that, for a moment, I believe you."
        Andrew "What would you do if I give up the keys?"
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny chat1 at right
        Johnny "I’ll go down,{w} ask for something to drink,{w} and then, when you have found it appropriate and walked away,{w} I’ll take the car and bring it back to its respective owner."
        hide Johnny
        show Johnny serious1 at right
        Johnny "No question, no cops, and no more stories."
        Johnny "It ends there."
        hide Andrew
        show Andrew confused at left
        Andrew "And if I don’t?"
        hide Johnny
        show Johnny at right
        Johnny "Well, let's just say that you will have a guy neither as kind nor handsome as me looking for your soft and beautiful booty."
        hide Johnny
        show Johnny smug2 at right
        hide Andrew
        show Andrew nervous2 at left
        Johnny "And also... a ten-foot-tall guy named Larry waiting for it in a nice cell."
        hide Johnny
        show Johnny serious3 at right
        Johnny "I would consider that last thingy if I was you."
        hide Andrew
        show Andrew chat1 at left
        Andrew "That sounded like something you’ve experienced before…"
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny chat1 at right
        Johnny "Not by myself, thankfully.{w} But let's just say that...{w} there’s a few people who want this bubble butt on their walls nowadays."
        hide Johnny
        show Johnny at right
        hide Andrew
        show Andrew facepalm at left
        "He sigh while considering his little options."
        "He doesn’t seemed like he’ll run away now, but neither was about to buy me any drinks for sure."
        hide Andrew
        show Andrew angry1 at left
        "Still, I don't think I could have solved it better."
        hide Andrew
        show Andrew at left
        Andrew "Fine…{w} here you go."
        Andrew "Just leave us alone now, please…"
        show keys at center
        play sound "audio/sfx/item_got.ogg"
        "{i}Jonathan has picked up the car-keys! (finally){/i}"
        hide keys with dissolve
        pause 0.5
        hide Johnny
        show Johnny chat1 at right
        Johnny "Without problems, brother.{w} You just took a weight off your shoulders."
        scene black with fade
        jump main_route3

    label Sharpness2:
        pause 0.5
        hide Johnny
        show Johnny serious2 at right
        Johnny "Listen,{w} you don’t need to be scared, man. Really..."
        hide Andrew
        show Andrew confused at left
        Johnny "Do you have any idea how many criminals I met on my daily basis?{w} Do you know how I call them?"
        hide Johnny
        show Johnny chat1 at right
        Johnny "{b}Potential clients{/b}."
        hide Johnny
        show Johnny smile2 at right
        Johnny "There’s no need to put my nose where I don’t mind. That's part of the job."
        hide Andrew
        show Andrew chat1 at left
        Andrew "Being a jackass is also part the job?{w} Because you just sounded like one."
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny smile2 at right
        Johnny "And you're absolutely right,{w} it's all about that."
        hide Johnny
        show Johnny serious3 at right
        Johnny "BUT, that’s also a good thing for you, fancy pants~"
        hide Andrew
        show Andrew sigh at left
        Andrew "Dear god..."
        hide Andrew
        show Andrew angry2 at left
        Andrew "Why does everything always have to happen to me?"
        hide Johnny
        show Johnny chat1 at right
        Johnny "By the way,{w} you should stop smoking."
        hide Andrew
        show Andrew what at left
        Johnny "I gotta tell you, you’ll cough your lungs out when trying to run."
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny smug2 at right
        "His eyes locked on me with a tired-wrathful expression."
        "I could even feel his need to tear my eyes out,{w} but he wouldn’t have any success even if tried."
        hide Johnny
        show Johnny smug1 at right
        "So I just smiled at him for a while."
        "He looked kinda adorable when angry."
        Andrew "Are you here to arrest us or just wanna get into our lives?"
        hide Johnny
        show Johnny smile1 at right
        Johnny "Hmmm…{w} Well, putting you some cuffs sounds like a lot of fun."
        hide Johnny
        show Johnny chat1 at right
        hide Andrew
        show Andrew facepalm at left
        extend " But I don’t know if you’re into that~"
        hide Andrew
        show Andrew superangry at left
        hide Johnny
        show Johnny smug2 at right
        Andrew "STOP IT."
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny chat1 at right
        Johnny "All right all right, I’m just messing a little."
        Johnny "You sister told me you have the car-keys.{w} If you give them to me, I’ll {b}smoke{/b} out of here and leave you in peace with your cancer cue."
        hide Johnny
        show Johnny smug1 at right
        hide Andrew
        show Andrew facepalm at left
        Andrew "Cancer cue he says…{w} uuuuuhhh…"
        hide Andrew
        show Andrew at left
        extend " FINE!"
        Andrew "Take the stupid keys and leave us alone.{w} I already have enough with Ashley and her..."
        hide Andrew
        show Andrew worried1 at left
        extend " ideas…"
        show keys at center
        play sound "audio/sfx/item_got.ogg"
        "{i}Jonathan has picked up the car-keys! (finally){/i}"
        hide keys with dissolve
        pause 0.5
        hide Johnny
        show Johnny chat1 at right
        Johnny "Oh yeah,{w} she indeed has a good pair of ideas on her own."
        hide Andrew
        show Andrew angry1 at left
        extend "Would even ask for them I were a little less professional."
        hide Johnny
        show Johnny serious3 at right
        hide Andrew
        show Andrew angry2 at left
        Andrew "Whatever, dude..."
        hide Johnny
        show Johnny chat1 at right
        hide Andrew
        show Andrew at left
        Johnny "Anyway! It’s a pleasure to do business with you, Mr. Graves!"
        Johnny "I'll see you when you get a van and start cooking some meth in a plain—{nw}"
        hide Andrew
        show Andrew superangry at left
        Andrew "JUST FUCK OFF!"
        scene black with fade
        pause 0.5
        "Personal Note:{w} Finish Breaking Bad."
        jump main_route3

    label Subtlety2:
        Johnny "You have some serious problems, don’t you?"
        hide Andrew
        show Andrew at left
        "I got to caught his attention with that question."
        hide Andrew
        show Andrew confused at left
        "His face changed momentarily before letting out a deep sigh."
        hide Andrew
        show Andrew sigh at left
        Andrew "As if you care, man…"
        hide Andrew
        show Andrew angry1 at left
        Andrew "Those are personal problems, none of your business."
        hide Andrew
        show Andrew confused at left
        Johnny "True, but that doesn’t mean we can’t talk about it."
        hide Johnny
        show Johnny confused at right
        Johnny "You sister is...{w} weird."
        hide Johnny
        show Johnny chat1 at right
        hide Andrew
        show Andrew angry1 at left
        extend " In the good way, off course."
        Johnny "She’s a closed book, I could barely read what she was doing."
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny serious1 at right
        Johnny "But you?{w} Bud, you’re nothing like that..."
        hide Andrew
        show Andrew chat1 at left
        stop music fadeout 1.0
        Andrew "She’s not a closed book, she’s just…"
        hide Andrew
        show Andrew angry2 at left
        Andrew "She’s just {b}her{/b} being herself…"
        play sound "audio/sfx/static.wav" fadein 1.0 loop
        extend " It’s always about it.{w} Her ideas, her {b}feelings{/b}, her way to… to be, as a whole"
        hide Andrew
        show Andrew facepalm at left
        hide Johnny
        show Johnny smile1 at right
        Johnny "Right…{w} Kinda catching the thing now."
        hide Johnny
        show Johnny chat1 at right
        Johnny "She has the upper hand, doesn’t?"
        play music "audio/music/Ennio Morricone - The Thing.wav" fadein 1.0
        hide Johnny
        show Johnny confused at right
        hide Andrew
        show Andrew at left
        "The mere mention of that caused a reaction in him."
        hide Johnny
        show Johnny serious1 at right
        "His brow furrowed tightly, and I could see the vein in his throat throbbing as if were going to burst."
        "His fist clenched in place with clear intentions. I could tell he was trying his best to not punch me on the face,{w} moment that I realized that comment touched a sensitive fiber."
        hide Johnny
        show Johnny angry1 at right
        Johnny "Calm.{w} Down.{w} Brother."
        "I expressed a calm, yet serious tone,{w} indicating that if he decided to take actions...{w} I would too."
        "And believe me when I say that, if that would've happened...{w} thing would've gone nasty."
        pause 0.5
        Johnny "It was just a silly joke, that’s all."
        pause 0.5
        hide Andrew
        show Andrew facepalm at left
        stop music fadeout 2.0
        stop sound fadeout 2.0
        pause 3.0
        hide Andrew
        show Andrew superangry at left
        hide Johnny
        show Johnny serious1 at right
        Andrew "It wasn’t a joke for me, you penguin dressed asshole!"
        "He exploded, releasing his nerves within the words."
        hide Andrew
        show Andrew chat1 at left
        Andrew "She’s always doing whatever the hell she wants!"
        Andrew "Always getting into my life,{w} messing with my things,{w} breaking my…"
        hide Andrew
        show Andrew chat1 at left
        Andrew "my…"
        hide Andrew
        show Andrew facepalm at left
        stop music fadeout 1.5
        pause 1.5
        hide Johnny
        show Johnny confused at right
        Andrew "Whatever, dude…"
        Andrew "I don't even know why I'm telling you this."
        hide Johnny
        show Johnny serious2 at right
        Johnny "She treats you as a rug, I get that."
        play music "audio/music/Passion.wav"
        hide Andrew
        show Andrew sigh2 at left
        "He didn’t answered but his expression said more than a thousand words."
        hide Andrew
        show Andrew angry1 at left
        hide Johnny
        show Johnny chat1 at right
        Johnny "I see… I can relate to that."
        Johnny "Yes… being the bigger brother is a whole thing."
        Johnny "You take all the responsibilities and rarely get any appreciations for it."
        hide Johnny
        show Johnny serious2 at right
        hide Andrew
        show Andrew confused at left
        Johnny "But that’s how it is…{w} And you know why?"
        hide Johnny
        show Johnny angry1 at right
        hide Andrew
        show Andrew nervous1 at left
        Johnny "Because we’re MEN,{w} and that’s what MEN do."
        Johnny "We don't search for love or appreciation...{w} We take {b}care{/b} of the people we care about."
        hide Johnny
        show Johnny angry2 at right
        Johnny "End of story."
        hide Andrew
        show Andrew sigh2 at left
        Andrew "Heh…{w} Believe me, you don’t get the situation..."
        hide Johnny
        show Johnny angry1 at right
        hide Andrew
        show Andrew confused at left
        Johnny "You think so?{w} Well… Maybe I do."
        Johnny "My sister was a complicated woman too."
        hide Johnny
        show Johnny serious1 at right
        Johnny "We never got to understand each other...{w} but that's ok.{w} Like I said, it was never necessary."
        "Suddenly, the realization hit me.{w} The environment had changed in an unexpected way."
        hide Johnny
        show Johnny confused at right
        "I found myself quite involved in this conversation, way more than I would liked to."
        hide Andrew
        show Andrew at left
        "I realized that… I was in danger of speaking too much."
        "So, in an attempt to get back in character, I cough and I recovered my facade."
        hide Johnny
        show Johnny smile2 at right
        Johnny "Anyway… that’s beside the point."
        hide Johnny
        show Johnny chat1 at right
        Johnny "The girl downsides told me you have the car-keys,{w} is that right?"
        hide Johnny
        show Johnny serious3 at right
        hide Andrew
        show Andrew sigh at left
        "He let out a sonorous sigh before taking the keys out of his pocket."
        hide Andrew
        show Andrew angry1 at left
        Andrew "Yeah… You can have them."
        Andrew "The car is out of gas anyway so... here it goes."
        show keys at center
        play sound "audio/sfx/item_got.ogg"
        "{i}Jonathan has picked up the car-keys! (finally){/i}"
        hide keys with dissolve
        pause 0.5
        hide Johnny
        show Johnny smile2 at right
        Johnny "All right, I think that’s everything then."
        hide Andrew
        show Andrew nervous1 at left
        Andrew "Wait…{w} that’s it?"
        Andrew "I thought you were about to interrogate me or something."
        hide Johnny
        show Johnny chat1 at right
        Johnny "Hah!{w} Do I look like a cop to you?"
        hide Andrew
        show Andrew facepalm at left
        hide Johnny
        show Johnny smile1 at right
        Johnny "Please don’t answer…"
        scene black with fade
        "A close one…{w} and not the kind of close I like."
        jump main_route3

    ############################# End Andrew's choices

label main_route3:
    stop music fadeout 2.0
    pause 2.0
    play music "audio/music/Delay.wav" fadein 1.0
    pause 2.0
    "So, the job was done."
    "As a final celebration for my success, I went down to the bar and ordered something pretty to drink."
    "Off course,{w} this wasn’t just for the sake of it."
    "I wanted to see how this two characters interact with each other."
    pause 1.5
    "After a while, Andrew went stairs down to sit beside his sister."
    show Ashley think at right with dissolve
    show Andrew at left with dissolve
    "Their looks fell over me on more than one occasion."
    "I saw them whispering among themselves under the soft sound of the music plying.{w} Off course, there was no way to know whay they were talking about, but I have the feeling that I was a recurring theme."
    "I gift a little smile as I saw them slowly walking out of the bar.{w} Got no answer in exchange."
    "They took a quick peek inside the vehicle before keep moving towards the darkness, where their silhouettes disappeared among the shadows."
    scene black with fade
    "As for me,{w} I stayed there for a little more,{w} trying to imagine what kind of events could have led those two to this particular situation."
    "Maybe something simple..."
    "Maybe something I wasn't able to even think about..."
    stop music fadeout 2.0
    pause 2.0
    "And that's about it..."
    play music "audio/music/Cruel Summer Start.wav"
    queue music "audio/music/Cruel Summer Tense.wav" loop
    pause 5.0
    scene table with fade
    "Entry number one:"
    pause 1.0
    "During the development of my investigation of the stolen Málaga,{w} I came across a series of unusual events."
    "The death body,{w} the couple of siblings,{w} the death certificates,{w} the police department somehow involved..."
    "I'm aware that it could be just my imagination... again...{w} that there's the chance of everything to be just a REALLY intricated string of coincidences."
    "But still...{w} I have that strange feeling that everything is somehow related.{w} The tiny protruding tip of a large iceberg emerging from the bottom of the sea."
    "I have... very little connections at the moment,{w} just a few dots that keep ringing on my head."
    "Call it…{w} {b}my intuition{/b}, if you want."
    "But—{nw}"
    play sound "audio/sfx/mumbling1.wav" volume 0.4
    pause 3.0
    stop sound
    play sound "audio/sfx/static.wav" volume 0.3 fadein 1.0
    Johnny "..."
    stop sound fadeout 1.0
    "I kept thinking about those two after our first meet."
    "It’s strange,{w} usually I don’t feel this level of interest with my clients,{w} much less with random people I found on a club."
    "But this duo…{w} There’s something really appealing about them."
    "A {b}spark{/b}, to call it anything.{w} Something different from everyone else."
    "Perhaps I’m just searching for excuses to talk with them again.{w} That’s a possibility too…"
    "But then again—{nw}"
    stop music fadeout 1.0
    play sound "audio/sfx/mumbling2.wav" volume 0.4
    pause 3.0
    Johnny "Please…"
    stop sound
    Johnny "A little peace over here?{w} I'M TRYING TO WRITE MY THOUGHTS!"
    play music "audio/music/Cruel Summer ost.wav" fadein 1.5
    scene black with fade
    play sound "audio/sfx/item_got.ogg"
    "{i}Jonathan has picked up his shovel...{/i}"
    play sound "audio/sfx/Steps wood.wav"
    pause 3.0
    play sound "audio/sfx/Wooden door open.wav"
    pause 3.0
    play sound "audio/sfx/mumbling3.wav" loop
    pause 1.0
    "As the door opened, I was blasted with the mumblings of that police officer."
    "Leather ropes restrained his hands and legs,{w} drool and blood dripped from the gag on his mouth,{w} and his teary eyes watched with paralyzing horror as I appeared under the frame."
    scene JohnnyF1 with fade
    if "PoliDisdain" in locals():
        Johnny "What’s wrong officer?"
        Johnny "Scared of the parasite that lives from the misery of the people?"
        pause 1.5
        Johnny "That’s funny…{w} You seemed a lot more confident back then on the city.{w} But I guess it isn't as simple when you're not surrounded by the filth of {b}your{/b} kind."
        scene black
        play sound "audio/sfx/shovel hit1.wav"
        pause 1.0
        Johnny "But,{w} my friend,{w} that's the thing..."
        play sound "audio/sfx/bng sfx/1.wav"
        pause 1.0
        Johnny "Here,{w} in the tranquility of {b}my{/b} forest,{w} {b}MY{/b} domains..."
        Johnny "...with the animals, the silence, the lack of rules and condescending looks..."
        play sound "audio/sfx/bng sfx/2.wav"
        pause 1.0
        Johnny "Here..."
        Johnny "People often show their true selves.{w} And this...{w} pathetic, scared little thing..."
        Johnny "This is your true self, my friend."
        play sound "audio/sfx/bng sfx/3.wav"
        pause 2.3
        Johnny "Or it was...{w} more likely."
        Johnny "Oh well,{w} guess I'll have to clean this up."
        Johnny "More things to do... just what I needed."

    else:
        if "PoliDemureness" in locals():
            Johnny "Well officer…{w} Seems like you gave me everything you had."
            pause 1.0
            Johnny "I was hoping to play with you a little more.{w} At least for a couple of days, since you were soo kind to me earlier."
            Johnny "I’m very good keeping people entertained, you know?{w} Once interrogated a guy for almost a month."
            Johnny "It was interesting.{w} I thought he would go crazy in less than a week, but he put up a good fight."
            scene black
            play sound "audio/sfx/shovel hit1.wav"
            pause 1.0
            Johnny "But let's not start telling anecdotes.{w} Something new just came up..."
            play sound "audio/sfx/bng sfx/1.wav"
            pause 1.0
            Johnny "Something big!"
            Johnny "And I don't want to be distracted by other {b}minor{/b} stuff.{w} Don't expect you to understand tho."
            Johnny "So let's try not to enjoy this, hm?"
            play sound "audio/sfx/bng sfx/3.wav"
            pause 2.3
            Johnny "And maybe...{w} not to make this so dirty this time..."
            Johnny "Uh... this will take a while to clean up."
            Johnny "Oh well,{w} work for later."
        else:
            Johnny "Hey officer~"
            Johnny "Quite the night we’re having today, huh?"
            Johnny "Moon is shining,{w} very little bugs,{w} a great time to take a walk!"
            Johnny "Or to write your thoughts..."
            scene black with fade
            play sound "audio/sfx/shovel hit1.wav"
            pause 1.5
            Johnny "You see, officer...{w} I am a very reasonable person when you're good with me.{w} And while I must say that you haven't been an angel, you answered all my questions to my satisfaction."
            Johnny "But interrupting me when I'm writing?"
            play sound "audio/sfx/bng sfx/1.wav"
            pause 2.0
            Johnny "That is a lack of respect to my person...{w} And I {b}really really REALLY{/b} hate when people disrespects me."
            Johnny "So, I'm going to finish this interview as quickly as possible."
            Johnny "Only then I'll be able to be peace... and enjoy the rest of the night."
            play sound "audio/sfx/bng sfx/3.wav"
            pause 2.3
            Johnny "uuhh...{w} You splashed on my hands..."
            Johnny "Disgusting...{w} You can't even die cleanly."
            Johnny "You see? That's why you're dead!{w} Because you are disgusting."


    pause 1.0
    play sound "audio/sfx/Steps wood.wav"
    pause 3.0
    scene table with fade
    Johnny "Now...{w} What was I saying?"
    Johnny "Oh yeah,{w} the siblings."
    "I’m gonna start a new case just for them."
    "Call it... {w} a personal project."
    "I have the feeling that it will be my biggest work yet."
    scene club_night with fade
    stop music fadeout 1.0
    pause 1.0
    "And I have the perfect name for it..."
    scene black with fade
    pause 1.0
    play music "audio/music/Cruel Summer end.wav"
    pause 2.0
    scene end1 with fade
    pause 23.0
    scene black with fade
    pause 2.7
    stop music fadeout 1.0

    ####################### 1° Encounter

    pause 2.5
    play music "audio/music/The Thing - What Appears to be Normal.wav" fadein 2.0
    pause 3.0
    Andrew "You’ve been quite silent since we get out of that club."
    Andrew "What's happening?{w} Did the bartender catch you stealing his tips?"
    Ashley "Hah!{w} He wish. He was too busy looking at that girl’s ass for even notice I was there."
    Ashley "It was a perfect move, if I can say so~"
    Andrew "Then what?{w} Stop acting as if wouldn't be obvious when you have something in mind."
    scene M_Room with fade
    show Andrew at left
    show Ashley mad at right
    Ashley "..."
    Ashley "That guy…{w} the detective.{w} Did you notice something off on him?"
    hide Ashley
    show Ashley at right
    Ashley "Something…{w} I don’t know, weird?"
    hide Andrew
    show Andrew chat1 at left
    Andrew "Duh, he IS weird."
    hide Andrew
    show Andrew angry2 at left
    Andrew "He was just an asshole with 80's delusions."
    hide Andrew
    show Andrew angry1 at left
    Andrew "Now we don't even have a vehicle because of him..."
    hide Ashley
    show Ashley ewww at right
    Ashley "You expect me to believe that’s everything that bothers you?{w} Seriously Andy?"
    hide Ashley
    show Ashley mad3 at right
    hide Andrew
    show Andrew worried1 at left
    Ashley "You’re gonna tell me that, {b}YOU{/b} in particular, aren't feeling a little uneasy by the fact that he let us go like that?{w} Without questions…{w} without warnings…"
    pause 2.0
    Andrew "..."
    hide Andrew
    show Andrew serious1 at left
    Andrew "He scared me...{w} but not in a normal way."
    hide Ashley
    show Ashley at right
    hide Andrew
    show Andrew angry1 at left
    pause 1.5
    hide Ashley
    show Ashley worried1 at right
    pause 1.5
    Andrew "His eyes,{w} his gaze,{w} his whole presence…"
    Andrew "He didn’t show up, but it felt… really oppressive."
    Andrew "As if he were…"
    hide Ashley
    show Ashley at right
    hide Andrew
    show Andrew at left
    Ashley "…watching through you. Yeah, I noticed."
    hide Ashley
    show Ashley smug1 at right
    Ashley "Not like it's very complicated, Andy dear."
    hide Andrew
    show Andrew facepalm at left
    pause 1.0
    Andrew "Can you be serious? PLEASE?"
    hide Ashley
    show Ashley mocking1 at right
    Ashley "Yeah yeah, I’m just messing a little."
    hide Ashley
    show Ashley at right
    Ashley "But... He did got me a little nervous tho..."
    hide Andrew
    show Andrew at left
    hide Ashley
    show Ashley mad at right
    Ashley "Still, it didn't felt like he wanted to hurt us."
    Ashley "More like..."
    pause 2.0
    hide Andrew
    show Andrew confused at left
    Andrew "He was curious?{w} Like some kind of strange fixation?"
    Ashley "..."
    pause 1.0
    scene black with fade
    Ashley "Do you think we’re gonna see him again?"
    stop music fadeout 2.0
    pause 1.5
    Andrew "I don’t know,{w} but…"
    Ashley "But we have the way to know it."
    Ashley "Well…{w} something like that."
    pause 1.0
    Andrew "Uh…{w} does it mean more soup for dinner?"
    play sound "audio/sfx/blingy_sp.ogg"
    Ashley "A lot more soap for dinner~"
    Ashley "And you'll love it, you heard me?"
    pause 1.0
    Andrew "I have a terrible feeling about this..."
    Ashley "Yeah, like... with everything else."

    pause 3.0
    play sound "audio/sfx/typing.wav"
    scene start2 with fade
    pause 3.0
    scene black with fade

    "I had that strange dream again."
    play sound "audio/sfx/static.wav" fadein 2.0 loop volume 0.6
    pause 3.0
    "I was on that old, cold, nasty house."
    "The air was as dense as smoke,{w} with a jarring atmosphere that didn’t let me archive peace at any moment."
    "At the same time, however, I was tempted by a constant feelings of closeness that tried to distract my mind from the latent danger."
    "But danger of what?"
    "I've been here {b}many{/b} times, and even if I know what is gonna happen next, I can't avoid this damn sensation."
    scene dream1 with fade
    "I was sitting at the table.{w} There was a plate in front of me, but the food was nowhere to be seeing."
    "But even so, I could still smell its scent."
    "It was hefty and unpleasant — toxic,{w} unhealthy,{w} like the putrid stench that emanates from stagnant pipes of the city's streets."
    "And there was...{w} an echo...{w} people around me."
    stop sound fadeout 1.0
    pause 1.0
    play music "audio/sfx/Humming.wav"
    pause 3.0
    "It was the voice of a woman,{w} with a voice so relaxing, so perfect that could only exist in the non-existent confines of my mind."
    "She was humming a beautiful song, "
    play sound "audio/sfx/Coughing.wav" loop volume 0.1
    extend "and alongside with it, the incessant symphony of deep and painful coughs."
    "I knew they were somewhere around me, hiding between the shadows and the intoxicating miasma."
    "But...{w} Why giving me to the labor of searching for them?{w} It wasn't as if I was going to find them anyway."
    pause 1.5
    "Instead, I stood in my place enjoying the mesmerizing tone of that song."
    "It was... {w} it was perfect.{w} Would've stayed there forever if someone had given me the opportunity."
    "Apathy reigned over me,{w} the inability to feel any type of happiness, sadness or worry for those besides the lady."
    "I had ears only for her... {w} for that precious voice..."
    pause 1.5
    "And then...{w} as quick as it began..."
    stop music fadeout 1.0
    pause 1.5
    "It stopped."
    stop sound fadeout 1.0
    pause 1.0
    play sound "audio/sfx/Body Fall.wav"
    pause 2.0
    "And rumble was heard twice before the arrival of complete silence.{w} And loneliness was everything that was left now."
    scene black with fade
    pause 1.0
    play music "audio/sfx/static.wav" fadein 2.0 loop
    "No more colors,{w} no more sound…{w} the end of everything."
    "Except by the fact that...{w}"
    pause 1.5
    "I was still there."
    "Somewhere...{w} somehow..."
    pause 1.0
    "I was there."
    stop music fadeout 1.0
    pause 2.0
    "I've been having this same dumb dream for years now..."
    play music "audio/music/Provoker - Dark Angel.wav"
    pause 1.0
    "It doesn't bother me anymore.{w} Actually, it never did."
    "It's just a stupid dream.{w} It's useless, just there to try to scaring me."
    "Heh... scaring me. Think about that."
    "The only thing that annoys me is the fact that, once I wake up from their disgusting clutches, I am no longer able to fall asleep again."
    "So...{w} with all the pain of the world for another early-start of the morning..."
    pause 1.5
    "I went out for a walk."
    pause 1.5
    scene Forest1 with fade
    pause 1.5
    "I love the smell the forest in the morning.{w} It’s clean, fresh, intoxicating."
    "People generally don't come to these parts.{w} They think it’s dangerous,{w} that they’ll get face to face with some freak, will get lost or attacked by an animal."
    scene Forest3 with fade
    Johnny "Hah! Poor idiots."
    "Much better for me.{w} It may be a bit lonely, but I prefer it before having all those annoying voices disturbing the surroundings."
    "All those complaints,{w} that stench coming from those...{w} insufferable mediocres."
    scene Forest2 with fade
    "Hating them is something easy to learn.{w} What's not, is having to leave this peace to venture into their concrete jungle."
    "That circus filled with clowns and two legged animals..."
    pause 1.0
    "Sadly… I do need their garbage to survive."
    "To coexist with their... filth."
    scene Forest4 with fade
    "But that's how it is...{w} What's the point on trying to fight it anyway?"
    pause 1.0
    "Things like that lead me to think...{w} to dream...{w} to remember..."
    stop music fadeout 2.0
    pause 3.0
    "..."
    "Whatever."
    "I made a small summary of my progress on the Graves Case."
    play music "audio/music/Delay.wav" fadein 1.0
    play sound "audio/sfx/paper.wav"
    show Pol9 with Dissolve(0.5)
    pause 1.0
    "First of all,{w} I couldn't get much information from my last night's visitor."
    "The police forces at the station seems to be hiding something, but the information is protected by the high command."
    "I’m gonna need something more than just {b}Human Resources{/b} if I want to put my hands on that…"
    "Don’t know if it’s worth it either."
    hide Pol9 with Dissolve(0.5)
    "Second point,{w} the stuff I took from the siblings."
    play sound "audio/sfx/paper.wav"
    show butcher with Dissolve(0.5)
    pause 1.0
    "The butcher cleaver…{w} It has something strange on it."
    "Its smell's…{w} odd,{w} to put it simple."
    "Whatever they used it for, they didn't wash it properly.{w} It's like, when you eat fish and leave the cutlery dirty."
    "It may look, clean but the aroma persist on the metal."
    "I have a partner who can help with this.{w} I'll stop by to see him later."
    hide butcher with Dissolve(0.5)
    pause 1.0
    play sound "audio/sfx/paper.wav"
    show notepad with Dissolve(0.5)
    pause 1.0
    "My greatest interest,{w} however,{w} is the notepad."
    "While yes,{w} the death certificates where a great finding,{w} the numbers written of its pages are way more useful at the moment."
    "Numbers…{w} and names too."
    "I could get great places to begin my research thanks to this.{w} But the best of all, and my main objective right now, was for sure…"
    stop music fadeout 1.0
    scene black with fade
    pause 1.5
    play music "audio/music/Get On My Knees by Brian Deady.wav"
    Johnny "Mommy and daddy’s house~"
    pause 3.0
    "Hands to work then."
    "The day has begun."
    pause 2.0
    scene drive with fade
    pause 1.0
    "I drove towards thenorthern area of the city while preparing to met with my my partner."
    "His name was Lars, and he was an old reliable when it comes to analyzing evidence."
    "Off course, I can’t say we understand each other,{w} but when work is involve?{w} Then that bastard is a compliant."
    scene LabOut with fade
    pause 1.0
    "The biochemical laboratory waited with its usual quietness.{w} It is rare to find people in this area, and if it happens they are generally not in the mood to even exchange glances with you."
    "That's the exact reason I like to come here."
    scene black with fade
    stop music fadeout 1.0
    Johnny "It was time to ask for a favor."
    pause 1.5
    scene Lab1 with fade
    play music "audio/music/Magnum Force.wav" fadein 1.0
    show Lars 1 right at right
    pause 0.5
    Lars "..."
    pause 0.5
    show Johnny chat1 R at left with moveinleft
    Johnny "Hey pal~"
    Johnny "How's the crime doing?"
    pause 0.5
    hide Johnny
    show Johnny serious3 R at left
    hide Lars
    show Lars 3 at right
    "As always, I didn’t receive a warm smile as a welcome."
    Lars "Paddle...{w} Let me guess,{w} you’re out of HF already?"
    hide Johnny
    show Johnny chat1 R at left
    hide Lars
    show Lars 4 at right
    Johnny "These have been very productive weeks."
    hide Johnny
    show Johnny R at left
    extend " I would’ve paid you a visit, but…{w} you know."
    Johnny "This job is killing me..."
    hide Johnny
    show Johnny smug1 R at left
    extend " and not just me~"
    hide Lars
    show Lars 2 at right
    Lars "Uh…{w} the day you pay me a visit I’ll have a window to jump from."
    hide Johnny
    show Johnny R at left
    hide Lars
    show Lars 1 at right
    Lars"Even if that’s not enough to stop you, I can at least make you do some exercise."
    Johnny "I do plenty of exercises, thank you very much."
    hide Johnny
    show Johnny confused R at left
    Johnny "Just… not in the conventional way, but I keep myself in check."
    hide Johnny
    show Johnny serious1 R at left
    hide Lars
    show Lars 3 at right
    Lars "And since you clearly don’t need to do more of that,{w} how about going to a therapist instead?"
    hide Johnny
    show Johnny serious2 R at left
    hide Lars
    show Lars 4 right at right
    Johnny "How about you going to one?"
    pause 1.5
    Lars "..."
    pause 1.5
    Johnny "..."
    pause 1.5
    hide Johnny
    show Johnny smug1 R at left
    hide Lars
    show Lars 3 at right
    Lars "All right, you have a point there."
    hide Lars
    show Lars 5 right at right
    Lars "On the other side,{w} Don't you think you may be attracting unwanted attention?"
    hide Lars
    show Lars 2 right at right
    hide Johnny
    show Johnny serious1 R at left
    Lars "{b}Working{/b} that much could be raising the bar too high."
    hide Lars
    show Lars 1 right at right
    hide Johnny
    show Johnny chat1 R at left
    Johnny "The bar is in a perfect place if that’s what you’re asking."
    hide Johnny
    show Johnny serious2 R at left
    Johnny "Now, changing the subject…"
    play sound "audio/sfx/item_got.ogg"
    items "Jonathan paid 1500 bucks."
    Johnny "For the last liter, and an extra..."
    hide Lars
    show Lars 3 at right
    Lars "An extra?"
    "Old fox immediately took the message."
    hide Lars
    show Lars 1 at right
    Lars "What is it?{w} I’m not in the mood for games, Paddle.{w} It better be important."
    "I took the cleaver out of my jacket and placed it on his working table."
    hide Lars
    show Lars 4 at right
    hide Johnny
    show Johnny serious1 R at left
    Johnny "Found this little thingy.{w} I suspect it may have been used, and not exactly to prepare food."
    hide Johnny
    show Johnny chat1 R at left
    Johnny "Take a sniff!"
    hide Lars
    show Lars 6 right at right
    hide Johnny
    show Johnny smug1 R at left
    Lars "That’s disgusting…{w} and very unprofessional."
    hide Johnny
    show Johnny R at left
    Lars "You bring an old, stinking blade without the slightest care in the world, and expect me to look at it and tell you if anyone has been chopped with it?"
    Lars "Do I look like a genius to you?"
    hide Lars
    show Lars 1 at right
    extend " Because is so, I’m not the wish-fulfilling type."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "I expect you to do your job.{w} Use your instruments, play with your tools or do whatever you do with {b}that{/b} machine."
    hide Lars
    show Lars 2 at right
    hide Johnny
    show Johnny smile1 R at left
    stop music
    Lars "That’s a microwave…"
    pause 1.5
    Johnny "Yeah..."
    play music "audio/music/Magnum Force.wav" fadein 1.0
    hide Johnny
    show Johnny serious2 R at left
    Johnny "I just want to know if you can find residues of meat or blood in it."
    Johnny "Come on, give me a hand on this."
    pause 1.5
    hide Lars
    show Lars 1 at right
    Lars "You’re being too demanding…{w} And for worse you’re asking me to do it for free."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "Free?"
    hide Johnny
    show Johnny angry1 R at left
    extend " Do I have to remind you the {b}small inconvenient{/b} with your dealer?"
    hide Lars
    show Lars 2 at right
    extend " The one you strongly asked me to intervene in?"
    Johnny "You still own me that favor."
    pause 2.0
    Lars "..."
    hide Lars
    show Lars 3 at right
    hide Johnny
    show Johnny serious1 R at left
    Lars "My schedule is busy, and this is very complicated process.{w} It’ll take at least a week to have the first result."
    hide Johnny
    show Johnny serious2 R at left
    hide Lars
    show Lars 1 right at right
    Johnny "I have time.{w} Can you do it?"
    pause 1.0
    Johnny "Please?"
    pause 1.0
    hide Lars
    show Lars 2 at right
    Lars "If I can?{w} Hah!"
    hide Johnny
    show Johnny smile2 R at left
    hide Lars
    show Lars 1 at right
    Lars "But after that I don't owe you anything."
    hide Johnny
    show Johnny smug1 R at left
    Johnny "For now, pal… for now~"
    stop music fadeout 1.0
    hide Lars
    show Lars 4 right at right
    Lars "So…{w} if that’s everything you need, I would be happy to return to my solitude."
    hide Johnny
    show Johnny serious2 R at left
    Johnny "Actually,{w} there’s something I wanted to ask."
    hide Johnny
    show Johnny serious1 R at left
    play music "audio/music/Cruel Summer Tense.wav"
    Johnny "Have you heard about the building [[REDACTED]?{w} The one that caught fire not long ago."
    pause 1.5
    Lars "..."
    pause 1.0
    hide Lars
    show Lars 1 at right
    Lars "Don’t tell me you’re investigating that."
    hide Johnny
    show Johnny R at left
    Johnny "What do you know?"
    pause 1.5
    hide Lars
    show Lars 3 at right
    Lars "Look…{w} No matter how much the authorities, the media or the people involved try to deny it.{w} There’s some serious bullshit around it."
    hide Lars
    show Lars 2 right at right
    Lars "There is very little information about the quarantine buildings, but it's rumored that...{w} {b}THAT{/b} one in particular…{w} suffered a leak."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "A leak..."
    Johnny "Someone escaped?"
    hide Lars
    show Lars 1 right at right
    Lars "Exactly."
    hide Johnny
    show Johnny serious2 R at left
    Johnny "And what bases do you have to support that?"
    hide Lars
    show Lars 3 at right
    hide Johnny
    show Johnny confused R at left
    Lars "My unholy balls, and my intuition,{w} and neither of them have ever failed me."
    hide Lars
    show Lars 4 right at right
    hide Johnny
    show Johnny R at left
    Lars "Listen, I’ve been on the wrong side of the street for a long time,{w} way more than you."
    Lars "When I smell something dirty, it’s because there {b}IS{/b} something dirty."
    hide Johnny
    show Johnny serious1 R at left
    "I can't argue against that logic."
    hide Johnny
    show Johnny serious2 R at left
    hide Lars
    show Lars 1 at right
    Lars "And I'll tell you one last thing..."
    Lars "If you're really convinced in going down that road, you need to know something."
    Lars "It may be a little more dangerous than what you’re used to."
    hide Johnny
    show Johnny smug1 R at left
    Johnny "You know that only encourages me, right?"
    hide Lars
    show Lars 2 at right
    Lars "Yeah, but I don’t wanna have to search for a new associated.{w} So you better keep an eye on that little butt of yours, ok?"
    hide Lars
    show Lars 4 at right
    hide Johnny
    show Johnny chat1 R at left
    Johnny "This butt is in good hands, for your information~"
    hide Johnny
    show Johnny smile2 R at left
    hide Lars
    show Lars 6 right at right
    Lars "Then get out of here and give it a good use!"
    scene black with fade
    "The pieces kept moving..."
    "It seemed like there was going to have some troubles on the road.{w} The sense of urgency is something that adds to the thrill, so I had no hurries."
    "What if it is a little more dangerous?"
    "For someone like me,{w} someone smart,{w} strong,{w} astute,{w} how bad could it be?"

    play sound "audio/sfx/item_got.ogg"
    show HF
    pause 1.0
    "{i}Jonathan has picked up HF! (hydrofluoric acid){/i}"
    scene black with fade
    pause 1.0
    "So,{w} I took the barrel of acid and moved out of the building."
    stop music fadeout 1.0
    "I was planning my next stop when I was surprised with the arrival of…{w} {b}something new.{/b}"
    "A new face, to be more specific."
    play music "audio/music/Ennio Morricone - The Thing.wav"
    pause 1.0
    scene CarsonEntrance with fade
    "The vision of a man standing next to my beloved vehicle came to me along with the feeling of insertion.{w} A abnormal chill at the back of my head."
    "He was standing blankly at the window,{w} looking at insides of the car with intentions beyond the idea of appreciate its beauty."
    scene JvC with fade
    "When our eyes met,{w} I immediately knew that this unfortunate bastard wouldn't cause nothing but trouble."
    "And without more choices but facing the inevitable, I approached him for confrontation."
    scene black with fade
    pause 1.0
    scene car0 with fade
    UnCarson "A nice model, partner.{w} You can easily tell it was made on the glory of our beloved country."
    "His voice and smile were prideful,{w} lacking of harmful intentions,{w} but the suspicion on his eyes revealed something different."
    scene car1 with fade
    show Johnny R at left
    show Carson 2 at right
    Johnny "Can I help you?{w} Brother?"
    hide Carson
    show Carson 4 at right
    UnCarson "That’s a nice barrel you have there…"
    hide Carson
    show Carson 1 at right
    extend " A chemistry fan, perhaps?"
    hide Johnny
    show Johnny chat1 R at left
    hide Carson
    show Carson 5 at right
    Johnny "We can say so.{w} I have a couple of bad weeds back in home.{w} They’re a whole problem, but this beauty just burns them like nothing."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "The sad part is that, no matter how much you try to get rid of them, they always find their way back."
    hide Carson
    show Carson 1 at right
    hide Johnny
    show Johnny serious2 R at left
    UnCarson "I can’t be more on agreement with that, {b}Mr. Paddle{/b}."
    UnCarson "A clean garden is a pride for our beloved country.{w} Its beauty demonstrates the purity of this land,{w} and the commitment of its people."
    Johnny "Uh…{w} Yeah…"
    hide Johnny
    show Johnny chat1 R at left
    Johnny "I couldn’t avoid to notice that you know me."
    hide Johnny
    show Johnny smile2 R at left
    extend "The pleasure is all yours,{w} I assume presentations aren’t necessary."
    hide Carson
    show Carson 4 at right
    hide Johnny
    show Johnny confused R at left
    "He extended his presentation card without giving me a chance to reject."
    hide Carson
    show Carson 1 at right
    Carson "Carson Hasstle,{w} just a noble instrument of this gorgeous society."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "P.I?"
    hide Johnny
    show Johnny chat1 R at left
    Johnny "Oh, what a surprise…{w} What brings you to my city?{w} I can tell that you’re another dream-chaser, I respect that."
    hide Carson
    show Carson 2 at right
    hide Johnny
    show Johnny serious1 R at left
    "I didn't take my eyes off of him for even an instant...{w} and he did the same."
    hide Carson
    show Carson 3 at right
    hide Johnny
    show Johnny R at left
    Carson "Far from that, my estimated."
    Carson "As I said, I only serve the well-intentioned wings of this country.{w} If something’s dirtying it,{w} then I’m here to clean it up."
    hide Carson
    show Carson 2 at right
    hide Johnny
    show Johnny confused R at left
    stop music fadeout 1.5
    Carson "Which takes me back to…"
    hide Johnny
    show Johnny serious1 R at left
    "He pointed at the rear window of the car.{w} I...{w} I may have stained it with my fingertips when I was moving the officer last night..."
    play music "audio/music/Cruel Summer ost.wav" fadein 1.5
    hide Johnny
    show Johnny angry1 R at left
    hide Carson
    show Carson 1 at right
    "The drops of blood were barely noticeable."
    "You would need to have seen them a couple of times before to actually notice."
    pause 1.0
    Carson "You should take care of that."
    pause 1.0
    Johnny "Yeah…{w} I was a little busy lately...{w}"
    hide Johnny
    show Johnny chat1 R at left
    Johnny "You see, I have something bit within hands, and I can’t lose much time on cat-laundries."
    hide Johnny
    show Johnny angry2 R at left
    hide Carson
    show Carson 3 at right
    Carson "A man dedicated to his dream…"
    Carson "I like your kind, Mr. Paddle.{w} I really do…"
    hide Carson
    show Carson 4 at right
    Carson "The problem is that,{w} when you spend so much time on them,{w} you tend to make some mistakes in the present..."
    hide Carson
    show Carson 1 at right
    hide Johnny
    show Johnny angry1 R at left
    Carson "Do you understand what I'm saying, Mr. Paddle?"
    pause 1.0
    Johnny "..."
    pause 1.0
    hide Johnny
    show Johnny chat1 R at left
    Johnny "I’m afraid I don’t, Carson.{w} Because I NEVER make mistakes."
    hide Johnny
    show Johnny serious1 R at left
    hide Carson
    show Carson 5 at right
    Johnny "And I would love to stay here and chit-chat about the national construction,{w} but I need to move on."
    hide Carson
    show Carson 3 at right
    Carson "I see...{w} So I'm not entertaining you any longer.{w} And since we are at it,{w} I’m in the same road right now."
    scene car0 with fade
    Carson "Hopefully we’ll meet again, Mr. Paddle…{w} You seem like a reasonable guy,{w} and I would {b}really{/b} enjoy a second talk."
    stop music fadeout 1.5
    scene black with fade
    "In an instant,{w} his tone turned shady and way more serious that it was a moment ago."
    Carson "Are you?{w} A reasonable guy?"
    pause 0.5
    play sound "audio/sfx/Steps stone.wav"
    pause 2.5
    "For your sake, it will be better if that second talk never happen..."

    pause 0.5
    play music "audio/sfx/car turning on.wav"
    pause 2.0
    "Who the hell does he think he is?"
    play music "audio/music/Cruel Summer tense.wav"
    "Such a nerves he had to even think about coming to my territory,{w} to look into my car,{w} to see me with those…{w} those donkey eyes…"
    "He probably thought he was worth more than a rusted penny."
    "Wanted to play mysterious and all elegant, ha!"
    pause 1.5
    "Everyone’s a macho-man till a cockroach flies.{w} I’m pretty sure he would piss himself with just that.{w} I can't even help to laugh at the thought."
    "That would be worth to watch…"
    pause 2.0
    "Still…{w} Got to admit that left me a little uneasy."
    "I don't like that... not at all."
    "Did he see through me?{w} It surely seemed like that, but..."
    pause 1.0
    "Can you believe that?{w} I didn’t even realized until…{w} until I stopped to write this…"
    "Huh…"
    pause 1.5
    "Anyway...{w} better not lose our time with that for now."
    "There will be a special moment for Mr. Blondecai.{w} I'm really sure of that."
    stop music fadeout 1.5
    "But for now,{w} I must move on."
    pause 3.0
    play music "audio/music/Bananarama - Cruel Summer.wav"
    pause 2.0
    scene city1 with fade
    "I drove towards the residential area of the city,{w} a small neighbor filled with hundreds of ugly and noisy houses."
    "This kinds of places are very annoying,{w} always so full of unbearable old people, dirty children and neglected animals."
    "Sadly, it's also where the majority of messed up things happen.{w} Not so surprising, to be honest."
    "Who wouldn’t become crazy when living in a place like this?"
    "I wouldn’t last a single day without putting an axe on the head of my neighbor."
    pause 1.5
    "…"
    "I don’t even have an axe, there’s the problem."
    scene car2 with fade
    "Anyway."
    "With the help of the names wrote on the notebook,{w} the number,{w} and a little chat with the neighbors,{w} I managed to reach my desired destination."
    "It's amazing how easily you can track a person."
    "Perfect for a psycho or someone like me…"
    pause 1.5
    "...a little redundant?{w} Yeah, maybe.{w} But I’m not making judgements here."
    scene black with fade
    "To my surprise,{w} the moment I made visual contact with the residence, I noticed the presence of a third party."
    scene Jul with fade
    "I saw a women standing right in the front door.{w}"
    "Long straight hair,{w} dressing fresh but with strangely thick arm sleeves."
    "Her figure had a strange feeling of…{w} innocence, I suppose?{w} Her posture didn't help her at all, that's for sure."
    "She looked like the kind of person who would be first on some serial killer's list."
    scene black with fade
    play sound "audio/sfx/car door.wav"
    pause 2.0
    "This was my first encounter with her."
    "Her yellow eyes pointed at me the moment I stood out of the car, and her delicate fingers crossed within each other with palpable nerves."
    "From that mere gleam, I could assume she wasn’t related with the siblings.{w} Not directly at least."
    scene HouseOut with fade
    show Johnny chat1 R at left
    show Julia at right
    Johnny "Morning, miss."
    Johnny "Is this the house of the Graves family?{w} I would need to have a little talk with them."
    hide Johnny
    hide Julia
    show Johnny smile1 R at left
    show Julia chat2 at right
    UnJulia "Eh?{w} Y-Yes, Miss and Mr Graves lives here…"
    UnJulia "But they’ve been pretty absent lately, so I don't know if..."
    hide Johnny
    hide Julia
    show Johnny serious1 R at left
    show Julia down at right
    Johnny "How absent?"
    hide Julia
    show Julia chat2 at right
    UnJulia "W-Well…{w} They haven’t answered the door in… "
    hide Julia
    show Julia at right
    extend "a couple of days, actually."
    hide Johnny
    show Johnny serious2 R at left
    "A couple of days, huh?"
    "Something’s telling me that I know where the shoots are going."
    hide Julia
    show Julia sad at right
    UnJulia "Maybe it's just that they don't want to talk to me...{w} I wouldn't blame them..."
    hide Johnny
    show Johnny smile1 R at left
    Johnny "Yeah, probably.{w} Excuse me one second..."
    hide Johnny
    show Johnny at left
    play sound "audio/sfx/Steps grass.wav"
    hide Johnny with moveoutleft
    pause 1.5
    UnJulia "..."
    UnJulia "You see...{w} they probably hate me at this point."
    UnJulia "I shouldn't even be here..."
    Johnny "Keep talking, dear!{w} I'm listening."
    play sound "audio/sfx/item_got.ogg"
    items "{i}Jonathan has picked up Human Resources (his shovel) from the back into the car!{/i}"
    Johnny "Mind telling me your name, miss?"
    hide Julia
    show Julia chat2 at right
    UnJulia "Oh, it’s Julia. Julia [[REDACTED].{w} I'm sorry I didn't mention it."
    hide Julia
    show Julia down at right
    "I picked the name almost immediately.{w} She appeared on the notebook’s list."
    hide Julia
    show Julia at right
    Johnny "Johnny Paddle, P.I."
    Johnny "If there’s a problem..."
    play sound "audio/sfx/whip.wav"
    pause 1.0
    Johnny "Better call me~"
    play sound "audio/sfx/Steps grass.wav"
    hide Johnny
    show Johnny shovel at left with moveinleft
    pause 1.0
    hide Julia
    show Julia at right
    stop music fadeout 1.0
    Julia "..."
    pause 0.5
    hide Julia
    show Julia chat1 at right
    Julia "You mean, you’re a detective?{w} Did something happen with Mr. and Mrs. Graves?"
    scene FrontDoor with fade
    pause 0.5
    Julia "W-Wait…{w} W-What are you doing?{w} Is that a...{nw}"
    scene DoorOpening
    play sound "audio/sfx/Door Kick Down Break.wav"
    pause 1.0
    "I sank the tip of the shovel between the bolt and the frame before she could say another word."
    scene OpenFrontDoor
    play sound "audio/sfx/Door Kick Down Break.wav"
    pause 1.0
    "It required much less strength that I expected to get through it.{w} With a slight push, the door swung open."
    scene black with fade
    play sound "audio/sfx/Steps wood.wav"
    pause 1.5
    scene HouseIn1 with fade
    show Johnny chat1 R at center
    Johnny "Knock knock!{w} Anyone’s home?!"
    hide Johnny
    show Johnny smile1 R at center
    pause 3.0
    play music "audio/music/The Thing - What Appears to be Normal.wav"
    Johnny "Huh... {w}No answers.{w} Who would have guessed?"
    hide Johnny
    show Johnny serious1 R at center
    "The moment I stepped into the house, I was received by two things.{w} An echo as deep and rumbling as the one you would find in caves..."
    "...and a putrid odor that resembled the tunnels of a sewer."
    "Besides that, only silence."
    show Julia giggle R at left with moveinleft
    Julia "What have you done?!"
    Julia "You…"
    hide Julia
    show Julia ewww at left
    Julia "EWWWWWWWW!!!"
    hide Johnny
    show Johnny chat1 at center
    Johnny "Cover your nose, dear."
    hide Johnny
    show Johnny smile2 at center
    Julia "What's that smell?"
    hide Johnny
    show Johnny chat1 at center
    Johnny "The smell of the {b}adventure{/b}, off course."
    hide Johnny
    show Johnny R at center
    extend " And here is where my work begins."
    Johnny "You coming?"
    hide Julia
    show Julia giggle R at left
    Julia "W-What?!{w} You can’t be serious!"
    hide Julia
    show Julia nervous R at left
    hide Johnny
    show Johnny at center
    Johnny "No, I’m actually pretty serious.{w} I've come for answers, and I ain't going anywhere without them."
    hide Johnny
    show Johnny chat1 at center
    Johnny "So, what do you say, cutie?{w} You come in for a ride or run away like a little rabbit?"
    hide Johnny
    show Johnny serious2 at center
    hide Julia
    show Julia angry R at left
    Julia "Don't call me that!"
    Julia "I..."
    hide Julia
    show Julia down R at left
    Julia "..."
    pause 2.0
    Julia "We can’t just get inside Mrs. Graves house without their permission..."
    hide Johnny
    show Johnny smug2 at center
    hide Julia
    show Julia R at left
    "That was adorable."
    hide Julia
    show Julia sad R at left
    "I tried my best to suppress a chuckle, but it wasn’t hard for her to notice."
    Julia "Don’t laugh, I’m being serious..."
    hide Julia
    show Julia nervous R at left
    Julia "Can you at least tell me why you’re here?"
    hide Johnny
    show Johnny chat1 at center
    Johnny "Well, that answer comes with another question."
    hide Johnny
    show Johnny serious1 at center
    Johnny "The names {nw}"
    hide Julia
    show Julia sad R at left
    extend "{b}Ashley{/b} and {b}Andrew{/b} are somehow familiar to you?"
    "At that moment, her heart skipped a beat.{w} A wave of discomfort washed her whole body, as if the mere mention of their names brought with it a storm of emotions."
    Julia "..."
    Julia "We had some story..."
    hide Johnny
    show Johnny serious2 at center
    Johnny "How much?"
    Johnny "Are you their friend?{w} Cousin?{w} Maybe even…{nw}"
    hide Johnny
    show Johnny confused at center
    hide Julia
    show Julia R at left
    Julia "I was Andrew’s girlfriend."
    hide Johnny
    show Johnny smug1 at center
    "Look what a cute little thing we found here…"
    hide Johnny
    show Johnny chat1 at center
    Johnny "I see…{w} the emo-boy."
    Johnny "I respect that, could never say no to a cold one neither."
    hide Johnny
    show Johnny serious1 at center
    hide Julia
    show Julia down R at left
    "Her eyes looked away."
    "Her expression changed without giving further explanations.{w} The nerves were substituted by a strong sense of sadness, regret, maybe even doubt."
    hide Julia
    show Julia sad R at left
    "But that wasn’t the only."
    "There was a lot of repressed feelings in those eyes…{w} yeah, I could sense them.{w}"
    hide Julia
    show Julia serious1 R at left
    "Fear, anger, desperation, loneliness…{w} betrayal."
    "That expression was a known one...{w} a very known I would say."
    hide Johnny
    show Johnny angry1 at center
    Johnny "They hurt you."
    hide Julia
    show Julia down R at left
    Julia "..."
    pause 1.5
    hide Julia
    show Julia R at left
    Julia "It's complicated...{w} Would rather not talk about it."
    hide Julia
    show Julia sad at left
    "I saw potential on that girl."
    "She could be a very valuable asset,{w} someone I could use to get thought that guy."
    "There was something she wasn’t telling me…{w} it could come in handy.{w} Could use it on my favor."
    pause 1.5
    hide Johnny
    show Johnny sigh at center
    "But…"
    pause 1.0
    "What if I…"
    pause 1.0
    hide Johnny
    show Johnny confused at center
    "What if she..."
    pause 2.0
    hide Johnny
    show Johnny angry2 at center
    "No...{w}"
    "No, that’s a dumb idea..."
    "How to trust someone like her?"
    "Someone weak,{w} so naive,{w} so stupid,{w} so easy to…"
    stop music fadeout 1.0

    ###################################### JULIA CHOICES

    menu:
        "..."

        "Honesty":
            jump Honesty
        "Fraudulence":
            jump Fraudulence

    label Honesty:
        hide Johnny
        show Johnny sigh at center
        Johnny "Listen…"
        "I swear, I can’t believe I did this…"
        hide Johnny
        show Johnny at center
        Johnny "He isn’t gone."
        hide Julia
        show Julia R at left
        pause 1.5
        Julia "W-Who?"
        Julia "Who isn’t gone?"
        pause 1.5
        hide Johnny
        show Johnny serious2 at center
        Johnny "Your boyfriend."
        Johnny "He’s alive."
        hide Julia
        show Julia down R at left
        play music "audio/music/Radiohead — Exit Music.wav"
        pause 2.0
        "Those words took a good of a moment to sink."
        hide Julia
        show Julia R at left
        Julia "You’re lying…"
        hide Julia
        show Julia nervous R at left
        Julia "I saw it on the news.{w} The building set on fire and—{nw}"
        hide Johnny
        show Johnny serious1 at center
        Johnny "The building burned down, there’s nothing but ashes there."
        Johnny "But your boyfriend and her sister are alive.{w} I know because I spoke with them…{w} {b}in person{/b}."
        hide Julia
        show Julia down R at left
        "This time,{w} a different look appeared."
        hide Julia
        show Julia smile R at left
        "I could see the relief on her gaze,{w} a small yet glowing spark of hope coming from her deepest soul."
        hide Johnny
        show Johnny serious2 at center
        hide Julia
        show Julia serious1 R at left
        "However, the confusion and fear were still there."
        Julia "I can’t believe this..."
        hide Julia
        show Julia nervous R at left
        Julia "It’s impossible, he…"
        hide Julia
        show Julia sad R at left
        pause 1.5
        Julia "I-I want to talk to him."
        Julia "How can I—{nw}"
        hide Johnny
        show Johnny angry1 at center
        hide Julia
        show Julia R at left
        Johnny "No."
        "The moment that thought left her lips, I knew I had to stop her."
        hide Johnny
        show Johnny angry2 at center
        Johnny "I can’t let you put a step near him.{w} You could compromise everything."
        hide Julia
        show Julia chat1 R at left
        Julia "B-But…{nw}"
        hide Julia
        show Julia R at left
        hide Johnny
        show Johnny angry1 at center
        Johnny "First of all,{w} I don’t even know where they’re staying.{w} And second…{w} because that boy and his sister are in something shady."
        hide Johnny
        show Johnny serious1 at center
        Johnny "I can’t tell you what,{w} I can’t tell you why,{w} but since you’re still here…"
        pause 1.5
        hide Johnny
        show Johnny sigh at center
        Johnny"I guess you could help me investigate the house."
        Johnny "Who knows…{w} maybe we could find something."
        hide Johnny
        show Johnny serious2 at center
        hide Julia
        show Julia sad R at left
        Julia "..."
        hide Julia
        show Julia R at left
        Julia "No..."
        hide Julia
        show Julia chat1 R at left
        extend" I-I can’t believe that, not without proofs!"
        hide Julia
        show Julia R at left
        hide Johnny
        show Johnny sigh at center
        Johnny "That's also something I can't give you. And you don’t need to believe it if you don't want."
        hide Johnny
        show Johnny at center
        Johnny "But that’s the truth, deary.{w} Take it or leave it."
        hide Julia
        show Julia sad R at left
        Julia "..."
        Julia "Are you gonna arrest him?"
        Julia "I-I don’t want anything to happen to Andrew…"
        hide Johnny
        show Johnny sigh at center
        "Dear god…"
        "I knew this would come out."
        "Great job, Paddle…"
        Johnny "It's...{w} complicated."
        hide Johnny
        show Johnny at center
        Johnny "Look, I can’t point my finger and say that he killed someone,"
        hide Johnny
        show Johnny serious1 at center
        extend " but I do have a couple of theories about it."
        hide Julia
        show Julia R at left
        Johnny "Still, that doesn’t necessarily point him as the villain of the story."
        hide Julia
        show Julia serious1 R at left
        pause 1.0
        Julia "Is there a possibility that someone could be incriminating him?{w} Or maybe…{w} {b}manipulating{/b}?"
        hide Johnny
        show Johnny serious2 at center
        hide Julia
        show Julia R at left
        Johnny "I never said that."
        Johnny "But if you have something that could indicate it…"
        hide Julia
        show Julia serious1 R at left
        "She thought about it for a long moment.{w} The contemplation of the scenario made her lost in the idea."
        hide Johnny
        show Johnny angry1 at center
        "I should’ve lied to her.{w} This could’ve been much easier,{w} but for some…{w} bullshit reason I wasn’t able to allow myself."
        "I don’t know what happened to me…"
        hide Johnny
        show Johnny sigh at center
        "Uuuuhh..."
        Julia "If I help you… "
        hide Julia
        show Julia R at left
        hide Johnny
        show Johnny confused at center
        extend "will you tell me more about Andrew?"
        hide Julia
        show Julia sad R at left
        Julia "He…{w} He’s really special to me,{w} even if we're nothing now."
        hide Johnny
        show Johnny sigh at center
        Johnny "You complicate my life, dear."
        pause 1.5
        hide Johnny
        show Johnny chat1 at center
        hide Julia
        show Julia smile R at left
        Johnny "Deal!"
        hide Johnny
        show Johnny smile2 at center
        "Those words returned a resolution I wasn’t expecting."
        hide Johnny
        show Johnny confused at center
        hide Julia
        show Julia happy R at left
        "There weren’t doubts not any kind of nerves on her voice."
        hide Johnny
        show Johnny serious1 at center
        "She was just… completely decided to help."
        pause 1.5
        "Why?"
        stop music fadeout 1.0
        scene black with fade
        Johnny "All right…{w} Let's start searching."
        Johnny "And if someone appears, not a single word."
        Johnny "Got it?"
        Julia "Yes, detective..."
        Johnny "Johnny is fine, deary…"
        play sound "audio/sfx/whip.wav"
        pause 0.7
        Johnny "Handsome Johnny~"
        Julia "Y-Yeah, I-I think Johnny it’s fine…"
        Johnny "You ain’t funny."
        jump main_route4


    label Fraudulence:
        hide Johnny
        show Johnny serious1 at center
        Johnny "Oh..."
        Johnny "He was a good one, wasn't?"
        play music "audio/music/Cruel Summer Tense.wav" fadein 1.0
        pause 1.5
        Julia "Andrew and I…{w} We had our differences."
        pause 1.5
        hide Julia
        show Julia R at left
        Julia "We had our problems, some more serious than others."
        hide Julia
        show Julia down R at left
        Julia "I was so overwhelmed at that time so...{w} a week before the incident, I called him and…"
        hide Julia
        show Julia sad R at left
        pause 1.5
        Julia "I broke up with him."
        hide Johnny
        show Johnny chat1 at center
        Johnny "Problems in heaven, huh?"
        Johnny "Yeah, I know how it is…{w} My first girlfriend tried to stab me with a spoon."
        hide Johnny
        show Johnny smug2 at center
        Julia "With…"
        hide Julia
        show Julia R at left
        extend "With a spoon?"
        hide Johnny
        show Johnny chat1 at center
        Johnny "She was such a sweetheart..."
        hide Johnny
        show Johnny at center
        Johnny "Sadly, she also had this little {b}personality{/b} problem."
        Johnny "We could be making up an instant and next she would try to choke me to death."
        hide Johnny
        show Johnny angry1 at center
        Johnny "Was your boy something like that?"
        hide Julia
        show Julia nervous R at left
        Julia "N-No!{w} Off course not!"
        hide Julia
        show Julia angry R at left
        Julia "He had other problems..."
        hide Julia
        show Julia down R at left
        hide Johnny
        show Johnny serious1 at center
        extend " like anyone else..."
        hide Julia
        show Julia angry R at left
        Julia "But he wouldn't hurt a fly!"
        hide Julia
        show Julia sad R at left
        pause 2.0
        Julia "I...{w} I hope so..."
        pause 1.0
        Johnny "Yeah..."
        pause 1.0
        hide Julia
        show Julia R at left
        hide Johnny
        show Johnny chat1 at center
        Johnny "Anyway, that’s aside."
        hide Johnny
        show Johnny serious1 at center
        Johnny "I understand the pain you’re dealing with right now.{w} I’ve seen a lot of people losing their love ones, and I’ve lost mine too."
        Johnny "Said this, you have to know that I am being completely honest when I say..."
        hide Johnny
        show Johnny angry1 at center
        extend " I am truly sorry."
        hide Julia
        show Julia down R at left
        pause 1.5
        hide Johnny
        show Johnny serious2 at center
        Julia "T-Thank you…{w} I appreciate your condolences."
        hide Julia
        show Julia sad R at left
        Julia "From the deep of my heart,{w} I really hope there was something I could do."
        hide Julia
        show Julia R at left
        hide Johnny
        show Johnny at center
        Johnny "There is something, actually."
        "I lowered my tone while getting a little closer."
        hide Johnny
        show Johnny serious1 at center
        Johnny "But before anything,{w} I want to know if I can trust you."
        hide Johnny
        show Johnny angry1 at center
        extend " That you’re not going to say a {b}single word{/b} from what I'm going to tell you."
        hide Julia
        show Julia nervous R at left
        Johnny "Can you make that promise?"
        hide Julia
        show Julia chat2 R at left
        Julia "I..."
        hide Julia
        show Julia down R at left
        pause 1.5
        Julia "Yes."
        Julia "I swear I won't say a single word."
        pause 0.5
        Johnny "Ok."
        hide Johnny
        show Johnny serious1 at center
        extend " In that case..."
        pause 1.0
        Johnny "Andrew and Ashley didn’t die from an accident."
        stop music
        Johnny "They were killed."
        pause 1.0
        hide Julia
        show Julia R at left
        pause 2.0
        Julia "W-What?"
        play music "audio/music/Ennio Morricone - The Thing.wav" fadein 1.0
        hide Johnny
        show Johnny at center
        Johnny "What you just heard."
        pause 1.0
        hide Johnny
        show Johnny serious2 at center
        Johnny "I found their bodies in the investigation of a similar case.{w} They were lying in a mass grave on the outskirts of the city,{w} {b}in the woods{/b}."
        hide Julia
        show Julia nervous R at left
        hide Johnny
        show Johnny angry1 at center
        Johnny "I'm sorry for what I'm about to say but... {w}They were on a terrible,{w} {b}terrible{/b} state…"
        hide Julia
        show Julia sad R at left
        hide Johnny
        show Johnny serious1 at center
        Johnny "I also found a couple of things on their belongings.{w} Among them,{w} a {b}notepad{/b} with telephone numbers."
        Johnny "That’s how I got here."
        pause 2.0
        Julia "Who…{w} who did this?"
        hide Julia
        show Julia R at left
        Julia "Why?"
        Julia "Does the police know?"
        hide Julia
        show Julia angry R at left
        Julia "Why is nobody talking about it!"
        hide Johnny
        show Johnny at center
        hide Julia
        show Julia R at left
        Johnny "Calm down, please..."
        pause 1.0
        Johnny "The police know, but...{w} They're compromised."
        Julia "W-What do you mean by that?"
        hide Johnny
        show Johnny angry1 at center
        Johnny "You need to know something, Julia.{w} This is way bigger than you think."
        Johnny "I can't explain it to you right now, but there's a lot moving in the background."
        hide Johnny
        show Johnny serious1 at center
        hide Julia
        show Julia nervous R at left
        Johnny "And sadly,{w} Andrew and Ashley got caught in the middle."
        hide Julia
        show Julia sad R at left
        "This answers destroyed her.{w} I could feel the pain flowing though her veins — the sadness and repentance on her eyes."
        "I thought she was about to explode at any moment, but..."
        Julia "I…{w} want to help…"
        hide Julia
        show Julia nervous R at left
        Julia "I need to help you on this, Mr. Paddle."
        hide Johnny
        show Johnny at center
        Johnny "I'm afraid you're not understanding the scope of this."
        Johnny "It’s a very dangerous situation, girl.{w} You may not like what—{nw}"
        hide Johnny
        show Johnny confused at center
        hide Julia
        show Julia angry R at left
        Julia "I DON’T CARE!"
        hide Julia
        show Julia R at left
        hide Johnny
        show Johnny serious1 at center
        Julia "I…"
        hide Julia
        show Julia nervous R at left
        pause 1.5
        Julia "I want justice for Andrew…"
        hide Julia
        show Julia chat1 R at left
        Julia "I want them exposed to the world."
        hide Julia
        show Julia sad R at left
        Julia "Please…{w} let me help with this."
        "Perfect, "
        hide Johnny
        show Johnny smug1 at center
        extend "just where I wanted her."
        scene black with fade
        "She was angry,{w} blinded by her emotions."
        "Her blood boiled with resentment.{w} She wanted revenge, and who was I to deny such a thing to a spiteful girl?"
        "I would have to move the pieces a little bit, but…{w} I saw myself able to maintain this."
        pause 1.0
        Johnny "All right then, miss Julia. You have my word… We’re gonna put those bastards down."
        pause 1.0
        Julia "T-Thank you... Mr. Paddle..."
        Johnny "Please,{w} call me Johnny."
        jump main_route4

    ###################################### JULIA CHOICES END


    label main_route4:
    pause 2.5
    "So,{w} more people means more space to cover."
    play music "audio/music/Delay.wav" fadein 1.0
    pause 1.5
    "Even if I’m not the “teamwork” kind of guy, I do know how to appreciate a little extra help."
    "Said this, the first thing to do was a bit obvious."
    scene HouseIn2 with fade
    show Johnny chat1 at right
    show Julia R at left
    Johnny "All right, Jennifer."
    hide Julia
    show Julia down R at left
    hide Johnny
    show Johnny smile1 at right
    Julia "It’s Julia..."
    Johnny "Julia, off course, that’s what I said."
    hide Johnny
    show Johnny chat1 at right
    Johnny "I'm going to need you to help me investigate the house.{w} Look for something that catches your attention in a bad way."
    hide Julia
    show Julia R at left
    hide Johnny
    show Johnny smile1 at right
    Julia "L-Like…{w} what,{w} exactly?"
    hide Johnny
    show Johnny serious1 at right
    Johnny "Documents,{w} blood,{w} passports,{w} bones,{w} whatever you could find that may seem out of place."
    hide Julia
    show Julia down R at left
    hide Johnny
    show Johnny chat1 at right
    Johnny "Come on, you'll notice immediately."
    hide Johnny
    show Johnny at right
    hide Julia
    show Julia chat1 R at left
    Julia "Mr. Paddle…"
    hide Julia
    show Julia chat2 R at left
    Julia "I-I mean, Johnny."
    hide Julia
    show Julia chat1 R at left
    Julia "Mr. and Miss. Graves are a very peculiar kind of…"
    hide Julia
    show Julia R at left
    pause 1.0
    Julia "D-Did you just said blood and bones?"
    hide Johnny
    show Johnny serious1 at right
    Johnny "Well yeah,{w} documents, blood, passports, bones and out of place stuff."
    hide Johnny
    show Johnny at right
    Johnny "I thought I was clear."
    hide Julia
    show Julia chat2 R at left
    Julia "B-B-But are you implying that Mr. and Miss. Graves may be…"
    hide Julia
    show Julia R at left
    hide Johnny
    show Johnny chat1 at right
    Johnny "At the doors of Saint Peter?{w} Well, it’s a possibility."
    hide Johnny
    show Johnny serious2 at right
    Johnny "I don’t see them here,{w} and you said they haven’t answered the door in days,{w} so I think there’s a good chance for that."
    hide Johnny
    show Johnny chat1 at right
    hide Julia
    show Julia nervous R at left
    Johnny "Said this, if you find one or two corpses just try searching for clues."
    hide Johnny
    show Johnny confused at right
    hide Julia
    show Julia scream R at left
    Julia "I don’t want to touch a dead body!"
    hide Johnny
    show Johnny at right
    hide Julia
    show Julia nervous R at left
    Johnny "What?{w} You…"
    hide Johnny
    show Johnny sigh at right
    hide Julia
    show Julia sad R at left
    Johnny "uuuhh…{w} fine."
    Johnny "Just call me and I’ll touch what needs to be touched."
    hide Julia
    show Julia scream R at left
    Julia "Why did you say it like that?!"
    hide Julia
    show Julia nervous R at left
    hide Johnny
    show Johnny confused at right
    Johnny "How do you want me to say it?"
    hide Johnny
    show Johnny serious1 at right
    Johnny "Just…{w} Walk around and scream if you see something."
    hide Julia
    show Julia sad R at left
    Julia "Oh jeez…"
    hide Julia
    show Julia at left
    hide Julia with moveoutleft
    extend "I don’t like any of this…"
    hide Johnny
    show Johnny sigh at right
    "She may not be as useful as I thought…"
    "Action clearly aren’t her strength."
    hide Johnny
    show Johnny at right
    "Anyway.{w} Let’s hope Miss Lettuce doesn’t faint because of a mouse, and begin to work."
    ""


    menu:
        "..."

        "Salir?":
            return
        "Salir!":
            return


    # This ends the game.

    return
