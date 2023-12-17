#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "python is an easy programing language to learn",
        ]

    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]