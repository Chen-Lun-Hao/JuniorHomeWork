users=["user1","user2","user3","user4","user5"]
items=["itemA","itemB","itemC","itemD","itemE",]
#用户购买记录数据
datasets=[
    [1,0,1,1,0],
    [1,0,0,1,1],
    [1,0,1,0,0],
    [0,1,0,1,1],
    [1,1,1,0,1],
]
import pandas as pd
df=pd.DataFrame(datasets,
               columns=items,
               index=users)
print(df)
#from sklearn.metrics import jaccard_score
#jaccard_score(df['itemA'],df['itemB'])
#print(jaccard_score(df['itemA'],df['itemB']))


from sklearn.metrics.pairwise import pairwise_distances
user_similar = 1-pairwise_distances(df.values,metric="jaccard")
user_similar = pd.DataFrame(user_similar,columns=users,index=users)
print("用户之间的两两相似度：")
print(user_similar)
topN_users = {}
for i in user_similar.index:
    #取出每列数据，并删除自身，然后排序数据
    _df = user_similar.loc[i].drop([i])
    _df_sorted =_df.sort_values(ascending=False)
    top2=list(_df_sorted.index[:2])
    topN_users[i]=top2
    print("Top2相似用户：")
    from pprint import pprint
    pprint(topN_users)

#构建推荐结果
import  numpy as np
rs_results={}
for user, sim_users in topN_users.items():
    rs_result = set() #存储推荐结果
    for sim_user in sim_users:
        #构建初始的推荐结果
        rs_result =rs_result.union(set(df.loc[sim_user].replace(0,np.nan).dropna().index))

        rs_result -= set(df.loc[user].replace(0, np.nan).dropna().index)
        rs_results[user] = rs_result
    print("最终推荐结果：")
    pprint(rs_results)


