import pandas as pd
import numpy as np
from collections import defaultdict
import ImputingValuesSolns as s



## Imputing Values
# Question 1 Part 1
def check_sal_dropped(drop_sal_df):
    '''
    INPUT drop_sal_df - a pandas dataframe with all rows that are missing a value the salary column removed.  The dataframe should only have the columns of num_vars (quant variables)

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if drop_sal_df.equals(s.drop_sal_df):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, this should be the num_vars dataframe with salary removed.")


# Question 1 Part 2
def check_fill_df(fill_df):
    '''
    INPUT
    fill_df - a pandas dataframe with the mean imputed for all the missing numeric columns of drop_sal_df

    Prints statement related to the correctness of the solution of the dataframe.
    '''
    if fill_df.equals(s.fill_df):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, this should be the num_vars dataframe with salary removed.  Then you should fill all the numeric columns with the mean for each column.")


# Question 2
def r2_y_test_check(rsquared_score, length_y_test):
    '''
    INPUT
    rsquared_score - float

    length_y_test - int

    Prints statement related to the correctness of the rsquared_score and length_y_test
    '''
    if rsquared_score == s.rsquared_score and length_y_test == s.length_y_test:
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try the steps again, and feel free to use the steps at the top of this notebook to help you out if you get stuck.")
