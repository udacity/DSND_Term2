import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv('./survey_results_public.csv')
schema = pd.read_csv('./survey_results_schema.csv')

## A Look at the Data
# Solution to Question 1
num_rows = df.shape[0]
num_cols = df.shape[1]

# Solution to Question 2
no_nulls = set(df.columns[df.isnull().mean()==0])

# Solution to Question 3
most_missing_cols = set(df.columns[df.isnull().mean() > 0.75])

## How To Break Into the Field
# Solution to Question 1
def get_description(schema, column_name):
    '''
    INPUT - schema - pandas dataframe with the schema of the developers survey
            column_name - string - the name of the column you would like to know about
    OUTPUT -
            desc - string - the description of the column
    '''
    desc = list(schema[schema['Column'] == column_name]['Question'])[0]
    return desc

descrips = set(get_description(schema, col) for col in df.columns)

# Solution to Question 4
higher_ed = lambda x: 1 if x in ("Master's degree", "Doctoral", "Professional degree") else 0

df['HigherEd'] = df["FormalEducation"].apply(higher_ed)
higher_ed_perc = df['HigherEd'].mean()


# Solution to Question 6
sol = {'Everyone should get a higher level of formal education': False,
       'Regardless of formal education, online courses are the top suggested form of education': True,
       'There is less than a 1% difference between suggestions of the two groups for all forms of education': False,
       'Those with higher formal education suggest it more than those who do not have it': True}

# What Happened?
# Question 1
desc_sol = {'A column just listing an index for each row': 'Respondent',
       'The maximum Satisfaction on the scales for the survey': 10,
       'The column with the most missing values': 'Salary',
       'The variable with the highest spread of values': 'Salary'}

# Question 2
scatter_sol = {'The column with the strongest correlation with Salary': 'CareerSatisfaction',
       'The data suggests more hours worked relates to higher salary': 'No',
       'Data in the ______ column meant missed data in two other columns': 'ExpectedSalary',
       'The strongest negative relationship had what correlation?': -0.12}

# Question 3
a = 'it is a way to assure your model extends well to new data'
b = 'it assures the same train and test split will occur for different users'
c = 'there is no correct match of this question'
d = 'sklearn fit methods cannot except NAN values'
e = 'it is just a convention people do that will likely go away soon'
f = 'python just breaks for no reason sometimes'

lm_fit_sol = {'What is the reason that the fit method broke?': d,
       'What does the random_state parameter do for the train_test_split function?': b,
       'What is the purpose of creating a train test split?': a}

## Job Satisfaction?
# Question 1
job_sol_1 = {'The proportion of missing values in the Job Satisfaction column': 0.214,
             'According to EmploymentStatus, which group has the highest average job satisfaction?': 'contractors',
             'In general, do smaller companies appear to have employees with higher job satisfaction?': 'yes'}

# Question 2
job_sol_2 = {'Do individuals who program outside of work appear to have higher JobSatisfaction?': 'yes',
             'Does flexibility to work outside of the office appear to have an influence on JobSatisfaction?': 'yes',
             'A friend says a Doctoral degree increases the chance of having job you like, does this seem true?': 'yes'}

## Removing Values

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
r2_test = 0.030994664959115625
# Question 7
question7_solution = {'The number of reported salaries in the original dataset': 12891,
                       'The number of salaries predicted using our model': 1602,
                       'If an individual does not rate stackoverflow, but has a salary': 'We still want to predict their salary',
                       'If an individual does not have a a job satisfaction, but has a salary': 'We still want to predict their salary',
                       'Our model predicts salaries for the two individuals described above.': False}


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
a = "Did not impute the mode."
b = "Imputes the mode."

impute_q4 = {'Filling column A': b,
             'Filling column D': a,
             'Filling column E': a}

##Imputing Values
#Question 1 Part 1
#Drop the rows with missing salaries
drop_sal_df = num_vars.dropna(subset=['Salary'], axis=0)
#Question 1 Part 2
# Mean function
fill_mean = lambda col: col.fillna(col.mean())
# Fill the mean
fill_df = drop_sal_df.apply(fill_mean, axis=0)

# Question 2
rsquared_score = 0.04072431792894726
length_y_test = 3868


##Categorical Variables
# Question 1
cat_df = df.select_dtypes(include=['object'])
cat_df.shape[1]
#Question 2
cat_df_dict = {'the number of columns with no missing values': 6,
               'the number of columns with more than half of the column missing': 50,
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

#Question 5
cat_cols_lst = cat_df.columns

def create_dummy_df(df, cat_cols, dummy_na):
    '''
    INPUT:
    df - pandas dataframe with categorical variables you want to dummy
    cat_cols - list of strings that are associated with names of the categorical columns
    dummy_na - Bool holding whether you want to dummy NA vals of categorical columns or not
    
    OUTPUT:
    df - a new dataframe that has the following characteristics:
            1. contains all columns that were not specified as categorical
            2. removes all the original columns in cat_cols
            3. dummy columns for each of the categorical columns in cat_cols
            4. if dummy_na is True - it also contains dummy columns for the NaN values
    '''
    for col in  cat_cols:
        try:
            # for each cat add dummy var, drop original column
            df = pd.concat([df.drop(col, axis=1), pd.get_dummies(df[col], prefix=col, prefix_sep='_', drop_first=True, dummy_na=dummy_na)], axis=1)
        except:
            continue
    return df

#Dropping where the salary has missing values
df  = df.dropna(subset=['Salary'], axis=0)

#Pull a list of the column names of the categorical variables
cat_df = df.select_dtypes(include=['object'])
cat_cols_lst = cat_df.columns

df_new = create_dummy_df(df, cat_cols_lst, dummy_na=False) 


#dummy cols
dummy_cols_df = pd.get_dummies(dummy_var_df['col1'], dummy_na=True)

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
