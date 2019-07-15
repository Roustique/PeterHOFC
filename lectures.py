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
