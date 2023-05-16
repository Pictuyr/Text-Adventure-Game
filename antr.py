import sys
import time
import random

# HELPING FUNCTIONS

WHITE = '\033[97m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
PURPLEBG = '\033[45m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
REDBG = '\033[41m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

loop = 1
textchoice = 0.0
smoked = 0
coatandhat = 0
detectiveid = 0
camera = 0
gun = 0
cigarette = 1
caffeinated = 0
newdeskitems = 0
newlistofapartmentitems = 0
searched = 0
boughtammo = 0
boughtcigarettes = 0
petrol = 0
playercmd = 'error'

investigatedaltar = 0
investigatedcabinet = 0
investigatedcorpse = 0
investigatedshackles = 0
investigatedmarkings = 0
investigatedritual = 0
money = 0
codex = 0

playerhp = 30
sanity = 100
enemyhp = 10

enemyname = 'error'
enemyattack = 0

combatstate = 'error'
outcome = 'error'
turnnumber = 0
skipplayerturn = 0

ammo = 0
evidence = 0

enemies = {
    'mansizedbat': [30, 6],
    'corpse': [10, 2],
    'cultist': [45, 12],
    'Nyarlathotep': [9999, 18]
}


def maingame():
    global textchoice, loop, smoked, coatandhat, playercmd, playerhp, enemyhp, enemyname, enemyattack
    global combatstate, outcome, turnnumber
    start()


def newprint(y):
    for character in y:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(textchoice)
    time.sleep(0.5)


def testsmoked():
    global smoked, playerhp, sanity
    if smoked == 10:
        newprint(RED + '\nWhile lighting your cigarette you start to feel extreme pressure in your chest')
        newprint(RED + '\nYou start feeling light-headed, almost fainting')
        newprint(RED + '\nYou try to hold on but suddenly-')
        newprint(RED + '\nYou fall to the floor in sudden death, you were overtaken by a blood clot in your heart')
        newprint(RED + '\nYOU DIED OF A HEART ATTACK' + END)
        newprint("\nTry not to smoke too much next time, it's bad for your health\n")
        input('\nPress Enter to restart ')
        smoked = 0
        maingame()
    if 5 >= smoked > 0:
        newprint("\nLighting it up, the nicotine enters into your bloodstream as you inhale the cancerous fumes")
        newprint("\nIt feeds into your addiction")
        newprint("\nYou think that you should probably stop\n")
    if 5 < smoked > 9:
        newprint("\nYou hesitate before putting the lighter to the cigarette")
        newprint("\nYou feel that it's unhealthy to smoke this much")
    newprint('\nYOU GAIN 10 HP, 10 SANITY')
    sanity += 10
    playerhp += 10


# GAME

def start():
    global textchoice
    newprint(PURPLEBG + WHITE + 'A Night to Remember' + END)
    newprint('\n-------------------')
    textspeed = input('\nWould you like FAST, NORMAL, or SLOW text? ')

    if textspeed.lower() == 'slow':
        textchoice = 0.05
    elif textspeed.lower() == 'normal':
        textchoice = 0.04
    elif textspeed.lower() == 'fast':
        textchoice = 0.0
    else:
        print("\nThat's not an option, try again")
        start()

    return apartment()


def apartment():
    global loop, playercmd, coatandhat, camera, searched
    global smoked, cigarette, detectiveid, caffeinated, gun, ammo
    newprint(
        BOLD + "\nAs your eyes gradually open to view your dim apartment room, you can feel a dull pain throbbing in "
               "the back of your head")
    newprint(
        END + "\n(You think to yourself that you should get better sleep next time)")
    newprint(
        BOLD + "\nAs you steep in your cold sweat, you notice that it is only 5:03 AM")
    newprint(
        END + "\nIt's been several months that you've been experiencing nightmares about that particular case. It often"
              " wakes you up in these tenebrous hours... but this morning was different")
    newprint(
        BOLD + "\nIt feels as though something calamitous is going to happen today, even worse than the night terrors"
               " and that case that still haunts you.")
    newprint(
        END + "\nYou can go out for a smoke to calm your anxiety like you always do, but taking a shower could also "
              "help your groggy awakening.\n")

    while loop == 1:
        playercmd = input('\n')
        if playercmd.lower() in {'go for a smoke', 'go for smoke', 'smoke', 'go smoke', 'go to smoke'}:
            newprint("\nYou get up from your bed and walk over to your foggy apartment window. It's raining outside")
            newprint("\nTaking your last cigarette off of your desk, you put it into your mouth")
            smoked += 1
            cigarette -= 1
            testsmoked()
            loop = 2

        elif playercmd.lower() in {'go for a shower', 'go for shower', 'shower', 'go to shower', 'go shower'}:
            newprint('\nYou get up from your bed and walk over to the bathroom door')
            newprint('\nThe bathroom is illuminated by a dim yellow light bulb')
            newprint("\nYou've been meaning to fix it for sometime now")
            newprint("\nStepping into the shower, you turn the knob and feel the warm water")
            newprint("\nYou feel refreshed\n")
            loop = 2

        else:
            newprint("\nI don't understand that command\n")

    while loop == 2:
        newprint("\nYou're a lot more awake than before, however you still feel a stiffness in your joints")
        newprint("\nPerhaps a coffee would be ni-\n")
        newprint(UNDERLINE + "\nA knock suddenly comes from your door\n" + END)
        newprint("\nYou open it up and see a lone newspaper on your doorstep\n")
        loop = 3

    while loop == 3:
        playercmd = input('\n')
        if playercmd.lower() in {'read', 'read newspaper', 'read it', 'look at newspaper', 'look', 'read it',
                                 'pick up newspaper', 'pick it up', 'pick up', 'look it up'}:
            newprint("\nYou decide to pickup the newspaper and read it")
            newprint(BOLD + "\nBREAKING NEWS: Church Caught On Fire, Culprit Still At Large\n")
            newprint(
                END + "\nYour heart starts beating the more you read, It's too similar to" + RED + " the case" + END)
            newprint("\nAs your eyes dart across the page, you find the church's name. Your suspicions were right:")
            newprint(REDBG + "\nSt. Michael's Church of Ash" + END)
            newprint("\nAll though the Church seems inconspicious, it's a cult hidden in plain sight")
            newprint("\nYour vision gets blurry, you're nauseous")
            newprint("\nThe night of " + RED + 'the case' + END + ' comes back to you')
            newprint("\nThe ritual, the screams," + BLUE + " the void" + END)
            newprint("\nYou wish you could go back to save " + GREEN + "him" + END)
            newprint("\nThat's it, You've decided to end this cult's madness in perpetuity\n")
            loop = 4

        else:
            newprint("\nI don't understand that command\n")

    while loop == 4:
        apartmentitems()
        playercmd = input('\n')
        if playercmd.lower() in ('go to coat hanger', 'walk to coat hanger'):
            newprint("\nYou walk over to the coat-hanger by the apartment's exit")
            newprint('\nIt has your brown overcoat and classy hat')
            yesorno = input('\nTake your coat and hat?\n')
            if yesorno.lower() in {'yes', 'yeah'}:
                newprint('\nYou take your clothes\n')
                coatandhat += 1
            if yesorno.lower() in {'no', ''}:
                loop = 4

        if playercmd.lower() in ('go to desk', 'walk to desk', 'go desk', 'walk desk'):
            loop = 5

        while loop == 5:
            newprint("\nYou walk over to your desk")
            newprint("\nThe desk is situated over rotted floorboards causing a creak everytime you move")
            newprint("\nThe desk itself is not in quality condition")
            newprint("\nThe metal legs show signs of rusting and the wood is full of scratches and stains")
            cameraandid()
            deskcmd = input('\n')
            if deskcmd.lower() in {'take camera', 'pick up camera'}:
                newprint("\nYou think it'd be best to take photos of the crime scene")
                newprint("\nYou take your polaroid camera\n")
                camera = 1
            if deskcmd.lower() in {'take id', 'pick up id'}:
                newprint("\nYou should probably take this incase police show up")
                newprint('\nYou pick up your id\n')
                detectiveid = 1
            if deskcmd.lower() in {'look at paper', 'search papers', 'search folders', 'look at folders',
                                   'search ',
                                   'mess',
                                   'search desk',
                                   'pickup paper'}:
                newprint('\nYou go through your mess of papers and folders')
                newprint('\nWhile going through, you spot a page containing underlined text')
                newprint(UNDERLINE + "\nA Study in Scarlet, Publication" + END)
                newprint("\nYou wonder if it's important\n")
                searched = 1
            if deskcmd.lower() in {'leave', 'walk away', 'leave desk', 'walk away from desk', ''}:
                loop = 4

        if playercmd.lower() in ('go to safe', 'walk to safe', 'go safe', ' walk safe'):
            newprint('\nYou walk over to your safe')
            newprint("\nAlthough your neighbourhood is quiet, you still worry about thieves")
            newprint("\nYou set a password for it, but you don't quite remember it\n")
            safecmd = input('\n')
            if safecmd.lower() in (
                    'open safe', 'unlock safe', 'use safe', 'use password', 'input password', 'put password',
                    'type password'):
                opensafe = input('\nPlease input safe password: ')
                if opensafe in '1887':
                    newprint('\nYou unlocked the safe!')
                    newprint("\nIt only contains your gun and full clip for your revolver")
                    takegun = input('\nTake gun and ammo? ')
                    if takegun.lower() in ('yes', 'yeah'):
                        newprint('\nYou place your gun in your leather holster\n')
                        ammo += 6
                        gun = 1
                        loop = 4
                    else:
                        loop = 4
                else:
                    newprint('\nThat is not the password\n')
                    loop = 4
            else:
                loop = 4

        if playercmd.lower() in (
                'go to coffee maker', 'go to kitchen', 'walk to coffee maker', 'walk to kitchen', 'go in kitchen',
                'walk in kitchen', 'go to coffee machine'):
            newprint('\nYou walk to the kitchen')
            newprint("\nIt's quite bare of appliances and dinnerware, but you have the essentials")
            newprint(
                "\nYou left a cup of coffee on the kitchen table from yesterday, you think that you'll wash it "
                "eventually")
            newprint("\nIn fact, your sink holds plates and mugs that you should really be cleaning")
            newprint("\nOtherwise, on the kitchen counter is a coffee machine\n")
            playercmd = input('\n')
            if playercmd.lower() in (
                    'clean dishes', 'go to clean dishes', 'clean cup', 'wash cup', 'wash dishes',
                    'go to wash dishes',
                    'go to sink', 'walk to sink'):
                newprint("\nUnfortunately, you are much too pre-occupied with the current case to do your dishes")
            if playercmd.lower() in ('use coffee machine', 'turn on coffee machine', 'make coffee', 'use coffee '
                                                                                                    'maker'):
                newprint("\nPerhaps having a cup of coffee will ease your mind")
                newprint("\nYou take your coffee grinds and water and put them into the machine")
                newprint("\nIt still amazes you how it works, you only bought it a month ago")
                newprint("\n.")
                newprint("\n.")
                newprint("\n.")
                newprint("\nIt's done")
                newprint("\nAs soon as it cools down enough you drink it down\n")
                caffeinated = 1
            if playercmd.lower() in 'leave':
                loop = 4

        if playercmd.lower() in ('leave', 'leave room', 'leave apartment'):
            newprint("\nIt's time you get to investigating the trepid case at hand\n")
            store()


def store():
    global loop, money, playercmd, ammo, boughtammo, boughtcigarettes, cigarette, petrol, smoked
    newprint('\nYou exit your apartment building into the pouring night and start walking towards your vehicle')
    newprint('\nA frigid night, the wind blows droplets into your face')
    newprint("\nYou get into your beaten up car, it's not much but it's yours")
    newprint("\nAs you start your car, you notice that it doesn't have much fuel")
    newprint('\nIt might be best to drive to the gas station and buy gas for the trip\n')
    newprint("\n            ____")
    newprint("\n        __/  |_\_")
    newprint("\n        |  _     _``-.")
    newprint("\n        '-(O)---(O)--'")
    newprint("\n=================================================\n")
    newprint("\nYou arrive at the gas station")
    newprint("\nStepping outside of the car, you approach the station's store")
    newprint('\nIt only opened just 45 minutes ago.')
    newprint("\nThere's nobody here besides the teenage cashier\n")
    money += 20
    loop = 6

    while loop == 6:
        newprint('\nYou take out your wallet and see that you have ${}'.format(money))
        newprint(UNDERLINE + '\nLooking around, you see' + END)
        storeoptions()
        playercmd = input('\n')
        if playercmd.lower() in {'smoke', 'smoke cigarettte'} and cigarette > 0:
            newprint("\nMaybe not, you're not allowed to smoke in here\n")
        if playercmd.lower() in {'buy ammo', 'walk to ammo', 'walk to counter', 'go to counter', 'walk counter',
                                 'buy cigarettes', 'buy cigarette', 'buy cigarette packs', 'buy ammunition',
                                 ' go to ammo', 'go to cigarettes'}:
            loop = 7

        while loop == 7:
            newprint('\nYou walk over to the counter')
            newprint('\nThe tired cashier greets you in a dull manner')
            newprint('\nWhat would you like to buy?\n')
            storecmd = input('\n')
            if storecmd.lower() in {'ammo', 'buy ammo', 'ammunition', 'buy ammunition'}:
                if money < 15:
                    newprint("\nYou can't buy ammunition with the money you have")
                    loop = 6
                    boughtammo = 1
                    break
                newprint('\nYou ask to buy moon clips for your revolver')
                newprint('\nCashiers ask for $15, you oblige and hand over the money\n')
                money -= 15
                ammo += 12
                newprint('\nYou obtain TWELVE ROUNDS and lose FIFTEEN DOLLARS')
            if storecmd.lower() in {'cigarettes', 'buy cigarettes', 'cigarette packs', 'cigarette pack',
                                    'buy cigarette', 'buy cigarette pack', 'buy cigerette packs'} and money >= 5:
                newprint('\nYou ask to buy a pack of cigarettes')
                newprint('\nThe cashier asks for $5, you oblige and hand over the money\n')
                money -= 5
                cigarette += 12
                boughtcigarettes = 1
            if storecmd.lower() in {'leave', 'walk away from counter', 'walk away'}:
                loop = 6

        if playercmd.lower() in {'walk to petrol canisters', 'buy petrol canisters', 'buy fuel', 'buy petrol',
                                 'buy gas', 'walk to gas', 'walk to fuel', 'go to back', 'walk to back'}:
            newprint('\nYou walk over to the back where petrol canisters are located')
            newprint('\nIt might be a good a idea to buy fuel incase I run out')
            newprint('\nBuy fuel?\n')
            petrolcmd = input('\n')
            if petrolcmd.lower() in {'yes', 'yeah'}:
                if money < 15:
                    newprint("\nYou can't buy fuel with the money you have")
                    break
                newprint('\nYou pick up a petrol canister and take it over to the front counter')
                newprint('\nThe cashier helps you fill up the can')
                newprint('\nIt cost you FIFTEEN DOLLARS\n')
                money -= 15
                petrol = 1
            if petrolcmd.lower() in {'no', 'nah', 'leave'}:
                newprint('\nYou decide not to\n')

        if playercmd.lower() in {'leave', 'leave store'}:
            newprint('\nYou leave the store with the items you bought')
            newprint("\nIt's time to face the crime scene head on\n")
            church()


def church():
    global sanity, cigarette, investigatedaltar, investigatedcabinet, investigatedcorpse, money, loop, playercmd, evidence, smoked, codex
    newprint('\nYou arrive at the scene of the burning, there is yellow tape covering the entire area')
    newprint('\nTrying to supress the memories you duck under the tape and walk up the steps towards the church')
    newprint('\nOne of its religious figures is still standing despite the fire, however its face is deformed')
    newprint("\nAs you step through the burnt gates, the morning sun's warmth hits you in the face")
    newprint("\nEverything is covered in ash, charred, or broken down")
    newprint("\nYou feel that taking a photo of the crime scene would help connect the pieces\n")
    sanity -= 10
    loop = 8

    while loop == 8:
        newprint('\nLooking around you see')
        churchoptions()
        playercmd = input('\n')

        if playercmd.lower() in {'smoke', 'smoke cigarette'} and cigarette > 0:
            testsmoked()
            smoked += 1
            cigarette -= 1

        if playercmd.lower() in {'search altar', 'search the altar', 'investigate altar', 'investigate the altar',
                                 'look at altar', 'look altar', 'walk to altar', 'walk altar', 'go to altar'}:
            loop = 9

            while loop == 9:
                newprint('\nThe altar appears to be undamaged by the fire, quite peculiar')
                newprint(
                    '\nYou step up to the front of the pulpit, its intricate carvings covered in ash but no signs of '
                    'burning')
                newprint(
                    '\nYou go around and walk up to the altar, there is a book and a small shelf area underneath\n')
                altarcmd = input('\n')
                if altarcmd.lower() in {'search book', 'examine book', 'investigate book', 'look at book', 'read book'}:
                    newprint('\nPicking up the book, you notice the leather has an ophidian pattern to it')
                    newprint("\nThe book looks charred, but it's surprisingly fine on the inside")
                    newprint('\nYou flip through the pages of the book, most of them are empty but...')
                    newprint('\nYou find pages that have scrawled eldritch sketches in red ink')
                    newprint('\nIt was as though they could only scratch the pages with their drawing tool')
                    newprint(
                        '\nThis specific drawing seemed to be accompanied with hieroglyphics, but none of the symbols '
                        'seem to be of middle eastern origin')
                    newprint(
                        '\nThe composition seems to be a depiction of a man, in a room, surrounded by what you can '
                        'deduce to be flames')
                    if codex == 0:
                        newprint("\nYou're not sure what the accompanying text says\n")
                    if codex == 1:
                        newprint('\nThe accompanying text says MAY EIGHTEEN NINETEEN EIGHTY, JUDGEMENT AT APRIL SHRINE')
                        newprint('\nWhatever that means')
                    if investigatedaltar > 2:
                        investigatedaltar += 1
                if altarcmd.lower() in {'search shelf', 'search underneath', 'search small shelf', 'investigate shelf',
                                        'investigate underneath', 'investigate small shelf', 'look underneath'}:
                    newprint('\nYou look at the shelf underneath')
                    newprint("\nIt's a little figurine")
                    newprint('\nAs you inspect it in your hands you start to feel a presence behind you')
                    newprint('\nYou feel an immense dread and throw the figure at it')
                    newprint('\n')
                    newprint('\nThere was nothing there.\n')
                    if investigatedaltar > 2:
                        investigatedaltar += 1
                    sanity -= 10
                if altarcmd.lower() in {'leave', 'leave altar', 'walk away'}:
                    loop = 8

        if playercmd.lower() in {'search steel cabinet', 'search the steel cabinet', 'investigate steel cabinet',
                                 'investigate the steel cabinet',
                                 'look at steel cabinet', 'look steel cabinet', 'walk to steel cabinet',
                                 'walk steel cabinet', 'go to steel cabinet'}:
            newprint('\nYou walk over to the steel cabinet')
            newprint('\nYou take a good look at it')
            newprint('\nSuddenly, you hear a loud thrashing within the cabinet')
            newprint('\nOpen cabinet?')
            cabinetcmd = input('\n')
            if cabinetcmd.lower() in {'yes'}:
                investigatedcabinet = 1
                newprint('\nYou take the handle and tur-')
                newprint('\nA man-sized bat unexpectedly bursts through the cabinet')
                wincheck = battlestate(0)
                if wincheck == 1:
                    newprint("\nYou successfully defended against the bat's attack")
                    newprint('\nWhy was it so big?')
                    newprint('\nYou find a book full of translations for hieroglyphics')
                    newprint('\nThis might be useful somewhere else')
                    newprint('\nYou take a photo for evidence\n')
                    evidence += 1
                    codex = 1
                if wincheck == 2:
                    newprint(RED + '\nWhile you make your last stand against the man-sized bat')
                    newprint(RED + '\nYou feel weak in the knees, your body slumped, your heart racing')
                    newprint(RED + "\nYou go for one final gun shot, but it's too late")
                    newprint(RED + "\nIt has already flown in from above and punctured your skull")
                    newprint(RED + '\nYOU DIED FROM A BAT ATTACK' + END)
                    break

        if playercmd.lower() in {'search corpses', 'search the corpses', 'investigate corpses',
                                 'investigate the corpses',
                                 'look at corpses', 'look corpses', 'walk to corpses',
                                 'walk corpses', 'go to corpses'}:
            newprint('\nYou walk over to the charred remains of what appear to be the followers of the church')
            newprint('\nA ghastly site, you carefully step over the bodies so as not to desecrate them')
            newprint('\nThe smell is putrid')
            newprint('\nInsects crawl in and over the corpses\n')
            corpsecmd = input('\n')
            if corpsecmd.lower() in {'take photo', 'use camera', 'investigate'}:
                newprint('\nAll though grim, you take a photo as evidence for your investigation\n')
                sanity -= 5
                evidence += 1
                investigatedcorpse = 1
            if corpsecmd.lower() in {'leave'}:
                loop = 8

        if playercmd.lower() in {'search trapdoor', 'search the trapdoor', 'investigate trapdoor',
                                 'investigate the trapdoor',
                                 'look at trapdoor', 'look trapdoor', 'walk to trapdoor',
                                 'walk trapdoor', 'go to trapdoor'}:
            newprint('\nOpening the trapdoor, it descends down into a basement area')
            newprint('\nDescend?\n')
            trapdoorcmd = input('\n')

            if trapdoorcmd.lower() in {'yes'}:
                trapdoor()


def trapdoor():
    global sanity, cigarette, loop, playercmd, evidence, smoked, investigatedshackles, investigatedmarkings, investigatedritual
    newprint('\nPeering in, the basement has shackles, markings, dried blood, fresh blood, ashes')
    newprint("\nIt doesn't seem to have been affected by the arson on top")
    newprint('\nYou hesitate going down, but it could help in solving the case')
    newprint("\nAs you descend down the rickety ladder, you start to regret your decision to take on the case")
    newprint("\nBut your conscience reprimands you")
    newprint("\nYou remember why you're doing this")
    newprint("\nMaybe it'll finally stop the night terrors, to forgive yourself of what you had done")
    newprint("\nTo forgive yourself of your cowardice, how you failed your partner")
    newprint("\nYou relive your last case over and over again every time you try to sleep")
    newprint("\nYou let the culprits get away with their horrors, you let your partner-")
    newprint('\nSnapping out of it, you go back to the case at hand')
    newprint("\nYou feel that taking a photo of the crime scene would help connect the pieces\n")
    loop = 10
    sanity -= 10

    while loop == 10:
        newprint('\nLooking around in the dingy stone room around you, you see')
        trapdooroptions()
        playercmd = input('\n')

        if playercmd.lower() in {'smoke', 'smoke cigarette'} and cigarette > 0:
            testsmoked()
            smoked += 1
            cigarette -= 1

        if playercmd.lower() in {'search shackles', 'search the shackles', 'investigate shackles',
                                 'investigate the shackles',
                                 'look at shackles', 'look shackles', 'walk to shackles',
                                 'walk shackles', 'go to shackles'}:
            newprint('\nWalking over to the shackles you notice rusting around the shackles')
            newprint("\nYou don't see any evidence of water")
            shacklescmd = input('\n')
            if shacklescmd.lower() in {'take photo', 'use camera', 'investigate'}:
                newprint('\nYou take a photo of the shackles, it was most likely used for torture')
                newprint('\nBut what why would this church need to interrogate people?')
                newprint('\nMaybe they were purging defiant members here')
                newprint('\nIt would explain all the blood around')
                sanity -= 5
                evidence += 1
                investigatedshackles = 1
            if shacklescmd.lower() in {'leave'}:
                loop = 10

        if playercmd.lower() in {'search markings', 'search the markings', 'investigate markings',
                                 'investigate the markings',
                                 'look at markings', 'look markings', 'walk to markings',
                                 'walk markings', 'go to markings'}:
            newprint('\nYou look at the markings on the wall')
            newprint('\nStone dust litters the floor')
            newprint('\nThe markings appear to be mathematics, abstract shapes, runes')
            newprint("\nYou can't discern what the math is equal to")
            newprint('\nThe runes are unintelligible, but you do recognize it from your last case')
            newprint('\nIt appears to be a language exclusive to this church')
            newprint('\nThe abstract shapes tell a story, it seems')
            newprint('\nIt begins at what appears to be a crude drawing of Earth')
            newprint('\nThen mankind inhabiting the land, wars, famine, drought, all pictured')
            newprint('\nFinally, mankind bows down to a being')
            newprint(
                '\nThat being looks as though it is made up of the several appendages attached to an eternally '
                'burning mass')
            newprint('\nEyes and mouths are all over the being')
            newprint(
                '\nThis being spreads flames all across the land, burning everything in its path, no matter follower '
                'or heathen')
            newprint(
                '\nYou think that the being is uncaring of the world, that it could even be unbeknownst of our '
                'existence')
            newprint("\nBut... what are you even thinking?! This being doesn't existence")
            newprint("\nYou can't shake this feeling though that, maybe our gods are wrong")
            markingscmd = input('\n')
            if markingscmd.lower() in {'take photo', 'use camera', 'investigate'}:
                newprint('\nYou take a photo of the markings')
                newprint('\nYou see another part of the story on the wall')
                newprint('\nIt looks like it was drawn on the floor instead')
                newprint('\nThe molten being looks to be repelled/banished by the ritual circle drawn on the ground')
                sanity -= 5
                evidence += 1
                investigatedmarkings = 1
            if markingscmd.lower() in {'leave'}:
                loop = 10

        if playercmd.lower() in {'search ritual circle', 'search the ritual circle', 'investigate ritual circle',
                                 'investigate the ritual circle',
                                 'look at ritual circle', 'look ritual circle', 'walk to ritual circle',
                                 'walk ritual circle', 'go to ritual circle'}:
            newprint('\nYou go over to the ritual circle on the ground')
            newprint("\nAt least, that's what you assume it to be")
            newprint('\nIntricate lines, curves, dots are drawn within the circle')
            newprint('\nBurn marks are seen around the ritual circle')
            newprint('\nThe copper stench is permeates around the room')
            ritualcmd = input('\n')
            if ritualcmd.lower() in {'take photo', 'use camera', 'investigate'}:
                newprint('\nYou take a photo of the ritual circle')
                sanity -= 5
                evidence += 1
                investigatedritual = 1
            if ritualcmd.lower() in {'leave'}:
                loop = 10

        if playercmd.lower() in {'search door', 'search the door', 'investigate door',
                                 'investigate the door',
                                 'look at door', 'look door', 'walk to door',
                                 'walk door', 'go to door'}:
            newprint("\nThe rusted door calls to you, like it's whispering at you")
            newprint('\nYou feel yourself stepping towards it')
            newprint('\nYour hand places it on the handle')
            newprint('\nDo you want to enter?\n')
            doorcmd = input('\n')
            if doorcmd.lower() in {'yes'}:
                door()
            if doorcmd.lower() in {'leave'}:
                loop = 10


def door():
    global sanity, cigarette, loop, playercmd, evidence, smoked
    newprint('\nYou slowly open the door')
    newprint('\nThe room is barren, the only thing in the room is the wooden door on the opposite side')
    newprint('\nBlood and rust is all over the metallic room')
    newprint('\nAs you observe your surroundings, the door suddenly shuts')
    newprint('\nYou look back, you thought that was strange')
    newprint('\nWhen you turn back, a corpse is suddenly on the ground')
    newprint("\nFear shoots up your body, but it seems to be dead")
    newprint('\nAs you walk past it, your leg is instantly caught by its hand')
    newprint('\nIt grabs you with immense strength')
    newprint('\nYou kick the corpse off your leg and prepare yourself')
    newprint("\nHow the hell did it just move? Isn't it dead?")
    newprint('\nWhile your mind deliberates the possibilities, it rises to its feet')
    newprint("\nIts face eerily looks like someone you know...\n")
    wincheck = battlestate(1)
    if wincheck == 1:
        newprint('\nYou are taken aback by the undead corpse')
        newprint('\nA headache permeates throughout your mind')
        newprint("\nIt's impossible to think straight")
        newprint("\nThoughts race throughout your mind, every memory, every idea")
        newprint('\nYou attempt to push through and head towards the door')
        newprint('\nAt the door you take your hand')
        newprint('\nPush the door open')
        newprint('\n')
        newprint('\n')
        newprint('\n')
        newprint("\nIt's the same room...?")
        newprint('\nEND OF PART ONE')
        return
    if wincheck == 2:
        newprint(RED + "\nThe corpse' constant screaming rattles your brain")
        newprint(RED + '\nYou cover your ears but you feel blood start to leak')
        newprint(RED + "\nThe walls around you turn into eyes and mouths")
        newprint(RED + "\nRotting appendages shoot out of the walls")
        newprint(RED + "\nThey grab you at your limbs")
        newprint(RED + "\nThe room closes in on you")
        newprint(RED + "\nIt consumes you whole")
        newprint(RED + '\nYOU DIED FROM YOUR OWN MIND' + END)
        return

def trapdooroptions():
    global investigatedshackles, investigatedmarkings, investigatedritual
    trapdooritems = ['\nThe shackles attached to the wall', '\nThe markings written all over the room',
                     '\nThe ritual circle on the floor',
                     '\nThe rusted door']

    if investigatedshackles == 1:
        trapdooritems.remove('\nThe shackles attached to the wall')
    if investigatedmarkings == 1:
        trapdooritems.remove('\nThe markings written all over the room')
    if investigatedritual == 1:
        trapdooritems.remove('\nThe ritual circle on the floor')
    newprint(trapdooritems)


def churchoptions():
    global investigatedaltar, investigatedcabinet, investigatedcorpse
    churchitems = ['\nThe altar that appears to be intact', '\nThe corpses on the pews', '\nThe steel cabinet',
                   '\nThe trapdoor']

    if investigatedcabinet == 1:
        churchitems.remove('\nThe steel cabinet')
    if investigatedcorpse == 1:
        churchitems.remove('\nThe corpses on the pews')
    if investigatedaltar == 2:
        churchitems.remove('\nThe altar that appears to be intact')
    newprint(churchitems)


def storeoptions():
    global money, boughtammo, petrol, boughtcigarettes, money
    storeitems = ['\nPetrol canisters near the back', '\nCigarette packs at the counter', '\nAmmo behind the counter',
                  '\nOr you can leave']
    if petrol == 1 and boughtcigarettes == 1 or boughtammo == 1 and petrol == 1 or money == 0:
        storeitems = ["\nYou don't have money to buy anything else"]
    elif petrol == 1:
        storeitems.remove('\nPetrol canisters near the back')
    elif boughtammo == 1:
        storeitems.remove('\nCigarette packs at the counter')
    elif boughtcigarettes == 1:
        storeitems.remove('\nAmmo behind the counter')
    newprint(storeitems)


def cameraandid():
    global newdeskitems, detectiveid, camera
    deskitems = ['\nYour desk is crowded with books, papers, folders', ', you can also see', ' your camera', ' and',
                 ' your id']

    if newdeskitems == 1:
        deskitems = ['\nYour desk is crowded with books, papers, folders']
    elif camera == 1 and detectiveid == 1:
        deskitems.remove(', you can also see')
        deskitems.remove(' your camera')
        deskitems.remove(' and')
        deskitems.remove(' your id')
        newdeskitems = 1
    elif camera == 1:
        deskitems.remove(' your camera')
        deskitems.remove(' and')
    elif detectiveid == 1:
        deskitems.remove(' and')
        deskitems.remove(' your id')

    newprint(deskitems)


def apartmentitems():
    global coatandhat, camera, detectiveid, gun, caffeinated, searched
    listofapartmentitems = [(UNDERLINE + '\nYou should probably take a few things before going out' + END),
                            '\nWithin your room you see', '\nThe coat-hanger', '\nYour desk crowded with junk',
                            '\nA safe',
                            '\nYour coffee maker on the kitchen\n',
                            '\nOr you could just leave\n']

    if coatandhat == 1 and camera == 1 and detectiveid == 1 and gun == 1 and caffeinated == 1:
        listofapartmentitems = ["\nYou don't have anything to do"]
    elif coatandhat == 1:
        listofapartmentitems.remove('\nThe coat-hanger')
    elif camera == 1 and detectiveid == 1 and searched == 1:
        listofapartmentitems.remove('\nYour desk crowded with junk')
    elif gun == 1:
        listofapartmentitems.remove('\nA safe')
    elif caffeinated == 1:
        listofapartmentitems.remove('\nYour coffee maker on the kitchen\n')
    newprint(listofapartmentitems)


def battlestate(enemytype):
    global combatstate, outcome, enemyhp, enemyname
    newprint('\nCOMBAT INITIATED')
    combatstate = "start"
    outcome = "none"
    enemyname = 'error'
    enemyhp = 'error'

    #  STATES
    while outcome == "none":
        if combatstate == "start":
            introstate(enemytype)

        if combatstate == "playerturn":
            playerturnstate(enemytype)

        if combatstate == "enemyturn":
            enemyturnstate(enemytype)

        if combatstate == "winstate":
            winstate()

        if combatstate == "losestate":
            losestate()

        if combatstate == "progressbattle":
            progressbattle()

        if combatstate == "execute":
            return
    if outcome == 'playerwin':
        return 1
    if outcome == 'playerlose':
        return 2


def introstate(enemytype):
    global enemyname
    global enemyattack
    global combatstate
    global playerhp
    global enemyhp
    enemyname = list(enemies)[enemytype]
    enemyhp = list(enemies.values())[enemytype][0]
    enemyattack = list(enemies.values())[enemytype][1]
    combatstate = 'playerturn'


def progressbattle():
    global turnnumber, combatstate, enemyhp, playerhp
    turnnumber += 1
    newprint('\nTurn {}'.format(turnnumber))
    combatstate = "playerturn"
    newprint('\nYour current HP is ' + str(playerhp))
    newprint("\nThe enemy's HP is " + str(enemyhp))


def checkforwin():
    global combatstate, enemyhp, playerhp
    if enemyhp <= 0:
        combatstate = 'winstate'
    if playerhp <= 0:
        combatstate = 'losestate'


def winstate():
    global outcome
    newprint('\nYou have won the battle')
    outcome = 'playerwin'


def losestate():
    global outcome
    newprint('\nYou have failed the battle')
    outcome = 'playerlose'


def damageunit(damage, unit):
    global enemyname, enemyhp, playerhp, combatstate
    flavourtext = False
    if unit == 'player':
        if damage <= 5 and playerhp <= 20 and flavourtext is False:
            newprint('\nWeak hit ' + str(damage))
            flavourtext = True

        if damage <= 10 and playerhp <= 10 and flavourtext is False:
            newprint('\nThe enemy attacks for ' + str(damage))
            flavourtext = True

        if 11 <= damage and flavourtext is False:
            newprint('\nThe enemy critically strikes you for ' + str(damage))
            flavourtext = True

        playerhp -= damage

    if unit == 'enemy':
        if damage >= (enemyhp / 2):
            newprint('\nYou attack for ' + str(damage))
        enemyhp -= damage


def playerturnstate(enemytype):
    global playercmd, combatstate, ammo, sanity, smoked, cigarette, skipplayerturn
    if skipplayerturn == 1:
        newprint('\nYour turn has been skipped')
        skipplayerturn -= 1
        combatstate = "enemyturn"
        return

    newprint('\nIt is your turn')
    if sanity < 50:
        newprint('\nYou clutch your head, the enemy seems to warp in and out of reality\n')
    playercmd = input('\n')

    if playercmd.lower() in {'shoot', 'shoot your gun', 'shoot your revolver', 'shoot enemy', 'use gun', 'shoot gun'}:
        newprint('\nYou aim your six shooter at the enemy')
        shootchance = random.randint(1, 10)
        chancetohit(shootchance)
        ammo -= 1
        combatstate = "enemyturn"

    if playercmd.lower() in {'reload', 'reload gun', 'reload weapon'} and ammo > 6:
        newprint("\nYou take a revolver round from your pocket and load it into your gun's chamber")
        ammo += 1
        combatstate = 'enemyturn'

    if playercmd.lower() in {'punch', 'melee', 'punch enemy', 'melee enemy'}:
        newprint('\nYou attack the enemy with your fist')
        damageunit(5, 'enemy')
        combatstate = 'enemyturn'

    if playercmd.lower() in {'light', 'use lighter', 'use lighter on enemy', 'light enemy on fire'}:
        newprint('\nYou use your lighter on the enemy')
        damageunit(1, 'enemy')
        if enemytype == 1:
            damageunit(10, 'enemy')
        combatstate = 'enemyturn'

    if playercmd.lower() in {'smoke', 'smoke cigarette'} and cigarette > 0:
        testsmoked()
        smoked += 1
        cigarette -= 1
        combatstate = 'enemyturn'

    checkforwin()


def enemyturnstate(enemytype):
    global combatstate
    choice = random.randint(1, 10)

    if enemytype == 1:
        if choice <= 4:
            uniqueattack(enemytype)
            combatstate = 'progressbattle'

        if choice > 4:
            newprint("\nThe corpse flails it's arms around, but it misses")
            combatstate = 'progressbattle'

    # light hit
    elif choice <= 5:
        newprint('\nThe enemy used a light hit')
        damageunit(enemyattack / 2, "player")
        combatstate = "progressbattle"

    # heavy hit
    elif 8 >= choice > 5:
        newprint('\nThe enemy used a heavy hit')
        damageunit(enemyattack, "player")
        combatstate = "progressbattle"

    # unique
    elif choice >= 9:
        newprint('\nThe enemy used a critical hit')
        damageunit(enemyattack * 1.5, 'player')
        combatstate = "progressbattle"

    checkforwin()


def uniqueattack(enemytype):
    global sanity, skipplayerturn
    choice = random.randint(1, 3)

    if enemytype == 1:
        if choice == 1:
            newprint('\nThe corpse speaks to you, it reprimands you, it cries in anger, fear, distress')
            newprint('\nThe corpse affects your sanity by 2')
            sanity -= 2
            damageunit(enemyattack, 'player')
            skipplayerturn += 1

        if choice == 2:
            newprint('\nYou stare the corpse in the face, you start to tear up as you realise what he looks like')
            newprint('\nThe corpse affects your sanity by 2')
            sanity -= 2
            damageunit(enemyattack, 'player')
            skipplayerturn += 1

        if choice == 3:
            newprint(
                '\nThe corpse screams at you, the piercing scream makes you drop your weapon as you cover your ears')
            newprint('\nThe corpse affects your sanity by 2')
            sanity -= 2
            damageunit(enemyattack, 'player')
            skipplayerturn += 1


def chancetohit(shootchance):
    global sanity

    if sanity <= 50 and shootchance >= 6:
        newprint(
            '\nWith your hand tremors, it gets harder to focus on the enemy, however, you managed to hit your shot')
        damageunit(10, 'enemy')
        return

    if sanity <= 50 and shootchance < 6:
        newprint('\nWith your hand tremors, it gets harder to focus on the enemy, you miss your shot')
        return

    if 2 < shootchance <= 5 and sanity > 50:
        newprint('\nYou fire... and it grazes the enemy')
        damageunit(8, 'enemy')
        return

    if 5 < shootchance <= 9 and sanity > 50:
        newprint('\nYou fire... and it hits the enemy')
        damageunit(10, 'enemy')
        return

    if 9 < shootchance and sanity > 50:
        newprint('\nYou fire... and it hits a vital organ')
        damageunit(15, 'enemy')
        return

    if shootchance <= 2 and sanity > 51:
        newprint('\nYou fire... and you completely miss')
        return


start()
