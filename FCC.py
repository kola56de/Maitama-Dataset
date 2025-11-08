import streamlit as st
import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

st.set_page_config(page_title="Maitama District ML App", layout="wide")
st.title("Maitama District Route Analysis and Speed Pridiction (Intaractive App)")

data = {
    "ROUTES": [
        "Banex - Hospital Junction", 
        "Banex - University Junction",
        "Banex - Wuse Market Junction",
        "Banex - Head of Service Junction", 
        "Hospital Junction - University Junction",
        "Hospital Junction - Wuse Market Junction", 
        "Hospital Junction - Head of Service",
        "Wuse Market Junction - University Junction", 
        "Wuse Market Junction - Head of Service Junction",
        "University Junction - Head of Service"
    ],
    "LENGTH_KM": [2.5, 3.9, 1.7, 7.0, 1.3, 2.5, 4.8, 3.6, 5.3, 1.0],
    "TIME_SEC": [471, 364, 101, 408, 132, 227, 218, 185, 312, 149],
    "AVG SPEED": [19, 29, 62, 61, 35, 39, 28, 37, 62, 25]

    
}
df = pd.DataFrame(data)
st.subheader("Maitama District Dataset")
st.dataframe(df)

st.subheader("Intaractive Data Visualization")
col1, col2 = st.columns([1, 2])

with col1:
    x_var = st.selectbox("Select X-axis variable:", ["LENGTH_KM", "TIME_SEC", "AVG SPEED"])
    y_var = st.selectbox("Select Y-axis variable:", ["LENGTH_KM", "TIME_SEC", "AVG SPEED"])
    plot_type = st.radio("Select Plot Type:", ["Scatter Plot", "Line Plot", "Regression Plot"])

with col2:
    fig, ax = plt.subplots()
    if plot_type == "Scatter Plot":
        sns.scatterplot(x=x_var, y=y_var, data=df, ax=ax, s=100)
    elif plot_type == "Line Plot":
        sns.lineplot(x=x_var, y=y_var, data=df, ax=ax, marker="o")
    elif plot_type == "Regression Plot":
        sns.regplot(x=x_var, y=y_var, data=df, ax=ax, scatter_kws={"s":80})
    ax.set_title(f"{plot_type} of {y_var} vs {x_var}")
    st.pyplot(fig)

     

    