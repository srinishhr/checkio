'''
Created on Dec 14, 2015

@author: SRawoor
'''

def count_neighbours(grid, row, col):
    
    count = 0
    row_max = len(grid)
    for item in grid:
      col_max = len(item) 
    '''
    [row-1][col-1]  [row-1][col]  [row-1][col+1]
    [row][col-1]                  [row][col+1]
    [row+1][col-1]  [row+1][col]  [row+1][col+1]
    '''

    for item1 in [-1,0,1]:
      row_n = row+item1;
      #print row_n
      #print '**************'
      if row_n>=0 and row_n<row_max:
        for item2 in [-1,0,1]:
          col_n = col+item2
          #print col_n
          #print '-----'
          if col_n>=0 and col_n<col_max:
            #print 'grid['+str(row_n)+']['+str(col_n)+']-->'+str(grid[row_n][col_n])
            count = count + grid[row_n][col_n]
            #print count 
          
    return count-grid[row][col]
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    print count_neighbours(((1, 0, 1, 0, 1),
                      (0, 1, 0, 1, 0),
                      (1, 0, 1, 0, 1),
                      (1, 1, 0, 1, 0),
                      (0, 0, 1, 0, 1),
                      (0, 1, 0, 1, 0),), 5, 4)
    print '-------------------'
    '''                            
    count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
                                 
    count_neighbours(((1, 1, 1),
                      (1, 1, 1),
                      (1, 1, 1),), 0, 2) == 3, "Dense corner"
    
    count_neighbours((((1,0,1,0,1),
                      (0,1,0,1,0),
                      (1,0,1,0,1),
                      (0,1,0,1,0),
                      (1,0,1,0,1),
                      (0,1,0,1,0),), 5, 4)
                     
    '''