import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv('./survey_results_public.csv')
schema = pd.read_csv('./survey_results_schema.csv')

##Categorical Variables
# Question 1
cat_df = df.select_dtypes(include=['object'])
cat_df.shape[1]
#Question 2
cat_df_dict = {'the number of columns with no missing values': 6,
               'the number of columns with more than half of the column missing': 49,
               'the number of columns with more than 75% of the column missing': 13
}
#Question 3
sol_3_dict = {'Which column should you create a dummy variable for?': 'col1',
              'When you use the default settings for creating dummy variables, how many are created?': 2,
              'What happens with the nan values?': 'the NaNs are always encoded as 0'
             }
#Question 4
#create needed dataframe
dummy_var_df = pd.DataFrame({'col1': ['a', 'a', 'b', 'b', 'a', np.nan, 'b', np.nan],
                             'col2': [1, np.nan, 3, np.nan, 5, 6, 7, 8]
})
#dummy cols
dummy_cols_df = pd.get_dummies(dummy_var_df['col1'], dummy_na=True)

#Question 5
cat_cols_lst = cat_df.columns
def create_dummy_df(df, cat_cols, dummy_na):
    for col in  cat_cols:
        try:
            # for each cat add dummy var, drop original column
            df = pd.concat([df.drop(col, axis=1), pd.get_dummies(df[col], prefix=col, prefix_sep='_', drop_first=True, dummy_na=dummy_na)], axis=1)
        except:
            continue
    return df
df_new = create_dummy_df(df, cat_cols_lst, dummy_na=False)
