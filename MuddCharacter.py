#Stewart Towle
#10/19/2020
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
    def __init__(self, name, sort = "human", job = "random", level = 1, hp = 1, str = 10, dex = 10, vit = 10, wis = 10, charisma = 10):
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
        if job == "random":
            self.job = JobClass(name)
        else:
            self.job = JobClass(job)

def create_character(creation_method):
        return MuddCharacter("poopanna")


# test_char = MuddCharacter("poopanna")
# test_char2 = MuddCharacter("dance dance revolution", "elf", "sorcerer")
# test_char3 = MuddCharacter("tad")
# test_char4 = MuddCharacter("oxford", job = "student")
# print(test_char2.name, "is a", test_char2.sort, test_char2.job.get_job())
# print(test_char3.name, "is a", test_char3.sort, test_char3.job.get_job())
# print(test_char4.name, "is a", test_char4.sort, test_char4.job.get_job())
# print(test_char.name, "is a", test_char.sort, test_char.job.get_job())

