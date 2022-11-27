# IPL_win_predictor

## Overview
Indian Premier League is the biggest cricket league in the entire world and is one of the most watched league. Every year we see the match and in between matches we often see win prediction for the batting/bowling team in the 2nd inning. I wondered how they calculate this win prediction and based on which parameters. This motivated to find out how its done and hence this project was introduced.

## Dataset

The dataset has been obtained from the repository Indian Premier League (Cricket) hosted on Kaggle. The dataset comprised of two csv files “matches.csv” and “deliveries.csv”. The characteristics of the individual files are as below:  

Matches.csv  
This data file comprises of records of all matches played in IPL from season 2008 to 2017. The data file comprises of 18 features. It contains data corresponding to the name of the teams, venue of the match, outcome, umpires and details pertaining to the matches played. There are 636 entries in the data file.

Deliveries.csv  
This data file comprises of records of every delivery bowled in each of the matches. The records are chronologically arranged. The data includes 23 features including the outcome of every delivery and the number of runs scores and the way runs were scored. There are 150460 entries in the data file.

## Models Trained
For the prediction 2 models were trained:  
* Logistic Regression
* Random Forest Classifier
With these Logistic Regression model was able to achieve an accuracy of 81% and Random Forest Classifier model was able to achieve an accuracy of 97%. Random Forest Classifier model proved to accurately predict winning team.

## Results
![IPL_pred](https://user-images.githubusercontent.com/47081733/204125023-a7a8bd3e-6dfc-4a2d-acac-0298440b7521.jpg)

The above plot shows the entire summary of 20 overs match, runs scored per over, winning probability in green and losing probability in red.
![IPL_result](https://user-images.githubusercontent.com/47081733/204125027-68d23463-c02e-4abc-be0c-c0c0ab1c1a0b.jpg)

This is the final tool which shows prediction based on the input given.

---
Project Link
---
Heroku : https://ipl-win-prediction123.herokuapp.com/
