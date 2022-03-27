import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# def countPlot():
#     fig = plt.figure(figsize=(10, 4))
#     sns.countplot(x = "year", data = df)
#     st.pyplot(fig)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout="wide")
df = pd.read_csv('heart.csv')
df2 = df.copy()

def chng(sex):
    if sex == 0:
        return 'female'
    else:
        return 'male'

df2['sex'] = df2['sex'].apply(chng)

df3 = df2[df2['target'] == 0 ][['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
    'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']] 

df4 = df[df['target'] == 0 ][['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
    'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']] 

with st.container():
    st.markdown('# Heart Conditions Analysis ')
    # st.dataframe(df)
    # st.sidebar.header('Change parameters')
    
    with st.expander(label='Interactive charts', expanded=True):

        col4, col5 = st.columns(2)

        with col4:
            
            st.sidebar.header('Histogram Parameters')
            hist_labels = st.sidebar.multiselect(label='Choose categories to be plotted in histogram', options = df3.columns, default='age')
            size_of_bins = st.sidebar.select_slider(label='Number of bins', options=range(1,16), value=3)
            st.header((', '.join(hist_labels) + ' with ' + str(size_of_bins) + ' bin(s)').title())
            plt.hist(x=[df4[str(i)] for i in hist_labels], bins=size_of_bins)
            st.pyplot()
            

        


        with col5:
            st.sidebar.header('Hexbin chart parameters')
            xBox = str(st.sidebar.selectbox("X Axis", df3.columns, index=0))
            yBox = str(st.sidebar.selectbox("Y Axis", df3.columns, index=3))
            pal = sns.light_palette("blue", as_cmap=True)
            st.header((xBox + ' vs '+ yBox).title())
            # sns.jointplot(data=df3, x='age', y='trestbps', kind='hex', cmap='BuPu')
            
            # plt.hexbin(df3[xBox],df3[yBox], cmap='BuPu')
            sns.jointplot(data=df4, x=df4[xBox], y=df4[yBox], kind='hex', cmap='BuPu')
            st.pyplot()


        

    with st.expander(label='Static Charts', expanded=True):
        col1, col2, col3 = st.columns(3)
 

        with col1:

            sns.countplot(data= df2, x='sex',hue='target', palette='mako')
            plt.title('Gender v/s target\n')
    
            st.pyplot()

            plt.figure(figsize=(16,7))
            sns.distplot(df[df['target']==1]['age'],kde=False,bins=50, color='blue')
            plt.title('Age of Heart Diseased Patients\n')
            st.pyplot()


            sns.boxplot(data=df2,x='target',y='age', palette='mako')
            st.pyplot()

            sns.boxplot(data=df2,x='cp',y='thalach',hue='target', palette='mako')
            st.pyplot()




        with col2:

            sns.countplot(data= df2, x='cp',hue='target', palette='mako')
            plt.title('Chest Pain Type v/s target\n')
            st.pyplot()

            plt.figure(figsize=(16,7))
            sns.distplot(df[df['target']==1]['chol'],kde=False,bins=40, color='blue')
            plt.title('Chol of Heart Diseased Patients\n')
            st.pyplot()       

            plt.figure(figsize=(10,7))
            sns.boxplot(data=df2,x='fbs',y='trestbps',hue='target', palette='mako')
            st.pyplot()

            sns.heatmap(df.corr(),annot=True, cmap='BuPu')
            st.pyplot()     

        with col3:

            sns.countplot(data= df2, x='sex',hue='thal', palette='mako')
            plt.title('Gender v/s Thalassemia\n')
            print('Thalassemia (thal-uh-SEE-me-uh) is an inherited blood disorder that causes your body to have less hemoglobin than normal. Hemoglobin enables red blood cells to carry oxygen')
            st.pyplot()

            plt.figure(figsize=(16,7))
            sns.distplot(df[df['target']==1]['thalach'],kde=False,bins=40, color='blue')
            plt.title('thalach of Heart Diseased Patients\n')
            st.pyplot()

            plt.figure(figsize=(10,7))
            sns.violinplot(data=df2,x='exang',y='oldpeak',hue='target', palette='mako')
            st.pyplot()

            plt.figure(figsize=(10,7))
            sns.boxplot(data=df2,x='slope',y='thalach',hue='target', palette='mako')
            st.pyplot()
            


        
        
    
            

       