import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with st.container():
    st.markdown('# Heart Conditions Analysis ')
    df = pd.read_csv('heart.csv')
    st.dataframe(df)
    st.bar_chart(df)


    
