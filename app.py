import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def countPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x = "year", data = df)
    st.pyplot(fig)

with st.container():
    st.markdown('# Heart Conditions Analysis ')
    df = pd.read_csv('heart.csv')
    st.dataframe(df)
    st.bar_chart(df)
    sns.lineplot(df)
    countPlot()


    
