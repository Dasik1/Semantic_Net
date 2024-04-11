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


Net = NET()

bird = Net.add_vertex(Vertex("bird"))
wing = Net.add_vertex(Vertex("wing"))
Net.add_edge(Edge('has', bird, wing, {"quantor":"most"}))

feather = Net.add_vertex(Vertex("feather"))
Net.add_edge(Edge("has", wing, feather)) #quantor all is default

seagull = Net.add_vertex(Vertex("seagull"))
Net.add_edge(Edge("is a", seagull, bird, {'quantor':"all"}))

print(Net.answer({"from":"seagull",
                  "edge":"has",
                  "to":"feather"
                  }))

q = Net.vetex_connection