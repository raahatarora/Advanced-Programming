# To generate list of 25 elements and find the number of frequency in the list

import random

def CountFrequency(my_list):
    
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] +=1
        else:
            freq[item] = 1
            
    for key,value in freq.items():
        print("%d : %d " % (key,value))
        
lis = []
i = 0
while i < 25:
    lis_items = lis.append(random.randint(1, 100))
    i +=1
    

CountFrequency(lis)