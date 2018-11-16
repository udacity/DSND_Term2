import pandas as pd
import numpy as np
from collections import defaultdict
import CatVarSolns as s



        
## Categorical Variables
# Question 1
def cat_df_check(cat_df):
    '''
    INPUT
    cat_df - a pandas dataframe of only the categorical columns of df

    Prints statement related to the correctness of the dataframe provided.
    '''
    if cat_df.equals(s.cat_df):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  The input cat_df variable should be a dataframe of all of the categorical variables.  You can use select_dtypes to select the 'object' data type.")

#Question 2
def cat_df_dict_check(cat_df_dict):
    '''
    INPUT cat_df_dict - a dictionary with numbers for each value corresponding the the number described by each key.

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if cat_df_dict == s.cat_df_dict:
        print('Nice job! That looks right to me!')
    else:
        print("Oops! One or more of those doesn't look quite right.  Each value should be an integer corresponding to the number of columns described.")

#Question 3
def sol_3_dict_check(sol_3_dict):
    '''
    INPUT sol_3_dict - a dictionary with variables for each value corresponding the the key that describes it.

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if sol_3_dict == s.sol_3_dict:
        print('Nice job! That looks right to me!')
    elif sol_3_dict['Which column should you create a dummy variable for?'] != s.sol_3_dict['Which column should you create a dummy variable for?']:
        print("Oops! That is not the column you should be using to create a dummy variable. Try again.")
    elif sol_3_dict['How many new dummy columns do you get when creating dummy variables?'] != s.sol_3_dict['How many new dummy columns do you get when creating dummy variables?']:
        print("Oops! Though you could get that number of dummy variables, that is not what you get using the default setting using one hot encoding or pandas `get_dummies` encoding. Try again.")
    elif sol_3_dict['What happens with the nan values?'] != s.sol_3_dict['What happens with the nan values?']:
        print("Oops! Though that could happen with the NaN values, that is not the default when working with pandas.")

#Question 4
def dummy_cols_df_check(dummy_cols_df):
    '''
    INPUT
    dummy_cols_df - a pandas dataframe of the dummy variables associated with the levels as well as the missing values.

    Prints statement related to the correctness of the dataframe provided.
    '''
    if dummy_cols_df.equals(s.dummy_cols_df):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Your input should just be the 3 columns resulting as dummy variables.  One column for a, one for b, and one for the nan values.")


