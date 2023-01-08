'''
Description: 读取数据
Author: Xiao
Date: 2022-12-26 17:01:28
LastEditTime: 2022-12-28 14:03:33
LastEditors: Xiao
'''

import pandas as pd

def MathorCup2022(path):
    df = pd.read_excel(path)
    #指标文件名称
    c = list(df.columns)
    # print(c)
    return df, c

def transform(df):#数据编码处理
    del df['用户id']
    del df['用户描述']
    del df['用户描述.1']
    del df['终端品牌']
    del df['终端品牌类型']

    # print(list(df.columns))

    d4 = {1:1,2:0} # 是否遇到过网络问题 0 1
    d5_19 = {-1:0,1:1,2:1,3:1,4:1,5:1,6:1,7:1,98:1}
    # d13_19 = {-1:0,1:1,2:1,3:1,4:1,5:1,6:1,7:1,98:1}
    d245g = {'2G':0,'4G':1,'5G':2}
    d_yuyin = {'GSM':0, 'CSFB':1, 'VOLTE':2,'VoLTE':2,'EPSFB':3,'VONR':4}
    d_yesno = {0:0,'是':1,'否':0}
    d_level = {'未评级':1,'准星':2, '一星':3,'二星':4,'三星':5, '白金卡':6, '钻石卡':7, '银卡':8,'金卡':9}

    df.iloc[:,4] = df.iloc[:,4].map(d4)

    # for i in range(5,13):
    #     df.iloc[:,i] = df.iloc[:,i].map(d5_12)
        
    # for i in range(13,20):
    #     df.iloc[:,i] = df.iloc[:,i].map(d13_19)
    for i in range(5,20):
        df.iloc[:,i] = df.iloc[:,i].map(d5_19)
        
    df['重定向次数'] = df['重定向次数'].fillna(0)
    df['重定向驻留时长'] = df['重定向驻留时长'].fillna(0)
    df['4\\5G用户'] = df['4\\5G用户'].map(d245g)
    df['语音方式'] = df['语音方式'].map(d_yuyin)
    df['外省流量占比'] = df['外省流量占比'].fillna(0)

    for i in ['是否关怀用户', '是否去过营业厅','是否4G网络客户（本地剔除物联网）', '是否5G网络客户', '是否实名登记用户']:
        df[i] = df[i].fillna(0).map(d_yesno)

    df['客户星级标识'] = df['客户星级标识'].fillna(0).map(d_level)

    print(df.head(5))
    
    df=df.dropna() # 只有五行有缺失，直接删除
    return df
    
def savecsv(df,path):
    df.to_csv(path)
    return 0

df, c = MathorCup2022('C:/Users/20851/Desktop/2022年MathorCup大数据竞赛-赛道B初赛/附件1语音业务用户满意度数据.xlsx')
df = transform(df)
savecsv(df,'C:/Users/20851/Desktop/2022年MathorCup大数据竞赛-赛道B初赛/附件1.csv')