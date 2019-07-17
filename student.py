#!/usr/bin/env python
# -*- coding: utf-8 -*-

from entity import Entity
from serialize import SerializableEntity


class Student_Player(SerializableEntity):
    """
    real student
    """

    yaml_tag = u'!Student'

    def __init__(self, firstname, lastname, health, mana, money, fatigue,
                 hunger, interest, karma, **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.mana = mana
        self.money = money
        self.fatigue = fatigue
        self.hunger = hunger
        self.interest = interest
        self.karma = karma


class Student_NPC(Entity):
    """
    doppelganger of a student,
    therefore can't be serialized
    and has to be simulated

    however, some cameos may subclass this class
    """

    def __init__(self, firstname, lastname, relation, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.relation = relation
        self.grade = grade
