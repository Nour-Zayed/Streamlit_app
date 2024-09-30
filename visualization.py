import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np

@st.cache_data
def load_data(file):
    return pd.read_csv(file)


file=st.file_uploader("Upload file",type=['csv'] )

if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    
    n_rows = st.slider("Choose number of row to display",
                       min_value=5,max_value=len(df),step=1)
    columns_toshow= st.multiselect("Select Columns to show ",df.columns.to_list(),default=df.columns.to_list()
                                   )
    numerical_columns=df.select_dtypes(include=np.number).columns.to_list()
    
    st.write(df[:n_rows][columns_toshow])
    
    tab1,tab2=st.tabs(["Scatter plot","Histogram"])
    with tab1:
        col1,col2,col3,col4=st.columns(4)
    with col1:
    
         x_column=st.selectbox("Select column in x_axis :",numerical_columns)
    with col2:     
         x_column=st.selectbox("Select column in y_axis :",numerical_columns)
    with col3:
        color=st.selectbox("Select column to be color", df.columns)
    with col4:
        size=st.selectbox("Select siza", df.columns)
            

    fig_scatter=px.scatter(df,x=x_column,y=x_column,color=color)
    st.plotly_chart(fig_scatter)
    
    with tab2:
        hisrogram_features=st.selectbox("Select feature to hisrogram",numerical_columns)
        
    
    
    
        fig_hist=px.histogram(df,x=hisrogram_features)
        st.plotly_chart(fig_hist)
    
