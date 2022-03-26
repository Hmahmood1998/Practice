from tracemalloc import Snapshot
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from visulization import *
# import plotly.graph_objs as go

def readData():
    mall_customer = pd.read_csv('Mall_Customers.csv')
    mall_customer.drop(["CustomerID"], axis=1, inplace=True)
    return mall_customer

df=readData()

st.title("My Mini Project Name")

# plt.figure(1, figsize=(15,6))
# n=0
# for x in ['Age','Annual Income (k$)','Spending Score (1-100)']:
#     n+=1
#     plt.subplot(1,3,n)
#     plt.subplots_adjust(hspace=0.5, wspace=0.5)
#     sns.distplot(df[x], bins=20)
#     plt.title('Distplot of {}'.format(x))
# plt.show()

plt.figure(1, figsize=(15,5))
sns.countplot(y='Gender',data=df)
plt.show()


# fig=plotBar(y='Gender',data=df)
# st.plotly_chart(fig, use_container_width=True)
# plt.show()


sidebar = st.sidebar

sidebar.title('User Options')


def introduction():
    st.markdown("""
        ## Heading Level 2
        - Feature 1
        - Feature 2
        - Feature 3
    """)

    c1, c2 = st.columns(2)

    c1.header("Column 1 Content")
    c2.header("Column 2 Content")


def execute():
    st.subheader('project working here')
    st.dataframe(df)


options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()