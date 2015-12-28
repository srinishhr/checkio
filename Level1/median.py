'''
Created on Dec 12, 2015

@author: SRawoor
'''
def checkio(data):
    data.sort()
    if(len(data)%2!=0):
        print data[len(data)/2]
    else:
        print (float)(data[(len(data)/2)-1]+data[len(data)/2])/2
    #replace this for solution
    return data[0]

#These " s" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    #checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")
    