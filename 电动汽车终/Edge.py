# 边类
class Edge(object):
    def __init__(self, adjVex):
        # adjVex是集合，(起点，终点)
        #
        self.adjVex = adjVex
        self.next = None
        self.lanes = None
        self.road_type = None
        self.blocking_probability = None
        self.charging_distance = None
        self.charging_number = None
        self.charging_price = None
        self.edge = []