import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


st.title("114k Spotify songs analysis")

df = pd.read_csv('dataset.csv')
st.write("### Dataset overview")
st.write(df.head())

st.write("### Dataset info")
buffer = StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

st.write("### Dataset description")
st.write(df.describe())

# Data cleaning
# Deleting duplicates, leaving the more popular one
df = df.sort_values(['track_id', 'popularity'], ascending=[True, False])
df = df.drop_duplicates('track_id', keep='first')

# Deleting unnecessary column
df = df.drop(columns=['Unnamed: 0'])

# Deleting rows with missing values
df = df.dropna()

# Changing 'duration_ms' values to seconds and renaming
df['duration_ms'] = df['duration_ms']/1000
df.rename(columns={"duration_ms": "duration_s"}, inplace=True)

# Binary encoding 'explicit' column
df['explicit'] = df['explicit'].astype(int)



# Interactive histogram
st.write("### Interactive histogram of numeric features")
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
selected_hist_col = st.selectbox("Select a column for histogram:", numeric_cols)
fig = px.histogram(df, x=selected_hist_col, nbins=20, title=f"Distribution of {selected_hist_col}")
st.plotly_chart(fig)

# Unique values count
st.write("### Unique values count")
st.write(df.nunique())

# Explicit content pie chart
st.write("### Proportion of explicit songs")
explicit_counts = df['explicit'].value_counts()
fig = px.pie(names=['Not explicit', 'Explicit'], values=explicit_counts, title='Explicit songs')
st.plotly_chart(fig)

# Top 10 artists bar chart
st.write("### Top 10 most frequent artists")
top_artists = df['artists'].value_counts().nlargest(10)
fig = px.bar(x=top_artists.index, y=top_artists.values, title='10 most frequent artists', labels={'x': 'Artist', 'y': 'Song count'})
st.plotly_chart(fig)

# Top 10 track titles bar chart
st.write("### Top 10 most frequent track titles")
top_tracks = df['track_name'].value_counts().nlargest(10)
fig = px.bar(x=top_tracks.index, y=top_tracks.values, title='10 most frequent track titles', labels={'x': 'Title', 'y': 'Song count'})
st.plotly_chart(fig)

# Correlation matrix heatmap
st.write("### Correlation matrix")
correlation_matrix = df.corr(numeric_only=True)
fig = px.imshow(correlation_matrix, text_auto=True, title='Correlation Matrix')
st.plotly_chart(fig)

# Strongest correlations
st.write("### Strongest correlations")
corr_pairs = correlation_matrix.unstack().sort_values(ascending=False)
corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]
strongest_correlations = corr_pairs.drop_duplicates().head(5)
st.write(strongest_correlations)

# Interactive hexbin plots
st.write("### Interactive Hexbin Plots")
selected_feature1 = st.selectbox("Select Feature 1:", numeric_cols)
selected_feature2 = st.selectbox("Select Feature 2:", numeric_cols)
if selected_feature1 and selected_feature2:
    fig = px.density_heatmap(df, x=selected_feature1, y=selected_feature2, title=f'{selected_feature1} vs. {selected_feature2}')
    st.plotly_chart(fig)

# Boxplot for popularity by genre
st.write("### Boxplot of popularity by genre")
genres = df['track_genre'].unique()
selected_genres = st.multiselect("Select genres:", genres, default=['pop', 'edm', 'heavy-metal', 'hip-hop', 'jazz', 'alt-rock', 'k-pop'])
df_genres = df[df['track_genre'].isin(selected_genres)]
fig = px.box(df_genres, x='track_genre', y='popularity', title='Boxplot of popularity by genre')
st.plotly_chart(fig)



