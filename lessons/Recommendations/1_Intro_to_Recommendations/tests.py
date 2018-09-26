import numpy as np
import pandas as pd

def q1_check(input_dict):
    a = 53968
    b = 10
    c = 7
    d = 31245
    e = 15
    f = 0
    g = 4
    h = 712337
    i = 28

    dict_sol1 = {
    'The number of movies in the dataset': d,
    'The number of ratings in the dataset': h,
    'The number of different genres': i,
    'The number of unique users in the dataset': a,
    'The number missing ratings in the reviews dataset': f,
    'The average rating given across all ratings': c,
    'The minimum rating given across all ratings': f,
    'The maximum rating given across all ratings': b
    }

    if input_dict == dict_sol1:
        print("That looks good to me!")

    else:
        print("Oops!  That doesn't look quite right.  Try again.")



def create_ranked_df(movies, reviews):
    '''
    INPUT
    movies - the movies dataframe
    reviews - the reviews dataframe

    OUTPUT
    ranked_movies - a dataframe with movies that are sorted by highest avg rating, more reviews,
                    then time, and must have more than 4 ratings
    '''

    # Pull the average ratings and number of ratings for each movie
    movie_ratings = reviews.groupby('movie_id')['rating']
    avg_ratings = movie_ratings.mean()
    num_ratings = movie_ratings.count()
    last_rating = pd.DataFrame(reviews.groupby('movie_id').max()['date'])
    last_rating.columns = ['last_rating']

    # Add Dates
    rating_count_df = pd.DataFrame({'avg_rating': avg_ratings, 'num_ratings': num_ratings})
    rating_count_df = rating_count_df.join(last_rating)

    # merge with the movies dataset
    movie_recs = movies.set_index('movie_id').join(rating_count_df)

    # sort by top avg rating and number of ratings
    ranked_movies = movie_recs.sort_values(['avg_rating', 'num_ratings', 'last_rating'], ascending=False)

    # for edge cases - subset the movie list to those with only 5 or more reviews
    ranked_movies = ranked_movies[ranked_movies['num_ratings'] > 4]

    return ranked_movies




def popular_recommendations(user_id, n_top, ranked_movies):
    '''
    INPUT:
    user_id - the user_id (str) of the individual you are making recommendations for
    n_top - an integer of the number recommendations you want back
    ranked_movies - a pandas dataframe of the already ranked movies based on avg rating, count, and time

    OUTPUT:
    top_movies - a list of the n_top recommended movies by movie title in order best to worst
    '''

    top_movies = list(ranked_movies['movie'][:n_top])

    return top_movies



def show_clean_dataframes():
    reviews = pd.read_csv('./reviews_clean.csv')
    print(reviews.head())
    movies = pd.read_csv('./movies_clean.csv')
    print(movies.head())
    return reviews, movies



def popular_recs_filtered(user_id, n_top, ranked_movies, years=None, genres=None):
    # Filter movies based on year and genre
    if years is not None:
        ranked_movies = ranked_movies[ranked_movies['date'].isin(years)]

    if genres is not None:
        num_genre_match = ranked_movies[genres].sum(axis=1)
        ranked_movies = ranked_movies.loc[num_genre_match > 0, :]


    # create top movies list
    top_movies = list(ranked_movies['movie'][:n_top])

    return top_movies


def test_recs(sol_dict):
    a = "pearson's correlation and spearman's correlation"
    b = 'item based collaborative filtering'
    c = "there were too many ratings to get a stable metric"
    d = 'user based collaborative filtering'
    e = "euclidean distance and pearson's correlation coefficient"
    f = "manhatten distance and euclidean distance"
    g = "spearman's correlation and euclidean distance"
    h = "the spread in some ratings was zero"
    i = 'content based recommendation'
    sol_dict1 = {
        'The type of recommendation system implemented here was a ...': d,
        'The two methods used to estimate user similarity were: ': e,
        'There was an issue with using the correlation coefficient.  What was it?': h
    }

    if sol_dict == sol_dict1:
        print("Looks like you have a good grasp of the recommendations made in this notebook!")

    if sol_dict['The type of recommendation system implemented here was a ...'] !=  d:
        print("Oops!  The first key, value pair doesn't look right!  This is a collaborative filtering recommendation system based on users.")

    if sol_dict['The two methods used to estimate user similarity were: '] != e:
        print("Oops! The second key, value pair doesn't look right!  Pearson's correlation coefficient and euclidean distance were used in understanding the relationships between users.")

    if sol_dict['There was an issue with using the correlation coefficient.  What was it?'] != h:
        print("Oops!  The third key, value pair doesn't look right!  Because when comparing two users, there were times when the ratings were all the same.  Therefore, the standard deviation was 0, and the correlation coefficient would become a NaN value.")




def test_recs2(sol_dict2):
    a = 567
    b = 1503
    c = 1319
    d = 1325
    e = 2526710
    f = 0
    g = 'Use another method to make recommendations - content based, knowledge based, or model based collaborative filtering'

    sol_dict2_check = {
        'For how many pairs of users were we not able to obtain a measure of similarity using correlation?': e,
        'For how many pairs of users were we not able to obtain a measure of similarity using euclidean distance?': f,
        'For how many users were we unable to make any recommendations for using collaborative filtering?': c,
        'For how many users were we unable to make 10 recommendations for using collaborative filtering?': d,
        'What might be a way for us to get 10 recommendations for every user?': g
    }

    if sol_dict2 == sol_dict2_check:
        print("Nice job! Your solution looks like it matches what we expected.")

    else:
        print("Oops!  That doesn't look right! Use df_corrs - a dataframe of user1, user2, pearson correlation between the two users, df_dists - a dataframe of user1, user2, euclidean distance between the two users, and all_recs_sol - a dictionary of all recommendations (key = user, value = list of recommendations to assist with filling in the dictionary.  If you get stuck check out the solution by clicking the orange Jupyter icon in the top left.")


def sim_2_sol(sol_dict):
    a = True
    b = False
    c = "We can't be sure."


    pearson_dct = {"If when x increases, y always increases, Pearson's correlation will be always be 1.": b,
                   "If when x increases by 1, y always increases by 3, Pearson's correlation will always be 1.": a,
                   "If when x increases by 1, y always decreases by 5, Pearson's correlation will always be -1.": a,
                   "If when x increases by 1, y increases by 3 times x, Pearson's correlation will always be 1.": b
    }

    if pearson_dct == sol_dict:
        print("That's right!  Pearson's correlation relates to a linear relationship.  The second and third cases are examples of perfect linear relationships, where we would receive values of 1 and -1.  Only having an increase or decrease that are directly related will not lead to a Pearson's correlation coefficient of 1 or -1.  You can see this by testing out your function using the examples above without using assert statements.")

    else:
        print("Oops!  That doesn't look right... Pearson's correlation relates to a linear relationship.  The second and third cases are examples of perfect linear relationships, where we would receive values of 1 and -1.  Only having an increase or decrease that are directly related will not lead to a Pearson's correlation coefficient of 1 or -1.  You can see this by testing out your function using the examples above without using assert statements.  Try looking at the correlation of different relationships to prove the values to yourself.")


def sim_4_sol(sol_dict):
    a = True
    b = False
    c = "We can't be sure."


    spearman_dct = {"If when x increases, y always increases, Spearman's correlation will be always be 1.": a,
                    "If when x increases by 1, y always increases by 3, Pearson's correlation will always be 1.": a,
                    "If when x increases by 1, y always decreases by 5, Pearson's correlation will always be -1.": a,
                    "If when x increases by 1, y increases by 3 times x, Pearson's correlation will always be 1.": a
}
    if spearman_dct == sol_dict:
        print("That's right!  Unlike Pearson's correlation, Spearman's correlation can have perfect relationships (1 or -1 values) that aren't linear relationships.  You will notice that neither Spearman or Pearson correlation values suggest a relation when there are quadratic relationships.")

    else:
        print("Oops!  That doesn't look right...these are actually all true statements! Unlike Pearson's correlation, Spearman's correlation can have perfect relationships (1 or -1 values) that aren't linear relationships.  You will notice that neither Spearman or Pearson correlation values suggest a relation when there are quadratic relationships.")


def sim_6_sol(sol_dict):
    a = True
    b = False
    c = "We can't be sure."


    corr_comp_dct = {"For all columns of play_data, Spearman and Kendall's measures match.": a,
                    "For all columns of play_data, Spearman and Pearson's measures match.": b,
                    "For all columns of play_data, Pearson and Kendall's measures match.": b}

    if corr_comp_dct == sol_dict:
        print("That's right!  Pearson does not match the other two measures, as it looks specifically for linear relationships.  However, Spearman and Kenall's measures are exactly the same to one another in the cases related to play_data.")

    else:
        print("Oops!  That doesn't look right...Pearson does not match the other two measures, as it looks specifically for linear relationships.  However, Spearman and Kenall's measures are exactly the same to one another in the cases related to play_data.")

def test_recs(sol_dict):
    sol_dict1 = {
        'The type of recommendation system implemented here was a ...': 'user based collaborative filtering',
        'The two methods used to estimate similarity were: ': "euclidean distance and pearson's correlation coefficient",
        'There was an issue with using the correlation coefficient.  What was it?': 'the spread in some ratings was zero'
    }
    if sol_dict1 == sol_dict:
        return "That's right! All of your solutions look good!"
    else:
        for k, v in sol_dict.items():
            if sol_dict1[k] != sol_dict[k]:
                print("Oops! Your answer to: {} doesn't look quite right.".format(k))


def test_recs2(sol_dict2):
    a = 567
    b = 1503
    c = 1319
    d = 1325
    e = 2526710
    f = 0
    g = 'Use another method to make recommendations - content based, knowledge based, or model based collaborative filtering'

    sol_dict1 = {
        'For how many pairs of users were we not able to obtain a measure of similarity using correlation?': e,
        'For how many pairs of users were we not able to obtain a measure of similarity using euclidean distance?': f,
        'For how many users were we unable to make any recommendations for using collaborative filtering?': c,
        'For how many users were we unable to make 10 recommendations for using collaborative filtering?': d,
        'What might be a way for us to get 10 recommendations for every user?': g
    }
    if sol_dict1 == sol_dict2:
        return "That's right! All of your solutions look good!"
    else:
        for k, v in sol_dict2.items():
            if sol_dict1[k] != sol_dict[k]:
                print("Oops! Your answer to: {} doesn't look quite right.".format(k))

          
