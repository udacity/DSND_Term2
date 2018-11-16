import pandas as pd
import numpy as np
from collections import defaultdict
import solution1 as s
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

## A Look at the Data
# Question 1
def check_rows_cols(num_rows, num_cols):
    '''
    INPUT:
    num_rows - int the number of rows in df
    num_cols - int the number of cols in df

    This function will print a statement related to whether or not you provided the correct number of rows and columns of the dataset.
    '''
    if num_rows == s.num_rows:
        print("Nice job there are {} rows in the dataset!".format(num_rows))
    else:
        print("That doesn't look like what we were expecting for the number of rows.")

    if num_cols == s.num_cols:
        print("Nice job there are {} columns in the dataset!".format(num_cols))
    else:
        print("That doesn't look like what we were expecting for the number of columns.")

# Question 2
def no_null_cols(no_nulls):
    '''
    INPUT:
    no_nulls - a set of columns with no missing values

    This function will print a statement related to whether or not you provided the correct set of columns with no missing values
    '''
    if no_nulls == s.no_nulls:
        print("Nice job that looks right!")
    else:
        print("That doesn't look like for the set of no nulls.  There should be {} columns in your list".format(len(s.no_nulls)))

# Question 3
def most_missing_cols(most_missing_cols):
    '''
    INPUT:
    most_missing_cols - a set of columns with more than 75% of the values in the column missing

    This function will print a statement related to whether or not you provided the correct set of columns with more than 75% of the values in the column missing
    '''
    if most_missing_cols == s.most_missing_cols:
        print("Nice job that looks right!")
    else:
        print("That doesn't look like for the set of most nulls.  There should be {} columns in your list".format(len(s.most_missing_cols)))


## How To Break Into the Field
# Question 1
def check_description(descrips):
    '''
    INPUT:
    descrips - should be a set of all descriptions in the dataset - each description should be a string.  You should not need to change the descrips variable at all if your function works correctly.

    This function will print a statement related to whether or not you provided the correct solution for the get_description function
    '''
    val_type = type(next(iter(descrips)))
    if descrips == s.descrips:
        print("Nice job it looks like your function works correctly!")
    elif val_type != str:
        print("Oops - Looks like your column descriptions aren't strings.")
    else:
        print("Though you did provide the correct data type, your result does not match what we were expecting.  Try again.\n\n  Your function should return the description for any column name passed to it.")


#Question 3
def total_count(df, col1, col2, look_for):
    '''
    INPUT:
    df - the pandas dataframe you want to search
    col1 - the column name you want to look through
    col2 - the column you want to count values from
    look_for - a list of strings you want to search for in each row of df[col]

    OUTPUT:
    new_df - a dataframe of each look_for with the count of how often it shows up
    '''
    new_df = defaultdict(int)
    #loop through list of ed types
    for val in look_for:
        #loop through rows
        for idx in range(df.shape[0]):
            #if the ed type is in the row, add the devs
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])
    #clean up the resulting dataframe8
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df

def mean_amt(df, col_name, col_mean, look_for):
    '''
    INPUT:
    df - the pandas dataframe you want to search
    col_name - the column name you want to look through
    col_count - the column you want to count values from
    col_mean - the column you want the mean amount for
    look_for - a list of strings you want to search for in each row of df[col]

    OUTPUT:
    df_all - holds sum, square, total, mean, variance, and standard deviation for the col_mean
    '''
    new_df = defaultdict(int)
    squares_df = defaultdict(int)
    denoms = dict()
    for val in look_for:
        denoms[val] = 0
        for idx in range(df.shape[0]):
            if df[col_name].isnull()[idx] == False:
                if val in df[col_name][idx] and df[col_mean][idx] > 0:
                    new_df[val] += df[col_mean][idx]
                    squares_df[val] += df[col_mean][idx]**2 #Needed to understand the spread
                    denoms[val] += 1

    # Turn into dataframes
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    squares_df = pd.DataFrame(pd.Series(squares_df)).reset_index()
    denoms = pd.DataFrame(pd.Series(denoms)).reset_index()

    # Change the column names
    new_df.columns = [col_name, 'col_sum']
    squares_df.columns = [col_name, 'col_squares']
    denoms.columns = [col_name, 'col_total']

    # Merge dataframes
    df_means = pd.merge(new_df, denoms)
    df_all = pd.merge(df_means, squares_df)

    # Additional columns needed for analysis
    df_all['mean_col'] = df_means['col_sum']/df_means['col_total']
    df_all['var_col'] = df_all['col_squares']/df_all['col_total'] - df_all['mean_col']**2
    df_all['std_col'] = np.sqrt(df_all['var_col'])
    df_all['lower_95'] = df_all['mean_col'] - 1.96*df_all['std_col']/np.sqrt(df_all['col_total'])
    df_all['upper_95'] = df_all['mean_col'] + 1.96*df_all['std_col']/np.sqrt(df_all['col_total'])
    return df_all


#Question 4
def higher_ed_test(higher_ed_perc):
    '''
    INPUT:
    higher_ed_perc - a float of the percentage of individuals who received a master's, phd, or professional degree in the stackoverflow dataframe

    This function will print a statement related to whether or not you provided the correct percentage of individuals who received a master's, phd, or professional degree in the stackoverflow dataframe
    '''
    val_type = type(higher_ed_perc)
    if higher_ed_perc == s.higher_ed_perc:
        print("Nice job!  That's right.  The percentage of individuals in these three groups is {}.".format(higher_ed_perc))
    elif val_type != float:
        print("Oops - your final result should be a decimal value associated with the proportion of individuals who are in these three categories (ex. Provide 0.50798 if ~50% of individuals are in these categories)")
    else:
        print("That doesn't look quite like expected.  You can get the percentage of 1's in a 1-0 column by using the .mean() method of a pandas series.")

#Question 6
def conclusions(sol):
    '''
    INPUT:
    sol - a dictionary with keys as strings of statements and values as True or False as to the truth of the string according to the data.

    This function will print a statement related to whether or not you provided the correct in terms of the True or False statement
    '''
    if sol == s.sol:
        print("Nice job that looks right!")
    if sol['There is less than a 1% difference between suggestions of the two groups for all forms of education']:
        print("That's not quite right.  Almost all are less than a 1% difference.  However, there is almost a 3% difference in those that ")
    if sol['Everyone should get a higher level of formal education']:
        print("That's not quite right.  The data suggests there are a number of ways to become a developer that don't require one of the categories of degree labeled as 1.")
    if not sol['Regardless of formal education, online courses are the top suggested form of education']:
        print("That's not quite right.  Notice that online courses are the top way to break into the field for both audiences.")
    if not sol['Those with higher formal education suggest it more than those who do not have it']:
        print("Not quite.  Notice that those in the 1 category pushed earning a higher degree by approximately 2 times the other group.")


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

    if scatter_sol['Data in the ______ column meant missed data in two other columns'] != s.scatter_sol['Data in the ______ column meant missed data in two other columns']:
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


## Removing Values
# Question 1
def all_drop_test(all_drop):
    '''
    INPUT all_drop - a pandas dataframe with all rows with missing values dropped.

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if all_drop.equals(s.all_drop):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, or take a look at the solution notebook if you get stuck.")


# Question 2
def all_row_test(all_row):
    '''
    INPUT all_row - a pandas dataframe with all rows that have every value as a missing value dropped.

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if all_row.equals(s.all_row):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, or take a look at the solution notebook if you get stuck.")

# Question 3
def only3_drop_test(only3_drop):
    '''
    INPUT all_row - a pandas dataframe with all rows that are missing a value in col3

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if only3_drop.equals(s.only3_drop):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, or take a look at the solution notebook if you get stuck.")

# Question 4
def only3or1_drop_test(only3or1_drop):
    '''
    INPUT all_row - a pandas dataframe with all rows that are missing a value in col1 or col3

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if only3or1_drop.equals(s.only3or1_drop):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, or take a look at the solution notebook if you get stuck.")

### Your Turn
# Question 1
def prop_sals_test(prop_sals):
    '''
    INPUT prop_sals - a float as the percent of missing values in the salary column

    Prints statement related to the correctness of the solution of the proportion
    '''
    if prop_sals == s.prop_sals:
        print("Nice job! That looks right!")
    else:
        print("Oops!  Make sure your value is for the proportion of nan values in only the Salary column.")


# Question 2
def sal_rm_test(sal_rm):
    '''
    INPUT sal_rm - a pandas dataframe with all rows that are missing a value the salary column removed.  The dataframe should only have the columns of num_vars (quant variables)

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if sal_rm.equals(s.sal_rm):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, this should be the num_vars dataframe with salary removed.")

# Question 3
def question3_check(question3_solution):
    '''
    INPUT question3_solution - the letter (a, b, or c) corresponding to the statement that best describes what happend when fitting your model.

    Prints statement related to the correctness of the letter chosen.
    '''
    if question3_solution == s.question3_solution:
        print("Nice job! That's right! Those missing values in the X matrix will still not allow us to predict the response.")
    else:
        print("Oops!  That wasn't what we were expecting.  Your solution should be either a, b, or c for the string that best relates to what happened.")


# Question 4
def all_rm_test(all_rm):
    '''
    INPUT all_rm - a pandas dataframe with all rows that are missing a value in any column removed from num_vars (only the numeric columns)

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if all_rm.equals(s.all_rm):
        print("Nice job! That looks right.  The default is to drop any row with a missing value in any column, so we didn't need to specify any arguments in this case.")
    else:
        print("Oops!  That doesn't look like what we were expecting.  Make sure you are working with only the numeric columns, and you have dropped any rows with missing values.")

# Question 5
def question5_check(question5_solution):
    '''
    INPUT question3_solution - the letter (a, b, or c) corresponding to the statement that best describes what happend when fitting your model.

    Prints statement related to the correctness of the letter chosen.
    '''
    if question5_solution == s.question5_solution:
        print("Nice job! That's right! Python isn't exactly magic, but sometimes it feels like it is!")
    else:
        print("Oops!  Your solution should have worked.  In which case, no output should have printed.  This solution should follow just as in the screencast.")

# Question 6
def r2_test_check(r2_test):
    '''
    INPUT r2_test - the rsquared value from fitting a model with all nan values dropped and only using quantitative variables.

    Prints statement related to the correctness rsquared matching solution.
    '''
    if r2_test == s.r2_test:
        print("Nice job! That's right! Your rsquared matches the solution.")
    else:
        print("Oops!  That wasn't the value that was expected.  You should fit your model using the training data, predict on the X_test data, and then score comparing the y_test and your predicted values.")

# Question 7
def question7_check(question7_solution):
    '''
    INPUT question7_solution - a dictionary with statements of takeaways from the rest of the notebook.  The values should be the variables a, b, c, d, e, f, or g

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if question7_solution == s.question7_solution:
        print("Nice job! That looks right to me!  We would really like to predict for anyone who provides a salary, but our model right now definitely has some limitations.")
    elif question7_solution['The number of reported salaries in the original dataset'] == s.question7_solution['The number of reported salaries in the original dataset']:
        print("The number of reported salaries in the original dataset doesn't look quite right.")
    elif question7_solution['The number of salaries predicted using our model'] == s.question7_solution['The number of salaries predicted using our model']:
        print("The number of salaries predicted using our model doesn't look quite right.")
    elif question7_solution['If an individual does not rate stackoverflow, but has a salary'] == s.question7_solution['If an individual does not rate stackoverflow, but has a salary']:
        print("Whether an individual rates stackoverflow or has a job satisfaction we would still like to predict the salary if we can.")
    elif question7_solution['If an individual does not have a a job satisfaction, but has a salary'] == s.question7_solution['If an individual does not have a a job satisfaction, but has a salary']:
        print("Whether an individual rates stackoverflow or has a job satisfaction we would still like to predict the salary if we can.")
    elif question7_solution['Our model predicts salaries for the two individuals described above.'] == s.question7_solution['Our model predicts salaries for the two individuals described above.']:
        print("Unfortunately, our current model will not predict for anyone who has missing values in any column - even if they do have a salary!")


##Imputation Methods
# Question 1
def var_test(question1_solution):
    '''
    INPUT question1_solution - a dictionary with solutions regarding variable types.  The values should be the variables a, b, c, d

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if question1_solution == s.question1_solution:
        print('Nice job! That looks right to me!')
    else:
        print('Oops! Two of these should be quantitative.  One we cannot know for sure. One is a category. One is a boolean.')

# Question 2
def can_we_drop(should_we_drop):
    '''
    INPUT should_we_drop - A variable either a or b as to whether or not we should drop any of the columns above.

    Prints statement related to the correctness of the solution
    '''
    if should_we_drop == s.should_we_drop:
        print("That's right! You should feel comfortable dropping any rows or columns that are completely missing values (or if they are all the exact same value).  However, dropping other columns or rows, even if only containing a few values, should go through further consideration.")
    else:
        print("Actually, you should feel comfortable dropping any rows or columns that are completely missing values.")


# Question 3
def impute_q3_check(impute_q3):
    '''
    INPUT impute_q3 - a dictionary with solutions regarding variable types.  The values should be the variables a, b, c

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if impute_q3 == s.impute_q3:
        print("Nice job! That's right only the first column fills with the mean correctly.  We can't fill the mean of a categorical variable, and the boolean treats the True as 1 and False as 0 to give values that are not 1 or 0.")
    else:
        print('Oops! The first column looks okay, but are you sure the mean of True and False values makes sense?  Should the NaN values be True of False?  The last column is a string - what is the mean for that column?')

# Question 4
def impute_q4_check(impute_q4):
    '''
    INPUT impute_q4 - a dictionary with solutions regarding variable types.  The values should be the variables a, b

    Prints statement related to the correctness of the solution of the dictionary
    '''
    a = "Did not impute the mode."
    b = "Imputes the mode."


    impute_q4_1 = {'Filling column A': b,
                 'Filling column D': a,
                 'Filling column E': a}
    
    if impute_q4 == impute_q4_1:
        print("Nice job! That's right only one of these columns actually imputed a mode.  None of the values in the first column appeared more than once, and 0 was imputed for all of the NaN values.  There were an even number of True and False values, and False was imputed for all the NaN values.")
    else:
        print("Oops! Only one of these columns actually imputed a mode.  What happened with the columns that had no mode?")

## Imputing Values
# Question 1 Part 1
def check_sal_dropped(drop_sal_df):
    '''
    INPUT drop_sal_df - a pandas dataframe with all rows that are missing a value the salary column removed.  The dataframe should only have the columns of num_vars (quant variables)

    Prints statement related to the correctness of the solution of the dataframe
    '''
    if drop_sal_df.equals(s.drop_sal_df):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, this should be the num_vars dataframe with salary removed.")


# Question 1 Part 2
def check_fill_df(fill_df):
    '''
    INPUT
    fill_df - a pandas dataframe with the mean imputed for all the missing numeric columns of drop_sal_df

    Prints statement related to the correctness of the solution of the dataframe.
    '''
    if fill_df.equals(s.fill_df):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try again, this should be the num_vars dataframe with salary removed.  Then you should fill all the numeric columns with the mean for each column.")


# Question 2
def r2_y_test_check(rsquared_score, length_y_test):
    '''
    INPUT
    rsquared_score - float

    length_y_test - int

    Prints statement related to the correctness of the rsquared_score and length_y_test
    '''
    if rsquared_score == s.rsquared_score and length_y_test == s.length_y_test:
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Try the steps again, and feel free to use the steps at the top of this notebook to help you out if you get stuck.")


## Categorical Variables
# Question 1
def cat_df_check(cat_df):
    '''
    INPUT
    cat_df - a pandas dataframe of only the categorical columns of df

    Prints statement related to the correctness of the dataframe provided.
    '''
    if cat_df.equals(s.cat_df):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  The input cat_df variable should be a dataframe of all of the categorical variables.  You can use select_dtypes to select the 'object' data type.")

#Question 2
def cat_df_dict_check(cat_df_dict):
    '''
    INPUT cat_df_dict - a dictionary with numbers for each value corresponding the the number described by each key.

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if cat_df_dict == s.cat_df_dict:
        print('Nice job! That looks right to me!')
    else:
        print("Oops! One or more of those doesn't look quite right.  Each value should be an integer corresponding to the number of columns described.")

#Question 3
def sol_3_dict_check(sol_3_dict):
    '''
    INPUT sol_3_dict - a dictionary with variables for each value corresponding the the key that describes it.

    Prints statement related to the correctness of the solution of the dictionary
    '''
    if sol_3_dict == s.sol_3_dict:
        print('Nice job! That looks right to me!')
    elif sol_3_dict['Which column should you create a dummy variable for?'] != s.sol_3_dict['Which column should you create a dummy variable for?']:
        print("Oops! That is not the column you should be using to create a dummy variable. Try again.")
    elif sol_3_dict['How many new dummy columns do you get when creating dummy variables?'] != s.sol_3_dict['How many new dummy columns do you get when creating dummy variables?']:
        print("Oops! Though you could get that number of dummy variables, that is not what you get using the default setting using one hot encoding or pandas `get_dummies` encoding. Try again.")
    elif sol_3_dict['What happens with the nan values?'] != s.sol_3_dict['What happens with the nan values?']:
        print("Oops! Though that could happen with the NaN values, that is not the default when working with pandas.")

#Question 4
def dummy_cols_df_check(dummy_cols_df):
    '''
    INPUT
    dummy_cols_df - a pandas dataframe of the dummy variables associated with the levels as well as the missing values.

    Prints statement related to the correctness of the dataframe provided.
    '''
    if dummy_cols_df.equals(s.dummy_cols_df):
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Your input should just be the 3 columns resulting as dummy variables.  One column for a, one for b, and one for the nan values.")

#Question 5
def create_dummy_df_check(df_new):
    '''
    INPUT
    df_new - a pandas dataframe returned by create_dummy_df(df, cat_cols_lst, dummy_na=False)

    It should contain these four characteristics
        1. contains all columns that were not specified as categorical
        2. removes all the original columns in cat_cols
        3. dummy columns for each of the categorical columns in cat_cols
        4. if dummy_na is True - it also contains dummy columns for the NaN values
        5. Use a prefix of the column name with an underscore (_) for separating 


    Prints statement related to the correctness of the dataframe provided.
    '''
    if set(df_new.columns).difference(s.df_new.columns) == set():
        print("Nice job! This passes the simple tests I built!  It is a good idea to do a spot check yourself as well.")
    else:
        print("Looks like there is a difference due to these columns not matching: {}".format(set(df_new.columns).difference(s.df_new.columns)))
        print("That wasn't quite as expected.  Make sure your dataframe has these 4 characteristics:   1. contains all columns that were not specified as categorical 2. removes all the original columns in cat_cols 3. dummy columns for each of the categorical columns in cat_cols 4. if dummy_na is True - it also contains dummy columns for the NaN values 5. Use a prefix of the column name with an underscore (_) for separating ")

#Question 6
def train_test_scores_check(test_score, train_score):
    '''
    INPUT
    test_score - float - r2 score on the test data
    train_score - float - r2 score on the test data

    Prints statement related to the correctness of the rsquared_score and length_y_test
    '''
    if test_score == s.test_score and train_score == s.train_score:
        print("Nice job! That looks right!")
    else:
        print("That wasn't quite as expected.  Assure you followed the steps in the document string.  The very beginning of this notebook may also be useful to assist in completing this part!")

## Putting It All Together
#Helper functions
def clean_fit_linear_mod(df, response_col, test_size=.3, rand_state=42):
    '''
    INPUT:
    df - a dataframe holding all the variables of interest
    response_col - a string holding the name of the column
    test_size - a float between [0,1] about what proportion of data should be in the test dataset
    rand_state - an int that is provided as the random state for splitting the data into training and test

    OUTPUT:
    X - cleaned X matrix (dummy and mean imputation)
    y - cleaned response (just dropped na)
    test_score - float - r2 score on the test data
    train_score - float - r2 score on the test data
    lm_model - model object from sklearn
    X_train, X_test, y_train, y_test - output from sklearn train test split used for optimal model

    This function cleans the data and provides the necessary output for the rest of this notebook.
    '''
    #Dropping where the salary has missing values
    df  = df.dropna(subset=['Salary'], axis=0)

    #Drop columns with all NaN values
    df = df.dropna(how='all', axis=1)

    #Pull a list of the column names of the categorical variables
    cat_df = df.select_dtypes(include=['object'])
    cat_cols = cat_df.columns

    #dummy all the cat_cols
    for col in  cat_cols:
        df = pd.concat([df.drop(col, axis=1), pd.get_dummies(df[col], prefix=col, prefix_sep='_', drop_first=True, dummy_na=True)], axis=1)


    # Mean function
    fill_mean = lambda col: col.fillna(col.mean())
    # Fill the mean
    df = df.apply(fill_mean, axis=0)

    #Split into explanatory and response variables
    X = df.drop(response_col, axis=1)
    y = df[response_col]

    #Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=rand_state)

    lm_model = LinearRegression(normalize=True) # Instantiate
    lm_model.fit(X_train, y_train) #Fit

    #Predict using your model
    y_test_preds = lm_model.predict(X_test)
    y_train_preds = lm_model.predict(X_train)

    #Score using your model
    test_score = r2_score(y_test, y_test_preds)
    train_score = r2_score(y_train, y_train_preds)

    return X, y, test_score, train_score, lm_model, X_train, X_test, y_train, y_test


def find_optimal_lm_mod(X, y, cutoffs, test_size = .30, random_state=42, plot=True):
    '''
    INPUT
    X - pandas dataframe, X matrix
    y - pandas dataframe, response variable
    cutoffs - list of ints, cutoff for number of non-zero values in dummy categorical vars
    test_size - float between 0 and 1, default 0.3, determines the proportion of data as test data
    random_state - int, default 42, controls random state for train_test_split
    plot - boolean, default 0.3, True to plot result

    OUTPUT
    r2_scores_test - list of floats of r2 scores on the test data
    r2_scores_train - list of floats of r2 scores on the train data
    lm_model - model object from sklearn
    X_train, X_test, y_train, y_test - output from sklearn train test split used for optimal model
    '''
    r2_scores_test, r2_scores_train, num_feats, results = [], [], [], dict()
    for cutoff in cutoffs:

        #reduce X matrix
        reduce_X = X.iloc[:, np.where((X.sum() > cutoff) == True)[0]]
        num_feats.append(reduce_X.shape[1])

        #split the data into train and test
        X_train, X_test, y_train, y_test = train_test_split(reduce_X, y, test_size = test_size, random_state=random_state)

        #fit the model and obtain pred response
        lm_model = LinearRegression(normalize=True)
        lm_model.fit(X_train, y_train)
        y_test_preds = lm_model.predict(X_test)
        y_train_preds = lm_model.predict(X_train)

        #append the r2 value from the test set
        r2_scores_test.append(r2_score(y_test, y_test_preds))
        r2_scores_train.append(r2_score(y_train, y_train_preds))
        results[str(cutoff)] = r2_score(y_test, y_test_preds)

    if plot:
        plt.plot(num_feats, r2_scores_test, label="Test", alpha=.5)
        plt.plot(num_feats, r2_scores_train, label="Train", alpha=.5)
        plt.xlabel('Number of Features')
        plt.ylabel('Rsquared')
        plt.title('Rsquared by Number of Features')
        plt.legend(loc=1)
        plt.show()

    best_cutoff = max(results, key=results.get)

    #reduce X matrix
    reduce_X = X.iloc[:, np.where((X.sum() > int(best_cutoff)) == True)[0]]
    num_feats.append(reduce_X.shape[1])

    #split the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(reduce_X, y, test_size = test_size, random_state=random_state)

    #fit the model
    lm_model = LinearRegression(normalize=True)
    lm_model.fit(X_train, y_train)

    return r2_scores_test, r2_scores_train, lm_model, X_train, X_test, y_train, y_test

#Question 1
def q1_piat_answer():
    '''
    Prints the correct order of the letters in the format portion of the string
    '''
    print("This one is tricky - here is the order of the letters for the solution we had in mind:\n c, g, c, d, c, e, f, b, a, h")

#Question 2
def q2_piat_check(q2_piat):
    '''
    INPUT
    q2_piat - a dictionary

    Prints statement related to the correctness of q2_piat
    '''
    if q2_piat == s.q2_piat:
        print("Nice job! That looks right!  These two techniques are really common in Machine Learning algorithms to combat overfitting.  Though the first technique could be useful, it is not likely to help us right away with our current model.  These additional features would likely continue to worsen the nature of overfitting we are seeing here.")
    elif q2_piat['add interactions, quadratics, cubics, and other higher order terms'] != s.q2_piat['add interactions, quadratics, cubics, and other higher order terms']:
        print("In this case, it is not likely that having more complex features will help us.  The model is already forming too complex of a relationship to generalize to new data.")
    elif q2_piat['fit the model many times with different rows, then average the responses'] != s.q2_piat['fit the model many times with different rows, then average the responses']:
        print("Fitting the model on different rows and ctually a common technique for combatting overfitting.  It relates to an idea known as bootstrapping.")
    elif q2_piat['subset the features used for fitting the model each time'] != s.q2_piat['subset the features used for fitting the model each time']:
        print("Subsetting the features is actually a common way to combat overfitting.  This type of feature reduction is done in stochastic gradient methods related to gradient boosting and random forest methods.")
    elif q2_piat['this model is hopeless, we should start over'] != s.q2_piat['this model is hopeless, we should start over']:
        print("Don't give up hope!  We are just getting started!")

#Question 4
def q4_piat_check(q4_piat):
    '''
    INPUT
    q4_piat - a dictionary

    Prints statement related to the correctness of q4_piat
    '''
    if q4_piat == s.q4_piat:
        print("Nice job! That looks right!  We can see that the model we should impement was the 6th model using 1088 features.  It is the model that has the best test rsquared value.")
    elif q4_piat['The optimal number of features based on the results is'] != s.q4_piat['The optimal number of features based on the results is']:
        print("Oops!  That isn't right for the optimal number of features.  You can get this as the number of columns in either the training or testing datasets.  Note, this is different than the inputs, as they are checking the threshold for the number of missing values in a column, not a threshold for the number of features.")
    elif q4_piat['The model we should implement in practice has a train rsquared of'] != s.q4_piat['The model we should implement in practice has a train rsquared of'] or q4_piat['The model we should implement in practice has a test rsquared of'] != s.q4_piat['The model we should implement in practice has a test rsquared of']:
        print("The rsquared values don't look right.  The optimal model should be the model that performed the best on the test data.  The rsquared values should be the rsquared for the training and test sets of data using the same, best model based on the test data.")
    elif q4_piat['If we were to allow the number of features to continue to increase'] != s.q4_piat['If we were to allow the number of features to continue to increase']:
        print("If you were to allow the number of features to increase, you likely would see the same trend you can see in the visual.  That is the test data will continue to provide worse and worse rsquared values, while the training data would go towards 1.")

#Question 5
def q5_piat_check(q5_piat):
    '''
    INPUT
    q5_piat - a dictionary

    Prints statement related to the correctness of q5_piat
    '''
    if q5_piat == s.q5_piat:
        print("Nice job! That looks right! The country and years of experience both seem to have a significant impact on the salary of individuals.")
    else:
        print("Oops!  It appears that country and years of experience are indicators of salary values.  However, gender columns did not appear in the top 20 features.  Additionally, the years of programming didn't follow an always increasing order.  Therefore, it wasn't necessarily the case that longer you have programmed leads to higher salary based on the data.")





if __name__ == '__main__':
    df = pd.read_csv('../stackoverflow/survey_results_public.csv')
    schema = pd.read_csv('../stackoverflow/survey_results_schema.csv')

    num_rows = df.shape[0]
    num_cols = df.shape[1]
    check_rows_cols(num_rows, num_cols)

    df_all = mean_amt(df, 'CousinEducation', 'Salary', possible_vals)

    # To get a simple answer to our questions - see these two tables.
    df_all.sort_values('mean_col', ascending=False)
