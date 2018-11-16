import pandas as pd
import numpy as np
from collections import defaultdict
import RemovingValuesSolns as s

## Removing Values
# Question 1
def all_drop_test(all_drop):
    '''
    INPUT all_drop - a pandas dataframe with all rows with missing values dropped.

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if all_drop.equals(s.all_drop):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, or take a look at the solution notebook if you get stuck.")


# Question 2
def all_row_test(all_row):
    '''
    INPUT all_row - a pandas dataframe with all rows that have every value as a missing value dropped.

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if all_row.equals(s.all_row):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, or take a look at the solution notebook if you get stuck.")

# Question 3
def only3_drop_test(only3_drop):
    '''
    INPUT all_row - a pandas dataframe with all rows that are missing a value in col3

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if only3_drop.equals(s.only3_drop):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, or take a look at the solution notebook if you get stuck.")

# Question 4
def only3or1_drop_test(only3or1_drop):
    '''
    INPUT all_row - a pandas dataframe with all rows that are missing a value in col1 or col3

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if only3or1_drop.equals(s.only3or1_drop):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, or take a look at the solution notebook if you get stuck.")

