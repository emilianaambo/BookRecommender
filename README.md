# BookRecommender

Project Description:

This project aims at Building a Book Recommendation System by using the Book Crossing dataset which was collected by Cai-   Nicolas Ziegler in 2004. It contains 278,858 user data and provides 1,149,780 ratings (explicit / implicit) and about     271,379 books. 
The dataset can be downloaded as a zip from [here](http://www2.informatik.uni-freiburg.de/~cziegler/BX/).

### Preview of data:
* Books Data (BX-Books.csv) 

  Columns: ISBN', 'title', 'author', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL'

* Ratings data (BX-Book-Ratings.csv)

  Columns: userID', 'ISBN', 'rating'(implicit/explicit)

* User Data(BX-Users.csv)

  Columns: 'userID', 'location', 'age' 


## This project contains two Notebooks:
1. Data Cleaning/Analysis: can be found [here](https://github.com/emilianaambo/BookRecommender/blob/master/notebooks/1%20Data%20Analysis_Cleaning%20Book%20Recommendation.ipynb).

2. Data Modeling (Machine Learning): can be found [here](https://github.com/emilianaambo/BookRecommender/blob/master/notebooks/2%20Machine%20Learning%20Book%20Recommendation.ipynb).

   Achieved using Collaborative filtering: Alternating Least Square matrix (ALS) algorithm.
 
## Data (processed)
The final cleaned dataset used for the machine learning part is limited to only 50000 records out of about 383842 (also size limitations, too large to upload on github), just for  test purposes can be found [here](https://github.com/emilianaambo/BookRecommender/tree/master/data.csv).


## Required Frameworks/Libraries
* Spark environment
* pyspark
* numpy
* pandas
* matplotlib
* seaborn
