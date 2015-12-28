'''
Created on Dec 11, 2015

@author: SRawoor
'''
from array import array;

def checkio(data):
   
    print data;
    arr = array('i',data);
    length = len(data)

    listoflists = []
    templist = []
    
    for i in range(0,length,1):
        item = arr[i];
        listoflists.append([])
        for j in range(0,length,1):
            if(item==arr[j]):
                listoflists[i].append(j)
     
    for item in listoflists:
        if item not in templist:
            if(len(item)!=999999):
                templist.append(item)
            else:
                data[item[0]]=-999999    
    
    tempdata = [item for item in data if item!=-1]; 
    return tempdata

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
    #checkio([1, 2, 3, 1, 3])
    '''
        for i in range(0,length,1):
        for j in range(i+1,length,1):
            print str(arr[i])+"comp"+str(arr[j])
            if(arr[j]!=arr[i]):
                if(j==length-1):
                    arr[i]=-1
                    print 'true'+str(j)+'...arr['+str(i)+']='+str(arr[i])
            else:
                break;
            print '*****************'
        print '--------------------------------------------'
    '''