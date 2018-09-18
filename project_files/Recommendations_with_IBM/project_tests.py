import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('data/user-item-interactions.csv')
df_content = pd.read_csv('data/articles_community.csv')
del df['Unnamed: 0']
del df_content['Unnamed: 0']


def sol_1_test(sol_1_dict):
    sol_1_dict_ = {
    '`50% of individuals interact with ____ number of articles or fewer.`': 3,
    '`The total number of user-article interactions in the dataset is ______.`': 45993,
    '`The maximum number of user-article interactions by any 1 user is ______.`': 364,
    '`The most viewed article in the dataset was viewed _____ times.`': 937,
    '`The article_id of the most viewed article is ______.`': '1429.0',
    '`The number of unique articles that have at least 1 rating ______.`': 714,
    '`The number of unique users in the dataset is ______`': 5148,
    '`The number of unique articles on the IBM platform`': 1051,
    }
    
    if sol_1_dict_ == sol_1_dict:
        print("It looks like you have everything right here! Nice job!")
        
    else:
        for k, v in sol_1_dict.items():
            if sol_1_dict_[k] != sol_1_dict[k]:
                print("Oops! It looks like the value associated with: {} wasn't right. Try again.  It might just be the datatype.  All of the values should be ints except the article_id should be a string.".format(k))
                
                
def sol_2_test(top_articles):
    top_5 = top_articles(5)
    top_10 = top_articles(10)
    top_20 = top_articles(20)
    
    checks = ['top_5', 'top_10', 'top_20']
    for idx, file in enumerate(checks):
        if set(eval(file)) == set(pickle.load(open( "{}.p".format(file), "rb" ))):
            print("Your {} looks like the solution list! Nice job.".format(file))
        else:
            print("Oops! The {} list doesn't look how we expected.  Try again.".format(file))
    
    
    
def sol_5_test(sol_5_dict):
    sol_5_dict_1 = {
    'The user that is most similar to user 1.': 3933, 
    'The user that is the 10th most similar to user 131': 242,
    'A list of top 3 recommendations for user 2 by article id': ['1024.0', '833.0', '1186.0'],
    'A list of top 5 recommendations for user 4459 by article id': ['26.0', '833.0', '339.0', '76.0', '164.0']
    }
    if sol_5_dict == sol_5_dict_1:
        print("This all looks good!  Nice job!")
        
    else:
        for k, v in sol_5_dict.items():
            if sol_5_dict[k] != sol_5_dict_1[k]:
                print("Oops!  Looks like there is a mistake with the {} key in your dictionary.  The answer should be {}.  Try again.".format(k,v))
    
    
def sol_4_test(sol_4_dict):
    
    a = 662 # len(test_idx) - user_item_test.shape[0]
    b = 574 # user_test_shape[1] or len(test_arts) because we can make predictions for all articles
    c = 20 # user_item_test.shape[0]
    d = 0 # len(test_arts) - user_item_test.shape[1]

    sol_4_dict_1 = {
    'How many users can we make predictions for in the test set?': c, 
    'How many users in the test set are we not able to make predictions for because of the cold start problem?': a, 
    'How many movies can we make predictions for in the test set?': b,
    'How many movies in the test set are we not able to make predictions for because of the cold start problem?': d
    }
    
    if sol_4_dict == sol_4_dict_1:
        print("Awesome job!  That's right!  All of the test movies are in the training data, but there are only 20 test users that were also in the training set.  All of the other users that are in the test set we have no data on.  Therefore, we cannot make predictions for these users using SVD.")
    else:
        for k, v in sol_4_dict_1.items():
            if sol_4_dict_1[k] != sol_4_dict[k]:
                print("Sorry it looks like that isn't the right value associated with {}.  Try again.".format(k))
     
    
 