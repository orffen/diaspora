#!/usr/bin/env python3
#
# star_system.py
# Diaspora star system generator
# 
# This file is part of t# he Diaspora Toolbox
# 
# Copyright (c) 2017 Steve Simenic <orffen@orffenspace.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# 

import random
import sys

class StarSystem:
    """
    This class generates a Diaspora star system, which has the following
    attributes:

    - technology
    - environment
    - resources

    """
    def __init__(self, technology, environment, resources):
        self.technology  = technology
        self.environment = environment
        self.resources   = resources

    def __init__(self):
        self.technology  = self._roll()
        self.environment = self._roll()
        self.resources   = self._roll()

    def __str__(self):
        tech_lookup = {
            4 : "On the verge of collapse",
            3 : "Slipstream mastery",
            2 : "Slipstream use",
            1 : "Exploiting the system",
            0 : "Exploring the system",
            -1: "Atomic power",
            -2: "Industrialization",
            -3: "Metallurgy",
            -4: "Stone Age"
        }
        env_lookup = {
            4 : "Many garden worlds",
            3 : "Some garden worlds",
            2 : "One garden and several survivable worlds",
            1 : "One garden and several hostile environments",
            0 : "One garden world (perhaps additional barren worlds)",
            -1: "Survivable world",
            -2: "Hostile environment (gravity but dangerous athmosphere)",
            -3: "Barren world (gravity, no athmosphere)",
            -4: "No habitable gravity or athmosphere"
        }
        res_lookup = {
            4 : "All you could want",
            3 : "Multiple exports",
            2 : "One significant export",
            1 : "Rich",
            0 : "Sustainable",
            -1: "Almost viable",
            -2: "Needs imports",
            -3: "Multiple dependencies",
            -4: "No resources"
        }
        r = [
            "Technology: "  + tech_lookup[self.technology],
            "Environment: " + env_lookup[self.environment],
            "Resources: "   + res_lookup[self.resources]
        ]
        return "\n".join(r)

    def _roll(self):
        dice = [-1, 0, 1]
        result = 0
        for i in range(4):
            result += random.choice(dice)
        return result

if __name__ == "__main__":
    print(StarSystem())
