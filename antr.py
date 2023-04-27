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
textchoice = 0.03
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
playercmd = 'error'

playerhp = 30
enemyhp = 10

enemyname = 'error'
enemyattack = 0

combatstate = 'error'
outcome = 'error'
turnnumber = 0

ammo = 0

enemies = {
    'mansizedbat': [30, 8],
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
    global smoked
    if smoked == 10:
        newprint(RED + '\nWhile lighting your cigarette you start to feel extreme pressure in your chest')
        newprint(RED + '\nYou start feeling light-headed, almost fainting')
        newprint(RED + '\nYou try to hold on but suddenly-')
        newprint(RED + '\nYou fall to the floor in sudden death, you were overtaken by a blood clot in your heart')
        newprint(RED + '\nYOU DIED OF A HEART ATTACK' + END)
        newprint("\nTry not to smoke too much next time, it's bad for your health\n")
        input('\nPress Enter to restart ')
        smoked -= 1
        maingame()
    if 5 >= smoked > 0:
        newprint("\nLighting it up, the nicotine enters into your bloodstream as you inhale the cancerous fumes")
        newprint("\nIt feeds into your addiction")
        newprint("\nYou think that you should probably stop\n")
    if 5 < smoked > 9:
        newprint("\nYou hesitate before putting the lighter to the cigarette")
        newprint("\nYou feel that it's unhealthy to smoke this much")


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
        if loop == 1:
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
        if loop == 3:
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
        if loop == 4:
            playercmd = input('\n')
            if playercmd.lower() in ('go to coat-hanger', 'walk to coat-hanger'):
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
                if loop == 5:
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
                        leavedesk = input('\nWould you like to leave? ')
                        if leavedesk.lower() in {'yes', 'yeah'}:
                            loop = 4
                        else:
                            loop = 5
                    if deskcmd.lower() in {'leave', 'walk away', 'leave desk', 'walk away from desk', ''}:
                        loop = 4

            if playercmd.lower() in ('go to safe', 'walk to safe', 'go safe', ' walk safe'):
                newprint('\nYou walk over to your safe')
                newprint("\nAlthough your neighbourhood is quiet, you still worry about thieves")
                newprint("\nYou set a password for it, but you don't quite remember it\n")
                playercmd = input('\n')
                if playercmd.lower() in (
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
        else:
            newprint('\nI dont understand that command\n')


def store():
    newprint('\nyou go to store lol')


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
    global coatandhat, camera, detectiveid, gun, caffeinated, newlistofapartmentitems, searched
    listofapartmentitems = [(UNDERLINE + '\nYou should probably take a few things before going out' + END),
                            '\nWithin your room you see', '\nThe coat-hanger', '\nYour desk crowded with junk',
                            '\nA safe',
                            '\nYour coffee maker on the kitchen\n',
                            '\nOr you could just leave\n']
    if newlistofapartmentitems == 1:
        listofapartmentitems = ["\nYou don't have anything to do", '\nYou may leave']
    else:
        if coatandhat == 1:
            listofapartmentitems.remove('\nThe coat-hanger')
        if camera == 1 and detectiveid == 1 and searched == 1:
            listofapartmentitems.remove('\nYour desk crowded with junk')
        if gun == 1:
            listofapartmentitems.remove('\nA safe')
        if caffeinated == 1:
            listofapartmentitems.remove('\nYour coffee maker on the kitchen\n')
        if coatandhat == 1 and camera == 1 and detectiveid == 1 and gun == 1 and caffeinated == 1:
            newlistofapartmentitems = 1

    newprint(listofapartmentitems)


def battlestate(enemytype):
    global combatstate, outcome, enemyhp, enemyname
    combatstate = "start"
    outcome = "none"
    enemyname = 'error'
    enemyhp = 'error'

    #  STATES
    while outcome == "none":
        if combatstate == "start":
            introstate(enemytype)

        if combatstate == "playerturn":
            playerturnstate()

        if combatstate == "enemyturn":
            enemyturnstate()

        if combatstate == "winstate":
            winstate()

        if combatstate == "losestate":
            losestate()

        if combatstate == "progressbattle":
            progressbattle()

        if combatstate == "execute":
            return


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
    newprint('Your current HP is ' + str(playerhp))
    newprint("The enemy's HP is " + str(enemyhp))


def checkforwin():
    global combatstate, enemyhp, playerhp
    if enemyhp <= 0:
        combatstate = 'winstate'
    if playerhp <= 0:
        combatstate = 'losestate'


def winstate():
    global outcome
    newprint('\n')
    outcome = 'playerwin'


def losestate():
    global outcome
    newprint('\nYou fail')
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


def playerturnstate():
    global playercmd, combatstate, ammo
    newprint('\nIt is your turn\n')
    playercmd = input('\n')
    if playercmd.lower() in {'shoot', 'shoot your gun', 'shoot your revolver', 'shoot enemy'}:
        newprint('\nYou aim your six shooter at the enemy')
        shootchance = random.randint(1, 10)
        print(shootchance)
        chancetohit(shootchance)
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
        newprint('\n')
    checkforwin()


def enemyturnstate():
    global combatstate
    choice = random.randint(1, 10)

    # light hit
    if choice <= 5:
        newprint('\nThe enemy used a light hit')
        damageunit(enemyattack / 2, "player")
        combatstate = "progressbattle"

    # heavy hit
    if 8 >= choice > 5:
        newprint('\nThe enemy used a heavy hit')
        damageunit(enemyattack, "player")
        combatstate = "progressbattle"

    # unique
    if choice >= 9:
        uniqueattack()
        combatstate = "progressbattle"

    checkforwin()


def uniqueattack():
    newprint('\nTEMPORARY UNIQUE ATTACK')


def chancetohit(shootchance):
    if 2 < shootchance <= 5:
        newprint('\nYou fire... and it grazes the enemy')
        damageunit(8, 'enemy')
        return

    if 5 < shootchance <= 9:
        newprint('\nYou fire... and it hits the enemy')
        damageunit(10, 'enemy')
        return

    if 9 < shootchance:
        newprint('\nYou fire... and it hits a vital organ')
        damageunit(15, 'enemy')
        return

    if shootchance <= 2:
        newprint('\nYou fire... and you completely miss')
        return


maingame()
