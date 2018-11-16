import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv('./survey_results_public.csv')
schema = pd.read_csv('./survey_results_schema.csv')

## Your Turn
# Question 1
prop_sals = 1 - df.isnull()['Salary'].mean()
# Question 2
num_vars = df[['Salary', 'CareerSatisfaction', 'HoursPerWeek', 'JobSatisfaction', 'StackOverflowSatisfaction']]
sal_rm = num_vars.dropna(subset=['Salary'], axis=0)
# Question 3
question3_solution = 'It broke because we still have missing values in X'
# Question 4
all_rm = num_vars.dropna()
# Question 5
question5_solution = 'It worked, because Python is magic.'
# Question 6
r2_test = 0.019170661803761924
# Question 7
question7_solution = {'The number of reported salaries in the original dataset': 5009,
                       'The number of test salaries predicted using our model': 645,
                       'If an individual does not rate stackoverflow, but has a salary': 'We still want to predict their salary',
                       'If an individual does not have a a job satisfaction, but has a salary': 'We still want to predict their salary',
                       'Our model predicts salaries for the two individuals described above.': False}


