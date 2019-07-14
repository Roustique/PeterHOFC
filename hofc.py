#!/usr/bin/env python
# -*- coding: utf-8 -*-

from student import Student_Player
import serialize as s

Player = Student_Player(
    firstname = "Юзернейм",
    lastname = "Юзернеймов",
    health = 100,
    mana = 100,
    money = 1500,
    fatigue = 0,
    hunger = 0,
    interest = 0,
    karma = 0)

print(s.dump(Player))
