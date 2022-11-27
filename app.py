# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:13:49 2022

@author: Pushkar
"""
import streamlit as st
import pickle
import pandas as pd
import base64

original_title = '<p style="font-family:Courier; color:White; font-size: 40px;">IPL Win Predictor</p>'


st.markdown(original_title, unsafe_allow_html=True)


page_bg_img = '''
    <style>
    .stApp {
    background-image: url("https://wallpapercave.com/wp/wp6194569.jpg");
    background-size: cover;
    }
    </style>
    ''' 
st.markdown(page_bg_img, unsafe_allow_html=True)
col1, col2 = st.columns(2)

teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Kolkata Knight Riders',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Kings XI Punjab',
    'Royal Challengers Bangalore',
    'Delhi Capitals',
]

cities = ['Bengaluru', 'Mumbai', 'Chennai', 'Hyderabad', 'Kolkata', 'Durban',
       'Bangalore', 'Kimberley', 'Chandigarh', 'Port Elizabeth', 'Pune',
       'Jaipur', 'Delhi', 'Visakhapatnam', 'Ahmedabad', 'Cuttack',
       'Johannesburg', 'East London', 'Mohali', 'Centurion', 'Cape Town',
       'Raipur', 'Ranchi', 'Abu Dhabi', 'Indore', 'Dharamsala', 'Nagpur',
       'Sharjah', 'Bloemfontein']

pipe = pickle.load(open('pipe.pkl','rb'))


with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
    
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox("Select host city", sorted(cities))

target = st.number_input('Target')

col3, col4,col5 = st.columns(3)
with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets down')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 -(overs*6)
    wickets = 10-wickets
    current_rate =  score/overs
    required_rate = (runs_left*6)/balls_left
    
    input_df = pd.DataFrame({'batting_team':[batting_team],
                  'bowling_team':[bowling_team],
                  'city':[selected_city],
                  'runs_left':[runs_left],
                  'balls_left':[balls_left],
                  'wickets':[wickets],
                  'current_rate':[current_rate],
                  'required_rate':[required_rate],
                  'total_runs_x':[target]})
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    
    st.header(batting_team+"- "+str(round(win*100))+ "%")
    st.header(bowling_team+"- "+str(round(loss*100))+ "%")