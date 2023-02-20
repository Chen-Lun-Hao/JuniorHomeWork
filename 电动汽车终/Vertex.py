'''
Description: 节点的结构类
Author: Xiao
Date: 2022-11-02 08:37:46
LastEditTime: 2023-01-19 21:21:14
LastEditors: Xiao
'''
class Vertex:
    def __init__(self, name, X, Y):
        self.name = name
        self.id=[X,Y]#节点id和坐标
        self.edgelist = []
        self.inv = 0#入度
        self.outv = 0#出度
    
    def setCost(self,cost):
        self.cost = cost
    
    def setValue(self,values):
        self.lanes = values[0]
        self.road_type = values[1]
        self.road_relationship = values[2]
        self.traffic_flow = values[3]
        self.charge_station = values[4]
        self.power = values[5]
        self.lacharge_stationsnes = values[6]
        self.Charging_price = values[7]

    def setEdge(self,edge):#将边的属性给予节点
        #将边的属性转移至节点[终点，距离，车道数, 类型, 堵塞概率,充电桩距离，充电桩个数，充电桩价格]
        self.edgelist.append([edge.next,edge.length,edge.lanes,edge.road_type,edge.blocking_probability,
            edge.charging_distance,edge.charging_number,edge.charging_price])
        

    #对数据进行预处理
    #以充电桩到该节点最短距离为基准
    def process(self):
        lengthmax = 0
        lengthmin = 99999999
        lanesmax = 0
        laneshmin = 99999999
        road_typehmax = 0
        road_typehmin = 99999999
        # lengthmax = 0
        # lengthmin = 99999999
        for e in self.edgelist:#遍历每一条边
            if(lengthmax < e.length):#找到最大边
                lengthmax = e.length
            if lengthmin > e.length:#找到最小边
                lengthmin = e.length
            if(lanesmax < e.lanes):#找到最大车道数
                lanesmax = e.lanes
            if laneshmin > e.lanes:#找到最小车道数
                laneshmin = e.lanes
            if(road_typehmax < e.road_type):#找到最大类型
                road_typehmax = e.road_type
            if road_typehmin > e.road_type:#找到最小类型
                road_typehmin = e.road_type
        lt = 0
        lat = 0
        rtt = 0
        for e in self.edgelist:#遍历每一条边
            lt = (e.length - lengthmin) / (lengthmax - lengthmin)
            lat = (e.lanes - laneshmin) / (lanesmax - laneshmin)
            rtt = (e.road_type - road_typehmin) / (road_typehmax - road_typehmin)
        return lt * 0.1

    def setCharge(self, geshu, jiage, juli ):#充电桩个数，充电桩价格，充电桩距离
        self.geshu = geshu 
        self.jiage = jiage
        self.juli = juli
