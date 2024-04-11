# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sat Jan 27 08:19:25 2024
in Tims II Lab

@author: Stark
"""

from SemNetNode import Node
from SemNetFNode import Feature_Node









class SemNet:
    def __init__(self):
        self.nodes = {}
        
        pass
    
    def add(self, conection:str):
        name, func, *feature = conection.split(' ')
        if func == "has":
            if name not in self.nodes.keys():
                self.nodes[name] = Node()
            self.nodes[name].add(feature)
                
        
    