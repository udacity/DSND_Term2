import pandas as pd
import numpy as np
from collections import defaultdict
import RemovingDataSolns as s

# Question 1
def prop_sals_test(prop_sals):
    '''
    INPUT prop_sals - a float as the percent of missing values in the salary column

    Prints statement related to the correctness of the solution of the proportion
    '''
    if np.allclose(prop_sals, s.prop_sals):
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
    elif question7_solution['The number of reported salaries in the original dataset'] != s.question7_solution['The number of reported salaries in the original dataset']:
        print("The number of reported salaries in the original dataset doesn't look quite right.")
    elif question7_solution['The number of test salaries predicted using our model'] != s.question7_solution['The number of test salaries predicted using our model']:
        print("The number of salaries predicted using our model doesn't look quite right.")
    elif question7_solution['If an individual does not rate stackoverflow, but has a salary'] != s.question7_solution['If an individual does not rate stackoverflow, but has a salary']:
        print("Whether an individual rates stackoverflow or has a job satisfaction we would still like to predict the salary if we can.")
    elif question7_solution['If an individual does not have a a job satisfaction, but has a salary'] != s.question7_solution['If an individual does not have a a job satisfaction, but has a salary']:
        print("Whether an individual rates stackoverflow or has a job satisfaction we would still like to predict the salary if we can.")
    elif question7_solution['Our model predicts salaries for the two individuals described above.'] != s.question7_solution['Our model predicts salaries for the two individuals described above.']:
        print("Unfortunately, our current model will not predict for anyone who has missing values in any column - even if they do have a salary!")




















