'''
Logging exercise solution

# STEPS TO COMPLETE ##
1. import logging
2. set up config file for logging called `results.log`
3. add try except with logging for success or error
   in relation to checking the types of a and b
4. check to see that log is created and populated correctly
   should have error for first function and success for
   the second
5. use pylint and autopep8 to make changes
   and receive 10/10 pep8 score

author: gunnar
date: December 4, 2025
'''

import logging

logging.basicConfig(
    filename='results.log',  # Name of the log file
    level=logging.DEBUG,      # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def sum_vals(a, b):
    '''
    Args:
        a: (int)
        b: (int)
    Return:
        a + b (int)
    '''
    try:
        logging.info("%f, %f", a, b)
        assert isinstance(a, int)
        assert isinstance(b, int)
        logging.info("SUCCESS: it looks like the values are ints")
        return a+b
    except AssertionError:
        logging.error("It appears that the first value is not of type int or float")
        return "Change the inputs to int"


if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(4, 5)
