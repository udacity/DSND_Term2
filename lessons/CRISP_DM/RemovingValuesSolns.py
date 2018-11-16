import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv('./survey_results_public.csv')
schema = pd.read_csv('./survey_results_schema.csv')


# Removing Values

small_dataset = pd.DataFrame({'col1': [1, 2, np.nan, np.nan, 5, 6],
                             'col2': [7, 8, np.nan, 10, 11, 12],
                             'col3': [np.nan, 14, np.nan, 16, 17, 18]})
# Question 1
all_drop  = small_dataset.dropna()


# Question 2
all_row = small_dataset.dropna(axis=0, how='all')

# Question 3
only3_drop = small_dataset.dropna(subset=['col3'], how='any')

# Question 4
only3or1_drop = small_dataset.dropna(subset=['col1', 'col3'], how='any')