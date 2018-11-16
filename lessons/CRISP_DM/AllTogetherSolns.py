import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv('./survey_results_public.csv')
schema = pd.read_csv('./survey_results_schema.csv')




## Putting It All Together
#Question 2
q2_piat = {'add interactions, quadratics, cubics, and other higher order terms': 'no',
           'fit the model many times with different rows, then average the responses': 'yes',
           'subset the features used for fitting the model each time': 'yes',
           'this model is hopeless, we should start over': 'no'}
#Question 4
q4_piat = {'The optimal number of features based on the results is': 1088,
               'The model we should implement in practice has a train rsquared of': 0.80,
               'The model we should implement in practice has a test rsquared of': 0.73,
               'If we were to allow the number of features to continue to increase':
'we would likely have a better rsquared for the training data.'}

#Question 5
q5_piat = {'Country appears to be one of the top indicators for salary': True,
               'Gender appears to be one of the indicators for salary': False,
               'How long an individual has been programming appears to be one of the top indicators for salary': True,
               'The longer an individual has been programming the more they are likely to earn': False}


