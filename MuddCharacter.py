#Stewart Towle
#10/19/2020
# THis file containe the functions and classes for building a character in the mudd


def is_stat_letter(letter):
    """This function determines if the string is a letter that could correspond to a mudd character stat"""
    if letter == "s" or letter == "S":
        return True
    elif letter == "d" or letter == 'd':
        return True
    elif letter == "v" or letter == 'V':
        return True
    elif letter == 'w' or letter == 'W':
        return True
    elif letter == 'c' or letter == 'C':
        return True
    else:
        return False

#NEEDS COMPLETEING
class Item:
    """class for items, which have many features"""


#NEEDS COMPLETEING
class Inventory:
    """This is a class that contains a list of items in your inventory. Items can be active or inactive,
    which means currently worn/held or not currently worn/held"""
    #Elements are list of Items, bag_size, total_weight, worn_weight,

class JobClass:
    """this is a class that represents the job or class of the character, it stores it as a number but deals with it as a string"""

    ## Jobs are as follows, (0, peasant) (1, wanderer) (2, farmer) (3, trader) (4, student) (5, noble)
    # (6, barbarian) (7, sorcerer) (8, rogue) (9, ranger) (10, knight) (11, druid) (12, bard)
    def __init__(self, _job):
        """initializes character job. If invalid option entered sets job to one of 5 basic classes:
        wanderer, farmer, trader, student or noble"""
        self.jobs = ['peasant', 'wanderer', 'farmer', 'trader', 'student', 'noble', 'barbarian', 'sorcerer', 'rogue', 'ranger', 'knight', 'druid', 'bard']
        if _job == "barbarian" or _job == "Barbarian":
            self._job = 6
        elif _job == 'sorcerer' or _job == "Sorcerer":
            self._job = 7
        elif _job == 'rogue' or _job == "Rogue":
            self._job = 8
        elif _job == 'ranger' or _job == "Ranger":
            self._job = 9
        elif _job == 'knight' or _job == "Knight":
            self._job = 10
        elif _job == 'druid' or _job == "Druid":
            self._job = 11
        elif _job == 'bard' or _job == "Bard":
            self._job = 12
        elif _job == 'wanderer' or _job == "Wanderer":
            self._job = 1
        elif _job == 'farmer' or _job == "Farmer":
            self._job = 2
        elif _job == 'trader' or _job == "Trader":
            self._job = 3
        elif _job == 'student' or _job == "Student":
            self._job = 4
        elif _job == 'noble' or _job == "Noble":
            self._job = 5
        elif _job == "peasant" or _job == "Peasant":
            self._job = 0
        else:
            job_counter = 0
            for letter in _job:
                job_counter += 1
                if job_counter < 4:
                    self._job = 1
                elif job_counter < 8:
                    self._job = 2
                elif job_counter < 12:
                    self._job = 3
                elif job_counter < 20:
                    self._job = 4
                else:
                    self._job = 5

    def get_job(self):
        """returns the string name of the job"""
        return self.jobs[self._job]


class MuddCharacter:
    """This is a class that represents an avatar in a D&D style game"""
    def __init__(self, name, sort = "human", job = "random", level = 1, hp = 1, str = 10, dex = 10, vit = 10, wis = 10, charisma = 10, equipment = Inventory(), facing = 0):
        """initializes a character with name, and all the stuff"""
        self.name = name
        self.lvl = level
        self.hp = hp
        self.str = str
        self.dex = dex
        self.vit = vit
        self.wis = wis
        self.cha = charisma
        self.sort = sort
        self.equipment = equipment
        self.facing = facing
        if job == "random":
            self.job = JobClass(name)
        else:
            self.job = JobClass(job)

    def get_job(self):
        "returns the string name of the job of the character"
        return self.job.get_job()

    def generate_stats_auto(self):
        """this function automatically generates the stats of a charcter based on level and job"""
        if self.job._job == 0 or self.job._job == 2 or self.job._job == 10:
            for i in range(0, self.lvl + 5):
                if (i % 5) == 0:
                    self.str += 1
                elif (i % 5) == 1:
                    self.vit += 1
                elif (i % 5) == 2:
                    self.dex += 1
                elif (i % 5) == 3:
                    self.vit += 1
                else:
                    self.str += 1
        if self.job._job == 6:
            self.str += (2 + self.lvl)
            self.vit += 3
        if self.job._job == 1 or self.job._job == 9:
            for i in range(0, self.lvl + 5):
                if (i % 5) == 0:
                    self.dex += 1
                elif (i % 5) == 1:
                    self.str += 1
                elif (i % 5) == 2:
                    self.wis += 1
                elif (i % 5) == 3:
                    self.vit += 1
                else:
                    self.dex += 1
        if self.job._job == 3 or self.job._job == 12:
            for i in range(0, self.lvl + 5):
                if (i % 5) == 0:
                    self.cha += 1
                elif (i % 5) == 1:
                    self.wis += 1
                elif (i % 5) == 2:
                    self.vit += 1
                else:
                    self.cha += 1
        if self.job._job == 4 or self.job._job == 7:
            for i in range(0, self.lvl + 5):
                if (i % 5) == 0:
                    self.wis += 1
                elif (i % 5) == 1:
                    self.dex += 1
                elif (i % 5) == 2:
                    self.vit += 1
                else:
                    self.wis += 1
        if self.job._job == 11:
            for i in range(0, self.lvl + 5):
                if (i % 5) == 0:
                    self.wis += 1
                elif (i % 5) == 1:
                    self.vit += 1
                elif (i % 5) == 2:
                    self.str += 1
                elif (i % 5) == 3:
                    self.vit += 1
                else:
                    self.wis += 1
        if self.job._job == 8:
            for i in range(0, self.lvl + 5):
                if (i % 5) == 0:
                    self.dex += 1
                elif (i % 5) == 1:
                    self.cha += 1
                elif (i % 5) == 2:
                    self.wis += 1
                else:
                    self.dex += 1
        if self.job._job == 5:
            for i in range(0, self.lvl + 5):
                if (i % 5) == 0:
                    self.cha += 1
                elif (i % 5) == 1:
                    self.vit += 1
                elif (i % 5) == 2:
                    self.vit += 1
                else:
                    self.cha += 1

    ## Jobs are as follows, (0, peasant) (1, wanderer) (2, farmer) (3, trader) (4, student) (5, noble)
    # (6, barbarian) (7, sorcerer) (8, rogue) (9, ranger) (10, knight) (11, druid) (12, bard)


    def stat_up(self, letter):
        if letter == "s" or letter == "S":
            self.str += 1
        elif letter == "d" or letter == 'd':
            self.dex +=1
        elif letter == "v" or letter == 'V':
            self.vit += 1
        elif letter == 'w' or letter == 'W':
            self.wis += 1
        elif letter == 'c' or letter == 'C':
            self.cha += 1

    def full_heal(self):
        """this function returns the character to max hp, which is 1 + however much greater than 8 the vitality is"""
        if self.vit > 7:
            self.hp = self.vit - 7
        else:
            self.hp = 1

    def turn_char(self, how_to_turn):
        """This function allows a character to change its orientation"""
        # 0 is N, 1 is NE, 2 is E up to 7 is NW, then 8 is up, 9 is down
        self.facing = (self.facing + how_to_turn) % 10


def create_character(creation_method):
    """This is a method for creating a character. It takes as input 0, 1 or 2 to determine creation method"""
    if creation_method == 0:
        character = MuddCharacter(input("What is your name: "))
        character.generate_stats_auto()
    elif creation_method == 1:
        name = input("what is your name: ")
        sort = input("what sort of creature are you: ")
        print("possible character classes/jobs are limitted to")
        source_jobs = JobClass('peasant')
        for num in range(0, len(source_jobs.jobs)):
            print(source_jobs.jobs[num])
        job = input("what is your job/character class: ")
        character = MuddCharacter(name, sort, job)
        character.generate_stats_auto()
    elif creation_method == 2:
        name = input("what is your name: ")
        sort = input("what sort of creature are you: ")
        print("possible character classes/jobs are limitted to")
        source_jobs = JobClass('peasant')
        for num in range(0, len(source_jobs.jobs)):
            print(source_jobs.jobs[num])
        job = input("what is your job/character class: ")
        lvl = int(input("what is your starting level (please input an integer 1 or greater): "))
        character = MuddCharacter(name, sort, job, lvl)
        print("you get", (5 + lvl), "points to put into stats! The possible stats to put points in are strength, vitality, dexterity, wisdom, and charisma")
        i = 0
        while i < (lvl + 5):
            print("which stat would you like to increment up by 1? Please enter s for strength, d for dexterity, v for vitality, w for wisdom or c for charisma: ")
            letter = str(input())
            if is_stat_letter(letter):
                character.stat_up(letter)
                i += 1
            else:
                print("that's not an accepted input try again")

    else:
        character = MuddCharacter("poopanna")
    character.full_heal()
    return character


# test_char = MuddCharacter("poopanna")
# test_char2 = MuddCharacter("dance dance revolution", "elf", "sorcerer")
# test_char3 = MuddCharacter("tad")
# test_char4 = MuddCharacter("oxford", job = "student")
# print(test_char2.name, "is a", test_char2.sort, test_char2.job.get_job())
# print(test_char3.name, "is a", test_char3.sort, test_char3.job.get_job())
# print(test_char4.name, "is a", test_char4.sort, test_char4.job.get_job())
# print(test_char.name, "is a", test_char.sort, test_char.job.get_job())

