'''
Created on Dec 14, 2015

@author: SRawoor
'''
from operator import xor
def checkio(game_result):
    '''
    print (type1_func(game_result))or(type2_func(game_result))or(type3_func(game_result))or(type4_func(game_result))
    print '......................................'
    print type1_func(game_result)
    print type2_func(game_result)
    print type3_func(game_result)
    print type4_func(game_result)
    print '**********************'
    
    if (type1_func(game_result)[0])or(type2_func(game_result)[0])or(type3_func(game_result)[0])or(type4_func(game_result)[0]):
        print True
    #return "D" or "X" or "O"
    '''
    tuple1 = type1_func(game_result)
    tuple2 = type2_func(game_result)
    tuple3 = type3_func(game_result)
    tuple4 = type4_func(game_result)
    
    if tuple1[0]:
      return tuple1[1]
    elif tuple2[0]:
      return tuple2[1]
    elif tuple3[0]:
      return tuple3[1]
    elif tuple4[0]:
      return tuple4[1]
    else:
      return "D"
def type1_func(game_result):
    for i in [0,1,2]:
        j=0
        b1 = ((game_result[i][j]))
        b2 = ((game_result[i][j+1]))
        b3 = ((game_result[i][j+2]))
        #if (b1==b2)and(b2==b3)and(b3==b1):
        if (b1==b2==b3=='X')or(b1==b2==b3=='O'):
            #print 'type1:'+(b1)
            return (True,(b1))
    return (False,"D")
        
       
def type2_func(game_result):
    for j in [0,1,2]:
        i=0
        b1 = ((game_result[i][j]))
        b2 = ((game_result[i+1][j]))
        b3 = ((game_result[i+2][j]))
        #print str(b1)+' '+str(b2)+' '+str(b3)
        #if (b1==b2)and(b2==b3)and(b3==b1):
        if (b1==b2==b3=='X')or(b1==b2==b3=='O'):
            #print 'type2:'+(b1)
            return (True,(b1))
    return (False,"D")


def type3_func(game_result):
    #if (game_result[0][0]==game_result[1][1])and(game_result[1][1]==game_result[2][2])and(game_result[2][2]==game_result[0][0]):
    if (game_result[0][0]==game_result[1][1]==game_result[2][2]=='X')or(game_result[0][0]==game_result[1][1]==game_result[2][2]=='O'):
        #print 'type3:'+game_result[1][1]
        return (True,game_result[1][1])
    return (False,"D")


def type4_func(game_result):
    #if (game_result[0][2]==game_result[1][1])and(game_result[1][1]==game_result[2][0])and(game_result[0][2]==game_result[2][0]):
    if(game_result[0][2]==game_result[1][1]==game_result[2][0]=='X')or(game_result[0][2]==game_result[1][1]==game_result[2][0]=='O'):
        #print 'tyep4:'+game_result[1][1]
        return (True,game_result[1][1])
    return (False,"D")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    '''
    checkio([
        "X.O",
        "XX.",
        "XOO"])
    checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    '''