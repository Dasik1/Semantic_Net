# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created in March 2024
in Tims II Lab

@author: Stark
"""


class Vertex:
    def __init__(self,name = None, properties  = {}):
        self.name = name
        self.properties = properties
    
    def __eq__(self, other):
        if self.name == other.name:
            if self.properties == other.properties:
                return True
        return False

