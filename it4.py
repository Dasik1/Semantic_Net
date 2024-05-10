# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Wed Apr 24 12:04:36 2024
in Tims II Lab

@author: Stark
"""

from net import Net

Net = Net()

seagull = Net.add_Vertex("seagull")
bird = Net.add_Vertex("bird")
Net.add_Edge(seagull, "is a", bird)

wing = Net.add_Vertex("wing")
Net.add_Edge(bird, 'has', wing)

white = Net.add_Vertex("white")

wing_color = Net.add_Property("color", wing)
Net.add_Property_value(wing_color, seagull, white)


ans = Net.get_Property(seagull, wing, "color")
print(Net.vertex[ans])

#what color of wings does seagull have
#Net.answer("color", wing, seagull) # = white