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
[x] Add Team
[x] Delete Team
[ ] Undo Delete Team
[x] Add Army
[x] Delete Army
[ ] Undo Delete Army
[x] Add Race
[x] Delete Race
[ ] Undo Delete Race
[x] Add unit
[x] Delete unit
[ ] Undo Delete Unit
[ ] Can I make all of these methods of a GUI class or something? Seems like it should be modular to different parent and subclases...
[x] Import statistics library or math?
[x] class Army; Create a parent class Army
[x] class Race; Create a subclass of Army, Race
[x] class Unit; Create a subclass of Race, Unit
[x] class WeaponsAndArmor that can be added to units like a  stat boost
[x] class BuffsAndDebuffsCreate inherit strengths and weakness in the Race class that effect all units under that race class. For example, Orcs will have plus 10 strength but a weakness to fire damage or something like that.
[ ] Figure out web integration
[ ] Figure out page design and layout
[x] Log hours (write a script to clock time running pycharm)
[ ] Add a 'Random' button that creates a psuedo-random stats for a Unit. To automatically create units for a user who just needs "something". This random button would have a range that would be explicit and made known to the user; ie. 1-10 or something like that.
[ ] Report a bug icon added
[ ]

'''

# hours logged: 2
#Pick a team > player > army > unit > equipment
class Players:
    pass
class Teams:
    '''
    Teams class is where the user can add a team to the game
    '''

    def __init__(self, name):
        '''
        create empty list of teams
        '''
        self.name = name
        self.teamsList = [name]

    def add_team(self, team):
        '''
        Must be a unique team, with a unique name. Check list of teams for entries. No doubles
        :param team: User creates new team if not already existing
        :return: new team
        '''
        if not self.get_team_name(team):
            self.teamsList.append(team)
            return f"Team {team} created!"
        else:
            return f"Team {team} already exists."

    def delete_team(self, team):
        '''
        Checks if team exists in list and delets it from list.
        :param team: User deletes a Team
        :return: deleted team
        '''
        if self.get_team_name(team):
            self.teamsList.remove(team)
            return f"Team {team} deleted."

    def get_team_name(self, teamName):
        '''
        checks if name is on list
        :param teamName:
        :return: Boolean; T or F
        '''
        return teamName in self.teamsList

    class Army:
        '''
        Army class is where the user can add a team to the game
        '''

        def __init__(self):
            '''
            create empty list of armies
            '''
            self.armyList = []
        def add_army(self, army):
            '''
            Must be a unique army, with a unique name. Check list of army for entries. No doubles
            :param army: User creates new army if not already existing
            :return: new army
            '''
            if not self.get_army_name(army):
                self.armyList.append(army)
                return f"Army {army} created!"
            else:
                return f"Army {army} already exists."

        def delete_army(self, army):
            '''
            Checks if army exists in list and delets it from list.
            :param army: User deletes a army
            :return: deleted army
            '''
            if self.get_army_name(army):
                self.armyList.remove(army)
                return f"Army {army} deleted."

        def get_army_name(self, armyName):
            '''
            checks if name is on list
            :param armyName:
            :return: Boolean; T or F
            '''
            return armyName in self.armyList

        class Unit:
            def __init__(self, name, race):
                '''
                create empty list of armies
                '''
                self.unitList = []
                self.race = race
                self.name = name
                self.buffs = []
                self.debuffs = []
                self.equipment = []

            def add_buffs(self, buff):
                '''
                adds a buff to a unit
                :param buff: a stat boost
                :return: stat boost
                '''
                self.buffs.append(buff)

            def add_debuffs(self, debuff):
                '''
                adds a Debuff to a unit
                :param debuff: a stat Decrease
                :return: decrease a stat on a unit
                '''
                self.debuffs.append(debuff)

            def add_equipment(self, equipment):
                '''
                Adds equipment like weapons and armor which are stat boosts and modifiers
                :param equipment: Adds a weapon or armor
                :return: modifies stats
                '''
                self.equipment.append(equipment)
            def add_unit(self, unit):
                '''
                Must be a unique unit, with a unique name. Check list of units for entries. No doubles
                :param unit: User creates new unit if not already existing
                :return: new unit
                '''
                if not self.get_unit_name(unit):
                    self.unitList.append(unit)
                    return f"Unit {unit} created!"
                else:
                    return f"Unit {unit} already exists."

            def delete_unit(self, unit):
                '''
                Checks if unit exists in list and deletes it from list.
                :param unit: User deletes a unit
                :return: deleted unit
                '''
                if self.get_unit_name(unit):
                    self.unitList.remove(unit)
                    return f"Unit {unit} deleted."

            def get_unit_name(self, unitName):
                '''
                checks if name is on list
                :param unitName:
                :return: Boolean; T or F
                '''
                return unitName in self.unitList

class Race:
    '''
    A Race class that has buffs and debuffs that a user can define. The same race can be on differing teams. Not team locked!
    '''
    def __init__(self, name, stats):
        self.raceList = []
        self._name = name
        self._stats = stats

    def add_race(self, race):
        '''
        Adds a race to the list
        :param race: name of the race
        :return: race to the list of races
        '''
        if not self.get_race_list(race):
            return self.raceList.append(race)
        else:
            return f"Race {race} already exists."

    def delete_race(self, race):
        '''
        Deletes race from the raceList
        :param race: name of the race
        :return: deleted race from list
        '''
        if self.get_race_list(race):
            self.raceList.remove(race)
            return f"Race {race} deleted."

    def get_race_list(self, race_name):
        return race_name in self.raceList



team_name = Teams('Grogars')
print(team_name.add_team('Grogars'))
print(team_name.add_team('Grogars'))
print(team_name.add_team('Farlyns'))
print(team_name.delete_team('Grogars'))
print(team_name.teamsList)

human = Race("Human", 10)
team = Teams('Grogars')
army1 = .add_army("Gladiators")
unit1 = army1.add_unit("Slave", "Human")
unit1.buffs.append("Strength Boost")
unit1.equipment.append("Sword of Might")
unit1.equipment.append("Shield of Truth")

print(unit1)

'''
class Players:
    pass
class Race:
    def __init__(self, name, strength, agility):
        self.name = name
        self.strength = strength
        self.agility = agility

    def __str__(self):
        return f"{self.name} (Strength: {self.strength}, Agility: {self.agility})"

class Team:
    def __init__(self, name):
        self.name = name
        self.armies = []                        # A team can have multiple armies

    def add_army(self, army_name):
        army = self.Army(army_name)             # Create an instance of the nested Army class
        self.armies.append(army)
        return army

    class Army:
        def __init__(self, name):
            self.name = name
            self.units = []                     # An army can have multiple units

        def add_unit(self, unit_name, race):
            unit = self.Unit(unit_name, race)  # Create an instance of the nested Unit class
            self.units.append(unit)
            return unit

        class Unit:
            def __init__(self, name, race):
                self.name = name
                self.race = race
                self.buffs = []
                self.debuffs = []
                self.weapons = []
                self.armor = []

            def __str__(self):
                return (f"Unit: {self.name}, Race: {self.race}, "
                        f"Buffs: {self.buffs}, Debuffs: {self.debuffs}, "
                        f"Weapons: {self.weapons}, Armor: {self.armor}")
'''