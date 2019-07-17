#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


class Course():
    def __init__(self, difficulty, number_of_tasks, dullness, type, conspect, enabled):
        self.difficulty = difficulty
        self.number_of_tasks = number_of_tasks
        self.dullness = dullness
        self.type = type
        self.conspect = conspect
        self.enabled = enabled


Mathan = Course(9, 12, 4, "math", 0, True)
Algebra = Course(8, 15, 3, "math", 0, True)
Basic_Mech = Course(5, 10, 2, "phys", 0, True)
Analgem = Course(2, 4, 6, "math", 0, True)
Genastronomy = Course(6, 10, 3, "astro", 0, True)
ProgaFortran = Course(2, 20, 7, "CS", 0, True)
Unix = Course(5, 3, 4, "CS", 0, True)

Courseplan = np.array(["empty", "Mathan", "Algebra", "Basic_Mech", "Analgem", "Genastronomy", "ProgaFortran", "Unix"])
#  Timetable =

