# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created in March 2024
in Tims II Lab

@author: Stark
"""



class Edge:
    def __init__(self, name = None, f = None ,t = None, properties = {}):
        self.name = name
        self.f = f
        self.t = t
        self.properties = properties
        self.quantor = properties["quantor"] if "quantor" in properties.keys()\
                                             else "all"
    
    def __eq__(self, other):
        if type(other) is dict:
            return [other["from"], other['type'], other["to"], other["quantor"]] ==\
                   [self.f,        self.name,     self.t,      self.quantor    ]
        
        if self.name == other.name and\
            self.f == other.f and self.t == other.t and\
            self.properties == other.properties:
                return True
        return False   