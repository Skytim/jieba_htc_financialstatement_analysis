#encoding=utf-8
import jieba
import pickle
import numpy as np
import os
import csv
jieba.set_dictionary('dict.txt.big')
negative=[]
for i in open('ntusd-negative.txt'):
    negative.append(str(i))
positive=[]
for i in open('ntusd-positive.txt'):
    positive.append(str(i))
f = open("result.csv","w")
w = csv.writer(f)
w.writerow( ('index', 'value') )
for root, dirs, files in os.walk("htc_data"):
    for f in files:
        if (f!=".DS_Store"):

           content = open('htc_data/'+f, 'rb').read()
           words = jieba.cut(content, cut_all=False)
           score=[]
           for word in words:
              for a in range(len(positive)):
                 if(positive[a].find(word.encode('utf-8'))!=-1):
                    score.append(1)
                    break
         
              for b in range(len(negative)):
                 if(negative[b].find(word.encode('utf-8'))!=-1):
                    score.append(-1)
                    break
           print f         
           print np.sum(score)
           w.writerows([f,str(np.sum(score))])
f.close()







   
       








            










    
