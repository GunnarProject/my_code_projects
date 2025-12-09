'''## STEPS TO COMPLETE ##
# 1. import logging
# 2. set up config file for logging called `test_results.log`
# 3. add try except with logging and assert tests for each function
#    - consider denominator not zero (divide_vals)
#    - consider that values must be floats (divide_vals)
#    - consider text must be string (num_words)
# 4. check to see that the log is created and populated correctly
#    should have error for first function and success for
#    the second
# 5. use pylint and autopep8 to make changes
#    and receive 10/10 pep8 score
author: gunnar
date: December 4, 2025
'''

import logging

logging.basicConfig(
    filename='test_results.log',  # Name of the log file
    level=logging.DEBUG,      # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    try:
        logging.info("%f, %f", numerator, denominator)
        assert isinstance(numerator, float)
        assert isinstance(denominator, float)
        assert denominator != 0
        logging.info("SUCCES: numerator and denominator are both floats")
        fraction_val = numerator/denominator
        return fraction_val
    except AssertionError:
        return logging.error("ERROR: Denominator is zero or one the values is not a float")


def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    try:
        logging.info("%s", text)
        assert isinstance(text, str)
        logging.info("SUCCES: text is of type string")
        word_count = len(text.split())
        return word_count
    except AssertionError:
        return logging.error("ERROR: text is not of type string")


if __name__ == "__main__":
    divide_vals(3.4, 0)
    divide_vals(4.5, 2.7)
    divide_vals(-3.8, 2.1)
    divide_vals(1, 2)
    num_words(5)
    num_words('This is the best string')
    num_words('one')
