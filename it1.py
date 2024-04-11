# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created in March 2024
in Tims II Lab

@author: Stark
"""



from vertex import Vertex
from edge import Edge  

from net import NET





if __name__ == "__main__":
    
    Net = NET()
    a = Net.add_vertex(Vertex(name="bird"))
    b = Net.add_vertex(Vertex(name="wing"))
    Net.add_edge(Edge("part of", a, b))
    
    c = Net.add_vertex(Vertex(name="fly"))
    Net.add_edge(Edge("implication", c, b))
    
    
    
    print(f"{Net:vc}")
    print(f"{Net:edge}")
    print(Net.check(4, 'implication', 'to'))
