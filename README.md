# Project_5_Streamlit


**Project Goal:**

The goal of this project is to take existing data, clean it, find ingsights and meaningful correlations and finally create a dashboard via streamlit and delpoy it online. 


**Dataset:**

A dataset of 304 rows and 14 columns about data on the tendency of heart attack and various indicators such as age, gender, fasting blood sugar and maximum heartbeat level etc. All the datas we have are numeric and non of the cells contain NaN values. 


**Data Cleaning:**

As our data contains only numeric values, there is not much data cleaning needed. Based on information found online, we have decided to replace all the numeric values in the gender column by 'female' and 'male' in order to faciliate further data analysis and interpretation.


**Storytelling tactics:**

Our target audience for the dashboard would be health institutions wishing to grasp some information about the population regarding heart attacks and its potential causes and possible triggers. Through reviewing the dashboard, the audience should be able to know what elements are more prompt to cause heart attacks and what are not necessarily related.


**Charts and Widgets:**
1. st.expander(): to save more space and to better organize the display of our charts
2. st.multiselect(): to demonstrate reactive histogram by selecting one or various indicators
3. st.slider(): to choose the number of bins of the histogram
4. st.selectbox(): to choose different x-axis and y-axis to display the corresponding chart
5. Bar chart - gender vs target: to show the head counts of heart attacked population by gender
6. Bar chart - chest pain type vs target: to show the counts of heart attacked people by each chest pain type 
7. Bar chart - gender vs Thalassemia: to show the counts of each type of Thalassemia by gender
8. Histogram - age vs target: to show the distribution of heart attacked population by age
9. Histogram - cholesterol vs target: to show the distribution of heart attacked population by cholesterol level
10. Histogram - thalach vs target: to show the distribution of heart attacked population by thalach (maximum heart rate)
11. Boxplot - age vs target: to show show the difference in interquartile range of heart attacked and non heart attacked people
12. Boxplot - chest pain type vs thalach: to observe if there's correlation between chest pain type and maximum heart rate (all heart attacked chest pain cases have a higher maximum heart rate than non heart attacked ones)
13. Boxplot - fasting blood sugar vs resting blood pressure: to see if there's a correlation bewteen blood sugar and resting blood pressure (heart attacked cases in general have a lower resting blood pressure than non heart attacked ones)
14. Violin plot - exang (exercise angina) vs oldpeak (ST depression), heart attacked ones have in general more cases with oldpeak at 0
15. Heatmap - to desmonstrate a quick look on potential correlations of all elements


**Conclusions:**
- Surprisingly, women are more prompt to have heart attacks than men
- Out of the 4 types of chest pain, type 2 has the highest correlation to heart attack
- The highest number of heart attacks is found in the population between 50 and 60 years old 
- Heart-attacked cases in general have a lower resting blood pressure


**Link to our presentation:**

https://docs.google.com/presentation/d/1gLmwOgY6x6DMrmDvgPK1pQrImiylZkfaO8-EeO290ZY/edit?usp=sharing


**Link to the dashboard:**

https://tryingstreamlit.herokuapp.com/
