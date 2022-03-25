import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier

# def countPlot():
#     fig = plt.figure(figsize=(10, 4))
#     sns.countplot(x = "year", data = df)
#     st.pyplot(fig)

with st.container():
    st.markdown('# Heart Conditions Analysis ')
    df = pd.read_csv('heart.csv')
    st.dataframe(df)
    st.bar_chart(df)
    # sns.lineplot(df)



    plt.figure(figsize=(12,10))
    sns.heatmap(df.corr(),annot=True,cmap="magma",fmt='.2f')


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




    sns.countplot(data= df2, x='sex',hue='target')
    plt.title('Gender v/s target\n')


    # sns.countplot(data= df2, x='cp',hue='target')
    # plt.title('Chest Pain Type v/s target\n')



    # sns.countplot(data= df2, x='sex',hue='thal')
    # plt.title('Gender v/s Thalassemia\n')
    # print('Thalassemia (thal-uh-SEE-me-uh) is an inherited blood disorder that causes your body to have less hemoglobin than normal. Hemoglobin enables red blood cells to carry oxygen')


    # sns.countplot(data= df2, x='slope',hue='target')
    # plt.title('Slope v/s Target\n') 


    # sns.countplot(data= df2, x='exang',hue='thal')
    # plt.title('exang v/s Thalassemia\n')

    # plt.figure(figsize=(16,7))
    # sns.distplot(df[df['target']==0]['age'],kde=False,bins=50)
    # plt.title('Age of Heart Diseased Patients\n')

    # plt.figure(figsize=(16,7))
    # sns.distplot(df[df['target']==0]['chol'],kde=False,bins=40)
    # plt.title('Chol of Heart Diseased Patients\n')

    # plt.figure(figsize=(16,7))
    # sns.distplot(df[df['target']==0]['thalach'],kde=False,bins=40)
    # plt.title('thalach of Heart Diseased Patients\n')

    # df3 = df[df['target'] == 0 ][['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
    #    'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']] 

    # pal = sns.light_palette("blue", as_cmap=True)
    # print('Age vs trestbps(Heart Diseased Patinets)')
    # sns.jointplot(data=df3, x='age', y='trestbps', kind='hex', cmap='Reds')

    # sns.jointplot(data=df3, x='chol', y='age', kind='kde', cmap='PuBu')


    # sns.jointplot(data=df3, x='chol', y='trestbps', kind='resid')

    # sns.boxplot(data=df2,x='target',y='age')

    # plt.figure(figsize=(14,8))
    # sns.violinplot(data=df2,x='ca',y='age',hue='target')

    # sns.boxplot(data=df2,x='cp',y='thalach',hue='target')

    # plt.figure(figsize=(10,7))
    # sns.boxplot(data=df2,x='fbs',y='trestbps',hue='target')

    # plt.figure(figsize=(10,7))
    # sns.violinplot(data=df2,x='exang',y='oldpeak',hue='target')

    # plt.figure(figsize=(10,7))
    # sns.boxplot(data=df2,x='slope',y='thalach',hue='target')

    # sns.violinplot(data=df2,x='thal',y='oldpeak',hue='target')

    # sns.violinplot(data=df2,x='target',y='thalach')

    # sns.clustermap(df.corr(),annot=True)

    # sns.pairplot(df,hue='cp')

    plt.show()