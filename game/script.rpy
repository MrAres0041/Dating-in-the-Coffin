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
image Forest5 = "images/bgs/Forest5.png"
image LabOut = "images/bgs/LabOut.png"
image Lab1 = "images/bgs/Lab1.png"
image car0 = "images/bgs/car0.png"
image car1 = "images/bgs/car1.png"
image car2 = "images/bgs/car2.png"
image car3 = "images/bgs/car3.png"
image city1 = "images/bgs/ciity1.png"
image Jul = "images/bgs/Jul.png"
image HouseOut = "images/bgs/HouseOut.png"
image DoorOpening = "images/bgs/DoorOpening.png"
image FrontDoor = "images/bgs/FrontDoor.png"
image OpenFrontDoor = "images/bgs/OpenFrontDoor.png"
image HouseIn1 = "images/bgs/HouseIn1.png"
image HouseIn2 = "images/bgs/HouseIn2.png"
image V_Patch = "images/bgs/vegetable_patch.png"
image Ash1 = "images/bgs/Ash1.png"
image Ash2 = "images/bgs/Ash2.png"
image end2 = "images/bgs/TGC2.png"
image seriously = "images/bgs/Serious.png"




image start1 = "images/bgs/Encounter Zero.png"
image start2 = "images/bgs/First Encounter.png"



# Polaroids


image Pol4 = "images/polaroids/Pol4.png"
image Pol5 = "images/polaroids/Pol5.png"
image Pol6 = "images/polaroids/Pol6.png"
image Pol7 = "images/polaroids/Pol7.png"
image Pol8 = "images/polaroids/Pol8.png"
image Pol9 = "images/polaroids/Pol9.png"
image Pol10 = "images/polaroids/Pol10.png"
image Pol11 = "images/polaroids/Pol11.png"
image Pol12 = "images/polaroids/Pol12.png"
image JvC1 = "images/polaroids/C2.png"
image JvC2 = "images/polaroids/C3.png"
image JvC3 = "images/polaroids/C4.png"



# Items
image shovel ="images/objects/Shovel.png"
image butcher ="images/objects/butcher.png"
image sodas = "images/objects/soda.png"
image notepad = "images/objects/notepad.png"
image keys = "images/objects/keys.png"
image HF = "images/objects/HF.png"
image photo = "images/objects/photo.png"
image bones = "images/objects/bones.png"


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
define Who = Character("???", what_prefix='{i}"', what_suffix='"', color="#404040")



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
image Ashley excited = "images/sprites/Ashley/A_17.png"
image Ashley tired = "images/sprites/Ashley/A_18.png"
image Ashley worried3 = "images/sprites/Ashley/A_19.png"



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
image Andrew confused2 = "images/sprites/Andrew/An_17.png"

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
image Lars 7 = "images/sprites/Others/L7.png"


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
    pause 2.0
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
    "Nothing special at first instance."
    "People get their vehicles stolen every day,{w} and usually those corrupt pigs from the department always find excuses to keep them for themselves."
    "This off course, in case they find them in the first place..."
    scene office with fade
    "That’s why,{w} instead of going straight to the police as would be logical anywhere else,{w} people prefers to call someone special…"
    "Someone…"
    show Johnny P
    play sound "audio/sfx/Whip.wav"
    pause 1.0
    "...like me~"
    play sound "audio/sfx/Whip.wav"
    hide Johnny P
    show Johnny P2
    "If there's a problem,{w} better call me~"
    play sound "audio/sfx/Whip.wav"
    hide Johnny P2
    show Johnny smile2
    "A strong,{w} intelligent,{w} and seductive man who's more than capable of solving their problems."
    "And also..."
    hide Johnny smile2
    show Johnny sigh
    stop music
    play sound "audio/sfx/scratch.wav"
    items "Is broke as fuck..."
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
    pause 1.5
    play music "audio/music/Bananarama - Cruel Summer sing.wav" fadein 1.0
    items "Gotta admit one thing,{w} things have gotten easier lately."
    scene car0 with fade
    "A lot of calls,{w} a lot of work,{w} a lot of things that keep me going."
    "Bad for the people?{w} Yeah,{w} but good for me."
    "A double win I would say."
    "I’ve been living in that old, rotten cabin for…{w} a while."
    "I totally need to get out of that bloody mouse hole."
    scene drive with fade
    pause 1.0
    "Looking through the window, I met with the silhouette of the city drawn over the horizon."
    "The rumble of the cars and the echo of people yelling at each other’s started to fill my ears."
    "Its disgusting,{w} putrid smell is something that torments me every time I put a step on this circus."
    "And the faces...{w} The ones from those who mask their truths under smiles as empty as their heads."
    scene black with fade
    Johnny "Uh...{w} Repulsive…"
    "But that’s ok."
    pause 1.0
    "It shouldn't even bother me."
    "After all... I'm not like them."
    "I'm smarter,{w} more attractive,{w} and above all, much more honest than any of them."
    pause 0.5
    Johnny "Just smile and wave, Paddle...{w} Just smile and wave."
    scene car0 with fade
    "Once I get enough money for a new apartment,{w} I’ll be as far away as possible from this hell-hole."
    "And so,{w} I'll be able to live the life I deserve."
    scene black with fade
    pause 0.3
    Johnny "Sadly… {w} this case surely won't be the one to make my dream come true..."
    stop music fadeout 2.0
    pause 2.0
    scene motel1 with fade
    "I parked right in the crime zone."
    play music "audio/music/Delay.wav" fadein 2.0
    play sound "audio/sfx/car door.wav"
    pause 1.5
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
    "With this in mind, I began to work."
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
    "Taking into consideration the crime happened between the night and early morning,{w} it would be strange if someone had been present at that very moment."
    "In the best scenario,{w} the owners would be weirdos who have their alarms set for everything that happens in the neighborhood."
    "It happens way more often than you would expect..."
    Johnny "That’s left as an option for now."
    scene park with fade
    "At my right was the entrance to a public park."
    "A very frequented place."
    "Horny teenagers,{w} lurking perverts,{w} and lots of vagabonds {w}(usually a combination of both)."
    "There’s always somebody watching on these kinds of sites, so it was a clear choice."
    stop music fadeout 1.0
    scene black with fade
    "However..."
    "What I found in there wasn’t exactly what I was expecting at all...{w} not at all, actually."
    scene crime1 with fade
    "Behind a very remarkable police tape,{w} hide by the bushes and surrounded by men in blue uniforms,{w} was the cold and fetid corpse of a poor bastard."
    "A cloud of flies flew around the white blanket covering it.{w} They moved wildly in a vague attempt to find a minimum opening in the fabric."
    "It wasn't by any means something recent..."
    scene black with fade
    pause 1.0
    play music "audio/music/Magnum Force.wav" fadein 1.0
    "And off course,{w} this called my attention."
    scene crime2 with fade
    play sound "audio/sfx/Steps grass.wav"
    show Johnny at right
    with moveinright
    "Naturally, I approached the place with the intention of gathering some context."
    "But off course...{w} my intentions would be stopped by the arrival of a character in uniform."
    hide Johnny
    show Johnny confused at right
    Officer "Hey!!!"
    show Officer serious at left
    with moveinleft
    pause 1.0
    hide Johnny
    show Johnny sigh at right
    Johnny "Always...{w} Always a problem…"
    Officer "Problems is what you're looking for, opportunist."
    hide Officer
    show Officer at left
    Officer "Get out."
    Officer "This is a closed area,{w} and even more for people of your kind."
    hide Officer
    show Officer serious at left
    hide Johnny
    show Johnny serious1 at right
    Johnny "Of... my {b}kind{/b}?{w} I'll take that as a compliment..."
    hide Johnny
    show Johnny chat1 at right
    Johnny "Let me explain this to you, officer.{w} I'm not here to cause any trouble."
    hide Officer
    show Officer nervous1 at left
    hide Johnny
    show Johnny P at right
    play sound "audio/sfx/whip.wav"
    pause 1.0
    Johnny "Jonathan Paddle, PI."
    hide Johnny
    show Johnny P2 at right
    play sound "audio/sfx/whip.wav"
    pause 1.0
    Johnny "If there’s a problem,{w} better call me~"
    hide Johnny
    show Johnny confused at right
    hide Officer
    show Officer sigh1 at left
    Officer "Yeah, yeah...{w} I know you well, freak…"
    hide Officer
    show Officer serious at left
    Officer"You're the one who covered the agency's signs with those stupid advertising pamphlets."
    "Ups... thought nobody saw me..."
    hide Johnny
    show Johnny smile1 at right
    Johnny "Ehem…{w} yeah...{w} No hard vibes anyway, right?"
    hide Johnny
    show Johnny at right
    hide Officer
    show Officer indifferent at left
    Officer "Whatever…{w} Just go away, please."
    hide Officer
    show Officer nervous2 at left
    Officer "We're too busy already to deal with the delusions of an 80s fan."
    hide Officer
    show Officer chat at left
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
    show Officer sigh2 at left
    "Judging by his expression, we could assume that he didn't find my little joke to be amusing."
    hide Johnny
    show Johnny smug1 at right
    Officer "Whatever we're doing here is none of your business."
    Officer "I have a better idea,{w} why don't you go investigate the {b}who cares about your opinion{/b} case?"
    hide Johnny
    show Johnny chat1 at right
    hide Officer
    show Officer chat at left
    Johnny "Nah,{w} I looked into that last week."
    hide Officer
    show Officer sigh2 at left
    hide Johnny
    show Johnny smile1 at right
    Johnny "It was your mom~"
    hide Johnny
    show Johnny chat1 at right
    Johnny "But that's aside the point anyway."
    hide Johnny
    show Johnny smile2 at right
    hide Officer
    show Officer serious at left
    Johnny "The thing is, I’m just trying to do my job the same way you’re doing yours."
    Johnny "So why don't you step aside for me?"
    hide Johnny
    show Johnny at right
    hide Officer
    show Officer indifferent at left
    Officer "Becuase my job is not letting you do yours."
    hide Officer
    show Officer at left
    Officer "Is it that hard to understand?{w} Do I need to explain it with sticks and a blackboard?"
    hide Johnny
    show Johnny chat1 at right
    hide Officer
    show Officer serious at left
    Johnny "Look, pal.{w} I'm trying to be reasonable here."
    stop music fadeout 1.5
    hide Johnny
    show Johnny serious1 at right
    Johnny "I’m standing in the allowed zone.{w} So I can't see the reason why I wouldn't be able to stay."
    hide Officer
    show Officer sigh1 at left
    Officer "The reason is because I say so."
    hide Officer
    show Officer sigh2 at left
    Officer "You {b}CAN’T{/b} be here."
    hide Officer
    show Officer at left
    Officer "We have strict orders to not let anyone come closer.{w} Especially a fucking Larry Zito wanna be like you."
    hide Officer
    show Officer serious at left
    ################################### Police choice

    menu:
        "He was pretty serious about this so... I decided to answer with—"

        "Demureness":
            jump Demureness1
        "Indifference":
            jump Indifference1


    label Demureness1:
        $ PoliDemureness = True

        "Ignoring the warnings of the little man in blue, I decided to take a look at the corpse over his shoulder."
        "He wasn't that tall anyway..."
        play music "audio/music/The Thing - The Norwegian Camp.wav"
        scene black with fade
        "There was very little I could get with a view like this."
        "However, something particular caught my sight."
        play sound "audio/sfx/paper.wav"
        show Pol4 with fade
        pause 0.5
        "The soles of his shoes..."
        "They seemed pretty innocent at first glance,{w} however, their completely flat design gave me something to consider."
        "A lot of people have their shoes with plane sole,{w} but they're also very popular around people who don’t want to leave any clues."
        "To keep it simple,{w} I think there's a chance this person did't come with good intentions."
        "This is just a theory, but..."
        hide Pol4
        Officer "HEEEEEEY!!! {w} WHAT DO YOU THINK YOU'RE DOING?!"
        scene crime2 with fade
        show Officer at left
        show Johnny at right
        Officer "Didn’t you hear me? "
        show Officer sigh2 at left
        extend "I said you can't stay here!"
        Officer "This is my last warning.{w} Get out of here or I send you to resolve the case of the fallen soup in the bathroom."
        hide Officer
        show Officer serious at left
        hide Johnny
        show Johnny serious2 at right
        "His voice was so annoying...{w} Just a poor little thing who tried desperately to sound intimidating."
        hide Johnny
        show Johnny confused at right
        "But among his complaints,{w} I noticed something quite peculiar."
        "He was wearing shoes..."
        "Aslong as I know, officers should wear their full uniform...{w} that including boots."
        hide Johnny
        show Johnny serious1 at right
        Johnny "Those are pretty good, fella..."
        hide Officer
        show Officer nervous1 at left
        extend" They must be a gift, right?"
        "I noticed a change in his behavior.{w} He shivered like a scared little sheep the moment I mentioned that."
        "He thought I wouldn’t notice…"
        hide Officer
        show Officer serious at left
        "...but I did.{w} Oh, hell I did..."
        hide Johnny
        show Johnny at right
        hide Officer
        show Officer chat at left
        Officer "L-Let me give you a little advice, Mr. Detective...{w} Stay on your business."
        hide Johnny
        show Johnny smug1 at right
        hide Officer
        show Officer at left
        Johnny "Heh...{w} I’ll have that on mind."
        hide Johnny
        show Johnny chat1 at right
        Johnny "In that case, we’ll be in contact soon enough, officer."
        hide Johnny chat1
        show Johnny smug1 R at right
        pause 0.2
        hide Johnny
        show Johnny smug1 R at offscreenright
        with moveinleft
        hide Officer
        show Officer serious at left
        pause 2.0
        Officer "Uh..."
        hide Officer
        show Officer nervous2 at left
        Officer "For your own good, we better not..."
        pause 1.0
        hide Officer
        show Officer nervous1 at left
        Officer "..."
        stop music fadeout 2.0
        scene black with fade

        jump main_route

    label Indifference1:
        $ PoliIndifference = True
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
        show Officer indifferent with dissolve
        "Even at that moment,{w} just by the touching our gazes,{w} I could feel his heart racing."
        play sound "audio/sfx/static.wav" fadein 1.5
        pause 2.0
        "He was feeling nervous,{w} self-conscious,{w} probably {b}unsafe{/b}."
        "But why?{w} Why would anyone on his position feel intimidated?"
        "Being armed,{w} close to his colleagues,{w} in broad daylight..."
        "There was no way I could hurt him..."
        hide Officer
        show Officer nervous2
        extend " right?"
        "But that's the thing, you know?"
        "Deep down...{w} he was small,{w} just a little man pretending to be brave and strong."
        hide Officer
        show Officer nervous1
        "His nervousness increased the moment the questions began to multiply."
        "“What is he doing?”{w} “Why does he keep staring at me?”"
        "“What should I do?”{w} “Is he gonna hurt me?”{w} “I don’t wanna get hurt, should I yell”{w} “Maybe threaten him?”{w} “Hurt him?”{w} “Perhaps…”"
        pause 1.5
        "“Perhaps {b}shoot{/b} at him?”"
        hide Officer nervous1 with fade
        stop music fadeout 1.5
        "My thoughts were confirmed as I saw his hand slowly moving towards the gun on his belt."
        "A small grin started to creep on my face, and he clumsily failed a couple of times when trying to take it."
        play music "audio/sfx/static.wav" fadein 1.0
        "His pupils dilated,{w} small beads of sweat rolled down his skin,{w} and his pulse faltered as his fingers wrapped around the pistol."
        "But before he could even pull it out…"
        stop music
        scene crime2
        show Officer scared at left
        show Johnny chat1 at right
        Johnny "All right.{w} I think I'm going then."
        hide Johnny
        show Johnny smug1 at right
        hide Officer
        show Officer nervous1 at left
        "I spoke."
        Johnny "Until we see each other’s again,{w} officer~"
        pause 1.0
        scene black with fade
        "And so I did."
        "I moved on, leaving the little man alone with his thoughts."
        play sound "audio/sfx/Steps grass.wav"
        items "And as I walked away, I heard an almost inaudible sigh of tranquility.{w} The sound of his soul reentering his body."
        items "And then,{w} the distant voice of that poor guy prayed..."
        Officer "For fuck sake…{w} I need a moment..."

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
    "That seemed like the work of one of the mafias, perhaps some cartel.{w} However, the scene was too clean or too dirty to be one of them."
    hide Johnny
    show Johnny serious2 R at center
    if "PoliDemureness" in locals():
        "I could say the killer was an amateur,{w} but that {b}supposed officer{/b} was clearly compromised."
    else:
        "I could say the killer was an amateur,{w} but the police was clearly compromised."
    "Someone big placed his hands on this, but who and why?"
    hide Johnny
    show Johnny serious1 at center
    "And most importantly, is this somehow related with the stolen car?"
    "There’s also the possibility for them to be separate events,{w} which would make this an incredible and unfortunate coincidence."
    "The place...{w} the circumstance...{w} the time between events...{w} everything is so strange."
    scene black with fade
    Johnny "Strange..."
    stop music fadeout 2.0
    "And as this thought crossed my mind, something appeared on my field of view."
    scene malaga
    play sound "audio/sfx/static.wav" loop volume 0.6
    pause 1.5
    items "At a speed above the allowed,{w} a gray Seat Málaga with one of the rear lights broken crossed the street."
    stop sound fadeout 2.0
    scene black with fade
    "For a moment, I thought I imagined it."
    "Who would be so unaware as to pass right in front of their own crime scene?"
    scene motel2 with fade
    show Johnny sigh at center
    "It took me a few moments to process what I’ve just seen,{w} and when I came back to reality there was only one thing I could think about."
    pause 1.5
    hide Johnny
    show Johnny smug1 at center
    Johnny "Let’s drive!"
    play music "audio/music/Cruel Summer ost.wav"
    scene black with fade
    play sound "audio/sfx/car turning on.wav"
    pause 0.5
    scene driving with fade
    items "I followed the silhouette of the car, keeping a safe distance to avoid being noticed."
    "The driver clearly wasn’t an expert.{w} Reckless maneuvers,{w} overly-accelerated speed,{w} little control over the vehicle,{w} seemed to be the profile of someone nervous or upset."
    "I like that kind of people.{w} They usually make things more interesting."
    scene black with fade
    "However, those who came out of that car were quite far from what I had in mind."
    pause 2.0
    scene passion with fade
    "We were driving for a while until our little trip got to an end."
    "The sun was starting to set when they stopped in front of a nightclub."
    "In my case, I parked on the opposite side of the road and dedicated myself to observe."
    play sound "audio/sfx/car door.wav"
    pause 1.7
    "Two young adults emerged from the vehicle."
    play sound "audio/sfx/paper.wav"
    show pol6 with Dissolve(1.0)
    "A guy with green eyes,{w} slender,{w} disheveled,{w} looking like he haven't slept in days.{w} Quite handsome, if I can add."
    play sound "audio/sfx/paper.wav"
    show pol5 with Dissolve(1.0)
    "And a girl with pink eyes,{w} of relative short stature,{w} confident,{w} with a pretty but also messy hairstyle."
    "A particular duet, but nothing flashy."
    play sound "audio/sfx/paper.wav"
    show pol10 with Dissolve(1.0)
    "They seemed to have an argument moments after placing a foot out of the car."
    "I saw them yell at each other before their expressions changed from the anger to the calm, {w}and as if nothing had happened,{w} they walked straight into the building with two prominent smiles on their faces."
    Johnny "Ok...{w} talking about bipolarity."
    play sound "audio/sfx/paper.wav"
    hide pol6 with dissolve
    pause 0.5
    play sound "audio/sfx/paper.wav"
    hide pol5 with dissolve
    pause 0.5
    play sound "audio/sfx/paper.wav"
    hide pol10 with dissolve
    pause 1.0
    "With my first two suspects on the board it was time to work."
    "First of all,{w} checking the car."
    scene black with fade
    play sound "audio/sfx/car door.wav"
    pause 1.5
    "And for my not-so-big surprise,{w} the doors weren’t locked."
    scene car with fade
    "Sadly, the keys weren’t there neither.{w} But I do found some of interesting stuff."
    pause 0.8
    play sound "audio/sfx/item_got.ogg"
    show butcher
    pause 1.2
    "{i}Jonathan has picked up a butcher blade.{/i}"
    "Quite good to chop some meat, just what I was needing."
    hide butcher
    play sound "audio/sfx/item_got.ogg"
    show sodas
    pause 1.2
    "{i}Jonathan has picked up a couple of empty soda cans.{/i}"
    "Caramelized Apple and Cinnamon…{w} I heard people use this stuff to remove rust from engines."
    "You must have a really strong stomach to drink this thing…"
    hide sodas
    play sound "audio/sfx/item_got.ogg"
    show notepad
    pause 1.2
    "{i}Jonathan has picked up a folder full of documents...{/i}"
    "{i}...defunction documents.{/i}"
    "Now this…{w} this was something."
    play sound "audio/sfx/paper.wav"
    hide notepad with dissolve
    pause 1.2
    show Johnny R at center with Dissolve(0.2)
    Johnny "Andrew and Ashley Graves, huh?"
    Johnny "Siblings…"
    Johnny "Day of decease: [[REDACTED]"
    hide Johnny
    show Johnny confused R at center
    Johnny "Cause: Fire/Smoke suffocation."
    hide Johnny
    show Johnny serious1 R at center
    "This was a couple of weeks ago.{w} If I'm not mistaken, it happened the same day that quarantined apartment was burnt to ashes."
    Johnny "Back from the Graves, very interesting."
    hide Johnny
    show Johnny smug1 R at center
    Johnny "We can say that..."
    hide Johnny
    show Johnny smile2 R at center
    stop music
    extend" {i}this fans the flames of my interest.{/i}"
    pause 2.0
    hide Johnny
    show Johnny smile1 R at center
    Johnny "..."
    hide Johnny
    show Johnny confused R at center
    Johnny "Good thing nobody heard that..."
    pause 2.0
    play music "audio/music/Cruel Summer ost.wav"
    hide Johnny
    show Johnny serious1 R at center
    "Anyway..."
    "Most likely, these documents are fake."
    "Little siblings tried to fake their deaths, I get that."
    "Now,{w} why doing such thing in that way?{w} Did they take the entire apartment with them?{w} Was there an ulterior motive behind all this?"
    hide Johnny
    show Johnny sigh R at center
    "I had more questions than answers…"
    "Luckily I had those two just a couple of meters away."
    "The thing is..."
    scene black with fade
    "This wasn’t just a stolen car case anymore.{w} Which also means that the danger involved was also bigger."
    "Considering all the factors on board, I had no reasons to keep going."
    "Could have just walked away,{w} presented the information to my client and let him deal with the rest."
    "Work finished."
    stop music fadeout 1.5
    "But then again…{w} Where would be the fun on that?"
    play music "audio/sfx/static.wav" fadein 1.5 volume 0.4
    "And besides that,{w} would also get a nice recommendation if I return the car instead of just bringing some dirty information."
    Johnny "You always have to pamper your client,{w} no matter how idiotic they are."
    Johnny "You just low your head and say yes to the money fool."
    stop music fadeout 1.5
    pause 1.0
    play sound "audio/sfx/car door.wav"
    "With this in mind, I got out of the car, closed the door and fixed my clothes before walking into the club."
    play sound "audio/sfx/whip.wav"
    hide Johnny
    show Johnny P R at center
    pause 1.0
    Johnny "Show time~"
    hide Johnny with fade
    pause 1.5
    play music "audio/music/ALEX - AKUMA.wav"
    scene club_in with fade
    "The place was still a little empty."
    show pol8 with dissolve
    show pol7 with dissolve
    "The pixie-girl was sitting on a table at the bottom of the place while the emo-boy was leaning against the handrail of the balcony in the second floor."
    "Usually, women doesn’t give much troubles."
    "It’s just a matter of pulling out the {i}Paddle’s style{/i}, and they tell me what I want to hear~"
    "That...{w} or they attack me...{w} One of those options."
    scene club1 with fade
    show Ashley at right
    pause 0.5
    play sound "audio/sfx/Steps stone.wav"
    "So I walked into her with airs of calm."
    show Johnny smile2 R at left with easeinleft
    "Those eyes felt over me without much interest."
    hide Ashley
    show Ashley smug1 at right
    extend " However, the moment I sat on the chair, {nw}"
    extend"I was greeted by the smuggest smile I've ever seen in my life."
    hide Ashley
    show Ashley worried2 at right
    Ashley "You’re totally not a cop, are you?"
    hide Ashley
    show Ashley smug1 at right
    hide Johnny
    show Johnny chat1 R at left
    Johnny "Actually, I’m not.{w} I applied for the position, but got expelled from the academy before graduating."
    hide Johnny
    show Johnny smile1 R at left
    Johnny "Sad,{w} I really wanted to use a taser..."
    hide Johnny
    show Johnny smile2 R at left
    hide Ashley
    show Ashley mad3 at right
    "She inspected me from top to bottom with very little modesty."
    hide Ashley
    show Ashley think at right
    "Eventually, her eyes lit up on realization."
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
    "Ouch..."
    hide Johnny
    show Johnny chat1 R at left
    Johnny "Y-Yeah... that one..."
    hide Johnny
    show Johnny P R at left
    play sound "audio/sfx/whip.wav"
    pause 1.0
    Johnny "Johnny Paddle, P.I."
    hide Johnny P R
    show Johnny P2 R at left
    play sound "audio/sfx/whip.wav"
    pause 1.0
    hide Ashley
    show Ashley smug1 at right
    Johnny "If there’s a problem…{w} Better call me~"
    hide Johnny
    show Johnny smile2 R at left
    hide Ashley
    show Ashley giggle1 at right
    "I received a playful laugh from her part as an answer."
    hide Johnny
    show Johnny R at left
    extend" However, the tone, wasn’t exactly natural."
    hide Ashley
    hide Johnny
    show Ashley smug1 at right
    show Johnny serious1 R at left
    "Her face remained in constant smugness,{w} her eyes free of any nerves, regardless of disown my intentions."
    "It was easy to tell that she was playing.{w} Maybe because I wasn't consider a threat.{w} Not yet at least."
    hide Ashley
    show Ashley smug3 at right
    "She was a hard one.{w} No matter how much I tried to see through her, I wasn’t able to distinguish any trace of sincere emotions."
    "It felt…{w} particularly strange."
    hide Johnny
    show Johnny serious2 R at left
    "As if her whole figure wasn't but a lie trying to fool anyone at any moment."
    hide Ashley
    show Ashley smug2 at right
    hide Johnny
    show Johnny confused R at left
    Ashley "So, a detective talking to a pretty lady on a club.{w} It sounds like something out of those cheap 60's movies when you say it loud."
    hide Ashley
    show Ashley smug1 at right
    hide Johnny
    show Johnny chat1 R at left
    Johnny "What can I say?{w} It's not every day you can recreate a cliché scene from classic cinema."
    hide Johnny
    show Johnny smug2 R at left
    Johnny "Just don’t tell anybody you saw a handsome detective stealing the tips bottle, ok?"
    hide Ashley
    show Ashley smug2 at right
    hide Johnny
    show Johnny smile2 R at left
    Ashley "First of all,{w} those tips are mine, mister."
    hide Ashley
    show Ashley at right
    Ashley "And second, why don't we skip this whole part?"
    hide Ashley
    show Ashley worried2 at right
    Ashley "Just tell me what do you want from this sweet-innocent girl in front of you?"
    hide Ashley
    show Ashley at right
    hide Johnny
    show Johnny serious1 R at left
    "I haven’t seen a sweet and innocent person in years."
    "And frankly, with the little evidence I had till that moment, I could tell she was a lot of things but sweet or innocent."
    hide Johnny
    show Johnny confused R at left
    "Hot and dangerous maybe,{w} but not sweet and innocent."
    hide Johnny
    show Johnny R at left
    Johnny "I was hired to find the whereabouts of a car stolen a few days ago."
    Johnny "A gray Seat Málaga with one of the rear lights broken.{w} Does it sounds familiar to you?"
    hide Ashley
    show Ashley pout1 at right
    "She took the information and thought about it for a considerably long moment."
    hide Ashley
    show Ashley smug1 at right
    "The mischievous smile on her lips confirmed that she knew exactly what I was talking about."
    hide Ashley
    show Ashley smug3 at right
    hide Johnny
    show Johnny confused R at left
    Ashley "Nope.{w} Haven’t seen a car like that in my life."
    "The confidence in those words managed to surprise me."
    hide Johnny
    show Johnny smug1 R at left
    "A good liar…{w} one of the kind I would even say."
    "That made me a little more excited."
    "However, with that I also knew that had to proceed cautiously with this beautiful lady.{w} So I was forced to swallow those feelings and concentrate."

    #################################### Ashley 1 choice

    menu:
        "Let's try..."

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
        show Johnny smile2 R at left
        hide Ashley
        show Ashley smug2 at right
        Johnny "Heh, {w} you’re good,{w} gotta give you some points."
        hide Johnny
        show Johnny smug1 R at left
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
        hide Johnny
        show Johnny serious3 R at left
        Johnny "Much more, if we consider how attractive this one turns to be..."
        hide Johnny
        show Johnny smile2 R at left
        hide Ashley
        show Ashley giggle1 at right
        Ashley "Hahahahahahaha."
        hide Ashley
        show Ashley worried2 at right
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
        hide Ashley
        show Ashley pout1 at right
        Ashley "But I suppose you already knew it, don't you?"
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "You got me,{w} but I wanted to hear it from you.{w} Like a proper introduction, you know what I'm talking about."
        hide Ashley
        show Ashley at right
        hide Johnny
        show Johnny smile2 R at left
        Johnny "After all...{w} a name like that should be said by lips just as beautiful~"
        hide Johnny
        show Johnny smile1 R at left
        hide Ashley
        show Ashley mad at right
        "That...{w} was a little too much.{w} Her smile vanished to be replaced by an uncomfortable expression."
        hide Johnny
        show Johnny serious1 R at left
        "I overdid with the praises… damn it..."
        hide Johnny
        show Johnny serious3 R at left
        Johnny "A-Anyway…{w} Now that we know each others, would you mind telling me a little about the car outside?"
        Johnny "That’s why I’m here after all."
        hide Johnny
        show Johnny smile2 R at left
        hide Ashley
        show Ashley worried2 at right
        Ashley "And why would I do that?"
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Well, simply because it’s better for you two."
        hide Ashley
        show Ashley smug3 at right
        hide Johnny
        show Johnny smile2 R at left
        Johnny "We can say I’m just an employ."
        Johnny "I was hired to find it,{w} give some information, do paperwork, things like that."
        hide Johnny
        show Johnny serious3 R at left
        Johnny "Nothing will happen if you don't help me, but..."
        hide Ashley
        show Ashley at right
        hide Johnny
        show Johnny serious1 R at left
        stop music fadeout 1.0
        extend " There’s a big chance my client will send {b}someone else{/b} if you don't collaborate."
        hide Johnny
        show Johnny R at left
        Johnny "Probably not as reasonable as me."
        hide Johnny
        show Johnny smile2 R at left
        pause 1.5
        Ashley "..."
        Ashley "Was… "
        hide Ashley
        show Ashley mad3 at right
        extend "Was that a threat?{w} Because it sounded like a threat..."
        hide Johnny
        show Johnny chat1 R at left
        play music "audio/music/I'm a Little Tired After That.wav" fadein 1.0
        Johnny "I would prefer the term {b}bargain{/b}."
        hide Ashley
        show Ashley mad at right
        hide Johnny
        show Johnny smile2 R at left
        Johnny "In essence is the same, but it sounds way more elegant."
        pause 1.0
        hide Johnny
        show Johnny serious3 R at left
        Johnny "And don't you think I'm trying to scare you or anything here."
        hide Johnny
        show Johnny smug2 R at left
        hide Ashley
        show Ashley at right
        extend "If so I’m your benefactor."
        Johnny "I could just walk away and you’ll never see me again, OR…{w} you can be a good girl,{w} give me the keys so I can return the vehicle,{w} and everyone's happy."
        hide Johnny
        show Johnny smug1 R at left
        Johnny "I get my fee, and you two return to whatever you're doing~"
        hide Ashley
        show Ashley mad3 at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny"Sounds good? I think it sounds pretty good."
        hide Johnny
        show Johnny smile2 R at left
        "It did sound good…"
        hide Johnny
        show Johnny R at left
        hide Ashley
        show Ashley mad2 at right
        extend " but she didn't like it.{w} Not at all I would say."
        "I could feel the air change around us.{w} The tension raised up as she kept hiding behind that emotion wall."
        "Still,{w} hard to read,{w} but it was evident that she was pissed now."
        hide Johnny
        show Johnny serious1 R at left
        hide Ashley
        show Ashley ewww at right
        Ashley "And just when I was starting to like you, detective…"
        Ashley "Fine,{w} you want that piece of scrap? Is yours."
        hide Ashley
        show Ashley mad3 at right
        extend " It’s out of gas anyway."
        hide Johnny
        show Johnny confused R at left
        Ashley "But unfortunately for you,{w} I don’t have the keys."
        Ashley "Go talk with Andy up there…"
        scene black with fade
        "I woke from the chair and looked at her one last time."
        Johnny "Thank you for…{nw}"
        Ashley "Piss off."
        "All right…{w} That could have gone better, I have to admit."
        jump main_route2

    label Subtlety1:
        hide Ashley
        show Ashley smug1 at right
        "I turned to look at the guy on the second floor."
        hide Johnny
        show Johnny smile2 R at left
        Johnny "So,{w} a girl and her brother went to a bar in a stolen car and she doesn’t know anything about it?"
        hide Johnny
        show Johnny smug2 R at left
        Johnny "Sounds like the number of some half-time comedian if you ask me."
        hide Johnny
        show Johnny smug1 R at left
        hide Ashley
        show Ashley smug2 at right
        Ashley "It easily could be.{w} And the punchline would be the underpaid detective trying to get a confession out of the girl."
        hide Johnny
        show Johnny smug1 R at left
        Ashley "And I would say that it’s a fun joke, "
        hide Ashley
        show Ashley at right
        extend "but I'm not into comedies."
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Oh, me neither.{w} Too much chatter to come up with something dumb."
        hide Johnny
        show Johnny serious3 R at left
        Johnny "I’m more of a drama enjoyer, you see?"
        hide Johnny
        show Johnny smug2 R at left
        hide Ashley
        show Ashley smug3 at right
        Johnny "A nice tense environment,{w} people into suspense,{w} and the plot slowly revealing itself."
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
        Ashley "Andrew is worried on main.{w} I swear, that guy hasn’t know tranquility in his whole life."
        hide Ashley
        show Ashley smug3 at right
        Ashley "My bad, actually."
        hide Ashley
        show Ashley giggle1 at right
        hide Johnny
        show Johnny smile2 R at left
        "I couldn’t avoid to laugh at such little declaration."
        stop music fadeout 1.5
        "There was something odd and sinister on those words,{w} a strange ambiguity located between sincerity and jokes."
        "Couldn't really tell if she was being honest,{w} but rather than scare or disrupt..."
        hide Ashley
        show Ashley smug1 at right
        play music "audio/music/The Thing - What Appears to be Normal.wav"
        " It made me feel attracted to her game."
        hide Johnny
        show Johnny serious3 R at left
        Johnny "I got the feeling that you weren't exactly joking."
        hide Johnny
        show Johnny smile2 R at left
        Johnny "You like to {b}play{/b} with the little man,{w} don't you?"
        hide Ashley
        show Ashley smug3 at right
        pause 1.5
        Ashley "..."
        Ashley "I never said that~"
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Touché, touché..."
        hide Johnny
        show Johnny smile2 R at left
        Johnny "But still...{w} Throw me a stick."
        hide Johnny
        show Johnny smug1 R at left
        pause 1.5
        "She didn't said anything.{w} But her silence..."
        hide Ashley
        show Ashley mocking1 at right
        extend " that smile, those guiltless eyes, said enough."
        pause 1.5
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny smug2 R at left
        Johnny "I see..."
        hide Johnny
        show Johnny smug1 R at left
        hide Ashley
        show Ashley worried2 at right
        Ashley "You have good eyes, detective. {w} I don't like people who can see through me, you know?"
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
        Johnny "Yeah… That’s probable,{w} but maybe it’s a good thing."
        hide Johnny
        show Johnny smug1 R at left
        pause 1.5
        hide Ashley
        show Ashley at right
        hide Johnny
        show Johnny R at left
        Johnny "But...{w} Maybe in another oportunity."
        hide Johnny
        show Johnny chat1 R at left
        Johnny "For now, I'll you this."
        Johnny "If you give me the keys of the car I’ll tell my client that I found them somewhere in the middle of nowhere."
        hide Johnny
        show Johnny smile2 R at left
        Johnny "No clues,{w} no witnesses,{w} no butts."
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
        Ashley "I don’t have the keys."
        hide Ashley
        show Ashley mad at right
        Ashley "Andy doesn't trust me enough for that…{w} but whatever."
        hide Ashley
        show Ashley worried2 at right
        hide Johnny
        show Johnny sigh R at left
        Ashley "Oh, and it’s also out of gas by the way."
        hide Ashley
        show Ashley smug1 at right
        "Women...{w} all the same."
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
        Johnny "Say that I'm gonna put him in a cell with a six-foot black guy named Ramón.{w} Got it!"
        scene black with fade
        "Welp,{w} gotta admit,{w} that ended up better than expected."
        jump main_route2

    label Straightness1:
        hide Johnny
        show Johnny R at left
        play sound "audio/sfx/paper.wav"
        items "Without waiting for a call, I shown the documents."
        hide Johnny
        show Johnny serious3 R at left
        Johnny "So…{w} Mr. and Miss. Graves."
        hide Ashley
        show Ashley smug1 at right
        Johnny "Deceased on [[REDACTED].{w} And now founded in a crappy nightclub with a stolen vehicle."
        hide Johnny
        show Johnny chat1 R at left
        Johnny "That should be quite the story, am I right?"
        hide Ashley
        show Ashley mocking1 at right
        hide Johnny
        show Johnny smile2 R at left
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
        show Ashley worried2 at right
        Ashley "Good, I can work with that.{w} It means you know how to get what you want."
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
        show Johnny smile2 R at left
        Johnny "Still, I want to guess..."
        hide Johnny
        show Johnny smug1 R at left
        pause 1.5
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Parents?"
        hide Johnny
        show Johnny smile2 R at left
        hide Ashley
        show Ashley at right
        Ashley "Parents."
        hide Johnny
        show Johnny smile1 R at left
        "Yeah, it wasn't that hard."
        hide Ashley
        show Ashley worried2 at right
        hide Johnny
        show Johnny smug1 R at left
        Ashley "Will you believe me if I say that it was Andy's idea?{w} He may not look like, but he can be quite impulsive sometimes..."
        hide Ashley
        show Ashley at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Well, now that you mention it,{w} he definitely looks like the kind of guy who would drive the night out with electronic music playing in the background."
        hide Johnny
        show Johnny smile2 R at left
        hide Ashley
        show Ashley think at right
        Ashley "We had...{w} an {b}altercation{/b}{w} with mom and dad..."
        hide Ashley
        show Ashley smug2 at right
        extend " But that's in the past."
        hide Ashley
        show Ashley smug1 at right
        Ashley "Now everything we want is to began our new life {b}far away{/b} from them."
        hide Johnny
        show Johnny smug1 R at left
        Johnny "You know what, miss Graves?{w} Every word you just said is correct by my standards."
        hide Ashley
        show Ashley pout1 at right
        Ashley "Awwww, you flatter me, detective."
        hide Ashley
        show Ashley worried2 at right
        Ashley "Too bad you're here to put us some ugly handcuffs."
        hide Ashley
        show Ashley think at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "And who said such a thing?{w} I'm not here to put handcuffs on anyone, dear."
        hide Johnny
        show Johnny smug1 R at left
        Johnny "Unless you want me to, of course~"
        hide Ashley
        show Ashley mad at right
        Ashley "So… You aren't here for us?{w} Don't tell me you just want the stupid car..."
        hide Johnny
        show Johnny R at left
        Johnny "Well yes, that assumption is correct."
        hide Johnny
        show Johnny chat1 R at left
        hide Ashley
        show Ashley think at right
        Johnny "But also wanted to talk a little bit with you two.{w} Just for fun, you understand."
        hide Johnny
        show Johnny smug2 R at left
        Johnny " Now,{w} if you really want to confess any kind of crime I could…{nw}"
        hide Ashley
        show Ashley worried2 at right
        Ashley "No, no, no… I think I’m good like this."
        hide Ashley
        show Ashley at right
        hide Johnny
        show Johnny chat1 R at left
        Johnny "Great!{w} So, can you give me the keys now?"
        hide Johnny
        show Johnny serious1 R at left
        hide Ashley
        show Ashley smug2 at right
        Ashley "You can take that piece of scrap if you want."
        hide Ashley
        show Ashley smug3 at right
        Ashley "We almost ran out of gasoline{nw}"
        hide Ashley
        show Ashley smug1 at right
        extend " and I'm not in the mood for pushing it, so..."
        hide Ashley
        show Ashley at right
        hide Johnny
        show Johnny smile2 R at left
        Johnny "What a collaborator,{w} wish all of my jobs were like this."
        hide Ashley
        show Ashley smug2 at right
        hide Johnny
        show Johnny smile1 R at left
        Ashley "Not so fast, detective.{w} Andrew is the one who holds the keys"
        hide Johnny
        show Johnny confused R at left
        hide Ashley
        show Ashley mocking1 at right
        Ashley "Maybe I should've mentioned that before."
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny sigh R at left
        Johnny "Always... {w} Always a problem..."
        hide Ashley
        show Ashley giggle1 at right
        Ashley "Hahahaha"
        hide Johnny
        show Johnny confused R at left
        hide Ashley
        show Ashley smug3 at right
        Ashley "Anyway,{w} just try not to scare him too much."
        hide Ashley
        show Ashley smug1 at right
        hide Johnny
        show Johnny smile2 R at left
        Ashley "May even cry a little,{w} he likes to do that sometimes."
        hide Johnny
        show Johnny serious3 R at left
        Johnny "As fun as that sounds, I think I’ll try to make things easy."
        hide Johnny
        show Johnny chat1 R at left
        Johnny "But thanks anyway, miss Graves.{w} And of course…"
        hide Johnny
        show Johnny smug1 R at left
        "I slid one of my business cards on the table."
        play sound "audio/sfx/whip.wav"
        hide Johnny
        show Johnny P2 R at left
        pause 1.0
        Johnny "If there’s a problem…"
        play sound "audio/sfx/whip.wav"
        hide Johnny
        show Johnny P R at left
        pause 1.0
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
    "After this encounter,{w} I made my way into the stairway to find the guy leaning against the handrail."
    scene club2 with fade
    show Andrew confused at left
    "His gaze passed over me discreetly,{w} trying to get a sneaky-peeky look."
    pause 0.5
    play sound "audio/sfx/Steps stone.wav"
    show Johnny at right
    with easeinright
    items "I took my place at his aside and,{w} naturally..."
    hide Johnny
    show Johnny smile2 at right
    play sound "audio/sfx/blingy_sp.ogg"
    pause 0.7
    extend " gift a little smile."
    hide Andrew
    show Andrew worried1 at left
    "His answer wasn't but a dense silence."
    "He didn't even try to look back,{w} just kept himself isolated hoping that I would eventually get away from there."
    hide Johnny
    show Johnny smug1 at right
    "But of course, I wasn't going anywhere."
    pause 2.0
    "And,{w} eventually..."
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
    Andrew "Look, whatever she told you, it’s probably a lie."
    hide Johnny
    show Johnny smile2 at right
    hide Andrew
    show Andrew sigh at left
    Andrew "She’s very good at it and,{w} honestly?{w} Kinda insane…"
    hide Andrew
    show Andrew angry1 at left
    Andrew "...and adopted."
    hide Andrew
    show Andrew sigh at left
    extend " Specially adopted."
    hide Johnny
    show Johnny chat1 at right
    hide Andrew
    show Andrew confused at left
    Johnny "Well, that’s quite the revelation, Mr. Graves.{w} Let me introduce myself."
    hide Johnny
    show Johnny smile2 at right
    "I extended a presentation card."
    Johnny "If there’s a problem…"
    hide Johnny
    show Johnny P at right
    extend " better—{nw}"
    hide Johnny
    show Johnny confused at right
    Andrew "Quit that, I know you."
    hide Johnny
    show Johnny smile1 at right
    extend " You’re the clown from the posters."
    hide Johnny
    show Johnny sigh at right
    "Yeah, they're definitely siblings."
    hide Johnny
    show Johnny confused at right
    Johnny "You’re not funny, man.{w} Where’s the spirit?"
    hide Andrew
    show Andrew chat1 at left
    Andrew "Dead,{w} just like your 80's detective role."
    hide Andrew
    show Andrew angry2 at left
    hide Johnny
    show Johnny smile1 at right
    Andrew "Now would you mind to let me the fuck alone?"
    hide Andrew
    show Andrew at left
    extend " We have no business with you, and I really need a moment of peace..."
    hide Johnny
    show Johnny serious1 at right
    hide Andrew
    show Andrew angry1 at left
    "He turned out to be way less chatty than his sister."
    Johnny "Nah,{w} I'm afraid I can't do that, brother."
    hide Andrew
    show Andrew nervous1 at left
    "I had a feeling that,{w} at the slightest chance,{w} he would try to run away in an attempt to escape."
    pause 2.0

    ################################### Andrew choice


    if DualAff > 0:
        jump Straightness2
    else:
        if AshleyAff > 0:
            jump Sharpness2
        else:
            jump Subtlety2

    label Straightness2:
        pause 0.5
        hide Johnny
        show Johnny chat1 at right
        Johnny "Why so tense, brother?{w} I have nothing against you,{w} really, I'm not..."
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny smug2 at right
        Johnny "You can relax,{w} take a deep breath,{w} enjoy the music,{w} flavor the moment."
        Johnny "There's nothing to be afraid of."
        hide Johnny
        show Johnny smile2 at right
        hide Andrew
        show Andrew sigh at left
        Andrew "Oh please..."
        hide Andrew
        show Andrew angry1 at left
        Andrew "Don't give me the whole speech,{w} just jump straight to the point."
        hide Andrew
        show Andrew facepalm at left
        hide Johnny
        show Johnny serious3 at right
        Johnny "I would, but also love the sound of my voice~"
        hide Johnny
        show Johnny chat1 at right
        Johnny "I understand you may think I'm just trying to get a confession or some reasons to screw you up,{w} but the reality couldn't be further from that."
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny smug1 at right
        Johnny "The reason I'm here with you today, "
        hide Johnny
        show Johnny smile2 at right
        hide Andrew
        show Andrew confused at left
        extend "isn't but that piece of scrap you stole called a car."
        "The expression on his face softened a little."
        hide Andrew
        show Andrew worried1 at left
        "For an instant,{w} I really thought I had passed through him..."
        hide Johnny
        show Johnny confused at right
        hide Andrew
        show Andrew angry1 at left
        extend " But sadly, that spark of confidence didn't last longer."
        hide Andrew
        show Andrew chat1 at left
        Andrew "Let me tell you something.{w} Your facade isn't fooling anyone here."
        Andrew "I've been living with a liar long enough to recognize another."
        hide Andrew
        show Andrew angry2 at left
        hide Johnny
        show Johnny serious1 at right
        Andrew "Even the guy on the bar can tell you're full of bullshit."
        hide Andrew
        show Andrew at left
        Andrew "I told you,{w} we have no business."
        Andrew "So why don't you take your nice words and put them in...{nw}"
        stop music
        hide Andrew
        show Andrew nervous1 at left
        hide Johnny
        show Johnny angry1 at right
        Johnny "Slow.{w} Down.{w} Now..."
        scene black
        pause 1.5
        play music "audio/sfx/static.wav" fadein 1.0
        pause 1.5
        "I had to take a moment to relax..."
        pause 2.0
        "I began to feel a little agitated,{w} my heart beating at high speed as those words repeated in my mind."
        pause 2.0
        "A liar..."
        pause 1.5
        "Me...{w} a liar..."
        pause 2.0
        "A disgusting...{w} fucking... liar{nw}"
        stop music
        scene club2
        hide Andrew
        show Andrew nervous2 at left
        hide Johnny
        show Johnny smile2 at right
        Johnny "As I was saying,{w} the fact that you or the goth girl had rob a bank, killed a guy or maybe sold some meth doesn't concern me at all."
        hide Andrew
        show Andrew nervous1 at left
        pause 1.5
        Andrew "I...{w} understand...{w} I think..."
        hide Andrew
        show Andrew nervous2 at left
        "For moments,{w} his eyes locked over the lady on the first floor,{w} still trying to steal from the flask of tips."
        hide Johnny
        show Johnny serious3 at right
        "It was pretty funny, got to admit."
        hide Johnny
        show Johnny smile2 at right
        pause 2.0
        hide Andrew
        show Andrew nervous1 at left
        Andrew "L-Let’s say that,{w} for an instant,{w} I believe you."
        Andrew "What would you do if I give up the keys?"
        pause 1.5
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny chat1 at right
        Johnny "I’ll go down,{w} ask for a drink,{w} and when you two have found it appropriate and walked away,{w} I’ll take the car and bring it back to its respective owner."
        hide Johnny
        show Johnny smug2 at right
        Johnny "No question,{w} no cops,{w} and no stories."
        Johnny "It ends there."
        hide Johnny
        show Johnny chat1 at right
        Johnny "What do you say?"
        hide Johnny
        show Johnny smile2 at right
        hide Andrew
        show Andrew confused at left
        pause 2.0
        hide Andrew
        show Andrew nervous1 at left
        Andrew "F-Fine…"
        Andrew "Here you go.{w} Just leave us alone now…"
        show keys at center
        play sound "audio/sfx/item_got.ogg"
        pause 1.0
        "{i}Jonathan has picked up the car-keys! (finally){/i}"
        hide keys with dissolve
        pause 0.5
        hide Johnny
        show Johnny chat1 at right
        Johnny "Without a problem, brother."
        scene black with fade
        Johnny "You just took a weight off your shoulders."
        jump main_route3

    label Sharpness2:
        pause 0.5
        hide Johnny
        show Johnny serious2 at right
        Johnny "Listen,{w} there's no need to be scared, man.{w} I don't really care about what you or the hot babe down there did."
        hide Johnny
        show Johnny confused at right
        hide Andrew
        show Andrew confused at left
        Johnny "Do you have any idea how many criminals I met on my daily basis?{w} Do you know how I call them?"
        hide Johnny
        show Johnny chat1 at right
        Johnny "{b}Potential clients{/b}."
        hide Johnny
        show Johnny smile2 at right
        Johnny "There’s no need to put my nose where I don’t mind.{w} That's part of the fun."
        hide Andrew
        show Andrew chat1 at left
        Andrew "Being a jackass is also part the fun?{w} Because you're making sound like it."
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny chat1 at right
        Johnny "A little, actually.{w} Have you tried before?{w} It's quite de-stressing."
        hide Johnny
        show Johnny serious3 at right
        hide Andrew
        show Andrew facepalm at left
        Johnny "I think you would like it, fancy pants~"
        hide Johnny
        show Johnny smile2 at right
        hide Andrew
        show Andrew sigh at left
        Andrew "Dear god..."
        hide Andrew
        show Andrew at left
        Andrew "No, I don't want to try it."
        hide Andrew
        show Andrew chat1 at left
        Andrew "Why do you even care to begin with?"
        hide Andrew
        show Andrew angry2 at left
        hide Johnny
        show Johnny smile1 at right
        Andrew "Why am I always chased by idiots?"
        hide Johnny
        show Johnny chat1 at right
        Johnny "By the way,{w} you should stop smoking."
        hide Andrew
        show Andrew what at left
        extend " You’ll cough your lungs out when trying to run."
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny smug1 at right
        "His eyes locked on me with a tired-wrathful expression.{w} I could even feel the need to tear my eyes out."
        hide Johnny
        show Johnny serious3 at right
        "He looked kinda cute like that."
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
        show Johnny smug1 at right
        Andrew "STOP IT."
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny chat1 at right
        Johnny "All right all right, I’m just messing a little."
        Johnny "You sister told me you have the car-keys.{w} If you give them to me, I’ll {b}smoke{/b} out of here and leave you in peace with your cancer cue."
        hide Johnny
        show Johnny serious3 at right
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
        pause 1.0
        "{i}Jonathan has picked up the car-keys! (finally){/i}"
        hide keys with dissolve
        pause 0.5
        hide Johnny
        show Johnny chat1 at right
        Johnny "Oh yeah,{w} she indeed has a good pair of ideas on her own."
        hide Andrew
        show Andrew angry1 at left
        Johnny "Would even ask for them if I were a little less professional."
        hide Johnny
        show Johnny smile2 at right
        hide Andrew
        show Andrew angry2 at left
        Andrew "Whatever, dude..."
        scene black with fade
        Johnny "Anyway!{w} It was a pleasure to make business with you, Mr. Graves!"
        Johnny "I'll see you when you get a van and start cooking some meth in a plain—{nw}"
        stop music
        Andrew "JUST FUCK OFF!"
        pause 0.5
        jump main_route3

    label Subtlety2:
        hide Johnny
        show Johnny chat1 at right
        Johnny "You have the look of someone with a ton of problems."
        hide Johnny
        show Johnny smile2 at right
        hide Andrew
        show Andrew sigh at left
        "A deep sigh came out him as a confirmation."
        hide Andrew
        show Andrew at left
        Andrew "As if you care, man."
        hide Andrew
        show Andrew angry1 at left
        extend " These are personal problems,{w} none of your business."
        hide Andrew
        show Andrew confused at left
        hide Johnny
        show Johnny chat1 at right
        Johnny "True, very true!"
        Johnny "But what's better than telling your problems to a stranger?"
        hide Andrew
        show Andrew angry1 at left
        hide Johnny
        show Johnny smug2 at right
        Johnny "Isn't that what you're needing right now?{w} Fella?"
        hide Johnny
        show Johnny smug1 at right
        pause 2.0
        hide Johnny
        show Johnny at right
        Johnny "You sister is...{w} weird."
        hide Johnny
        show Johnny chat1 at right
        hide Andrew
        show Andrew at left
        extend " In the good way, off course."
        hide Johnny
        show Johnny smug2 at right
        Johnny "She’s a closed book,{w} could barely read what she was doing."
        hide Andrew
        show Andrew at left
        hide Johnny
        show Johnny serious1 at right
        Johnny "But you?{w} Bud, you’re nothing like that..."
        hide Andrew
        show Andrew angry1 at left
        stop music fadeout 1.5
        pause 2.0
        hide Andrew
        show Andrew angry2 at left
        Andrew "Ashley is not a closed book!{w} She’s just…"
        hide Andrew
        show Andrew angry1 at left
        pause 2.0
        Andrew "She’s just {b}her{/b} being herself…"
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
        scene black with fade
        "His brow furrowed tightly, and I could see the vein in his throat throbbing as if were going to burst."
        hide Andrew
        show Andrew at center with fade
        "In that moment,{w} I realized that comment touched a sensitive fiber."
        "His fist clenched in place with clear intentions. I could see the urge to attack in his eyes,{w} his starting to take control."
        scene black with fade
        scene club2 with fade
        show Andrew at left
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
        Andrew "I shouldn't even be telling you this..."
        pause 2.0
        hide Johnny
        show Johnny serious1 at right
        Johnny "She treats you as a rug,{w} I get that."
        hide Andrew
        show Andrew sigh2 at left
        "He didn’t answered but his expression said more than a thousand words."
        hide Andrew
        show Andrew angry1 at left
        hide Johnny
        show Johnny chat1 at right
        Johnny "I see…"
        hide Johnny
        show Johnny smile2 at right
        Johnny "Yes…{w} being the bigger brother is a whole thing."
        Johnny "You take all the responsibilities and rarely get any appreciations for it."
        hide Johnny
        show Johnny confused at right
        hide Andrew
        show Andrew confused at left
        Johnny "But that’s how it is, man…"
        hide Andrew
        show Andrew nervous1 at left
        Johnny "And you know why?"
        hide Johnny
        show Johnny angry1 at right
        hide Andrew
        show Andrew nervous1 at left
        Johnny "Because we’re MEN,{w} and that’s what MEN do."
        hide Andrew
        show Andrew at left
        Johnny "We don't search for love or appreciation...{w} We take {b}care{/b} of the people {b}we care{/b} about."
        hide Johnny
        show Johnny angry2 at right
        Johnny "End of story."
        pause 0.5
        play music "audio/music/Radiohead — Exit Music.wav" fadein 1.5
        pause 2.0
        hide Andrew
        show Andrew sigh2 at left
        Andrew "Heh…{w} Believe me, you don’t get the situation..."
        hide Johnny
        show Johnny angry1 at right
        hide Andrew
        show Andrew at left
        pause 2.0
        hide Johnny
        show Johnny angry1 at right
        Johnny "Perhaps... "
        hide Johnny
        show Johnny confused at right
        extend "Perhaps it's just my prejudices speaking..."
        pause 1.5
        hide Johnny
        show Johnny sigh at right
        Johnny "My sister...{w} Well, she was a complicated woman too."
        hide Johnny
        show Johnny serious1 at right
        Johnny "We never got to understand each other..."
        hide Johnny
        show Johnny confused at right
        hide Andrew
        show Andrew worried1 at left
        Johnny "Still,{w} can't avoid thinking about her in my daily basis."
        pause 1.0
        hide Andrew
        show Andrew smug1 at left
        Andrew "Heh,{w} she's probably way more tolerable than Ashley."
        hide Johnny
        show Johnny chat1 at right
        Johnny "Hey, don't say that. "
        hide Johnny
        show Johnny smug2 at right
        extend "I'll punch you in the nose if you say another word, hahahaha."
        hide Andrew
        show Andrew smug2 at left
        hide Johnny
        show Johnny smile2 at right
        pause 1.5
        hide Johnny
        show Johnny at right
        pause 1.5
        Johnny "She..."
        hide Andrew
        show Andrew confused2 at left
        pause 1.5
        hide Johnny
        show Johnny sigh at right
        Johnny "She's an angel..."
        pause 2.0
        hide Johnny
        show Johnny at right
        Johnny "A-Anyway…{w} that’s beside the point."
        Johnny "The girl downsides told me you have the car-keys,{w} is that right?"
        hide Johnny
        show Johnny serious1 at right
        hide Andrew
        show Andrew sigh at left
        "He let out a sonorous sigh before taking the keys out of his pocket."
        hide Andrew
        show Andrew angry1 at left
        Andrew "Yeah… You can have them."
        Andrew "The car is out of gas anyway, so...{w} here it goes."
        show keys at center
        play sound "audio/sfx/item_got.ogg"
        pause 1.0
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
        pause 1.0
        jump main_route3

    ############################# End Andrew's choices

label main_route3:
    stop music fadeout 2.0
    pause 2.0
    play music "audio/music/Delay.wav" fadein 1.0
    pause 2.0
    "I went down to the bar,{w} ordered something pretty to drink and took a seat."
    "Now,{w} it was time to wait."
    pause 1.5
    scene club1 with fade
    show Ashley mad at right
    show Andrew at left with easeinleft
    "Andrew went stairs down to meet his sister."
    hide Andrew
    show Andrew angry1 at left
    hide Ashley
    show Ashley at right
    "Couldn't ignore how their looks fell over me on more than one occasion."
    hide Andrew
    show Andrew chat1 at left
    hide Ashley
    show Ashley think at right
    "They talk with their tone hiding under the soft sound of the music playing."
    hide Andrew
    show Andrew serious1 at left
    hide Ashley
    show Ashley worried2 at right
    "Off course, there wasn't a way to know what they were saying,{w} but got the feeling that I was a recurring theme."
    hide Andrew
    show Andrew chat1 at left
    hide Ashley
    show Ashley at right
    scene black with fade
    pause 1.5
    play sound "audio/sfx/blingy_sp.ogg"
    pause 1.0
    items "I gift a little smile as they slowly walked out of the bar.{w} Got no answer in exchange."
    pause 0.5
    "They took a quick peek inside the vehicle before moving towards the darkness,{w} where their silhouettes disappeared among the shadows."
    pause 1.0
    show Johnny R at center with fade
    pause 1.0
    "As for me,{w} I stayed there for a little more,{w} trying to imagine what kind of events could have led those two to this particular situation."
    "Maybe something simple..."
    "Maybe something I wasn't able to even think about..."
    stop music fadeout 2.0
    pause 1.0
    hide Johnny
    show Johnny sigh R at center
    pause 1.0
    "And that's about it..."
    scene black with fade
    pause 2.0
    play music "audio/music/Cruel Summer Start.wav"
    queue music "audio/music/Cruel Summer Tense.wav" loop
    pause 5.0
    scene table with fade
    "Entry number one:"
    pause 1.0
    "During the development the stolen Málaga's investigation,{w} I came across a series of unusual events."
    "A death body,{w} a couple of siblings,{w} a death certificates,{w} and a policeman with a strange attitude..."
    "Isolated events,{w} whose origin may not be necessarily related."
    pause 2.0
    "However, once again my mind forces me to shuffle beyond the obvious..."
    "I have that strange feeling again.{w} That feeling of being in front of something dark and dangerous."
    "The tiny protruding tip of a large iceberg emerging from the bottom of the sea."
    pause 2.0
    "During my trip back home,{w} I was able to come up with a couple of connections,{w} just a few dots that kept ringing on my head."
    "I also—{nw}"
    play sound "audio/sfx/mumbling1.wav" volume 0.4
    pause 3.0
    stop sound
    play sound "audio/sfx/static.wav" volume 0.3 fadein 1.0
    Johnny "..."
    stop sound fadeout 1.0
    "I also kept thinking about those two after our first meet."
    Johnny "Andrew...{w} and Ashley..."
    "It’s strange,{w} usually I don’t feel this level of interest with my clients,{w} much less with potential suspects."
    "But this duo…{w} There’s something really interesting about them."
    "A {b}spark{/b}, to call it anything.{w} Something different from everyone else."
    pause 1.5
    Johnny "Those eyes...{w} Those pretty,{w} green and pink eyes..."
    pause 1.5
    "Perhaps I’m just chasing ghosts again...{w} That’s a possibility too."
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
    items "Jonathan has picked up his shovel..."
    play sound "audio/sfx/Steps wood.wav"
    pause 3.0
    play sound "audio/sfx/Wooden door open.wav"
    pause 3.0
    play sound "audio/sfx/mumbling3.wav" loop
    pause 1.0
    "As the door opened, I was blasted with the mumblings of the man dressed in a police suit."
    "Leather ropes restrained his hands and legs,{w} drool and blood dripped from the gag on his mouth."
    "The reflection of fear, a paralyzing horror was reflected in his eyes the moment we exchanged glances."

    if "PoliDemureness" in locals():
        Johnny "I think we've talked enough, officer."
        scene JohnnyF1 with fade
        Johnny "If I can call you that..."
        pause 1.0
        Johnny "You know?{w} I was hoping to play with you a little more.{w} At least for a couple of days, since you were soo kind to me earlier."
        Johnny "I really...{w} REALLY hate liars.{w} I swear they bring out the worst of me."
        scene black
        play sound "audio/sfx/shovel hit1.wav"
        pause 1.0
        Johnny "But let's not start with anecdotes.{w} I have something more important to take care of."
        play sound "audio/sfx/bng sfx/1.wav"
        pause 1.5
        Johnny "Something big!"
        Johnny "And I don't want to be distracted by other {b}minor{/b} stuff.{w} Don't expect you to understand tho."
        Johnny "So let's try not to enjoy this, hm?"
        stop music fadeout 2.0
        play sound "audio/sfx/bng sfx/3.wav"
        pause 3.5
        Johnny "And maybe...{w} try not to make this so dirty..."
        Johnny "Uh...{w} this will take a while to clean up."
        Johnny "Oh well,{w} work for later."
    else:
        Johnny "Hey officer~"
        scene JohnnyF1 with fade
        Johnny "Quite the night we’re having today, huh?"
        Johnny "Moon is shining,{w} very little bugs,{w} a great time to take a walk!"
        Johnny "Or to write your thoughts..."
        scene black
        play sound "audio/sfx/shovel hit1.wav"
        pause 1.5
        Johnny "You see, officer...{w} I am a very reasonable person when you're good with me.{w} And while I must say you haven't been an angel, you did answer all my questions."
        Johnny "But interrupting my writing?"
        play sound "audio/sfx/bng sfx/1.wav"
        pause 2.0
        Johnny "That is a lack of respect to my person...{w} That's very bad officer, someone should teach you to respect others.."
        play sound "audio/sfx/bng sfx/2.wav"
        pause 1.8
        Johnny "Just for that,{w} I'm going to end this interview as quickly as possible."
        Johnny "Because my time is {b}not{/b} for disrespectful people."
        stop music fadeout 2.0
        play sound "audio/sfx/bng sfx/3.wav"
        pause 3.5
        Johnny "uuhh...{w} You splashed on my hands..."
        Johnny "Disgusting...{w} You can't even die cleanly."
        Johnny "You see? That's why you're dead!{w} Because you are disgusting."


    pause 1.0
    play sound "audio/sfx/Steps wood.wav"
    pause 3.0
    scene table with fade
    Johnny "Now...{w} What was I saying?"
    pause 2.0
    Johnny "Oh, yeah!"
    pause 1.5
    "I’m gonna start a new case."
    "Something private,{w} a personal project."
    play music "audio/music/Tow Truck.wav" fadein 4.0
    "I have the feeling that it will be my biggest work yet."
    scene club_night with fade
    pause 1.0
    "And I have the perfect name for it..."

    pause 2.0
    scene end1 with Dissolve(2.0)
    pause 2.0
    menu:
        "Continue with the story? (Remember to save if not.)"

        "Yes.":
            stop music fadeout 1.5
            scene black with Dissolve(1.5)
            pause 2.5
        "No.":
            stop music fadeout 1.5
            scene black with Dissolve(1.5)
            pause 2.5
            return


    ####################### 1° Encounter
label yes_l:
    pause 1.0
    play music "audio/music/The Thing - What Appears to be Normal.wav" fadein 2.0
    pause 3.0
    Andrew "You’ve been pretty quiet."
    pause 1.0
    Ashley "..."
    pause 2.0
    scene M_Room with fade
    show Andrew angry2 at left
    show Ashley mad at right
    Andrew "Come on, just say it..."
    hide Andrew
    show Andrew at left
    Andrew "What's happening?{w} Did the bartender catch you stealing his tips?"
    hide Ashley
    show Ashley smug3 at right
    Ashley "Heh,{w} yeah sure."
    hide Ashley
    show Ashley smug2 at right
    extend " He was too busy looking at that girl’s ass to even notice."
    hide Ashley
    show Ashley worried2 at right
    hide Andrew
    show Andrew angry1 at left
    Ashley "It was a perfect move, if I can say so~"
    hide Andrew
    show Andrew chat1 at left
    hide Ashley
    show Ashley worried1 at right
    Andrew "Then what?{w} Stop acting like it wouldn't be obvious when something's bothering you."
    hide Andrew
    hide Ashley
    show Andrew at left
    show Ashley mad at right
    pause 1.0
    Ashley "..."
    pause 1.0
    Ashley "That guy…{w} the detective."
    hide Ashley
    show Ashley think at right
    extend " Did you notice something off on him?"
    hide Ashley
    show Ashley at right
    Ashley "Something, I don’t know...{w} weird?"
    hide Andrew
    show Andrew chat1 at left
    Andrew "Duh!{w} He IS weird."
    hide Andrew
    show Andrew angry2 at left
    Andrew "He's a guy that believes himself an 80s character."
    hide Andrew
    show Andrew angry1 at left
    Andrew "We spent all the gas trying to escape from him..."
    hide Andrew
    show Andrew at left
    extend " Now we don't even have a vehicle."
    hide Ashley
    show Ashley mad3 at right
    Ashley "You expect me to believe you haven't even thought about it?{w} Seriously Andy?"

    if DualAff > 0:
        jump res1
    else:
        if AshleyAff > 0:
            jump res2
        else:
            jump res3


    label res1:
        hide Ashley
        show Ashley ewww at right
        hide Andrew
        show Andrew worried1 at left
        Ashley "You’re gonna tell me that, {b}YOU{/b} in particular, aren't but a little uneasy by the fact that he let us go like that?"
        hide Ashley
        show Ashley mad3 at right
        Ashley "Without questions…{w} without warnings…{w} just taking the stupid car?"
        pause 2.0
        Andrew "..."
        hide Andrew
        show Andrew serious1 at left
        Andrew "He..."
        hide Ashley
        show Ashley think at right
        extend " He really scared me, ok?"
        hide Andrew
        show Andrew at left
        Andrew "And not in a normal way."
        pause 1.5
        hide Andrew
        show Andrew angry1 at left
        pause 1.5
        Andrew "I made him mad and..."
        extend " he almost jumped on my neck."
        hide Ashley
        show Ashley pout1 at right
        hide Andrew
        show Andrew at left
        Ashley "Awwww little Andy didn't want to throw hands with the big mean detective?"
        hide Ashley
        show Ashley smug1 at right
        hide Andrew
        show Andrew superangry at left
        Andrew "Can you be serious for a second?!"
        hide Ashley
        show Ashley smug2 at right
        hide Andrew
        show Andrew facepalm at left
        Ashley "Never!{w} And I really don't know what you're complaining about."
        hide Ashley
        show Ashley smug3 at right
        hide Andrew
        show Andrew angry2 at left
        Ashley "He was very kind to me."
        hide Ashley
        show Ashley pout1 at right
        hide Andrew
        show Andrew facepalm at left
        extend " Perhaps that's the problem, Aaaaaaaaandy?"
        Ashley "Were you spying our little chatty-chat?"
        hide Andrew
        show Andrew at left
        hide Ashley
        show Ashley smug1 at right
        Andrew "You're impossible."
        jump main_route5

    label res2:
        hide Ashley
        show Ashley ewww at right
        hide Andrew
        show Andrew chat1 at left
        Andrew "Well that's because I would prefer not to think about him."
        hide Andrew
        show Andrew angry2 at left
        Andrew "He just showed up and annoyed me until I gave up the fucking keys..."
        hide Andrew
        show Andrew chat1 at left
        hide Ashley
        show Ashley mad3 at right
        Andrew "And how come up that you're the worried one this time?{w} What did he tell you?"
        hide Ashley
        show Ashley angry1 at right
        hide Andrew
        show Andrew at left
        Ashley "We just talked,{w} he made some questions and I answered."
        hide Andrew
        show Andrew angry1 at left
        hide Ashley
        show Ashley at right
        Andrew "Ok,{w} and?"
        hide Andrew
        show Andrew at left
        pause 1.5
        hide Ashley
        show Ashley mad at right
        pause 1.5
        Ashley "Well..."
        hide Ashley
        show Ashley worried1 at right
        Ashley "He was nice...{w} strangely nice..."
        pause 2.0
        hide Ashley
        show Ashley ewww at right
        hide Andrew
        show Andrew chat1 at left
        Andrew "And that's all?{w} That's what left you so shocked?"
        hide Ashley
        show Ashley mad3 at right
        hide Andrew
        show Andrew angry1 at left
        Andrew "Though I shouldn't be surprised.{w} It's not every day you find someone who can put up with your garbage."
        hide Ashley
        show Ashley mad2 at right
        hide Andrew
        show Andrew facepalm at left
        Ashley "Well at least someone can without being constantly bitching about."
        hide Ashley
        show Ashley ewww at right
        hide Andrew
        show Andrew angry2 at left
        Andrew "Yeah, whatever you say..."
        hide Ashley
        show Ashley mad at right
        hide Andrew
        show Andrew angry1 at left
        jump main_route5

    label res3:
        hide Andrew
        show Andrew chat1 at left
        Andrew "And why would I?"
        extend " Yeah, it is suspicious, but you really think a guy like him could be into something else?"
        hide Ashley
        show Ashley at right
        hide Andrew
        show Andrew angry2 at left
        Andrew "He probably was just a jerk who wanted to go back home and watch his old flashy movies."
        hide Andrew
        show Andrew angry1 at left
        pause 2.0
        hide Andrew
        show Andrew worried1 at left
        Andrew "..."
        pause 2.0
        Ashley "That totally sounded like an excuse, you know?"
        pause 1.5
        hide Andrew
        show Andrew at left
        Andrew "Look, I know it sound strange coming from me, but I really think he isn't dangerous."
        hide Andrew
        show Andrew angry1 at left
        hide Ashley
        show Ashley think at right
        Andrew "We don't need to keep talking about this, if you don't feel like it."
        hide Ashley
        show Ashley at right
        Andrew "It's not like we're short of problems if you want to hear me complain about something..."
        hide Andrew
        show Andrew confused2 at left
        hide Ashley
        show Ashley worried1 at right
        Ashley "No...{w} No, I think I'm not in the mood right now..."
        jump main_route5


label main_route5:
    pause 2.0
    hide Andrew
    show Andrew worried1 at left
    hide Ashley
    show Ashley worried1 at right
    pause 1.5
    Andrew "Do you think we’re gonna see him again?"
    stop music fadeout 2.0
    pause 1.5
    Ashley "I...{w} I don’t know."
    hide Andrew
    show Andrew confused2 at left
    hide Ashley
    show Ashley smug1 at right
    Ashley "But..."
    extend " we do have a way to find out."
    hide Andrew
    show Andrew at left
    hide Ashley
    show Ashley smug3 at right
    Ashley "Well,{w} something like that."
    pause 1.0
    hide Andrew
    show Andrew chat1 at left
    Andrew "Uh…{w} does it mean more soup for dinner?"
    hide Andrew
    show Andrew facepalm at left
    hide Ashley
    show Ashley excited at right
    Ashley "Yes!{w} A lot more soap for dinner!"
    hide Ashley
    show Ashley angry1 at right
    Ashley "And you're gonna be a good boy and love it, understood?"
    scene black with fade
    Andrew "I have a terrible feeling about this..."
    if DualAff > 0:
        Ashley "Yeah, like... with everything else."
    else:
        if AshleyAff > 0:
            Ashley "That's the spirit! haha~"
        else:
            Ashley "Oh,{w} now you do..."

    pause 3.0
    play sound "audio/sfx/typing.wav"
    scene start2 with fade
    pause 3.0
    scene black with fade

    items "I had that weird dream again."
    play music "audio/sfx/static.wav" fadein 2.0 volume 0.6
    pause 3.0
    items "I was on that old, nasty house."
    items "The air was as dense as smoke and the atmosphere jarring and cold."
    items "It was impossible to achieve any kind of calm in a place like this."
    items "It was like being in an abandoned place,{w} a land where you would swear to be alone,{w} but maintaining the certainty that you're not."
    items "And yet,{w} I was tempted by a constant feelings of closeness that tried to distract my mind from the unseen danger."
    pause 1.5
    items "But danger of what?{w} Where and how big?"
    items "I've been there {b}many{/b} times, and even if I know what's around corner, I can't avoid that damn sensation."
    scene dream1 with fade
    items "I was sitting at the table.{w} There was a plate in front of me, but the food was nowhere to be seeing."
    items "But even so, I could smell its scent."
    items "It was hefty and unpleasant{w} — toxic,{w} unhealthy,{w} like the putrid stench that emanates from the stagnant pipes at city's streets."
    stop music fadeout 1.5
    items "And then, after moments of quiet tension...{w} an echo was heard..."
    pause 2.0
    play music "audio/sfx/Humming.wav"
    pause 3.0
    items "It was the voice of a woman,{w} with a voice so relaxing, so perfect that could only exist in the non-existent confines of my mind."
    items "She was humming a beautiful song, "
    play sound "audio/sfx/Coughing.wav" loop volume 0.1
    pause 1.5
    extend "and alongside with it, the incessant symphony of deep and painful coughs."
    items "They were somewhere around,{w} hiding between the malicious shadows and the intoxicating miasma."
    items "But...{w} Why giving me to the labor of searching for them?{w} Like I was going to find them anyway."
    items "No, there was no point on that."
    pause 1.5
    items "Instead,{w} I stood in place to enjoy the mesmerizing tone of the song."
    items "It was... {w} {b}perfect{/b}."
    items "If you gave me the chance,{w} I would've stay there forever just to hear that wonderful voice until my last breath."
    pause 1.5
    items "Apathy reigned over me,{w} the inability to feel any type of happiness, sadness or worry for anyone besides the lady."
    items "I had ears only for her... {w} for that precious and unknown being..."
    pause 1.5
    items "And then...{w} as quick as it began..."
    stop music fadeout 1.0
    pause 1.5
    items "It stopped."
    stop sound fadeout 1.0
    pause 1.0
    play sound "audio/sfx/Body Fall.wav"
    pause 2.0
    items "And a rumble was heard twice before the arrival of silence."
    pause 1.0
    items "The presences that I could feel from the very beginning had completely vanished."
    scene black with fade
    items "And with them,{w} both the color and the sound were swallowed by the darkness,{w} leaving nothing but a complete and absolute black canvas."
    items "Nothing left."
    pause 1.5
    items "Except off course for...{w} me."
    play music "audio/sfx/static.wav" fadein 2.0
    pause 1.5
    items "I was still there."
    items "Somewhere...{w} somehow...{w} sometime..."
    pause 1.0
    items "Existing..."
    pause 1.5
    extend " and maybe not even that."
    stop music fadeout 1.0
    pause 3.0
    play music "audio/music/Provoker - Dark Angel.wav"
    "I've been having this same dumb dream for years now..."
    pause 1.0
    "It doesn't bother me anymore.{w} Actually, it never did."
    "It's just a stupid dream,{w} just there to try to scaring me over and over again."
    "Heh... scaring me."
    "Think about that."
    pause 1.5
    scene Forest1 with fade
    "The only thing that annoys me is the fact that,{w} once I wake up from their disgusting clutches,{w} I am no longer able to fall asleep again."
    "So...{w} with all the pain of the world for another early-start of the morning..."
    "I went out for a walk."
    scene Forest3 with fade
    pause 1.0
    "I love the smell the forest in the morning.{w} It’s clean, fresh, intoxicating."
    "People generally don't come to these parts.{w} They think it’s dangerous."
    "That they’ll be face to face with some freak, get lost or attacked by an animal."
    Johnny "Hah! Poor idiots."
    scene Forest2 with fade
    "Much better for me.{w} It may be a bit lonely, but I prefer it before having all those annoying voices disturbing."
    "Hating them is something easy to learn.{w} What's not, is having to leave this peace to venture into that concrete jungle."
    "That {b}circus{/b} filled with clowns and two legged animals..."
    pause 1.5
    "Uh...{w} but I'm starting over again..."
    scene Forest4 with fade
    "It is how it is...{w} What's the point on trying to fight it anyway?"
    pause 1.0
    "Things like that lead me to think...{w} to dream...{w} to remember..."
    stop music fadeout 2.0
    pause 3.0
    "..."
    "Whatever.{w} That's not the point."
    pause 1.5
    scene black with fade
    "So...{w} I made a small summary of my discoveries regarding the Graves Case."
    play sound "audio/sfx/paper.wav"
    show Pol9 with Dissolve(0.5)
    pause 0.5
    play music "audio/music/Delay.wav" fadein 1.0
    pause 1.0
    "First of all,{w} the supposed official."
    "Couldn't get much information out of him,{w} but his belongings gave me plenty to think about."
    "First of all,{w} his badge didn't belong to an officer on service."
    "It's an old model, one that was changed a few months ago.{w} However,{w} due to the resemblance to the new version,{w} it could very well be used to fool clueless civilians."
    scene Forest4 with fade
    pause 1.0
    "This points to two things."
    "The first thing is the obvious...{w} someone wanted to keep the murder out of it.{w} This wasn't something planned at all."
    "If this is the case,{w} should consider the possibility that police stations are compromised."
    "Not like they're trustworthy anyway..."
    scene black with fade
    "Now,{w} the second thing would be..."
    pause 0.5
    stop music fadeout 1.5
    play sound "audio/sfx/paper.wav"
    show Pol11 with Dissolve(0.5)
    pause 1.0
    "My main concern."
    play music "audio/music/Ennio Morricone - The Thing.wav"
    pause 1.5
    "I found this book inside his pants.{w} It's compact, a bit smaller than a handbook."
    "I read a few pages before going to bed.{w} It seems to be some kind of instruction book or the strange bible of some cult."
    "It is fascinating, but beyond its symbology I doubt there is anything that can be useful."
    "Still...{w} I'll keep it close just in case."
    scene Forest4 with fade
    "And with this,{w} the theory about something bigger than just a car-rob gains strenght."
    "I don't know if I should be happy about that...{w} but it's at least exciting."
    stop music fadeout 1.5
    pause 2.0
    "And then we have the stuff I took from the siblings."
    scene black with fade
    pause 1.0
    play sound "audio/sfx/paper.wav"
    show butcher with Dissolve(0.5)
    pause 1.0
    "The butcher cleaver, for a start."
    play music "audio/music/Delay.wav" fadein 1.0
    "I found something very peculiar on it too."
    "It has a rather…{w} {b}odd{/b} smell stuck to it."
    "Whatever it was used for, they didn't wash it properly.{w} It's like, when you eat fish and leave the cutlery dirty.{w} The stench simply stays there, penetrating like a parasite..."
    "Good thing is that...{w} if there's a smell,{w} then there's also residue on the blade."
    scene Forest4 with fade
    "I have a partner who can help with this.{w} I'll stop by to see him later."
    scene black with fade
    pause 1.0
    play sound "audio/sfx/paper.wav"
    show notepad with Dissolve(0.5)
    pause 1.0
    "My greatest interest,{w} however,{w} is the notepad."
    pause 1.0
    "While yes,{w} the death certificates where a great finding,{w} the numbers written of its pages are way more useful at the moment."
    "Numbers…{w} with names."
    "With that,{w} we have a couple of places to start investigating."
    stop music fadeout 1.5
    pause 1.5
    "And clearly, the first two names I plan to address are..."
    play music "audio/music/Get On My Knees by Brian Deady.wav"
    scene black with fade
    pause 2.0
    Johnny "Mommy and daddy~"
    pause 1.0
    scene Forest5 with fade
    pause 1.0
    Johnny "Hands to work then."
    Johnny "The day has begun."
    scene black
    play sound "audio/sfx/car turning on.wav"
    pause 3.0
    scene drive with fade
    stop sound fadeout 1.0
    pause 1.0
    "I drove towards thenorthern area of the city."
    "His name was Lars.{w} He was an old reliable when it comes to analyzing evidence."
    "Off course, I can’t say we understand each other,{w} but when the work is involve?{w} Then that bastard is a compliant."
    scene LabOut with fade
    pause 1.0
    "The biochemical laboratory waited with its usual quietness.{w} It is rare to find people in this area, and if it happens they are generally not in the mood to even exchange glances with you."
    "That's the exact reason I like to come here."
    scene black with fade
    stop music fadeout 1.5
    pause 1.5
    Johnny "It's time to retrieve a favor"
    pause 1.5
    play music "audio/music/Bully - Walk Theme.wav"
    scene Lab1 with fade
    show Lars 1 right at right
    pause 0.5
    Lars "..."
    pause 0.5
    show Johnny smile2 R at left with easeinleft
    Johnny "Hey pal~"
    show Johnny chat1 R at left
    Johnny "How's the crime going?"
    pause 0.5
    hide Johnny
    show Johnny serious3 R at left
    hide Lars
    show Lars 7 at right
    "As always, I was received by Lar's kind and warm smile."
    show Johnny smile2 R at left
    Lars "Paddle...{w} Let me guess,"
    hide Lars
    show Lars 2 at right
    extend " you’re out of HF already?"
    hide Johnny
    show Johnny chat1 R at left
    Johnny "These have been very productive weeks."
    show Lars 3 at right
    hide Johnny
    show Johnny R at left
    extend " I would’ve paid you a visit, but…{w} you know."
    show Lars 3 at right
    Johnny "This job is killing me..."
    hide Johnny
    show Johnny smile2 R at left
    extend " and not just me~"
    hide Lars
    show Lars 2 at right
    Lars "Uh…{w} the day you pay me a visit I’ll have a window to jump from."
    hide Johnny
    show Johnny R at left
    hide Lars
    show Lars 7 at right
    Lars"And even if that’s not enough to stop you, I can at least make you do some exercise."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "I do plenty of exercise, thank you very much..."
    hide Johnny
    show Johnny confused R at left
    extend " Just…{w} not in the conventional way..."
    hide Johnny
    show Johnny serious1 R at left
    extend " But I do keep myself in check."
    hide Johnny
    show Johnny serious1 R at left
    hide Lars
    show Lars 3 at right
    Lars "Correct, and since you {b}clearly{/b} don’t need it, how about going to a therapist instead?"
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
    hide Johnny
    show Johnny serious2 R at left
    Johnny "Now, changing the subject…"
    play sound "audio/sfx/item_got.ogg"
    items "Jonathan paid 1500 bucks."
    hide Johnny
    show Johnny R at left
    Johnny "For the last liter, and some extra..."
    hide Lars
    show Lars 4 at right
    Lars "An extra?"
    hide Johnny
    show Johnny smug1 R at left
    "Old fox immediately took the message."
    hide Lars
    show Lars 7 at right
    Lars "What is it?{w} I’m not in the mood for games, Paddle.{w} Better be important."
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
    show Johnny serious3 R at left
    Lars "Yuck!{w} That’s disgusting!"
    hide Lars
    show Lars 7 at right
    extend" And very unprofessional..."
    Lars "What are you, 5?"
    hide Johnny
    show Johnny R at left
    Lars "You bring that...{w} old, stinky blade without the slightest care in the world,{w} and expect me to look at it and tell you if anyone has been chopped with it?"
    Lars "Do I look like a genius to you?"
    hide Lars
    show Lars 1 at right
    extend " Because is so, I’m surely not the wish-fulfilling type."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "I expect you to do your job.{w} Use your instruments, play with your tools or do whatever you do with {b}that{/b} machine."
    hide Lars
    show Lars 7 at right
    hide Johnny
    show Johnny confused R at left
    stop music
    Lars "That’s a microwave…"
    pause 1.5
    hide Johnny
    show Johnny smile1 R at left
    hide Lars
    show Lars 2 at right
    Johnny "Yeah..."
    play music "audio/music/Bully - Walk Theme.wav" fadein 1.0
    hide Johnny
    show Johnny serious2 R at left
    Johnny "The point is, I just want to know if there's residues of human flesh or blood in it."
    hide Johnny
    show Johnny R at left
    Johnny "Come on, give me a hand on this."
    pause 1.5
    hide Lars
    show Lars 1 at right
    Lars "You’re being too demanding…{w} And for worse you’re asking me to do it for free."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "Free?"
    hide Johnny
    show Johnny serious2 R at left
    extend " Do I have to remind you the {b}small inconvenient{/b} with your dealer?"
    hide Lars
    show Lars 2 at right
    extend " The one you strongly asked me to intervene in?"
    Johnny "You still own me that favor."
    hide Johnny
    show Johnny serious1 R at left
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
    pause 2.0
    hide Johnny
    show Johnny R at left
    Johnny "Please?"
    pause 2.0
    hide Lars
    show Lars 2 at right
    hide Johnny
    show Johnny confused R at left
    Lars "If I can?{w} Hah!"
    hide Johnny
    show Johnny smile2 R at left
    hide Lars
    show Lars 7 at right
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
    Johnny "Actually,{w} there’s something else I wanted to ask."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "Have you heard about the building [[REDACTED]?{w} The one that caught fire not long ago."
    play music "audio/music/Cruel Summer Tense.wav" fadein 1.5
    pause 1.5
    Lars "..."
    pause 1.0
    hide Lars
    show Lars 1 at right
    Lars "Don’t tell me you’re interested on that."
    hide Johnny
    show Johnny R at left
    Johnny "What do you know?"
    pause 1.5
    hide Lars
    show Lars 3 at right
    Lars "Look…{w} No matter how much the authorities, the media or the people involved try to deny it.{w} There’s some serious bullshit around it."
    hide Lars
    show Lars 2 right at right
    Lars "You won't be able to get much official information about the quarantine buildings, but it's rumored that...{w} one of them...{w} suffered a {b}leak{/b}."
    hide Johnny
    show Johnny confused R at left
    Johnny "A leak..."
    Johnny "You mean someone escaped?"
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
    hide Lars
    show Lars 2 right at right
    hide Johnny
    show Johnny serious1 R at left
    Lars "Don't you think it's strange that a pandemic suddenly emerged in a few buildings?{w} Or the fact that they shoot anyone who approaches the doors?"
    Lars "Or perhaps we should point out the fact that there is no record of any of the alleged victims."
    hide Lars
    show Lars 4 right at right
    Lars"I confirmed that myself."
    hide Johnny
    show Johnny serious2 R at left
    hide Lars
    show Lars 7 at right
    Johnny "I see what you're going for."
    hide Johnny
    show Johnny chat1 R at left
    extend " So the pandemic is nothing but a smokescreen?"
    hide Johnny
    show Johnny smile2 R at left
    hide Lars
    show Lars 2 at right
    Johnny "You know,{w} under normal circumstances I would say that the years begin to take their toll on your little head."
    pause 1.5
    hide Johnny
    show Johnny sigh R at left
    Johnny "But right now..."
    pause 1.5
    hide Johnny
    show Johnny R at left
    Lars "And I'll tell you one last thing..."
    Lars "If you're really convinced on going down that road..."
    hide Lars
    show Lars 1 at right
    Lars "You may like to know that it'll be a little more dangerous than you’re used to."
    hide Johnny
    show Johnny smug1 R at left
    Johnny "And you may like to know that it only encourages me~"
    hide Lars
    show Lars 2 at right
    Lars "Yeah, I supposed to..."
    Lars "Still, I don’t wanna have to look for a new associated.{w} So please keep an eye on that butt of yours, ok?"
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
    stop music fadeout 1.5
    "The pieces kept moving."
    "Good,{w} that's very good..."
    pause 1.5
    play sound "audio/sfx/item_got.ogg"
    show HF
    pause 1.0
    "{i}Jonathan has picked up HF! (hydrofluoric acid){/i}"
    scene black with fade
    pause 1.0
    "So,{w} I took the barrel and moved away."
    stop music fadeout 1.0
    "I started thinking about my next stop as I got closer to the exit."
    play music "audio/music/Ennio Morricone - The Thing.wav"
    play sound "audio/sfx/paper.wav"
    pause 0.5
    show JvC2 with Dissolve(1.0)
    "However, my intentions to leave the place were frustrated by the arrival of...{w} someone...{w} a new face..."
    play sound "audio/sfx/paper.wav"
    show JvC1 with Dissolve(1.0)
    pause 0.5
    "The vision of a man standing right next to my beloved vehicle came to me."
    "He was staring blankly at the window,{w} looking at insides with intentions beyond the mere idea of appreciating its beauty."
    "When our eyes met,{w} I immediately knew that this unfortunate bastard wouldn't cause nothing but trouble."
    play sound "audio/sfx/paper.wav"
    show JvC3 with Dissolve(1.0)
    pause 0.5
    "And without more choices but facing the inevitable, I approached him for the confrontation."
    scene black with fade
    pause 1.0
    scene car1 with fade
    show Carson 1 at right
    show Johnny R at left with easeinleft
    pause 1.0
    show Carson 4 at right
    pause 1.5
    show Carson 5 at right
    show Johnny serious1 R at left
    UnCarson "A nice model, partner.{w} You can easily tell it was made on the glory of our beloved country."
    show Carson 1 at right
    show Johnny serious2 R at left
    "His voice was prideful,{w} lacking of harmful intentions."
    "The suspicion on his eyes,{w} however,{w} revealed something different."
    show Johnny R at left
    show Carson 2 at right
    Johnny "Can I help you, Brother?"
    hide Carson
    show Carson 4 at right
    "His gaze went down to the chemicals before returning to me."
    hide Carson
    show Carson 5 at right
    UnCarson "That’s a nice barrel you have there…"
    hide Carson
    show Carson 1 at right
    extend " A chemistry fan, perhaps?"
    hide Johnny
    show Johnny chat1 R at left
    hide Carson
    show Carson 5 at right
    Johnny "We can say so.{w} I have a couple of bad weeds back in home."
    hide Johnny
    show Johnny smile2 R at left
    extend " They’re a whole problem, but this beauty just burns them like nothing."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "The sad part is that, no matter how much you try to get rid of them, they always find their way back."
    hide Carson
    show Carson 1 at right
    hide Johnny
    show Johnny serious2 R at left
    UnCarson "I can’t be more in agreement with that statement, {b}Mr. Paddle{/b}."
    hide Johnny
    show Johnny confused R at left
    UnCarson "A clean garden is a pride for our beloved country.{w} Its beauty demonstrates the purity of this land,{w} and the commitment of its people."
    Johnny "Uh…{w} Yeah…"
    pause 1.0
    hide Johnny
    show Johnny sigh R at left
    pause 1.0
    hide Johnny
    show Johnny chat1 R at left
    Johnny "Couldn’t avoid to notice that you know me."
    hide Johnny
    show Johnny smile2 R at left
    extend " The pleasure is all yours,{w} I assume presentations aren’t necessary."
    hide Johnny
    show Johnny confused R at left
    hide Carson
    show Carson 1 at right
    Carson "It's Carson,{w} Carson Hasstle."
    Carson "Just a noble instrument of this gorgeous society,{w} or a P.I. for short."
    hide Johnny
    show Johnny serious1 R at left
    Johnny "P.I?"
    hide Johnny
    show Johnny chat1 R at left
    hide Carson
    show Carson 2 at right
    Johnny "Oh, what a surprise. Then, we are two already."
    hide Johnny
    show Johnny smile2 R at left
    Johnny "What brings you to my city, Carson?{w} I can tell that you’re another dream-chaser like me,{w} I respect that."
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
    scene black with fade
    play audio "audio/sfx/Squeaky Glass.wav"
    pause 1.5
    show Pol12
    play audio "audio/sfx/paper.wav"
    pause 1.0
    "He touched the rear window of my car..."
    "He touched...{w} the glass...{w} with his hands..."
    hide Pol12 with Dissolve(1.0)
    play music "audio/music/Cruel Summer ost.wav" fadein 3.0
    "His dirty,{w} disgusting,{w} putrid hands..."
    Carson "You should take care of this.{w} It's pretty dirty you see?"
    scene car1 with fade
    show Carson 2 at right
    show Johnny angry1 R at left
    pause 1.0
    Johnny "Yeah…{w} I'm a little busy right now..."
    Johnny "I have this pretty-big job and...{w} I can’t lose much time on cat-laundries."
    hide Johnny
    show Johnny angry2 R at left
    hide Carson
    show Carson 3 at right
    Carson "A man dedicated to his dream…"
    Carson "I like your kind, Mr. Paddle.{w} I really do…"
    hide Carson
    show Carson 4 at right
    Carson "The problem when you spend that much time thinking on the future is...{w} that you tend to make some mistakes in the present."
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
    Johnny "I’m afraid I don’t, Carson."
    hide Johnny
    show Johnny serious2 R at left
    extend " Because I NEVER make mistakes."
    hide Johnny
    show Johnny serious1 R at left
    hide Carson
    show Carson 5 at right
    Johnny "And I would love to stay here and chit-chat all day about the national constitution,{w} but I need to move on."
    hide Carson
    show Carson 3 at right
    Carson "I see...{w} So I'm not entertaining you any longer.{w} And since we are at it,{w} I’m in the same road right now."
    stop music fadeout 1.5
    scene black with fade
    pause 1.5
    Carson "Hopefully we’ll meet again, Mr. Paddle…{w} You seem like a reasonable guy."
    pause 1.5
    Carson "Are you?{w} A reasonable guy?"
    pause 1.5
    Johnny "I am...{w} when the situation calls for it, off course."
    pause 1.5
    play sound "audio/sfx/Steps stone.wav"
    pause 2.0
    "Who the hell he think he is?"
    play music "audio/music/Cruel Summer tense.wav"
    "Such nerves to even think about coming to my territory,{w} to touch my car,{w} to see me with those…{w} those donkey eyes…"
    "He probably thought he was worth more than a rusted penny."
    "Wanted to play mysterious and all elegant, ha!"
    pause 1.5
    "Everyone’s a macho-man till a cockroach flies.{w} I’m pretty sure he would piss himself with just that.{w} I can't even help to laugh at the thought."
    "That would be worth to watch…"
    pause 2.0
    "Still…{w} Got to admit that left me a little uneasy."
    "I didn't like it...{w} not at all."
    pause 1.5
    "Did he see through me?{w} It surely seemed like that, but..."
    pause 1.0
    "Can you believe that?{w} I didn’t even realize until…{w} until I stopped to write this…"
    "Huh…"
    stop music fadeout 1.5
    pause 1.5
    "Anyway..."
    pause 1.5
    "Better not losing time with that for now."
    "There will be a special moment for Mr. Blondy."
    pause 2.0
    "I'm sure of that."
    "But for now,{w} let's just move on."
    play sound "audio/sfx/car turning on.wav"
    pause 3.0
    play music "audio/music/Bananarama - Cruel Summer.wav"
    pause 2.0
    scene city1 with fade
    "I drove towards the residential area of the city,{w} a small neighbor filled with hundreds of ugly and noisy houses."
    "This kinds of places are very annoying,{w} always so full of unbearable old people, dirty children and neglected animals."
    "The great majority of messed up things use to happen here,{w} and that's not surprising, to be honest."
    "Who wouldn’t become crazy when living in a place like this?"
    "I wouldn’t last a single day without putting an axe on the head of my neighbor."
    scene black with fade
    "I don’t even have an axe, that’s the problem."
    scene car2 with fade
    pause 1.5
    "With help of the names wrote on the notebook,{w} the numbers,{w} and a little chat with the people around here,{w} I managed to reach my destination."
    "It's amazing how easily you can track a person.{w} Perfect for a psycho or someone like me…"
    scene black with fade
    pause 1.0
    "...a little redundant?{w} Yeah, maybe.{w} But I’m not making judgements."
    pause 1.0
    stop music fadeout 1.5
    "And,{w} to my surprise,{w} the moment I made visual contact with the residence,{w} I noticed the presence of someone else in the area."
    "A women,{w} to be more specific."
    play music "audio/music/Bully - Walk Theme.wav"
    pause 2.0
    scene Jul with fade
    "Long straight hair,{w} dressing fresh but with strangely thick arm sleeves."
    "Her figure had a strange feeling of…{w} innocence, I suppose?{w} Her posture didn't help her at all, that's for sure."
    "She looked like the kind of person who would be first on some serial killer's list."
    scene black with fade
    play sound "audio/sfx/car door.wav"
    pause 2.0
    "This was my first encounter with her."
    "Her yellow eyes pointed at me the moment I stood out of the car, and her delicate fingers crossed within each other with palpable nerves."
    scene HouseOut with fade
    show Johnny chat1 R at left
    show Julia at right
    Johnny "Morning, miss."
    show Johnny smug2 R at left
    Johnny "Is this the residence of the Graves family?{w} I would need to have a little talk with them."
    hide Johnny
    hide Julia
    show Johnny smile1 R at left
    show Julia down at right
    UnJulia "Eh?"
    show Julia chat2 at right
    extend " Y-Yes, Mrs. and Mr. Graves lives here…"
    show Johnny confused R at left
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
    "A couple of days...{w} That's not a good sign."
    show Johnny sigh R at left
    hide Julia
    show Julia sad at right
    UnJulia "Maybe it's just...{w} that they don't want to talk to me..."
    UnJulia "I wouldn't blame them..."
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
    items "{i}Jonathan has picked up Human Resources!{/i}"
    play sound "audio/sfx/item_got.ogg"
    items "{i}Jonathan has picked up plastic bags!{/i}"
    pause 1.5
    Johnny "Mind telling me your name again, miss?"
    hide Julia
    show Julia chat2 at right
    UnJulia "Oh, it’s Julia. Julia [[REDACTED].{w} I'm sorry, I didn't mention it."
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
    play music "audio/music/The Thing - The Norwegian Camp.wav"
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
    Julia "What is that?!"
    hide Johnny
    show Johnny chat1 at center
    Johnny "The smell of the {b}adventure{/b}, off course."
    hide Johnny
    show Johnny at center
    extend " And this seems to be a pretty nasty one..."
    pause 2.0
    hide Johnny
    show Johnny serious3 at center
    Johnny "You coming?"
    hide Julia
    show Julia giggle R at left
    hide Johnny
    show Johnny smile2 at center
    Julia "W-What?!{w} You can’t be serious!"
    hide Julia
    show Julia nervous R at left
    hide Johnny
    show Johnny at center
    Johnny "No, I’m actually pretty serious.{w} I've come for answers, and I ain't going anywhere without them."
    hide Johnny
    show Johnny chat1 at center
    Johnny "So, what do you say, cutie?{w} Will you come in for a ride or run away like a little rabbit?"
    hide Johnny
    show Johnny smug1 at center
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
    show Johnny smile2 at center
    hide Julia
    show Julia R at left
    "That was adorable."
    hide Julia
    show Julia sad R at left
    "I tried my best to not laugh, but it wasn’t hard for her to notice."
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
    extend "{b}Andrew{/b} and {b}Ashley{/b} are somehow familiar to you?"
    "At that moment, her heart skipped a beat.{w} A wave of discomfort washed her, as if the mere mention of their names brought with it a storm of emotions."
    Julia "..."
    pause 1.5
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
    "Look what a cute little thing we just found here~"
    hide Johnny
    show Johnny chat1 at center
    Johnny "I see…{w} the emo-boy."
    hide Johnny
    show Johnny smug2 at center
    Johnny "You never say no to a cold one, huh?{w} I respect that."
    hide Johnny
    show Johnny serious1 at center
    hide Julia
    show Julia down R at left
    "Her eyes looked away.{w} The nerves were substituted by a strong sense of sadness, regret, maybe even doubt."
    hide Julia
    show Julia sad R at left
    "But that wasn’t the only."
    "There was a lot of repressed feelings in those eyes…{w} yeah, I could see it."
    hide Julia
    show Julia serious1 R at left
    "Fear,{w} anger,{w} desperation,{w} loneliness…"
    "{b}Betrayal{/b}."
    hide Johnny
    show Johnny smug1 at center
    "That expression was a known one...{w} a very well known, I would say."
    hide Johnny
    show Johnny confused at center
    Johnny "They hurt you."
    hide Julia
    show Julia down R at left
    Julia "..."
    pause 1.5
    hide Julia
    show Julia R at left
    hide Johnny
    show Johnny at center
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
    show Johnny serious1 at center
    "No..."
    pause 1.5
    hide Johnny
    show Johnny angry2 at center
    "No, that’s a dumb idea..."
    "How to trust someone like her?"
    "Someone weak,{w} naive,{w} of short minded and so easy to…"
    stop music fadeout 1.0

    ###################################### JULIA CHOICES

    menu:
        "..."

        "Honesty":
            $ JuliaAff+=1
            jump Honesty
        "Fraudulence":
            $ JuliaAff-=1
            jump Fraudulence

    label Honesty:
        pause 3.0
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
        hide Johnny
        show Johnny sigh at center
        Johnny "But both Andrew and Ashley are alive.{w} I know because I spoke with them yesterday."
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
        "However, the confusion and fear were still there.{w} And as soon as they came, such emotions disappeared."
        hide Johnny
        show Johnny at center
        pause 2.0
        Julia "I can’t believe this..."
        hide Julia
        show Julia nervous R at left
        Julia "It’s impossible, he…"
        hide Julia
        show Julia sad R at left
        pause 1.5
        Julia "I-If he's alive...{w} I want to talk to him."
        hide Julia
        show Julia nervous R at left
        Julia "How can I—{nw}"
        hide Johnny
        show Johnny angry1 at center
        hide Julia
        show Julia R at left
        Johnny "No."
        "I knew I had to stop that thought before it was even born."
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
        Johnny "And maybe...{w} we could find some answers."
        hide Julia
        show Julia sad R at left
        pause 2.0
        hide Johnny
        show Johnny serious2 at center
        Johnny "And?{w} Aren't you gonna say anything?"
        Julia "..."
        pause 2.0
        hide Julia
        show Julia R at left
        Julia "No..."
        hide Johnny
        show Johnny at center
        hide Julia
        show Julia chat1 R at left
        extend" I-I can’t believe that, not without proofs!"
        hide Julia
        show Julia R at left
        hide Johnny
        show Johnny sigh at center
        Johnny "That's also something I can't give you."
        hide Johnny
        show Johnny at center
        Johnny "And you don’t need to believe it if you don't want to."
        Johnny "But that’s the truth, deary.{w} Take it or leave it."
        hide Julia
        show Julia sad R at left
        Julia "..."
        pause 2.0
        Julia "Are you gonna arrest him?"
        Julia "I-I don’t want anything bad to happen to Andrew…"
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
        Johnny "Still, that doesn’t necessarily make him the villain of the story.{w} They are just assumptions."
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
        "I should’ve lied to her.{w} This could’ve been much easier..."
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
        "Suddenly, there wasn't any doubts or nerves on her face."
        hide Johnny
        show Johnny serious1 at center
        "She was just…{w} decided to help.{w} As if something was pushing her down a path of blind faith."
        pause 1.5
        "Why?"
        stop music fadeout 1.0
        scene black with fade
        Johnny "All right…{w} Let's start searching."
        Johnny "And if someone appears,{w} you'll not say a single word to anyone besides me."
        Johnny "Got it?"
        Julia "Yes, detective..."
        Johnny "Johnny is fine, deary…"
        play sound "audio/sfx/whip.wav"
        pause 1.0
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
        show Johnny smug2 at center
        Johnny "Was your boy something like that?"
        hide Julia
        show Julia nervous R at left
        Julia "N-No!{w} Off course not!"
        hide Julia
        show Julia angry R at left
        Julia "He had other problems!"
        hide Julia
        show Julia down R at left
        hide Johnny
        show Johnny serious1 at center
        extend " Like...{w} anyone else..."
        hide Julia
        show Julia scream R at left
        Julia "But he wouldn't hurt a fly!"
        hide Julia
        show Julia nervous R at left
        pause 2.0
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
        show Johnny confused at center
        Johnny "I understand the pain you’re dealing with right now.{w} I’ve seen a lot of people losing their love ones, and I’ve lost mine too."
        Johnny "You must to know I am being completely honest when I say..."
        extend " that I am truly sorry for you."
        hide Julia
        show Julia down R at left
        pause 1.5
        hide Johnny
        show Johnny serious2 at center
        Julia "T-Thank you…{w} I appreciate your condolences."
        hide Johnny
        show Johnny at center
        hide Julia
        show Julia sad R at left
        stop music fadeout 2.0
        Julia "From the deep of my heart,{w} I really hope there was something I could do."
        pause 1.5
        hide Johnny
        show Johnny smug1 at center
        pause 1.5
        hide Julia
        show Julia R at left
        hide Johnny
        show Johnny sigh at center
        Johnny "Maybe I shouldn't be telling you this, but..."
        hide Johnny
        show Johnny serious1 at center
        pause 1.5
        Johnny "Before saying anything,{w} I want to know if I can trust you."
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
        show Julia R at left
        extend " What do you..."
        hide Julia
        show Julia down R at left
        pause 2.0
        hide Johnny
        show Johnny at center
        Julia "Yes."
        Julia "I swear I won't say a single word."
        hide Johnny
        show Johnny smug1 at center
        "Ah,{w} the infamous curiosity strikes again."
        pause 1.0
        hide Johnny
        show Johnny at center
        Johnny "Ok."
        hide Johnny
        show Johnny serious1 at center
        extend " In that case..."
        pause 1.0
        Johnny "Andrew and Ashley didn’t die from an accident."
        stop music
        hide Johnny
        show Johnny sigh at center
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
        pause 2.0
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
        Johnny "Calm down, please... "
        hide Johnny
        show Johnny sigh at center
        hide Julia
        show Julia sad R at left
        extend "Lower your tone.{w} Someone could be hearing..."
        pause 1.0
        hide Johnny
        show Johnny serious1 at center
        Johnny "The police know, but...{w} They're compromised."
        hide Julia
        show Julia R at left
        Julia "W-What do you mean by that?"
        hide Johnny
        show Johnny angry1 at center
        Johnny "That's the thing, Julia."
        hide Johnny
        show Johnny angry2 at center
        Johnny "All this matter,{w} the quarantined buildings,{w} the murders,{w} your boyfriend...{w} is all part of something way bigger."
        hide Johnny
        show Johnny sigh at center
        hide Julia
        show Julia R at left
        Johnny "I can't explain it to you right now, but there's a lot moving in the background."
        hide Johnny
        show Johnny serious1 at center
        hide Julia
        show Julia nervous R at left
        Johnny "Sadly,{w} Andrew and Ashley got caught in the middle,{w} and were disappeared along with many others."
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
        extend "just the way I wanted."
        scene black with fade
        "She was angry,{w} blinded emotions too strong to be contained."
        "Her blood boiled with resentment.{w} She wanted revenge, and who was I to deny such a thing to a spiteful girl?"
        "I would have to move the pieces a little bit, but…{w} I saw myself able to maintain this."
        pause 1.0
        Johnny "All right then, miss Julia.{w} You have my word…{w} We’re gonna put those bastards down."
        pause 1.0
        Julia "T-Thank you... Mr. Paddle..."
        Johnny "Please,{w} call me Johnny."
        stop music fadeout 1.5
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
    Johnny "Come on, you'll get it immediately."
    hide Johnny
    show Johnny at right
    pause 1.0
    hide Julia
    show Julia chat1 R at left
    Julia "Mr. Paddle…"
    hide Julia
    show Julia chat2 R at left
    Julia "I-I mean, Johnny."
    hide Julia
    show Julia chat1 R at left
    Julia "Mr. and Mrs. Graves are a very peculiar kind of…"
    hide Julia
    show Julia R at left
    pause 1.5
    hide Johnny
    show Johnny confused at right
    Julia "D-Did you just said blood and bones?"
    hide Johnny
    show Johnny serious1 at right
    Johnny "Well yes,{w} documents, blood, passports, bones and out of place stuff."
    hide Johnny
    show Johnny at right
    Johnny "Thought I was clear."
    hide Julia
    show Julia chat2 R at left
    Julia "B-B-But are you implying that Mr. and Miss. Graves may be…"
    hide Julia
    show Julia R at left
    hide Johnny
    show Johnny chat1 at right
    Johnny "At the doors of Saint Peter?"
    hide Johnny
    show Johnny smile2 at right
    extend " Well, it’s a possibility."
    hide Johnny
    show Johnny at right
    Johnny "I don’t see them here,{w} and you said they haven’t answered the door in days,{w} so..."
    hide Julia
    show Julia down R at left
    Johnny "We can assume there’s a good chance for that."
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
    hide Johnny
    show Johnny serious1 at right
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
    Johnny "Just…{w} Walk around and scream if you find something."
    hide Julia
    show Julia sad R at left
    Julia "Oh jeez…"
    pause 0.5
    hide Julia
    show Julia at left
    hide Julia with moveoutleft
    pause 1.0
    Julia "I don’t like any of this…"
    hide Johnny
    show Johnny sigh at right
    "She may not be as useful as I thought…"
    "Action clearly aren’t her strength."
    hide Johnny
    show Johnny at right
    "Anyway.{w} Let’s hope Miss Lettuce doesn’t faint for a mouse, and let's start to work."
    scene black with fade
    play sound "audio/sfx/Steps wood.wav"
    items "So, I took a walk through the place."
    "Everything seemed normal at first.{w} Didn't find much beyond the origin of that not-so-great fragrance."
    "The basement was flooded,{w} completely submerged under a layer of nauseating water."
    "The fragrance was way stronger there.{w} It reminded me to that piece of chicken I forget on the fridge last month."
    "Damn that was disgusting…"
    "Off course,{w} wasn't about to swim inside that filth,{w} so I wrote it down as a possible clue and just passed by."
    play sound "audio/sfx/Steps wood.wav"
    pause 2.0
    "I also found a {b}“really messy place”{/b}, to call it something.{w} It seemed like the foundations for what could've been a bathroom."
    "A lot of bricks and materials scattered on the floor,{w} an uninstalled toilet,{w} closed pipelines (thank you)..."
    "The only thing that caught my attention there was a whole on the window."
    "It was large enough for a person to just squeeze inside,{w} and the fact that there was a plank pointing at it from outside didn't demystify my most obvious theory."
    play sound "audio/sfx/Steps wood.wav"
    pause 2.0
    "The other two rooms were just a kitchen and the parent’s room,{w} also lacked of clues or useful information."
    "Nothing."
    stop music fadeout 1.5
    "No papers,{w} no photos,{w} no letters or numbers to call."
    "It was just {b}empty{/b}."
    pause 1.5
    Johnny "Empty..."
    pause 1.0
    "And then,{w} it hit me."
    pause 1.0
    play music "audio/music/Cruel Summer Tense.wav"
    "A question came out,{w} and this brought with it another, which in turn was followed by one more..."
    "Where did the siblings sleep?"
    show Ashley at left with fade
    extend " Where are their photos?"
    show Andrew at right with fade
    extend " Why didn't they even keep their phone numbers?"
    "Where are the memories of a life?"
    pause 1.5
    "Why does it looks like they were avoiding them?"
    pause 1.0
    stop music
    scene HouseIn2
    show Johnny sigh R at right
    show Julia R at left
    Julia "..."
    Julia "Johnny?"
    hide Johnny
    show Johnny confused at right
    "I was detached from my thoughts by the gentle call of Julia."
    hide Johnny
    show Johnny at right
    Johnny "Oh, sorry,{w} I was having an internal monologue."
    hide Julia
    show Julia down R at left
    Julia "..."
    pause 1.5
    Julia "Right…"
    play music "audio/music/Delay.wav"
    hide Julia
    show Julia chat1 R at left
    hide Johnny
    show Johnny serious1 at right
    Julia "I-I just finished looking around the house."
    hide Julia
    show Julia nervous R at left
    Julia "I almost fell into the lake on the basement."
    hide Julia
    show Julia scream R at left
    Julia "God it was disgusting!"
    hide Julia
    show Julia R at left
    extend " I'll be smelling that water for days now."
    hide Johnny
    show Johnny chat1 at right
    Johnny "I've had worse things in my nose, honey."
    hide Johnny
    show Johnny at right
    extend " And I regret most of them..."
    hide Johnny
    show Johnny serious2 at right
    Johnny "Anyway, did you found anything?"
    hide Johnny
    show Johnny at right
    Julia "I’m afraid not."
    hide Johnny
    show Johnny serious1 at right
    hide Julia
    show Julia serious1 R at left
    extend " B-But maybe that's a good thing."
    Julia "It indicates that Mrs. And Mr. Graves haven’t been here for a while..."
    hide Johnny
    show Johnny sigh at right
    Johnny "Huh..."
    hide Johnny
    show Johnny confused at right
    Johnny " Ok, that's something, I guess."
    hide Julia
    show Julia R at left
    hide Johnny
    show Johnny at right
    Johnny "I just came out with something else."
    hide Johnny
    show Johnny sigh at right
    extend " Nothing related with the parents."
    hide Johnny
    show Johnny confused at right
    Johnny "Doesn’t this house seems a little {b}small{/b} for a family of four?"
    hide Johnny
    show Johnny serious1 at right
    hide Julia
    show Julia down R at left
    Johnny "I mean,{w} there aren't even enough beds, unless the siblings share one."
    hide Johnny
    show Johnny confused at right
    Julia "Of four?"
    hide Julia
    show Julia R at left
    Julia "Oh, no, Andrew and his sister didn't live with their parents."
    hide Julia
    show Julia chat2 R at left
    Julia "They made them move out because…"
    hide Julia
    show Julia down R at left
    pause 1.0
    Julia "well..."
    pause 1.0
    hide Julia
    show Julia chat2 R at left
    hide Johnny
    show Johnny serious1 at right
    Julia "I don’t really know why, now that you mention it."
    hide Johnny
    show Johnny sigh at right
    hide Julia
    show Julia down R at left
    "Great, more holes…"
    Johnny "Ok..."
    hide Julia
    show Julia R at left
    hide Johnny
    show Johnny serious1 at right
    extend " Let’s get to the beginning.{w} When did that happened?"
    hide Julia
    show Julia down R at left
    Julia "I would say..."
    hide Julia
    show Julia chat1 R at left
    extend" a couple of weeks before the quarantine started."
    hide Julia
    show Julia down R at left
    Julia "I think it was something abrupt because he didn't tell me until they were in the new apartment."
    hide Johnny
    show Johnny confused at right
    pause 1.5
    hide Julia
    show Julia nervous R at left
    Johnny "Or maybe he just wanted to keep the secret from you, girl…"
    hide Julia
    show Julia R at left
    Julia "What?"
    hide Julia
    show Julia angry R at left
    extend " Don’t say that! Why would he do that?"

    if JuliaAff > 0:
        hide Julia
        show Julia serious1 R at left
        hide Johnny
        show Johnny serious2 at right
        Johnny "Well, maybe he didn’t want to bother you."
        hide Johnny
        show Johnny sigh at right
        extend " It sounds like a complicated situation and blah blah blah..."
        hide Johnny
        show Johnny chat1 at right
        hide Julia
        show Julia R at left
        Johnny "OR..."
        hide Johnny
        show Johnny serious1 at right
        extend " there’s a part of this story we don’t know yet."
        hide Julia
        show Julia serious1 R at left
        pause 1.5
        hide Julia
        show Julia nervous R at left
        Julia "B-But what reasons could he have to lie?"
        hide Johnny
        show Johnny at right
        Johnny "Again, have a couple of theories, but give me some time to refine them."
        hide Johnny
        show Johnny serious1 at right
        hide Julia
        show Julia R at left
        Johnny "What we need to do now is to find their parents."
        hide Johnny
        show Johnny sigh at right
        extend " Maybe they will be able to clear up some doubts."
        hide Julia
        show Julia chat1 R at left
        hide Johnny
        show Johnny serious1 at right
        Julia "I-I can work on that!"
        hide Julia
        show Julia serious1 R at left
        Julia "I may not be an expert, but I know how to use internet and—{nw}"
        hide Julia
        show Julia R at left
        hide Johnny
        show Johnny confused at right
        Johnny "I don’t think internet will help us now, deary."
        hide Johnny
        show Johnny chat1 at right
        Johnny "Best thing you can do now is staying out of the fire."
        play sound "audio/sfx/Whip.wav"
        hide Johnny
        show Johnny P at right
        pause 1.0
        Johnny "And let the professionals work~"
        stop music fadeout 2.0
        hide Julia
        show Julia scream R at left
        Julia "But I can help too!"
        hide Johnny
        show Johnny confused at right
        hide Julia
        show Julia nervous R at left
        Julia "I know I’m not a detective, nor have any idea how to deal with dirty stuff as you probably do, but…"
        hide Julia
        show Julia sad R at left
        hide Johnny
        show Johnny at right
        pause 2.0
        Julia "This is an incomplete page for me."
        play music "audio/music/Radiohead — Exit Music.wav"
        hide Johnny
        show Johnny serious1 at right
        pause 2.0
        Julia "I've been coming to this place for days..."
        Julia "A part of me just wanted Mrs. Graves to open that door and..."
        hide Johnny
        show Johnny confused at right
        extend" to yell at me as much as she wanted."
        pause 1.5
        hide Julia
        show Julia R at left
        Julia "But then you showed up with the idea that Andrew is not only alive but in grave danger."
        pause 1.5
        hide Julia
        show Julia down R at left
        Julia "I can’t accept that,{w} not yet…"
        hide Julia
        show Julia nervous R at left
        hide Johnny
        show Johnny at right
        extend " but I want to know what's happening."
        hide Julia
        show Julia chat1 R at left
        Julia "And I'm willing to get my hands dirty if that's what it takes."
        hide Julia
        show Julia scream R at left
        Julia "So please, let me help with this!"
        hide Julia
        show Julia R at left
        hide Johnny
        show Johnny smile2 at right
        "That was adorable.{w} Little girl was being moved by her emotions."
        "She couldn't even handle the idea of seeing a death body, and still wanted to get deeper into this?"
        hide Johnny
        show Johnny serious2 at right
        "What a joke…"
        "She wasn’t but being a reactionary."
        scene black with fade
        "Without thinking,{w} without considering the dangers,{w} just walking blindly towards nothingness."
        "Dumb girl...{w} Just a poor, dumb girl."
        pause 3.0
        Johnny "Uhh..."
        pause 1.5
        "And yet...{w} there I was for second time,{w} putting a stick in my own wheel."
        play sound "audio/sfx/paper.wav"
        pause 1.5
        "Yes...{w} I gave her my presentation card."
        pause 0.5
        Johnny "Stay out of danger.{w} Call me only if you find something.{w} The line could be pinched, so let's find a meeting point..."
        show Julia with fade
        pause 1.0
        play sound "audio/sfx/blingy_sp.ogg"
        hide Julia
        show Julia smile
        pause 1.2
        "Her eyes lit up like the ones of a child when she heard that."
        Julia "Yes!{w} I’ll do my best, Mr. P..."
        hide Julia
        show Julia giggle
        Julia "I mean, Johnny."
        hide Julia
        show Julia smile
        Johnny "Yeah, yeah..."
        Johnny "Leave me alone now, please…"
        scene black with fade
        "Her silhouette rushed to the end of the living-room before disappearing on the broken entrance."
        "I was left with nothing but the silence and the weight of my thoughts."
        pause 1.5
        scene HouseIn2 with fade
        show Johnny
        "What was even that?"
        hide Johnny
        show Johnny sigh
        "Did I just…{w} compromise an entire case?{w} Just like that?{w} Really, Paddle?"
        "What is wrong with me?{w} That dumb girl will probably spread the voice across the whole city now."
        hide Johnny
        show Johnny angry1
        "Everyone will know what I’m into, and all because I couldn’t lie to…"
        hide Johnny
        show Johnny angry2
        extend " those damn eyes."
        pause 1.5
        hide Johnny
        show Johnny sigh
        Johnny "Uhh…{w} great job, Paddle…{w} great job…"
        scene black with fade
        stop music fadeout 2.0
        pause 2.0
        Johnny "She was very similar to…"
        pause 2.0
        Johnny "huh…{w} nevermind."

    else:
        hide Johnny
        show Johnny at right
        hide Julia
        show Julia R at left
        Johnny "Well I don’t want you to make conclusions,{w} but there's a big chance he's been lying to you."
        hide Julia
        show Julia down R at left
        Julia "N-No..."
        hide Julia
        show Julia nervous R at left
        Julia "W-What are you saying?{w} Why would he do that?"
        hide Johnny
        show Johnny serious1 at right
        Johnny "Have my own theories,{w} but I think that’s something you should ask yourself."
        hide Johnny
        show Johnny serious2 at right
        Johnny "Why do you think he could’ve lied?"
        hide Julia
        show Julia angry R at left
        hide Johnny
        show Johnny at right
        stop music fadeout 1.5
        Julia "I don’t think so!"
        hide Julia
        show Julia nervous R at left
        pause 2.0
        hide Julia
        show Julia sad R at left
        pause 2.0
        hide Julia
        show Julia down R at left
        Julia "…"
        Julia "But…"
        hide Julia
        show Julia R at left
        extend " he used to hide things from me..."
        hide Julia
        show Julia down R at left
        Julia "To make a lot of excuses…"
        hide Julia
        show Julia serious1 R at left
        hide Johnny
        show Johnny confused at right
        extend " to put his sister on everything…"
        pause 2.0
        Johnny "Hello?"
        hide Julia
        show Julia R at left
        Julia "Oh, sorry."
        hide Johnny
        show Johnny smile2 at right
        hide Julia
        show Julia down R at left
        Julia "I just…"
        pause 1.5
        hide Johnny
        show Johnny smug2 at right
        hide Julia
        show Julia nervous R at left
        Johnny "You think his sister had something to do with all this, don’t you?"
        play music "audio/music/Ennio Morricone - The Thing.wav"
        pause 1.5
        hide Julia
        show Julia down at left
        hide Johnny
        show Johnny smug1 at right
        Julia "..."
        Julia "Again,{w} I-I don’t think he had been lying to me."
        pause 2.0
        hide Julia
        show Julia at left
        Julia "But if…"
        hide Julia
        show Julia serious1 at left
        extend " {b}Ashley{/b}…{w} was involved on this…"
        hide Julia
        show Julia R at left
        extend " then I don’t know what to expect."
        "There's a weak spot here."
        hide Johnny
        show Johnny chat1 at right
        Johnny "Sounds like you two have some story."
        hide Johnny
        show Johnny smug2 at right
        Johnny "Wanna pull something out of your chest?"
        hide Johnny
        show Johnny smug1 at right
        hide Julia
        show Julia down R at left
        Johnny "Some... {b}old wounds{/b} perhaps?"
        hide Johnny
        show Johnny smug1 at right
        "For several moments, I received nothing but silence."
        hide Johnny
        show Johnny at right
        "I wasn’t able to read her eyes this time.{w} Her expression was blank,{w} doubtful,{w} as if she were rewinding the same scenario over and over again."
        pause 2.0
        Julia "No."
        pause 1.5
        Julia "I don’t want to."
        pause 1.0
        hide Johnny
        show Johnny smug1 at right
        "But then again,{w} her silence said more than enough."
        pause 0.5
        hide Johnny
        show Johnny chat1 at right
        Johnny "As you like, dear.{w} In that case I think that’s enough."
        hide Julia
        show Julia nervous R at left
        hide Johnny
        show Johnny smile2 at right
        Johnny "For now, I want you out of this house.{w} I’ll stay here and fix everything so nobody will rise their suspicions."
        hide Julia
        show Julia sad R at left
        pause 1.5
        hide Johnny
        show Johnny confused at right
        Julia "I would like to stay in contact."
        hide Julia
        show Julia R at left
        extend " I want to make some research by my own."
        hide Johnny
        show Johnny smile1 at right
        Johnny "Heh...{w} That may be quite dangerous, darling.{w} This is far from your—{nw}"
        hide Johnny
        show Johnny confused at right
        hide Julia
        show Julia scream R at left
        Julia "PLEASE!"
        hide Julia
        show Julia R at left
        extend " Please…"
        hide Julia
        show Julia sad R at left
        extend " just…{w} let me do this."
        hide Julia
        show Julia nervous R at left
        extend " For Andrew."
        hide Johnny
        show Johnny smile2 at right
        "She was making things easier than expected."
        hide Johnny
        show Johnny smug1 at right
        extend" I just wanted to make her beg a little, but it seems like the little girl had made a decision."
        scene black with fade
        "I extended my presentation card as an invitation."
        Johnny "Welcome aboard, miss Jennifer~"
        Johnny "I'm counting on you to stay out of danger and to call me only {b}and only me{/b} if something remotely strange appears."
        Julia "I-It's... Julia."
        Julia "And thank you, Mr. Paddle."

    pause 2.0
    stop music fadeout 2.0
    pause 3.0
    "Got this point,{w} I had the house to myself."
    play music "audio/music/The Thing - The Norwegian Camp.wav"
    "There wasn't much more to do now,{w} but still wanted to see what kind of useful staff I could take."
    "And to begin with…"
    play sound "audio/sfx/item_got.ogg"
    show photo
    pause 1.0
    "{i}Jonathan has picked up a familiar photo!{/i}"
    Johnny "Look what a nice little family.{w} Surely nothing bad could come out of them."
    play sound "audio/sfx/Steps wood.wav"
    scene black with fade
    pause 2.0
    items "Headed outside,{w} this time using the backdoor."
    play sound "audio/sfx/Door Kick Down Break.wav"
    pause 1.5
    scene V_Patch with fade
    show Johnny R at left with easeinleft
    "Before my eyes, a small orchard spread out in all its glory."
    hide Johnny
    show Johnny confused R at left
    "I saw a good number of vegetables and fruits,{w} much fresher than in those rotten market places."
    hide Johnny
    show Johnny sigh R at left
    "I’ve always been a fan of farming,{w} but with a job as demanding as mine it would be impossible to take care of the poor little plants."
    scene black with fade
    Johnny "Good thing these babies are spacious."
    play sound "audio/sfx/paper.wav"
    items "I took a plastic bag from my jacked and began to harvest."
    scene black with fade
    play sound "audio/sfx/harvesting.wav"
    pause 3.0
    "And then…{w} as my hands deliberately stole the precious vegetable from the earth,{w} I started to notice something."
    pause 1.5
    "There was a little lump within the dirt, something hide that was slyly standing out from the rest."
    play sound "audio/sfx/digging.wav"
    pause 1.5
    items "I scratched the surface noticing something hard hiding, so I dug my fingers into it to try pulling it out."
    pause 1.5
    items "It was bigger than I thought,{w} too light and too strange to be just a rock."
    stop sound fadeout 1.5
    pause 1.7
    Johnny "..."
    Johnny "What do we have here?"
    "With every second I admired it, my brain schemed more and more ideas until..."
    Johnny "Huh..."
    pause 1.5
    "I discovered not only what my hands were holding,{w} but that there was more than just one of them under the dirt."
    stop music
    play sound "audio/sfx/item_got.ogg"
    show bones
    pause 1.0
    "{i}Jonathan has picked up scorched human bones!{/i}"
    pause 2.0
    scene black with fade
    pause 1.5
    Johnny "So…{w} this is where Mr. and Mrs. Graves have been hiding."
    pause 2.0
    Johnny "Looks I'm not the only with skeletons in my closet."
    pause 3.0
    play music "audio/music/Karen Aoki - Faith.wav"
    pause 1.5
    scene Ash1 with fade
    pause 2.0
    scene Ash2
    pause 2.0
    scene M_Room with fade
    pause 0.5
    show Ashley tired at right
    Ashley "Uuuuh…{w} I’m not getting use to this…"
    show Ashley at right
    show Andrew confused2 at left with easeinleft
    Andrew "Oh! Look who woke up."
    show Ashley giggle1 at right
    Ashley "Andy!"
    show Ashley mad2 at right
    show Andrew at left
    extend " Did somebody see you?"
    show Ashley at right
    show Andrew angry2 at left
    Andrew "I’m fine…{w} thanks for asking."
    show Andrew serious1 at left
    Andrew "And yes,{w} I threw the bones with…"
    show Andrew angry1 at left
    pause 1.5
    show Andrew serious1 at left
    Andrew "Mom and dad’s skulls…"
    show Andrew angry1 at left
    show Ashley mad at right
    pause 2.0
    show Ashley worried1 at right
    Ashley "You’re still thinking about that, don’t you?"
    show Andrew confused2 at left
    show Ashley at right
    Andrew "What?"
    show Ashley mad at right
    show Andrew chat1 at left
    extend " Oh, you mean how we sold mom and dad’s soul to a demon to then eat their bodies in a half-made soup?"
    show Andrew at left
    show Ashley angry1 at right
    Ashley "I did the best with what I had at hand!"
    show Andrew facepalm at left
    show Ashley mad3 at right
    Ashley "That old cheapskate didn't even have condiments in her cupboard."
    show Andrew angry1 at left
    show Ashley at right
    Andrew "Whatever..."
    show Andrew at left
    extend" that’s not the everything on my mind lately if that's what bothers you."
    show Ashley smug1 at right
    play sound "audio/sfx/blingy_sp.ogg"
    pause 1.0
    Ashley "You're welcome~"
    show Ashley smug3 at right
    show Andrew angry2 at left
    Ashley "What would you do without me, dear Andy?"
    show Andrew what at left
    show Ashley smug1 at right
    Andrew "I would probably be a doctor by now."
    show Andrew confused2 at left
    show Ashley smug2 at right
    Ashley "Chopping living people,{w} chopping death people,{w} what’s the difference anyway?"
    show Ashley smug1 at right
    pause 1.5
    show Ashley worried1 at right
    show Andrew confused at left
    pause 1.5
    show Andrew sigh at left
    Andrew "Oh no…{w} that face again."
    show Andrew at left
    Andrew "What did the dream tell you this time?"
    show Andrew angry2 at left
    extend " And please tell me we're not making a threesome..."
    show Andrew at left
    pause 1.5
    Ashley "..."
    show Ashley worried3 at right
    Ashley "Well…{w} remember the detective?{w} Turns out he was on the dream..."
    show Andrew facepalm at left
    Andrew "Just what we needed..."
    show Andrew at left
    Andrew "Ok, what else?"
    play sound "audio/sfx/Door knocking sound effect.wav"
    show Ashley at right
    show Andrew worried1 at left
    pause 2.1
    Ashley "..."
    Andrew "..."
    pause 1.5
    show Andrew nervous1 at left
    show Ashley think at right
    play sound "audio/sfx/Door knocking sound effect.wav"
    Who "Come on, open up.{w} I know you two are in there."
    show Andrew nervous2 at left
    Andrew "Shit!{w} Who is he?"
    show Ashley at right
    Ashley "Lower the voice, genius.{w} He can hear you."
    show Andrew nervous1 at left
    Andrew "But what do we do?"
    show Andrew nervous2 at left
    show Ashley excited at right
    Ashley "Relax, fancy pants.{w} I have a plan…"
    scene black with fade
    pause 1.0
    Ashley "Call the detective."
    Andrew "What?"
    Ashley "Just call him, damnit!"
    play sound "audio/sfx/Door knocking sound effect.wav"
    pause 2.5
    scene club_night with fade
    pause 1.0
    "Entry number two:"
    scene table with fade
    pause 0.5
    "I got some advances on the Graves Case.{w} Ain’t much, but enough to start putting some pieces together."
    "We got some new players on this little game of ours."
    "That girl, Julia..."
    "She’s…{w} not a person of actions,{w} but her connection with Andrew may give me some good advances."
    "Even if I don’t want to admit it, she could be an important piece on this game."
    "The other one is that blondie."
    "What was his name again?{w} Carson, yeah, that one..."
    pause 1.5
    "Now,{w} I’m not saying that he’s a problem or anything."
    "I mean,{w} imagine that,{w} a random Bob comes to my city and managed to make the hair stand on end."
    "What a bad joke."
    pause 1.5
    "But…{w} he does apply some pressure over my shoulders."
    stop music fadeout 3.0
    scene black
    play sound "audio/sfx/phone ring.wav"
    pause 9.0
    "Who is it now?"
    pause 0.5
    Johnny "Hello?{w} Johnny Paddle,{w} P.I."
    pause 1.5
    Who "..."
    pause 1.5
    Who "Quit it."
    pause 1.0
    play music "audio/sfx/phone off the hook tone - sound effect.wav"
    pause 2.0
    scene club_night with fade
    pause 1.0
    Johnny "What?{w} Hello?{w} Who's there?!"
    pause 3.0
    scene end2 with Dissolve(1.0)
    pause 3.0
    stop music fadeout 1.0
    scene black with fade
    pause 3.0
    "Hello!{w} I'm Ares, creator of this fan-made."
    "Working on this first version of the game was quite an adventure.{w} Since this is the first game I've developed, it's very likely to have some error or problems."
    "I'm still learning,{w} to program, to draw, and even to manipulate audio.{w} Still, I have all the intention of taking this project forward."
    "Thank you very much for giving me a little of your time!"
    "And if you are really enjoying Johnny's story, I would really appreciate it if you could buy me a coffee."
    "I'm not especially proud to ask that,{w} but neither jobs nor money are abundant in my house so... it's a bit of a request for help."
    "But no one is obliged to comply, hahahaha"
    pause 1.5
    "And again, thank you very much for playing <3"



    menu:
        "..."

        "Continue":
            jump main_route6
        "Exit?":
            return
        "Exit!":
            return

    # This ends the game.

    label main_route6:
        scene seriously
        Andrew "CAN'T YOU JUST GET SERIOUS FOR A MOMENT?"


    return
