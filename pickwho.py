# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:59:13 2021

@author: peachrl
"""

import pandas as pd
import numpy as np
import os
  
    

dict_saved = {'余永亮': 0,
 '王智慧': 0,
 '鲍麟': 0,
 '朱博闻': 2015,
 '罗健': 2016,
 '李贤冬': 2016,
 '黄恺俊': 2016,
 '章顺良': 2017,
 '胡强强': 2017,
 '刘元森': 2018,
 '江松': 2018,
 '李欣欣': 2018,
 '高慧君': 2018,
 '徐梦凡': 2019,
 '周天翼': 2019,
 '陶瑞灵': 2019,
 '管尧雨': 2020,
 '林伟腾': 2020,
 '高天宇': 2020,
 '王凯华': 2020,
 '房玮': 2021}

def list_dict(doc_path):
    df = pd.read_table(f'{doc_path}\\namelist.txt', header=None, index_col=None, encoding='utf-8', names=['name', 'year'], sep='\s+', engine='python') 
    name_list = np.array(df)
    list_dict = dict(name_list)
    return list_dict

#picklist('E:/Python', 0, 0, 1, 1, 1, 1, 1, 1)
def picklist(doc_path, key_0, key_2021, key_2020, key_2019, key_2018, key_2017, key_2016, key_2015):
    name_list = []
    name_list_cut = []
    df = pd.read_table(f'{doc_path}\\namelist.txt', header=None, index_col=None, encoding='utf-8', names=['name', 'year'], sep='\s+', engine='python') 
    name_list = np.array(df)
    for i in range(name_list.shape[0]):
        # key_0=1:有老师
        if key_0:
            if name_list[i][1]==0:
                name_list_cut.append(name_list[i][0])
        # key_2021=1:有2021级
        if key_2021:
            if name_list[i][1]==2021:
                name_list_cut.append(name_list[i][0])
        # key_2020=1:有2020级
        if key_2020:
            if name_list[i][1]==2020:
                name_list_cut.append(name_list[i][0])
        # key_2019=1:有2019级
        if key_2019:
            if name_list[i][1]==2019:
                name_list_cut.append(name_list[i][0])
        # key_2018=1:有2018级
        if key_2018:
            if name_list[i][1]==2018:
                name_list_cut.append(name_list[i][0])
        # key_2017=1:有2017级
        if key_2017:
            if name_list[i][1]==2017:
                name_list_cut.append(name_list[i][0])
        # key_2016=1:有2016级
        if key_2016:
            if name_list[i][1]==2016:
                name_list_cut.append(name_list[i][0])
        # key_2015=1:有2015级
        if key_2015:
            if name_list[i][1]==2015:
                name_list_cut.append(name_list[i][0])
    return name_list_cut

  
def luckyone(name_list_cut):
    lucky_num = np.random.randint(len(name_list_cut))
    return name_list_cut[lucky_num]

def restlist(name_list_cut, kick_out):
    name_list_cut.remove(kick_out)
    return name_list_cut

def save(save_key, list_dict, name_list_cut):
    if save_key:
        data = open(os.getcwd()+r'\data\data.txt','w+',encoding='utf-8')
        for i in name_list_cut:
            data.write(i+' ')
            data.write(str(list_dict[i])+'\n')
        #     data.write(str(i.decode('utf-8'))+' ')
        #     data.write(str(list_dict[i.decode('utf-8')])+'\n')
        data.close()
        return
    else:
        return

def autosave(list_dict, name_list_cut):
    data = open(os.getcwd()+r'\data\tmp.txt','w+',encoding='utf-8')
    for i in name_list_cut:
        data.write(i+' ')
        data.write(str(list_dict[i])+'\n')
        # data.write(str(i)+' ')
        # data.write(str(list_dict[i])+'\n')
    data.close()
    return

def savedlist(list_dict):
    name_list = []
    name_list_cut = []
    df = pd.read_table(os.getcwd()+r'\data\tmp.txt', header=None, index_col=None, encoding='utf-8', names=['name', 'year'], sep='\s+', engine='python') 
    name_list = np.array(df)
    for i in range(name_list.shape[0]):
        name_list_cut.append(name_list[i][0])
    return name_list_cut
