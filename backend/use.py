import jieba as jb
import numpy as np
import pandas as pd
import heapq
import sys 
import copy 
import json
from functools import cmp_to_key 
class AiQuery:
    def __init__(self) -> None:     
        Pxy = pd.read_csv('./pxy.csv')
        #print(Pxy)
        with open('word_dict.json', encoding='utf8') as f1:
            self.word_dict = json.load(f1)
        #print(word_dict)
        with open('word_freq.json', encoding='utf8') as f2:
            self.word_freq = json.load(f2)
        #print(word_freq)
        with open('label_dict.json',encoding='utf8') as f3:
            self.label_dict = json.load(f3)
        self.label_dict_index = [0,] * (len(self.label_dict)+1)
        for i in self.label_dict.items():
            self.label_dict_index[i[1]] = i[0]
    def query(self,sentence:str):
        row = list(pd.Series(jb.lcut(sentence, cut_all=True)).unique())
        prob = np.zeros(shape=(len(self.label_dict),))
        Pxy = np.array(Pxy)

        tot_info = 0
        got = [False,] * (len(self.word_dict) + 1)
        for i in row:
            if (self.word_dict.get(i) and self.word_freq[i] < 15000 and not got[self.word_dict[i]]):
                tot_info += 1
                got[self.word_dict[i]] = True 
                
                for j in range(len(self.label_dict)):
                    prob[j] += Pxy[self.word_dict[i]][j]

        heap = []
        for j in range(3):
            heapq.heappush(heap, (prob[j], j))
        for j in range(3, len(self.label_dict)):
            heapq.heappushpop(heap, (prob[j], j))

        return '(仅供参考)根据您的描述，较可能的三种疾病类型是:{},{},{}'.format(self.label_dict_index[heap[0][1]], self.label_dict_index[heap[1][1]], self.label_dict_index[heap[2][1]])
        





