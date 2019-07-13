#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml


class Student_Player():
    yaml_tag = "!Student"
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
