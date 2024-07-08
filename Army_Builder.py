#Author: Andrew R Walsh
#Client: P&M
#Date: 7/1/24
#Description: Army builder web app. Allows user to create custom characters and add custom stats to each character.

#TODO
'''
s = started
x = done
y = why not working?
z = almost working?
[ ] Add Team
[ ] Delete Team
[ ] Undo Delete Team
[ ] Add Army
[ ] Delete Army
[ ] Undo Delete Army
[ ] Add Race
[ ] Delete Race
[ ] Undo Delete Race
[ ] Add unit
[ ] Delete unit
[ ] Undo Delete Unit
[ ] Can I make all of these methods of a GUI class or something? Seems like it should be modular to different parent and subclases...
[x] Import statistics library or math?
[s] class Army; Create a parent class Army
[s] class Race; Create a subclass of Army, Race
[s] class Unit; Create a subclass of Race, Unit
[s] class WeaponsAndArmor that can be added to units like a  stat boost
[s] class BuffsAndDebuffsCreate inherit strengths and weakness in the Race class that effect all units under that race class. For example, Orcs will have plus 10 strength but a weakness to fire damage or something like that.
[ ] Figure out web integration
[ ] Figure out page design and layout
[x] Log hours (write a script to clock time running pycharm)
[ ] Add a 'Random' button that creates a psuedo-random stats for a Unit. To automatically create units for a user who just needs "something". This random button would have a range that would be explicit and made known to the user; ie. 1-10 or something like that.
[ ] Report a bug icon added
[ ]

'''

import math

class Teams:
    pass
class Army(Teams):
    pass

class Race(Army):
    pass

class Unit(Race):
    pass

class BuffsAndDebuffs:
    pass

class WeaponsAndArmor:
    pass