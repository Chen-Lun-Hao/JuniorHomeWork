'''
Description: 图的结构类
Author: Xiao
Date: 2022-11-02 08:53:09
LastEditTime: 2023-01-21 22:59:51
LastEditors: Xiao
'''
import Vertex

class Graph:
    def __init__(self, vertexlist, edgelist,maxlane,minlane,):
        self.maxlane = maxlane
        self.minlane = minlane
        self.vertexlist = vertexlist#里面放的Vertex类型
        self.edgelist = edgelist#放置边
        self.Bigvert = {}#key是出口id，value是大节点包含的节点id
        self.vi={}#节点的重要度
        self.g = self.build()
    
    def build(self):#构造有向图,邻接表形式
        g = {}#图的结构，key是节点id,value是与之相连的节点id
        for v in range(len(self.vertexlist)):#循环获取节点
            g[self.vertexlist[v].id] = []
            for e in range(len(self.edgelist)):#循环获取边
                if self.vertexlist[v].id == self.edgelist[e][0]:#v是起点
                    self.vertexlist[v].setEdge(e)
                    self.vertexlist[v].inv = self.vertexlist[v].inv + 1#入度
                    g[self.vertexlist[v].id].append(self.getID(self.edgelist[e][1]), self.edgelist[e][2])#保存终点id，以及欧式距离
                if self.vertexlist[v].id == self.edgelist[e][1]:#v是终点
                    self.vertexlist[v].outv = self.vertexlist[v].outv + 1#出度
        return g

    # def calculate(self):#计算节点中的最大以及最小值，为计算重要度提供条件
    #     self.maxl = 0
    #     self.minl = 999
    #     self.maxn = 0
    #     self.minn = 999
    #     for v in self.vertexlist:
    #         if self.maxl < v.l:
    #             self.maxl = v.l
    #         if self.minl > v.l:
    #             self.minl = v.l
    #         if self.maxn < v.n:
    #             self.maxn = v.n
    #         if self.minn > v.n:
    #             self.minn = v.n

    def Vimportance(self):#节点重要度计算
        for v in range(len(self.vertexlist)):
            self.vi[v.id] = (v.lanes - self.minlane) / (self.maxlane - self.minlane)
        
        
    def getID(self, name):#根据name找到对应的id
        for i in self.vertexlist:
            if i.name == name:
                return i.id
    
    def getVertex(self,id):#根据id找节点
        #遍历图中所有的顶点
        for i in self.g.keys:
            if i == id:  # 节点id和n相同,返回节点
                return self.g[i]  # i是节点id,返回对应的相邻点
            else:
                return None#节点已经收缩

    def shousuo(self):#收缩节点
        '''
        随机寻找第一个点，然后遍历其2级节点，再遍历三级节点
        然后寻找下一个大节点，重复上述步骤
        '''
        while True:
            max_key = max(self.vi, key = self.vi.get)#获取最大值对应的节点id
            #去掉节点
            l = []
            l.append(max_key)
            # self.vertexlist.remove(max_key)
            for v1 in self.getVertex(max_key):#相邻节点
                self.Bigvert[max_key].append(v1)
                l.append(v1)
                for v2 in self.getVertex(v1):
                    self.Bigvert[max_key].append(v2)
                    l.append(v2)

                
            if len(self.vertexlist) == 0:
                return 0
        