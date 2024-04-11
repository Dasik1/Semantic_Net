# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created in March 2024
in Tims II Lab

@author: Stark
"""

class UID:
    def __init__(self):
        self.ID = 0
    
    def get(self):
        self.ID+=1
        return self.ID