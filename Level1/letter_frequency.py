'''
Created on Dec 14, 2015

@author: SRawoor
'''
import re
import operator
def checkio(text):
    '''
You are given a text, which contains different english letters and punctuation symbols. 
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". 
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. 
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
    '''
    dict = {} 
    list1 = text.lower()
    
    for item in list1:
        val = re.search(r'[a-z]', item)
        if val is not None:
            dict[val.group()] = list1.count(val.group());
    
    '''
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
    print sorted_dict
    max = 0;
    prev = ''
    for item in sorted_dict:
        if sorted_dict[item] >= max:
            if sorted_dict[item] == max:
                if ord(prev) < ord(item):
                    frequent_item_key = prev
                else:
                    frequent_item_key = item
        prev = item      
    print frequent_item_key
    '''
    max = 0;          
    dictKeys = dict.keys();
    print dictKeys
    
    frequent_item_key_list = []
    
    for item in dictKeys:
        if dict[item] >= max:
            max = dict[item];
            if item not in frequent_item_key_list: frequent_item_key_list.append(item)
    
    #print frequent_item_key_list == dictKeys
    frequent_item_key_list.sort()
    #print frequent_item_key_list
    #print frequent_item_key_list[0]
    #print sorted(frequent_item_key_list)
    return frequent_item_key_list[0]
    #print '*******'
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    '''
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    
    #print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
    '''
    checkio('AAaooo!!!!')
    checkio("One")