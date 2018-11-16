import pandas as pd
import numpy as np
from collections import defaultdict
import HowToBreakIntoTheFieldSolns as s


## How To Break Into the Field
# Question 1
def check_description(descrips):
    '''
    INPUT:
    descrips - should be a set of all descriptions in the dataset - each description should be a string.  You should not need to change the descrips variable at all if your function works correctly.

    This function will print a statement related to whether or not you provided the correct solution for the get_description function
    '''
    val_type = type(next(iter(descrips)))
    if descrips == s.descrips:
        print("Nice job it looks like your function works correctly!")
    elif val_type != str:
        print("Oops - Looks like your column descriptions aren't strings.")
    else:
        print("Though you did provide the correct data type, your result does not match what we were expecting.  Try again.\n\n  Your function should return the description for any column name passed to it.")


#Question 3
def total_count(df, col1, col2, look_for):
    '''
    INPUT:
    df - the pandas dataframe you want to search
    col1 - the column name you want to look through
    col2 - the column you want to count values from
    look_for - a list of strings you want to search for in each row of df[col]

    OUTPUT:
    new_df - a dataframe of each look_for with the count of how often it shows up
    '''
    new_df = defaultdict(int)
    #loop through list of ed types
    for val in look_for:
        #loop through rows
        for idx in range(df.shape[0]):
            #if the ed type is in the row add 1
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df


#Question 4
def higher_ed_test(higher_ed_perc):
    '''
    INPUT:
    higher_ed_perc - a float of the percentage of individuals who received a master's, phd, or professional degree in the stackoverflow dataframe

    This function will print a statement related to whether or not you provided the correct percentage of individuals who received a master's, phd, or professional degree in the stackoverflow dataframe
    '''
    val_type = type(higher_ed_perc)
    if higher_ed_perc == s.higher_ed_perc:
        print("Nice job!  That's right.  The percentage of individuals in these three groups is {}.".format(higher_ed_perc))
    elif val_type != float:
        print("Oops - your final result should be a decimal value associated with the proportion of individuals who are in these three categories (ex. Provide 0.50798 if ~50% of individuals are in these categories)")
    else:
        print("That doesn't look quite like expected.  You can get the percentage of 1's in a 1-0 column by using the .mean() method of a pandas series.")

#Question 6
def conclusions(sol):
    '''
    INPUT:
    sol - a dictionary with keys as strings of statements and values as True or False as to the truth of the string according to the data.

    This function will print a statement related to whether or not you provided the correct in terms of the True or False statement
    '''
    if sol == s.sol:
        print("Nice job that looks right!")
    if sol['There is less than a 1% difference between suggestions of the two groups for all forms of education']:
        print("That's not quite right.  Almost all are less than a 1% difference.  However, there is almost a 3% difference in those that ")
    if sol['Everyone should get a higher level of formal education']:
        print("That's not quite right.  The data suggests there are a number of ways to become a developer that don't require one of the categories of degree labeled as 1.")
    if not sol['Regardless of formal education, online courses are the top suggested form of education']:
        print("That's not quite right.  Notice that online courses are the top way to break into the field for both audiences.")
    if not sol['Those with higher formal education suggest it more than those who do not have it']:
        print("Not quite.  Notice that those in the 1 category pushed earning a higher degree by approximately 2 times the other group.")
