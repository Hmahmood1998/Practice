import streamlit as st
import pandas as pd
from visulization import *
import plotly.graph_objs as go


st.title("Mall Customer Segmentation")

def readData():
    Mall_Customers = pd.read_csv('Mall_Customers.csv')
    Mall_Customers.drop(["CustomerID"], axis=1, inplace=True)
    return Mall_Customers

df = readData()

sidebar = st.sidebar

sidebar.title('User Options')


def introduction():
    st.markdown("""
        ## Visulization of Mall Customer Segmentation
        
    """)

    c1, c2 = st.columns(2)

    c1.header("Column 1 Content")
    c2.header("Column 2 Content")


def execute():
    st.subheader('project working here')

    st.dataframe(df)

    # genx=df[]
    # fig=(data,)

    # 1 Graph
    st.markdown('## Numbers of Customer in different age gap ')
    
    data=df

    age_18_25 = df.Age[(df.Age>=18) & (df.Age<=25)]
    age_26_35 = df.Age[(df.Age>=26) & (df.Age<=35)]
    age_36_45 = df.Age[(df.Age>=36) & (df.Age<=45)]
    age_46_55 = df.Age[(df.Age>=46) & (df.Age<=55)]
    age_55_above = df.Age[df.Age>=56]

    agex = ["18-25","26-35","36-45","46-55","55+"]
    agey = [len(age_18_25.values), len(age_26_35.values), len(age_36_45.values), len(age_46_55.values), len(age_55_above.values)]

    fig=plotBar(data,agex,agey)
    st.plotly_chart(fig,use_container_width=True)

    st.markdown('## Numbers of Customer having the score ')

    ss_1_20 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >=1)&(df["Spending Score (1-100)"] <=20)]
    ss_21_40 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >=21)&(df["Spending Score (1-100)"] <=40)]
    ss_41_60 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >=41)&(df["Spending Score (1-100)"] <=60)]
    ss_61_80 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >=61)&(df["Spending Score (1-100)"] <=80)]
    ss_81_100 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >=81)&(df["Spending Score (1-100)"] <=100)]

    ssx = ["1-20","21-40","41-60","61-80","81-100"]
    ssy = [len(ss_1_20.values), len(ss_21_40.values), len(ss_41_60.values), len(ss_61_80.values), len(ss_81_100.values)]

    fig=plotBar(data,ssx,ssy)
    st.plotly_chart(fig,use_container_width=True)

    st.markdown('## Scatter Chart between Anuual Income and Spending Score')

    fig=plotScatter(data,'Annual Income (k$)','Spending Score (1-100)')
    st.plotly_chart(fig,use_container_width=True)

    st.markdown('## Numbers Of Customer having different Annual Income gap')

    ai_0_30 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >=0)&(df["Annual Income (k$)"] <=30)]
    ai_31_60 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >=21)&(df["Annual Income (k$)"] <=60)]
    ai_61_90 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >=61)&(df["Annual Income (k$)"] <=90)]
    ai_91_120 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >=91)&(df["Annual Income (k$)"] <=120)]
    ai_121_150 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >=121)&(df["Annual Income (k$)"] <=150)]

    ssx = ["$ 0-30,000","$ 30,001-60,000","$ 60,001-90,000","$ 90,001-1,20,000","$ 1,20,000-1,50,000"]
    ssy = [len(ai_0_30.values), len(ai_31_60.values), len(ai_61_90.values), len(ai_91_120.values), len(ai_121_150.values)]

    fig=plotBar(data,ssx,ssy)
    st.plotly_chart(fig,use_container_width=True)
    
    

options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()