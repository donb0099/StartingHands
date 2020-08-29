# starting-hands
A python script I created to lookup the action to take in texas-hold'em given the two down cards and table position.  
I have a rather dense table of what to do given the pair of cards dealt face down, and the position you are sitting
relative to the button.  The tables are for pairs, ax, kx, qx, 0gap, 1gap and 2gap.  Except for pairs, there is an
action for suited and unsuited versions of the candidates.  

There are two files involved, one contains the tables and is an import to the other file which contains the logic
to find the correct table, select the action based on table position and print out the action.  The actions are

  - Fold.  This hand is unplayable (typically a hand with gap greater than 2)
  - Call the blind, fold if there is one or more raises.  (usually a weak hand, often playable in the blinds)
  - Open with a raise or call if one raise is already in place, fold if 2 or more raises.  (potential hand, depends on flop)
  - Open with a raise or call any raise and call any subsequent raise.  Careful of all in pushes.  (strong hand, would like to narrow field of competitors)
  - Open with a raise and reraise any subseqent raise.  Careful of all in pushes.  (strongest hands, would like to add money to pot and narrow field of competitors)

The script runs in a command window on Win 10 using python 3.

It is a simple interface as I am using this to learn more about the capabilities of Python.  I plan to extend the 
program using additional facilities of Python as I learn them.  
