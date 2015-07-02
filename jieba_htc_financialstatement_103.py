#encoding=utf-8
import jieba
import pickle
import numpy as np

jieba.set_dictionary('dict.txt.big')
content = open('htc103_data.txt', 'rb').read()
words = jieba.cut(content, cut_all=False)
negative=[]
for i in open('ntusd-negative.txt'):
    negative.append(str(i))

positive=[]
for i in open('ntusd-positive.txt'):
    positive.append(str(i))
point=0
score=[]
for word in words:
    print word.encode('utf-8')
    for a in range(len(positive)):
    	if(positive[a].find(word.encode('utf-8'))!=-1):
           score.append(1)
           # point = point+1
    	   break
    	 
    for b in range(len(negative)):
    	if(negative[b].find(word.encode('utf-8'))!=-1):
            score.append(-1)
            # point = point-1
            break
       
print np.sum(score)
# print point 





   
	   










    
