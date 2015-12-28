'''
Created on Dec 11, 2015

@author: SRawoor
'''
import re
def checkio(data):

    '''
    The password will be considered strong enough if its length is greater than or equal to 10 symbols, 
    it has at least one digit, 
    as well as containing one uppercase letter and 
    one lowercase letter in it. 
    The password contains only ASCII latin letters or digits.
    '''
    if len(data)>=10 and re.search('[0-9]+', data) and re.search('[A-Z]+', data) and re.search('[a-z]+', data):
      return True
    else:
      return False
            
    
    #return True or False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These " s" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"