'''
Charlie lab 21 count words
display the most frequent words from a text file containing a book
'''
import string
from collections import Counter
word_count = {}
word_list = []
def txt_to_list(file_path):
    ''' put words into a list of tuples with the count as the value'''
    with open(file_path) as f: #open the file in a variable
        words = f.read().lower() # read and take out lowercase words
        translator = str.maketrans('', '', string.punctuation) #string method to strip punctuation
        string_without_punct = words.translate(translator)#translate stripped string
        word_list = string_without_punct.split()
        
    print(word_list)
    # print(word)
    # print(string_without_punct)

                

def list_to_dict(word_count):
    '''
    put list of words into dictionary with count as values
    '''
    # for word_list in f: 
    #     word_list[word] += 1
    # else:
    #     word_list[word] = 1
    
    pass
    
    
        
    



def main():
    txt_to_list('lab21.txt')
    print (word_count)
main()
    
        
    # print(list_of_dicts)
    # print(keys)

     


    



    



