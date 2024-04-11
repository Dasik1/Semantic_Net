# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created in March 2024
in Tims II Lab

@author: Stark
"""

from vertex import Vertex
from edge import Edge  

from UID import UID


class NET:
    
    def __init__(self):
        #net
        self.edges = {}
        self.vertexies = {}
        
        #connections
        self.edge_connection = {}
        self.vertex_connection = {}
        
        self.inherit_edges = ["is a"]
        self.upherit_edges = ["has"]
        self.UID_ = UID()
    
    def __format__(self, format_spec):
        if format_spec == "vc":
            return str(self.vertex_connection)
        elif format_spec == "ec":
            return str(self.edge_connection)
        elif format_spec == "vertex":
            return str(self.vertexies)
        elif format_spec == "edge":
            return str(self.edges)
    
    def postformat(self, pack):
        ans = []
        for i in pack:
            ans.append(((self.vertex_connection[i["vertex"]].name,
                         self.vertex_connection[i["vertex"]].properties),
                        i["quantor"]))
        return ans
        
    def disconnect(self):
        del self.UID_
    
    
    def add_vertex(self, vert):
        
        if vert in self.vertex_connection.values():
            return
        
        self.vertex_connection[(uid := self.UID_.get())] = vert
        self.vertexies[uid] = {"from":[], "to":[]}
        return uid
    
    
    
    def add_edge(self, edge):
        if edge in self.edge_connection.values():
            return
        
        self.edge_connection[(uid := self.UID_.get())] = edge
        
        self.edges[uid] = {"type":edge.name,
                           "from": (f:=edge.f),
                           "to": (t:=edge.t),
                           "quantor": edge.quantor}
        self.vertexies[t]["to"].append({"uid":uid, "vertex":f})
        self.vertexies[f]["from"].append({"uid":uid,"vertex":t})
            
                   
        
        
    def get_fromVertex(self, vert):
        for i in self.vertex_connection.keys():
            v=self.vertex_connection[i]
            if vert==v: return i
    
    def check(self, from_,  type_, to, quantor = "all"):
        for i in self.edges.keys():
            if self.edges[i] == {"from":from_, "type":type_, "to":to, "quantor":quantor}:
                return i
        return None
    
    def ping(self, vertex, type_, destination="from", quantor=None):
        '''check if vertex has this edge from it'''
        '''вернуть все исходящие ребра <edge_type> типа'''
        if type(type_) is list:
            ans = []
            for i in type_:
                for _ in self.ping(vertex,i,destination,quantor):
                    ans.append(_)
                    return ans
        
        if type(vertex) is Vertex: vertex = self.get_fromVertex(vertex)
        
        
        edges = [x["uid"] for x in self.vertexies[vertex][destination]]
        
        edges = [self.edges[e] for e in edges]
        
        destination = "from" if destination == "to" else "to"
        
        edges = [{"vertex":x[destination], "quantor":x["quantor"] }
                        if x["type"] == type_ else None 
                    for x in edges]
        
        while None in edges:edges.remove(None)
        return edges
    
    
    
    def answerYN(self, request):
        #request == "from":<f>,"edge":<e>,"to":<t>
        #where: f,t - Vertexies or ids
        #no string because of properties
        
        
        #check(t, e, t)
        #if not -> execute for all <q> <- ping(f, <inherit>, "from") == для всех предков
        #-> check(q, e, t) -- exist -> return
        #                   \ not -> No ........ | try to get from children
        
        
        if type(request["from"]) is Vertex:request["from"] = self.get_fromVertex(request["from"])
        if type(request["to"]) is Vertex:request["to"] = self.get_fromVertex(request["to"])
        
        ans = []
        try_uid = [request['from']]
        
        
        for uid in try_uid:
            ans_uid = self.check(uid, request["edge"], request["to"])
            if ans_uid is not None: ans.append(ans_uid)
            
            for _ in self.ping(uid,self.inherit_edges):try_uid.append(_['vertex'])
        
        return False if ans == [] else True
    
    def answerTYPE(self, vertex, postformat = True):
        ans = self.ping(vertex, "is a", "to")
        
        return self.postformat(ans) if postformat else ans

    