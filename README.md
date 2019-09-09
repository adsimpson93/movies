# Movies
This is my repository for for the movie mini-project.

# What was completed
* All required steps: Loading data from a db, computation of top 10 genres, computation of top 10 actors, and unit tests.  
* The first bonus question: Find best actor/director pairs

# Assumptions
* Profit of each film was calculated by gross minus budget 
* I was a little unclear about actor/director pairs. I decided an actor/director pair could be any pair of actor/director that have done 1 or more movies together. For example if a director (D1) has done 3 movies with 3 different actors (A1, A2, A3) and their respective IMBD scores are 98, 87, and 75. Then I would return (D1, A1, 98), (D1, A2, 87), and (D1, A3, 75) in that order if those were the only people/movies in the database.  

# How To Run
* This should run without any problem for most or all versions of Python 3
* I ran this with Python 3.7.3
* No libraries that do not come standard with 3.7.3 were used
* To run the different calculations/get the results just type (actor/director pair takes a few seconds): python calculations.py 
* To run the unit tests just type: python test.py 

# Note About Shortcuts Taken
* Do to trying to get this finished quickly, I did not put much effort into formatting the output
* Also, do to this not being a part of a larger project, I did not put as much effort into naming/documentation/scalibility/etc as I would normally.  
