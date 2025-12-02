# ### Task    
# try to return the fraction but if the denominator is zero
# catch the error and return a string saying: 
# "denominator cannot be zero"

def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    try:
        fraction_val = numerator / denominator
        return fraction_val
    except ZeroDivisionError:
        return "denominator cannot be zero"       

# ### Task:
# try to split based on spaces and return num of words
# but if text isnt a string return "text argument must be a string"

def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    try:
        num_words = len(text.split(' '))
        return num_words
    except AttributeError:
        return "text argument must be a string"
        

if __name__ == "__main__":
    fraction_val = divide_vals(10, 2)
    print(fraction_val)
    fraction_val = divide_vals(10, 0)
    num_words = num_words('text text text')
    print(num_words)
    num_words = num_words([1, 2, 3])