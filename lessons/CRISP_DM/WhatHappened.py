import pandas as pd
import numpy as np
from collections import defaultdict
import WhatHappenedSolns as s

## What Happened?
# Question 1
def describe_check(desc_sol):
    '''
    INPUT desc_sol - a dictionary with descriptions as keys, and letters as values that correspond to the correct columns and numbers associated with each description

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if desc_sol == s.desc_sol:
        print("Nice job that looks right!")
    if desc_sol['A column just listing an index for each row'] != s.desc_sol['A column just listing an index for each row']:
        print("Oops! Are you sure that is the column that is just keeping track of the index for each row?")
    if desc_sol['The column with the most missing values'] != s.desc_sol['The column with the most missing values']:
        print("That doesn't look like the column with the most missing values.  You can have a column appear in the dictionary more than once.")
    if desc_sol['The maximum Satisfaction on the scales for the survey'] != s.desc_sol['The maximum Satisfaction on the scales for the survey']:
        print("Oops! That doesn't look quite right. Are you sure that is the max value associated with the Satisfaction scales for the survey?")
    if desc_sol['The variable with the highest spread of values'] != s.desc_sol['The variable with the highest spread of values']:
        print("That doesn't look like the column with the largest spread.  You can have a column appear in the dictionary more than once.")


#Question 2
def scatter_check(scatter_sol):
    '''
    INPUT scatter_sol - a dictionary with descriptions as keys, and letters as values that correspond to the correct columns and numbers associated with each description

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if scatter_sol == s.scatter_sol:
        print("Nice job that looks right!")
    if scatter_sol['The column with the strongest correlation with Salary'] != s.scatter_sol['The column with the strongest correlation with Salary']:
        print("Oops! No, that is not the column with the strongest correlation with salary.")

    if scatter_sol['The data suggests more hours worked relates to higher salary'] != s.scatter_sol['The data suggests more hours worked relates to higher salary']:
        print("Oops! Actually, the more you work is actually correlated with lower salary values.")

    if scatter_sol['Data in the ______ column meant missing data in three other columns'] != s.scatter_sol['Data in the ______ column meant missing data in three other columns']:
        print("Oops! Actually, which column has two other columns with missing data when it is filled - your answer doesn't look like what I was expecting.")

    if scatter_sol['The strongest negative relationship had what correlation?'] != s.scatter_sol['The strongest negative relationship had what correlation?']:
        print("Oops! The strongest negative correlation is actually between HoursPerWeek and Salary.")


#Question 3
def lm_fit_check(lm_fit_sol):
    '''
    INPUT scatter_sol - a dictionary with descriptions as keys, and letters as values that correspond to the correct columns and numbers associated with each description

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if lm_fit_sol == s.lm_fit_sol:
        print("Nice job that looks right!")
    else:
        print("Oops! Your solution should use only the first three statements here (a,b, and d).  Try again.")


