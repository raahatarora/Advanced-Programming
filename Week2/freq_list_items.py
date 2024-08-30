# To generate a list and find the frequency of each item in the list

def CountFrequency(my_list):
    
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] +=1
        else:
            freq[item] = 1
            
    for key,value in freq.items():
        print("%d : %d " % (key,value))
        

n = int(input("Enter the no of items in the list: \n"))
lis = []
i = 0
print("Enter the items of the list:")
while i < n:
    lis_item = lis.append(int(input()))
    i +=1
    
CountFrequency(lis)
    
    
    