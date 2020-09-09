CardValues = { # dict to convert card label to appropriate value for comparison
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    't' : 10,
    'j' : 11,
    'q' : 12,
    'k' : 13,
    'a' : 14}

TablePositionValues = { # table to convert table position entered string
                        # to position value
    '0' : 10,
    'b' : 1,
    's' : 2,
    '*' : 3,
    '1' : 4,
    '2' : 5,
    '3' : 6,
    '4' : 7,
    '5' : 8,
    '6' : 9}

Actions = { # dict of descriptions of action codes
    0 : "fold",
    1 : "call, fold 1 or more raises",
    2 : "open raise or call 1 raise, fold 2 or more raises",
    3 : "open raise, call all raises",
    4 : "open raise, reraise any raises"}

PairsAction = {    # dict for pairs.  tuple is
                   #    (position where this can be played, action code)
    '2' : ('*', 1),
    '3' : ('1', 1),
    '4' : ('2', 1),
    '5' : ('3', 1),
    '6' : ('4', 1),
    '7' : ('5', 2),
    '8' : ('6', 2),
    '9' : ('0', 3),
    't' : ('0', 3),
    'j' : ('0', 3),
    'q' : ('0', 4),
    'k' : ('0', 4),
    'a' : ('0', 4)}

AceAction = { # dict for Ax and Axs.
              # tuple is
              # (suited position, action code, unsuited position, action code)

    '2' : ('1', 1, 's', 1),
    '3' : ('2', 1, '*', 1),
    '7' : ('3', 1, '1', 1),
    '8' : ('4', 1, '1', 1),
    '9' : ('5', 2, '2', 1),
    't' : ('6', 2, '4', 1),
    'j' : ('0', 3, '5', 3),
    'q' : ('0', 4, '0', 3),
    'k' : ('0', 4, '0', 4)}

KingAction = {  # dict for Kxs and Kx.
                # tuple is
                # (suited position, action code, unsuited position, action code)
    '2' : ('*', 1, 's', 1),
    '6' : ('1', 1, 's', 1),
    '7' : ('2', 1, '*', 1),
    '9' : ('3', 1, '*', 1),
    't' : ('4', 3, '1', 1),
    'j' : ('5', 2, '3', 1),
    'q' : ('6', 3, '4', 3)}

QueenAction = { # dict for Qxs and Qx.
                # tuple is
                # (suited position, action code, unsuited position, action code)
    '2' : ('s', 1, 's', 1),
    '4' : ('*', 1, 's', 1),
    '8' : ('1', 1, 's', 1),
    '9' : ('2', 1, '*', 1),
    't' : ('4', 1, '1', 1),
    'j' : ('5', 2, '3', 1)}

ZeroGapAction = {   # dict for 0 gap.
              # tuple is
              # zero gap means left card value is right card value +1
              # (suited position, action code, unsuited position, action code)
    '2' : ('s', 1, '0', 0),
    '3' : ('s', 1, 's', 1),
    '5' : ('*', 1, 's', 1),
    '7' : ('1', 1, 's', 1),
    '8' : ('2', 1, '*', 1),
    '9' : ('3', 1, '*', 1),
    't' : ('4', 3, '1', 1)}

OneGapAction = {  # dict for 1 gap.
            # tuple is
            # 1 gap means left card value is right card value +2
            # (suited position, action code, unsuited position, action code)
    '2' : ('s', 1, '0', 0),
    '3' : ('s', 1, 's', 1),
    '5' : ('*', 1, 's', 1),
    '7' : ('1', 1, 's', 1),
    '8' : ('2', 1, 's', 1),
    '9' : ('3', 1, '*', 1)}

TwoGapAction = {  # dict for 2 gap.
            # tuple is
            # 2 gap means other card value is this card value +3
            # (suited position, action code, unsuited position, action code)
    '2' : ('s', 1, '0', 0),
    '3' : ('s', 1, 's', 1),
    '7' : ('*', 1, '0', 0),
    '8' : ('1', 1, '0', 0)}

EverythingElse = {  # dict for everything else.
            # tuple is
            # (suited position, action code, unsuited position, action code)
			# this is basically for anything not in any other table when 
			# this hand is on the big blind.  Action is always check, fold 
			# on any raise. 
	'2' : ('b', 1, 'b', 1)}
	
			
