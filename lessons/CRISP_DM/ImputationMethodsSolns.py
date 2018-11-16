import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv('./survey_results_public.csv')
schema = pd.read_csv('./survey_results_schema.csv')

### Imputation Methods
#Question 1
question1_solution = {'Column A is': 'quantitative',
                      'Column B is': 'quantitative',
                      'Column C is': 'we cannot tell',
                      'Column D is': 'boolean - can treat either way',
                      'Column E is': 'categorical',
                     }

#Question 2
should_we_drop = 'Yes'

#Question 3
impute_q3 = {'Filling column A': "is no problem - it fills the NaN values with the mean as expected.",
             'Filling column D': "fills with the mean, but that doesn't actually make sense in this case.",
             'Filling column E': "gives an error."}

#Question 4
impute_q4 = {'Filling column A': "Did not impute the mode.",
             'Filling column D': "Did not impute the mode.",
             'Filling column E': "Imputes the mode."}