import numpy as np


class Student_Player():
    def __init__(self, firstname, lastname, health, mana, money, fatigue, hunger, interest, karma):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.mana = mana
        self.money = money
        self.fatigue = fatigue
        self.hunger = hunger
        self.interest = interest
        self.karma = karma


class Student_NPC():
    def __init__(self, firstname, lastname, relation, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.relation = relation
        self.grade = grade


class Lecturer():
    def __init__(self, speed, aggressivness, clarity, responsibility, knowledge):
        self.speed = speed
        self.aggressivness = aggressivness
        self.clarity = clarity
        self.responsibility = responsibility
        self.knowledge = knowledge


class Course():
    def __init__(self, difficulty, number_of_tasks, dullness, type, conspect, enabled):
        self.difficulty = difficulty
        self.number_of_tasks = number_of_tasks
        self.dullness = dullness
        self.type = type
        self.conspect = conspect
        self.enabled = enabled


firstname = "Юзернейм"   # Это временно, можно убрать
lastname = "Юзернеймов"  # Это тоже
init_money = 1500        # И это
Player = Student_Player(firstname, lastname, 100, 100, init_money, 0, 0)

Karpov = Lecturer(10, 2, 3, 8, 10)
Gromov = Lecturer(8, 0, 6, 10, 10)
PA = Lecturer(6, 2, 10, 9, 10)
Shney = Lecturer(2, 0, 7, 8, 6)
Jesus = Lecturer(4, 5, 4, 3, 9)
Resh = Lecturer(5, 7, 8, 8, 8)
Savchenko = Lecturer(6, 0, 8, 8, 8)
Nikiforov = Lecturer(7, 4, 8, 10, 8)

Mathan = Course(9, 12, 4, "math", 0, True)
Algebra = Course(8, 15, 3, "math", 0, True)
Basic_Mech = Course(5, 10, 2, "phys", 0, True)
Analgem = Course(2, 4, 6, "math", 0, True)
Genastronomy = Course(6, 10, 3, "astro", 0, True)
ProgaFortran = Course(2, 20, 7, "CS", 0, True)
Unix = Course(5, 3, 4, "CS", 0, True)

Courseplan = np.array(["empty", "Mathan", "Algebra", "Basic_Mech", "Analgem", "Genastronomy", "ProgaFortran", "Unix"])
Timetable =

time = 9
day = 1
semester = 1

