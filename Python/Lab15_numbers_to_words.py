# Charlie Lab15 numbers to words

# take entered integer and convert to string from dictionary

ones = ['zero', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine']

teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['zeroty', 'onety', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def ones_word(nums):
    global ones, teens, tens
    if nums < 10:
        return ones[nums]
    
    elif nums < 20:
        return teens[nums]
    
    elif nums < 100:
        tens_word = nums // 10
        ones_word = nums % 10
        if ones == 0:
            return tens[tens_word]
        else:
            return tens[tens_word] + '-' + ones[ones_word] 

        
        
def huns_word(num):
    ''' calculate hundreds words '''
    pass

def thous_word(num):
    '''calculate thousands'''

def main():
    ''' main function. test, then call the other functions with conditionals. 
    maybe a repl...
    '''
    print(ones_word(35))


main()

# nums = int(input('Enter a number from 1 - 999: '))
# 187 // 100 = 1
# 187 % 100 = 8
# 187 % 10 = 7
        
    # if nums < 100:
    #     nums % 100
    #     nums % 10
    #     return tens[nums]
        
        
    
    
        

