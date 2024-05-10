# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Wed Apr 24 11:54:27 2024
in Tims II Lab

@author: Stark
"""

from UID import UID
from multipledispatch import dispatch



class Net:
    
    def __init__(self):
        
        self.vertex = {} #v[id] = {name, <_>} to identify
        self.vertex_connection = {} #{[outgoing], [incoming], [related_properties]}
        
        self.properties = {} #p[id] = {name, related <_>}
        self.property_connection = {} #p[id] = {"caller":saved_property}
        
        
        self.edges = {} #e[id] = {name, <_>, from, to}
        
        self.inherit_edges = ["is a"] #edges that allows to inherit properties
        self.upherit_edges = ["has"]
    
        self.UID_ = UID()
        

    def disconnect(self):del self.UID_ #spyder joke)
    
    def add_Vertex(self, name, _desc = None) -> int:
        
        pack = {"name":name, "desc":_desc}
        
        if pack in self.vertex.values():
            return None
        
        self.vertex[(q:=self.UID_.get())] = pack
        self.vertex_connection[q] = {"outgoing":[], "incoming":[], "properties":[]}
        return q
    
    
    def add_Edge(self, from_v:int, name, to_v:int, _desc = None) -> int:
        
        pack = {"name":name,
                "from":from_v,
                "to"  :to_v,
                "desc": _desc}
        
        if pack in self.edges.values():
            return None
        
        
        self.edges[(q:=self.UID_.get())] = pack
        self.vertex_connection[from_v]['outgoing'].append({"id":q,"to":to_v})
        self.vertex_connection[to_v]['incoming'].append({"id":q,"from":from_v})
        return q
    
    
    def add_Property(self, name, related_v:int, _desc = None):
        
        pack = {"name":name, "related":related_v, "desc":_desc}
        
        if pack in self.properties.values():
            return None
        
        self.properties[(q:=self.UID_.get())] = pack
        self.vertex_connection[related_v]['properties'].append(q)
        self.property_connection[q] = {}
        return q
    
    
    #@dispatch(int, int, int)
    def add_Property_value(self, property_id:int, caller:int, property_val_id:int):
        
        self.property_connection[property_id][caller] = property_val_id
    
    
    def find(self, Vertex_name:str, _desc = None):
        
        for i in self.vertex.keys():
            if Vertex_name == self.vertex[i]["name"] and _desc == self.vertex[i]["desc"]:
                return i
        
    def check(self, v1, v2):
        v = self.vertex_connection[v1]
        og, ig, _ = v['outgoing'], v['incoming'], v['properties']
        
        for i in og:
            if i["to"] == v2:return self.edges[i["id"]]
        for i in ig:
            if i["from"] == v2:return self.edges[i["id"]]
        
        return {"name":None}
            
    
    
    def ping(self, vert, edge, father = True) -> int or None:
        
        v = self.vertex_connection[vert]
        og, ig, _ = v['outgoing'], v['incoming'], v['properties']
        ans = []
        if father:
            for i in og:
                if self.edges[i['id']]['name'] == edge:
                    ans.append(self.edges[i['id']]['to'])
            return ans
        elif father is False:
            for i in ig:
                if self.edges[i['id']]['name'] == edge:
                    ans.append(self.edges[i['id']]['from'])
            return ans
          
    
    
    def get_Connection(self, v1, v2, await_edge:str,  hist=[]):
        hist.append(v1)
        
        edge = self.check(v1, v2) #Edge or {name:None}
        
        if await_edge in [edge["name"], ""]:
            hist.append(v2)
            return hist
        if await_edge in ["?", "what"] and edge["name"] is not None:
            hist.append(v2)
            return hist, edge
        
        for child in self.inherit_edges:
            for try_v in self.ping(v1, child): #-> [Vertex]
                if try_v is not None:
                    return self.get_Connection(try_v, v2, await_edge)
        
        return None
                
                    
        
        
        
    
    def get_Property(self, obj, atribute, property_name): 
        '''
        color seagull wing
        input: <from where|seagull> <atribute|wing> <prop|color>
        
        get from seagull to wing -->> [seagull, bird, wing] | [obj...atr]
        
        recieve property name - p
        
        check for first p([obj..atr])
        '''
        
        hist = self.get_Connection(obj, atribute, "")
        
        #get all connected prop
        
        all_prop = self.vertex_connection[atribute]['properties']
        
        to_check = []
        for i in all_prop:
            if self.properties[i]['name'] == property_name:
                to_check.append(i)
        
        for i in to_check:
            for caller in hist:
                if caller in self.property_connection[i]:
                    return self.property_connection[i][caller]
    
    #last two answer questions