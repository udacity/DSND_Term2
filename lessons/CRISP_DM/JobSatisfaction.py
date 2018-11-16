import pandas as pd
import numpy as np
from collections import defaultdict
import JobSatisfactionSolns as s

## Job Satisfaction?
# Question 1
def jobsat_check1(job_sol_1):
    '''
    INPUT job_sol_1 - a dictionary with descriptions as keys, and letters as values that correspond to the correct columns and numbers associated with each description

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if job_sol_1 == s.job_sol_1:
        print("Nice job! That's what we found as well!")
    elif job_sol_1['The proportion of missing values in the Job Satisfaction column'] != s.job_sol_1['The proportion of missing values in the Job Satisfaction column']:
        print("Oops! That first proportion doesn't look like what I was expecting.")
    elif job_sol_1['According to EmploymentStatus, which group has the highest average job satisfaction?'] != s.job_sol_1['According to EmploymentStatus, which group has the highest average job satisfaction?']:
        print("Oops! Though it wasn't what I was expecting either, the job category with the highest job satisfaction was not fulltime nor retired individuals!")
    elif job_sol_1['In general, do smaller companies appear to have employees with higher job satisfaction?'] != s.job_sol_1['In general, do smaller companies appear to have employees with higher job satisfaction?']:
        print("Looking at the average job satisfaction for each group within CompanySize, and sorting using sort_values(), there is a bit of trend don't you think?  Maybe not significant, but still an intriguing trend!")

def jobsat_check2(job_sol_2):
    '''
    INPUT job_sol_2 - a dictionary with descriptions as keys, and letters as values that correspond to the correct columns and numbers associated with each description

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if job_sol_2 == s.job_sol_2:
        print("Nice job! That's what we found as well!")
    else:
        print("Are you sure at least one more of these wasn't true?  I thought a quick look suggested evidence for all, but maybe you found some evidence suggesting otherwise.  I did not do anymore than quick descriptive statistics to view the results. Certainly there could be confounding factors, and there is no evidence of statistically significant differences based on my solutions.")
