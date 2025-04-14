#Binary search algorithm implementation

#Proving that binary search is faster than naive search

#Naive search: scan entire list and ask if its equal to the target 
#if yes, return the index 
#if no, then return -1 

def naive_search(l, target):
    #exapmple l = [1,3,10,12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

#Binary search uses divide and conquer 
#We will leverage the fact that our list is SORTED to make search faster 

def binary_search(l, target, low=None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
        
    if high < low:
        return -1
        
    #exapmple l = [1,3,5,10,12] #Targer is 10, should return index 3
    midpoint = (low + high) //2
    
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        #target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)
    
if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))