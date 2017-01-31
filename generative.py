# -*- coding: utf-8 -*-
#! /usr/bin/python3

import sys
import time
import random
import numpy as np
import matplotlib.pylab as plt


def word_counter(file):
    words = {}
    Total = 0
    f = open(file,'r')
    
    for line in f:
        splited = line.split()
        for item in splited:
            if item in words.keys():
                words[item] += 1
                Total += 1
            else:
                words[item] = 1
                Total += 1
                
    f.close()
    return words,Total



def char_counter(file_name):
    try:
        file = open(file_name,'r')
    except:
        print("Something is wrong with your file name!")

    string = file.read()
    Total_char_count = len(string)
    
    return Total_char_count
    
#####################################################
def CDF(Input):
    cdf = len(Input)*[0]
    tmp = 0
    index = 0
    for item in Input:
        tmp += Input[item]    
        cdf[index] = [item,tmp]
        index += 1
        
    return cdf
    
######################################################
def y_scatter_axis(Input,Max):
    y = Max*[0]
    tmp = list(Input.values())
    index = 0
    for num in tmp:
        y[index] = num
        index += 1
    y = sorted(y)
    y.reverse()
    return y
###################################################

def CDF_words(List,Total):
    cdf_values = len(List)*[0]
    i = 0
    tmp = 0
    while i < len(List):
        tmp += List[i]/Total
        cdf_values[i] = tmp
        i += 1
    
    return cdf_values
    
    
##################################################    
def max_distance(L1,L2,L3):
    Max1 = 0
    Max2 = 0
    index = 0
    for num in L2:
        tmp = abs(L1[index]-num)
        if Max1 < tmp:
            Max1 = tmp
        index += 1
    index = 0
    for num in L3:
        tmp = abs(L1[index]-num)
        if Max2 < tmp:
            Max2 = tmp
        index += 1
    
    return Max1,Max2
    
##################################################    
def file_creator(Input,Len,file_name):
    
    file = open(file_name,'w')
    i = 0
    while i < Len:
        r = random.random()
        for item in Input:
            if item[1] > r:
                file.write(item[0])
                break
    
        i += 1
    file.close()    
        
#start of prigram
start_time = time.time()

zipf_probabilities = {' ': 0.17840450037213465, '1': 0.004478392057619917, 
'0': 0.003671824660673643, '3': 0.0011831834225755678, 
'2': 0.0026051307175779174, '5': 0.0011916662329062454,
'4': 0.0011108979455528355, '7': 0.001079651630435706, '6': 0.0010859164582487295,
'9': 0.0026071152282516083, '8': 0.0012921888323905763, '_': 2.3580656240324293e-05,
'a': 0.07264712490903191, 'c': 0.02563767289222365, 'b': 0.013368688579962115,
 'e': 0.09688273452496411, 'd': 0.029857183586861923,
'g': 0.015076820473031856, 'f': 0.017232219565845877, 'i': 0.06007894642873102, 
'h': 0.03934894249122837, 
'k': 0.006067466280926215, 'j': 0.0018537015877810488, 'm': 0.022165129421030945,
'l': 0.03389465109649857, 'o': 0.05792847618595622, 'n': 0.058519445305660105,
'q': 0.0006185966212395744, 'p': 0.016245321110753712, 's': 0.055506530071283755,
 'r': 0.05221605572640867, 'u': 0.020582942617121572,
't': 0.06805204881206219, 'w': 0.013964469813783246, 'v': 0.007927199224676324,
'y': 0.013084644140464391, 'x': 0.0014600810295164054, 'z': 0.001048859288348506}


uniform_probabilities = {' ': 0.1875, 'a': 0.03125, 'c': 0.03125, 'b': 0.03125, 
'e': 0.03125, 'd': 0.03125, 'g': 0.03125, 'f': 0.03125, 'i': 0.03125, 
'h': 0.03125, 'k': 0.03125, 'j': 0.03125, 'm': 0.03125, 'l': 0.03125, 'o': 0.03125, 
'n': 0.03125, 'q': 0.03125, 'p': 0.03125, 's': 0.03125, 'r': 0.03125, 'u': 0.03125, 
't': 0.03125, 'w': 0.03125, 'v': 0.03125, 'y': 0.03125, 'x': 0.03125, 'z': 0.03125}


file_name = sys.argv[1]

Total_char_count = char_counter(file_name)

cdf_zipf_chars = CDF(zipf_probabilities)
cdf_uniform_chars = CDF(uniform_probabilities)

file_creator(cdf_uniform_chars,Total_char_count,"uniform.txt")
file_creator(cdf_zipf_chars,Total_char_count,"zipf.txt")

simple_wiki_words , simple_total = word_counter("simple-20160801-1-article-per-line")
zipf_words,zipf_total = word_counter("zipf.txt")
uniform_words,uniform_total = word_counter("uniform.txt")


simp = len(simple_wiki_words)
uni = len(uniform_words)
zipf = len(zipf_words)
Max = max(simp,uni,zipf)


y_simple = y_scatter_axis(simple_wiki_words,Max)

y_zipf = y_scatter_axis(zipf_words,Max)

y_uniform = y_scatter_axis(uniform_words,Max)

Max_y = max(y_simple[0],y_uniform[0],y_zipf[0])

x_values = Max*[0]
for i in range (1,Max+1):
    x_values[i-1] = i
    
plt.title("Word rank frequency diagram")
plt.xlabel("Words Rank")
plt.ylabel("frequency")
plt.loglog(x_values,y_simple,c='r',label = 'Simple wikipedia')
plt.loglog(x_values,y_uniform,c='g',label = 'uniform ')
plt.loglog(x_values,y_zipf,c='b',label = 'zipf ')
plt.legend(loc=0)
plt.show()

cdf_simple = CDF_words(y_simple,simple_total)
cdf_uniform = CDF_words(y_uniform,uniform_total)
cdf_zipf = CDF_words(y_zipf,zipf_total)

plt.title("CDF PLOT (loglog-plot)")
plt.xlabel("Words Rank")
plt.ylabel("Cumulative frequency")

plt.yticks(np.arange(0,1.1,0.1))
plt.loglog(x_values,cdf_simple,c='b', label='Simple Wikipedia')
plt.loglog(x_values,cdf_zipf,c='r', label='Zipf')
plt.loglog(x_values,cdf_uniform,c='g', label='Uniform')
plt.legend(loc=0)
plt.show()

Max_zipf,Max_uniform = max_distance(cdf_simple,cdf_zipf,cdf_uniform)

print("max point-wise distance between zipf and data set : ",str(Max_zipf))
print("max point-wise distance between uniform and data set : ",str(Max_uniform))

print("Run time was : ",str(time.time()-start_time))