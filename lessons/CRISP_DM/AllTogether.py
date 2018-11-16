import pandas as pd
import numpy as np
from collections import defaultdict
import AllTogetherSolns as s
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

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
    a = 'we would likely have a better rsquared for the test data.'
    b = 1000
    c = 872
    d = 0.69
    e = 0.82
    f = 0.88
    g = 0.72
    h = 'we would likely have a better rsquared for the training data.'

    q4_piat_1 = {'The optimal number of features based on the results is': c, 
                   'The model we should implement in practice has a train rsquared of': e, 
                   'The model we should implement in practice has a test rsquared of': d,
                   'If we were to allow the number of features to continue to increase': h
    }

    if q4_piat == q4_piat_1:
        print("Nice job! That looks right!  We can see that the model we should impement was the 6th model using 1088 features.  It is the model that has the best test rsquared value.")
    elif q4_piat['The optimal number of features based on the results is'] != q4_piat_1['The optimal number of features based on the results is']:
        print("Oops!  That isn't right for the optimal number of features.  You can get this as the number of columns in either the training or testing datasets.  Note, this is different than the inputs, as they are checking the threshold for the number of missing values in a column, not a threshold for the number of features.")
    elif q4_piat['The model we should implement in practice has a train rsquared of'] != q4_piat_1['The model we should implement in practice has a train rsquared of'] or q4_piat['The model we should implement in practice has a test rsquared of'] != s.q4_piat['The model we should implement in practice has a test rsquared of']:
        print("The rsquared values don't look right.  The optimal model should be the model that performed the best on the test data.  The rsquared values should be the rsquared for the training and test sets of data using the same, best model based on the test data.")
    elif q4_piat['If we were to allow the number of features to continue to increase'] != q4_piat_1['If we were to allow the number of features to continue to increase']:
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
