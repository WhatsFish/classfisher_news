#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:29:20 2020

@author: lihaoyang03
"""

import numpy as np
import pandas as pd

datas =  pd.read_table("./data/toutiao_cat_data.txt",sep = "_!_",nrows=100)
datas.columns = ['新闻id','类别id','新闻类型','新闻标题','新闻关键词']
datas = datas.drop(['新闻关键词'],axis=1)

import jieba as jb
splt_sen = []
for sen in datas["新闻标题"]:
    splt = ' '.join(jb.cut(sen))
    splt_words = splt.split()
    splt_sen.append(splt_words)
    
    