import pandas as pd
import numpy as np
from collections import defaultdict
import ImputationMethodsSolns as s

##Imputation Methods
# Question 1
def var_test(question1_solution):
    '''
    INPUT question1_solution - a dictionary with solutions regarding variable types.  The values should be the variables a, b, c, d

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if question1_solution == s.question1_solution:
        print('Nice job! That looks right to me!')
    else:
        print('Oops! Two of these should be quantitative.  One we cannot know for sure. One is a category. One is a boolean.')

# Question 2
def can_we_drop(should_we_drop):
    '''
    INPUT should_we_drop - A variable either a or b as to whether or not we should drop any of the columns above.

    Prints statement related to the correctness of the solution
    '''
    if should_we_drop == s.should_we_drop:
        print("That's right! You should feel comfortable dropping any rows or columns that are completely missing values (or if they are all the exact same value).  However, dropping other columns or rows, even if only containing a few values, should go through further consideration.")
    else:
        print("Actually, you should feel comfortable dropping any rows or columns that are completely missing values.")


# Question 3
def impute_q3_check(impute_q3):
    '''
    INPUT impute_q3 - a dictionary with solutions regarding variable types.  The values should be the variables a, b, c

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if impute_q3 == s.impute_q3:
        print("Nice job! That's right only the first column fills with the mean correctly.  We can't fill the mean of a categorical variable, and the boolean treats the True as 1 and False as 0 to give values that are not 1 or 0.")
    else:
        print('Oops! The first column looks okay, but are you sure the mean of True and False values makes sense?  Should the NaN values be True of False?  The last column is a string - what is the mean for that column?')

# Question 4
def impute_q4_check(impute_q4):
    '''
    INPUT impute_q4 - a dictionary with solutions regarding variable types.  The values should be the variables a, b

    Prints statement related to the correctness of the solution of the dictionary
    '''
    a = "Did not impute the mode."
    b = "Imputes the mode."


    impute_q4_1 = {'Filling column A': b,
                 'Filling column D': a,
                 'Filling column E': a}

    
    if impute_q4 == impute_q4_1:
        print("Nice job! That's right only one of these columns actually imputed a mode.  None of the values in the first column appeared more than once, and 0 was imputed for all of the NaN values.  There were an even number of True and False values, and False was imputed for all the NaN values.")
    else:
        print("Oops! Only one of these columns actually imputed a mode.  What happened with the columns that had no mode?")

        