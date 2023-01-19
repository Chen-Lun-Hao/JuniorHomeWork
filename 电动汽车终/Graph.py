'''
Description: 图的结构类
Author: Xiao
Date: 2022-11-02 08:53:09
LastEditTime: 2023-01-09 21:50:18
LastEditors: Xiao
'''
import Vertex

class Graph:
    def __init__(self, vertexlist, edgelist):
        self.vertexlist = vertexlist#里面放的Vertex类型
        self.edgelist = edgelist
        self.Bigvert = {}#key是出口id，value是大节点包含的节点id
        self.vi={}#节点的重要度
        self.g = self.build(vertexlist, edgelist)
    
    def build(self,vertexlist, edgelist):#构造有向图,邻接表形式
        g = {}#图的结构，key是节点id,value是与之相连的节点id
        for v in vertexlist:#循环获取节点
            g[v.id] = []
            for e in edgelist:#循环获取边
                if v.id == e.link[0]:#v是起点
                    v.setEdge(e)
                    v.inv = v.inv + 1#入度
                    g[v.id].append(e.link[1])#保存终点id
                if v.id == e.link[1]:#v是终点
                    v.outv = v.outv + 1#出度
        return g

    def calculate(self):#计算节点中的最大以及最小值，为计算重要度提供条件
        self.maxl = 0
        self.minl = 999
        self.maxn = 0
        self.minn = 999
        for v in self.vertexlist:
            if self.maxl < v.l:
                self.maxl = v.l
            if self.minl > v.l:
                self.minl = v.l
            if self.maxn < v.n:
                self.maxn = v.n
            if self.minn > v.n:
                self.minn = v.n

    def Vimportance(self):#节点重要度计算
        for v in self.vertexlist:
            self.vi[v.id] = '公式'
        
        

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
        