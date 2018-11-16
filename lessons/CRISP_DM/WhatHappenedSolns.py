import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv('./survey_results_public.csv')
schema = pd.read_csv('./survey_results_schema.csv')



# What Happened?
# Question 1
desc_sol = {'A column just listing an index for each row': 'Respondent',
       'The maximum Satisfaction on the scales for the survey': 10,
       'The column with the most missing values': 'ExpectedSalary',
       'The variable with the highest spread of values': 'Salary'}

# Question 2
scatter_sol = {'The column with the strongest correlation with Salary': 'CareerSatisfaction',
       'The data suggests more hours worked relates to higher salary': 'No',
       'Data in the ______ column meant missing data in three other columns': 'ExpectedSalary',
       'The strongest negative relationship had what correlation?': -0.15}

# Question 3
a = 'it is a way to assure your model extends well to new data'
b = 'it assures the same train and test split will occur for different users'
c = 'there is no correct match of this question'
d = 'sklearn fit methods cannot accept NAN values'
e = 'it is just a convention people do that will likely go away soon'
f = 'python just breaks for no reason sometimes'

lm_fit_sol = {'What is the reason that the fit method broke?': d,
       'What does the random_state parameter do for the train_test_split function?': b,
       'What is the purpose of creating a train test split?': a}