#!/usr/bin/env python
# -*- coding: utf-8 -*-

from serialize import SerializableEntity

class Lecturer(SerializableEntity):
    """
    a lecturer person
    TODO: how about seminars?
    """

    yaml_tag = "!Lecturer"

    def __init__(self, name, surname, speed, aggressivness, clarity, responsibility, knowledge):
        self.name = name
        self.surname = surname
        self.speed = speed
        self.aggressivness = aggressivness
        self.clarity = clarity
        self.responsibility = responsibility
        self.knowledge = knowledge

# to emulate old behaviour
lrs = s.
globals().update()

Karpov = Lecturer(10, 2, 3, 8, 10)
Gromov = Lecturer(8, 0, 6, 10, 10)
PA = Lecturer(6, 2, 10, 9, 10)
Shney = Lecturer(2, 0, 7, 8, 6)
Jesus = Lecturer(4, 5, 4, 3, 9)
Resh = Lecturer(5, 7, 8, 8, 8)
Savchenko = Lecturer(6, 0, 8, 8, 8)
Nikiforov = Lecturer(7, 4, 8, 10, 8)
