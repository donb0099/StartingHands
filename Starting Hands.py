#! python3
#-------------------------------------------------------------------------------
# Name:        Starting Hands
# Purpose:     Given the 2 down cards dealt in Texas Hold'em, determine the
#              action to take at your turn.  Based on a table I read in a
#              book on tournament poker.
# Author:      Don Blaskowsky
#
# Completed:   18/08/2020
# Copyright:   (c) Donb 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import re
sys.path.append('C:UCSDE\Python Projects\Starting Hands')
from StartingHandsTables import *

sys.stdout.write("hello from Python %s\n" % (sys.version,))

##  RegExs used to validate input
validTest = re.compile(r"""^[akqjt2-9]{2,2}[s]$   # for suited hands
                          |^[akqjt2-9]{2,2}$      # for unsuited hands
                          |^[q]$                  # to force end of input"""
                          , re.VERBOSE)
PositionTest = re.compile(r"^[bs*123456]$")

##  Globals.
##  Once entered on input, these do not change for the rest of this
##  iteration of the script.

suited = False         # True if suited, False if unsuited
hand = 'xx'            # xxs for suited and xx for unsuited input by user
highCard = 'x'        # After entry, the highest card is in this variable
lowCard  = 'x'        # After entry, the lowest card is in this variable
position = 'b'        # The position at the table relative to the button

def orderPocketCards():
    ''' get card weights, and return a tuple of (highest, lowest).'''
    global highCard
    global lowCard
    if CardValues.get(hand[0]) < CardValues.get(hand[1]):
        highCard = hand[1]
        lowCard = hand[0]
        return None
    else:
        highCard = hand[0]
        lowCard = hand[1]
        return None

def findNextLowestKey(lookUpTable):
    ''' This routine is used when the card being searched for is not one of
        the keys in the action lookup table for the that card.  It returns
        the action of the next lowest key in the action lookup table.  The
        action lookup table keys are ordered from lowest to highest'''
    keys = lookUpTable.keys()
    keyList = list(keys)
    for y in range(0, len(keyList)):
        if keyList[y] > lowCard:
            nextLowest = y - 1
            break
    return keyList[y]

def pairsLookup ():
    ''' pairs represent a special case and are handled slightly different
        than other action tables.  This because they do not have a
        suited or unsuited component. '''
    ansPos, ansAction = PairsAction.get(highCard)
    if (TablePositionValues.get(position) <= TablePositionValues.get(ansPos)):
        return Actions.get(ansAction)
    else:
        return Actions.get(0)

def nonPairsLookup (lookUpTable):
        testCard = lowCard
        while not lookUpTable.get(testCard):
            testCard = findNextLowestKey(lookUpTable)
        sPos, sansAction, usPos, usansAction = lookUpTable.get(testCard)
        return actionPrint(sPos, sansAction, usPos, usansAction)

def actionPrint (sPos, sansAction, usPos, usansAction):
        if suited:
            if (TablePositionValues.get(position) \
                <= TablePositionValues.get(sPos)):
                return Actions.get(sansAction)
            else:
                return Actions.get(0)
        else:
            if (TablePositionValues.get(position) \
                <= TablePositionValues.get(usPos)):
                return Actions.get(usansAction)
            else:
                return Actions.get(0)

def lookupAction():
    message = "still testing"
    if (highCard == lowCard):         # this is a pair
        return pairsLookup()

    elif (highCard == 'a'):             # this hand is Ax
        return nonPairsLookup(AceAction)

    elif (highCard == 'k'):             # this hand is Kx
        return nonPairsLookup(KingAction)

    elif (highCard == 'q'):             # this hand is Qx
        return nonPairsLookup(QueenAction)

    elif (CardValues.get(highCard) == CardValues.get(lowCard)+1):
                                        # this hand is a 0 Gap
        return nonPairsLookup(ZeroGapAction)

    elif (CardValues.get(highCard) == CardValues.get(lowCard)+2):
                                        # this hand is a 1 Gap
        return nonPairsLookup(OneGapAction)

    elif (CardValues.get(highCard) == CardValues.get(lowCard)+3):
                                        # this hand is a 2 Gap
        return nonPairsLookup(TwoGapAction)

    elif (position == 'b'):
                                        # checks for special case
                                        # of being on the button.
                                        # any hand can call here
                                        # because the bet has
                                        # already been entered.
	    return nonPairsLookup(EverythingElse)

    else:
        return "fold this hand, it is unplayable"
    return message

def suitedPrint(suited):
        if(suited):
                return  "s"
        else:
                return  "uns"

def inputPocketCards():
    ''' input the pocket cards from the user,
        akqjt98765432 are valid
        followed by s if suited (both cards of the same suit)
        or a single q which quits the script'''
    global hand
    while (hand != "q") :
        hand = input(
        "enter the hand, with s if suited or q to quit ")
        ValidHand = re.match(validTest, hand)
        if ValidHand:
            TestHand = ValidHand.group()
            if (TestHand == "q") :
                print(TestHand + " is found, ending")
                exit()
            else:
                return TestHand
        else:
            print ("not a valid hand or q(uit).  retry")

def inputTablePosition():
    ''' input the table position where the hand is being played
        table position is defined as
            big blind(b),
            small blind(s),
            button(*) or
            position to the right of the button(1 thru 6).
            Assumes a standard 9 handed tournament table.'''
    inposition = 0
    while (inposition == 0):
        inposition = input("now enter your table position (bs*123456) ")
        ValidTP = re.match(PositionTest, inposition)
        if ValidTP:
            return ValidTP.group()
        else:
            print ("invalid table position, retry ")
            inposition = 0

running = True
''' This is the main routine.
    It requests the user to enter the two down cards dealt
        and whether they are suited or not.
    It then requests the user's seat position relative to the button.
    Based on this information, it looks up and reports to the
        user what action should be taken when it is the users turn
    The lookup is quite complex and copied from a table I use
        which I read about playing tournament poker.'''
while running:
    hand = inputPocketCards()
    if (len(hand) == 3): suited = True
    else: suited = False
    z = orderPocketCards()
    position = inputTablePosition()
    print ("in  ", highCard, lowCard, suitedPrint(suited), position)
    print("out ",lookupAction(), '\n')
##    decider = input("continue? ")
##    if (decider == 'n'):
##        running = False
##    else:
##        running = True
exit()







