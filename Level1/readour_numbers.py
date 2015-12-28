'''
Created on Dec 15, 2015

@author: SRawoor
'''
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    '''
    hundredth_digit = 0
    tenth_digit = 0
    units_digit = 0;
    return_string=''
    
    if number > 0 and number <1000:
      hundredth_digit = number/100
      if hundredth_digit != 0:
        return_string += FIRST_TEN[hundredth_digit-1]+' hundred'
        number = number%100
        print number
      tenth_digit = number/10
      print '****************'
      print tenth_digit
      if tenth_digit != 0:
          if tenth_digit == 1:
              return_string +=' '+SECOND_TEN[number-10]
              print return_string
              return
          else:
              return_string += ' '+OTHER_TENS[tenth_digit-2]
              number = number%10
      #print number
      units_digit = number 
      if units_digit !=0:
        #print '.........'
        return_string += ' '+FIRST_TEN[units_digit-1]
     
    print return_string
    '''
    
    #implement using stacks
    lst = []
    i = 0
    while number>0:
        if (int)(number/100) > 0:
          lst.insert(i,(int)(number/100))
          number = number%100
          i = i + 1
        elif (int)(number/10) > 0:
          lst.insert(i,(int)(number/10))
          number = number%10
          i = i +1
        else:
          lst.insert(number,i)
          number = number%1
        #number = number%10
        #print lst[i]
    print lst    
    
    print '*****************'             
    
    return 'string representation of n'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #checkio(1) == 'four', "1st example"
    checkio(133) == 'one hundred thirty three', "2nd example"
    checkio(12) == 'twelve', "3rd example"
    checkio(101) == 'one hundred one', "4th example"
    checkio(212) == 'two hundred twelve', "5th example"
    checkio(400) == 'forty', "6th example"
    #checkio(212)
    #"Don't forget strip whitespaces at the end of string"
