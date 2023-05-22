import streamlit as st
import glob
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob('diary/*.txt'))

analyzer = SentimentIntensityAnalyzer()

px.line()

entries = []

negativity = []
positivity = []
for filepath in filepaths:
    with open(filepath) as file:
        text = file.read()
    scores = analyzer.polarity_scores(text)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])

dates = [name.strip('.txt').strip('diary\\') for name in filepaths]

st.title('Diary Tone')
st.subheader('Positivity')
pos_figure = px.line(x=dates, y=positivity,
                     labels={'x': 'Date', 'y' : 'Positivity'})
st.plotly_chart(pos_figure)

st.subheader('Negativity')
neg_figure = px.line(x=dates, y=negativity,
                     labels={'x': 'Date', 'y' : 'Negativity'})
st.plotly_chart(neg_figure)

