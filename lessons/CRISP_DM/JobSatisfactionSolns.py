import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv('./survey_results_public.csv')
schema = pd.read_csv('./survey_results_schema.csv')

## Job Satisfaction?
# Question 1
job_sol_1 = {'The proportion of missing values in the Job Satisfaction column': 0.2014,
             'According to EmploymentStatus, which group has the highest average job satisfaction?': 'contractors',
             'In general, do smaller companies appear to have employees with higher job satisfaction?': 'yes'}

# Question 2
job_sol_2 = {'Do individuals who program outside of work appear to have higher JobSatisfaction?': 'yes',
             'Does flexibility to work outside of the office appear to have an influence on JobSatisfaction?': 'yes', 
             'A friend says a Doctoral degree increases the chance of having job you like, does this seem true?': 'yes'}

