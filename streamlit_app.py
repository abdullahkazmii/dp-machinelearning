import streamlit as st
import pandas as pd
st.title('🤖 Machine Learning App')

st.info("Abdullah's first Machine Learning App!")

with st.expander("Data"):
  st.write("**Raw Data:**")
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write("**X**")
  X = df.drop('species', axis=1)
  X
  
  st.write("**Y**")
  Y = df[['species', 'sex']]
  Y

