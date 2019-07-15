#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serialize as s

lrs = s.load(open('data/lecturers.yml'))
globals().update(lrs)
