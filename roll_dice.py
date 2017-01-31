# -*- coding: utf-8 -*-
#! /usr/bin/python3

import random
import time
import matplotlib.pylab as plt
import numpy as np
import statistics



def roll_dice():
    return random.randint(1,6)


def hist_plot(Input,Max):
    
    plt.hist(Input,bins=[1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.xlabel("Sum of two dice")
    plt.ylabel("Sum of two dice frequency")
    plt.title("Frequency of sum of rolling two dice in 100 times")
    plt.yticks(np.arange(0,Max+1,2))
    plt.xticks(np.arange(1,13,1))
    plt.show()

######################################################
def CDF(Input,count):
    Max_y = 0
    c= 0
    cdf_values = 13*[0]
    cdf = 0
    index = 1
    for j in range(2,13):
        c = Input.count(j)
        cdf += c
        cdf_values[index] = cdf/count
        index += 1
        if c > Max_y:
            Max_y = c
    
    return cdf_values,Max_y
######################################################
def dice_roller(count):
    i = 0
    results = count*[0]

    while i < count:
        first = roll_dice()
        second = roll_dice()
        results[i] = first + second
        i += 1
    
    return results


###############################################################
def max_distance(List1,List2):
    max_distance = 0
    n = 0
    for item in List1:
        tmp = abs(item - List2[n])
        if tmp > max_distance:
            max_distance = tmp
        n += 1
    
    return max_distance

#################################################################


def cdf_100():
    
    results1 = dice_roller(100)
    
    cdf_values1,Max_y = CDF(results1,100)

    results1 = sorted(results1)
    
    hist_plot(results1,Max_y)    
    
    less_nine = 0
    for num in results1:
        if num <= 9:
            less_nine += 1        

    less_nine = less_nine/100
    
    
    #print(results)

    median = statistics.median(results1)
    print("Median : ",str(median))    
    print("probability of dice sum to become less equal than 9 : ",str(less_nine))
    
    xvalues = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    yvalues1 = cdf_values1

    y_median = 13*[0.5]

    y_less_nine = 13*[less_nine]

    plt.xticks(np.arange(2,13,1))
    plt.yticks(np.arange(0,1.1,0.1))
    plt.title("CDF PLOT for 100 times rolling two dice(sum of two dice)")
    plt.xlabel("sume of two dice")
    plt.ylabel("Cumulative frequency in percentage")

    plt.plot(xvalues,yvalues1,drawstyle='steps-post' ,label='CDF')
    plt.plot(xvalues,y_median,label='y=0.5 for finding median') #y=0.5
    plt.plot(xvalues,y_less_nine,'--',label='y=probability for less equal 9')
    plt.legend(loc=0)
    plt.show()
    
     
    results2 = dice_roller(100)
    y_values2,Max = CDF(results2,100)
    results2 = sorted(results2)
    hist_plot(results2,Max)
    
    distance = max_distance(cdf_values1,y_values2)
    print("max point-wise distance for 100 times rolling : ",str(distance))
    
    plt.xticks(np.arange(2,13,1))
    plt.yticks(np.arange(0,1.1,0.1))
    plt.title("CDF PLOTs for 100 times rolling two dice(sum of two dice)")
    plt.xlabel("sume of two dice")
    plt.ylabel("Cumulative frequency in percentage")

    plt.plot(xvalues,yvalues1,drawstyle='steps-post' ,label='CDF for first time')
    plt.plot(xvalues,y_values2,drawstyle='steps-post',label='CDF for second time') #y=0.5
    plt.legend(loc=0)
    plt.show()
    
        
def cdf_1000():
    
    results1 = dice_roller(1000)
    results2 = dice_roller(1000)
    
    cdf_values1,Max_y1 = CDF(results1,1000)
    cdf_values2,Max_y2 = CDF(results2,1000)    
        
    
    distance = max_distance(cdf_values1,cdf_values2)
        
    print("max point-wise distance for 1000 times rolling : ",str(distance))
    results1 = sorted(results1)
    results2 = sorted(results2)
    xvalues = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    yvalues1 = cdf_values1
    yvalues2 = cdf_values2
    plt.xticks(np.arange(2,13,1))
    plt.yticks(np.arange(0,1.1,0.1))
    plt.title("CDF PLOTs for 1000 times rolling two dice(sum of two dice)")
    plt.xlabel("sume of two dice")
    plt.ylabel("Cumulative frequency in percentage")
    plt.plot(xvalues,yvalues1,drawstyle='steps-post', label='CDF of first time')
    plt.plot(xvalues,yvalues2,drawstyle='steps-post', label='CDF of second time')
    plt.legend(loc=0)
    plt.show()
    
###############################################################################    
    
# start
start = time.time()

cdf_100()
cdf_1000()

print("run time : ",str(time.time()-start))    
    