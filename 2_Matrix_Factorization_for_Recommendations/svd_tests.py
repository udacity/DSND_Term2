import numpy as np
import pandas as pd

def test1(sol_1_dict):
    a = 20
    b = 68646
    c = 'The Godfather'
    d = 'Goodfellas'
    e = 265
    f = 30685
    g = 4

    sol_1_dict_sol = {
    'the number of users in the user_movie_subset': a,
    'the number of movies in the user_movie_subset': g,
    'the user_id with the highest average ratings given': e,
    'the movie_id with the highest average ratings received': b,
    'the name of the movie that received the highest average rating': c
    }
    
    if sol_1_dict == sol_1_dict_sol:
        print("That's right!  There are 20 users in the dataset, which is given by the number of rows. There are 4 movies in the dataset given by the number of columns.  You can find the movies or users with the highest average ratings by taking the mean of each row or column.  Using the movies table, you can find the movie names associated with each id.  This shows the top rated movie is The Godfather!")
     
    if sol_1_dict['the number of users in the user_movie_subset'] != sol_1_dict_sol['the number of users in the user_movie_subset']:
        print("That doesn't look right for the number of users.  Notice, this should be the number of rows in the subset dataframe.")
        
    if sol_1_dict['the number of movies in the user_movie_subset'] != sol_1_dict_sol['the number of movies in the user_movie_subset']:
        print("That doesn't look right for the number of movies.  Notice, this should be the number of columns in the subset dataframe.")
    
    if sol_1_dict['the user_id with the highest average ratings given'] != sol_1_dict_sol['the user_id with the highest average ratings given']:
        print("That doesn't look right for the user with the highest average rating given.  Try again.")    

    if sol_1_dict['the movie_id with the highest average ratings received'] != sol_1_dict_sol['the movie_id with the highest average ratings received']:
        print("That doesn't look right for the movie_id with the highest average received.  Try again.") 
        
    if sol_1_dict['the name of the movie that received the highest average rating'] != sol_1_dict_sol['the name of the movie that received the highest average rating']:
        print("Oops!  The last one should be the name of the movie - not just the id.  You can get this from the movies dataframe.  Try again.")
        
        
def test2(sol_2_dict):
    a = 'a number that you can choose as the number of latent features to keep'
    b = 'the number of users'
    c = 'the number of movies'
    d = 'the sum of the number of users and movies'
    e = 'the product of the number of users and movies'

    sol_2_dict_sol = {
        'the number of rows in the U matrix': b, 
        'the number of columns in the U matrix': a, 
        'the number of rows in the V transpose matrix': a, 
        'the number of columns in the V transpose matrix': c
    }
    
    
    if sol_2_dict == sol_2_dict_sol:
        print("That's right!  We will now put this to use, so you can see how the dot product of these matrices come together to create our user item matrix.  The number of latent features will control the sigma matrix as well, and this will a square matrix that will at most be the minimum of the number of users and number of movies (in our case the minimum is the 4 movies).")
        
    if sol_2_dict['the number of rows in the U matrix'] != sol_2_dict_sol['the number of rows in the U matrix']:
        print("Oops!  The number of rows in the U matrix will be the same as the number of users.  Try again.")
        
    if sol_2_dict['the number of columns in the U matrix'] != sol_2_dict_sol['the number of columns in the U matrix']:
        print("Oops!  The number of columns in the U matrix will be determined by the number of latent features you decide to keep.  This will at most be the minimum of the number of users and number of movies (in our case the minimum is the 4 movies).  Try again.")
        
    if sol_2_dict['the number of rows in the V transpose matrix'] != sol_2_dict_sol['the number of rows in the V transpose matrix']:
        print("Oops!  The number of rows in the V transpose matrix will be determined by the number of latent features you decide to keep.  This will at most be the minimum of the number of users and number of movies (in our case the minimum is the 4 movies).  Try again.")
        
    if sol_2_dict['the number of columns in the V transpose matrix'] != sol_2_dict_sol['the number of columns in the V transpose matrix']:
        print("Oops!  The number of columns in the V transpose matrix will be determined by the number of movies. Try again.")   
    
    
def question4thoughts():
    print("Looking at the dimensions of the three returned objects, we can see the following:\n\n 1. The u matrix is a square matrix with the number of rows and columns equaling the number of users. \n\n 2. The v transpose matrix is also a square matrix with the number of rows and columns equaling the number of items.\n\n 3. The sigma matrix is actually returned as just an array with 4 values.  \n\n In order to set up the matrices in a way that they can be multiplied together, we have a few steps to perform: \n\n 1. Turn sigma into a square matrix with the number of latent features we would like to keep. \n\n 2. Change the columns of u and the rows of v transpose to match this number of dimensions. \n\n If we would like to exactly re-create the user-movie matrix, we could choose to keep all of the latent features.")