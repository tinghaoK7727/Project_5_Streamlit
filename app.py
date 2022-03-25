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

with st.container():
    st.markdown('# Heart Conditions Analysis ')
    df = pd.read_csv('heart.csv')
    # st.sidebar.header('This is the sidebar')
    col1, col2, col3 = st.columns(3)
    # st.dataframe(df)
    # st.bar_chart(df)
    # sns.lineplot(df)



    # plt.figure(figsize=(12,10))
    # sns.heatmap(df.corr(),annot=True,cmap="magma",fmt='.2f')
    # st.pyplot()

    df2 = df.copy()




    def chng(sex):
        if sex == 0:
            return 'female'
        else:
            return 'male'

    df2['sex'] = df2['sex'].apply(chng)



    # def chng2(prob):
    #     if prob == 0:
    #         return 'Heart Disease'
    #     else:
    #         return 'No Heart Disease'

    # df2['target'] = df2['target'].apply(chng2)


    with col1:
        # pal1 = sns.color_palette("mako", as_cmap=True) 
        sns.countplot(data= df2, x='sex',hue='target', palette='mako')
        plt.title('Gender v/s target\n')
        
        st.pyplot()


        sns.countplot(data= df2, x='cp',hue='target', palette='mako')
        plt.title('Chest Pain Type v/s target\n')
        st.pyplot()


        sns.countplot(data= df2, x='sex',hue='thal', palette='mako')
        plt.title('Gender v/s Thalassemia\n')
        print('Thalassemia (thal-uh-SEE-me-uh) is an inherited blood disorder that causes your body to have less hemoglobin than normal. Hemoglobin enables red blood cells to carry oxygen')
        st.pyplot()

        # sns.countplot(data= df2, x='slope',hue='target')
        # plt.title('Slope v/s Target\n') 
        # st.pyplot()

        # sns.countplot(data= df2, x='exang',hue='thal')
        # plt.title('exang v/s Thalassemia\n')
        # st.pyplot()

        plt.figure(figsize=(16,7))
        sns.distplot(df[df['target']==0]['age'],kde=False,bins=50, color='blue')
        plt.title('Age of Heart Diseased Patients\n')
        st.pyplot()

        plt.figure(figsize=(16,7))
        sns.distplot(df[df['target']==0]['chol'],kde=False,bins=40, color='blue')
        plt.title('Chol of Heart Diseased Patients\n')
        st.pyplot()

        plt.figure(figsize=(16,7))
        sns.distplot(df[df['target']==0]['thalach'],kde=False,bins=40, color='blue')
        plt.title('thalach of Heart Diseased Patients\n')
        st.pyplot()

        df3 = df[df['target'] == 0 ][['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
        'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']] 



    with col2:

        
        pal = sns.light_palette("blue", as_cmap=True)
        print('Age vs trestbps(Heart Diseased Patinets)')
        sns.jointplot(data=df3, x='age', y='trestbps', kind='hex', cmap='Reds')
        st.pyplot()

        # sns.jointplot(data=df3, x='chol', y='age', kind='kde', cmap='PuBu')
        # st.pyplot()


        # sns.jointplot(data=df3, x='chol', y='trestbps', kind='resid')
        # st.pyplot()

        sns.boxplot(data=df2,x='target',y='age', palette='mako')
        st.pyplot()

        # plt.figure(figsize=(14,8))
        # sns.violinplot(data=df2,x='ca',y='age',hue='target')
        # st.pyplot()

        sns.boxplot(data=df2,x='cp',y='thalach',hue='target', palette='mako')
        st.pyplot()

        plt.figure(figsize=(10,7))
        sns.boxplot(data=df2,x='fbs',y='trestbps',hue='target', palette='mako')
        st.pyplot()

    with col3:

        plt.figure(figsize=(10,7))
        sns.violinplot(data=df2,x='exang',y='oldpeak',hue='target', palette='mako')
        st.pyplot()

        plt.figure(figsize=(10,7))
        sns.boxplot(data=df2,x='slope',y='thalach',hue='target', palette='mako')
        st.pyplot()

        # sns.violinplot(data=df2,x='thal',y='oldpeak',hue='target')
        # st.pyplot()

        # sns.violinplot(data=df2,x='target',y='thalach')
        # st.pyplot()

        sns.clustermap(df.corr(),annot=True)
        st.pyplot()

        # sns.pairplot(df,hue='cp')
        # st.pyplot()

        
    # fig, [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10] = plt.subplots()
    # ax1.scatter([1, 2, 3], [1, 2, 3])
    # st.pyplot(fig)