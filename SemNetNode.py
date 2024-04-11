# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sat Jan 27 10:17:21 2024
in Tims II Lab

@author: Stark
"""


class Node:
    '''
    ласточка has перья that is белые
    ласточка has перья that is длинные
    ласточка has масса that is 2кг
    .
    .
    .
    перья has длину that can be [короткие, длинные, {точная длина}]
    перья has цвет that can be [<name>, {RGB}]
    '''
    
    def __init__(self):
        self.has_node = []
        
    