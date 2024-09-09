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

with st.expander("Data Visualization"):
  st.scatter_chart(data = df, x='bill_length_mm', y = 'body_mass_g', color = 'species')

#Data Preperation 
with st.sidebar:
  st.header("Input Features")
  island = st.selectbox('island', ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox('Gender', ('male', 'female'))
  bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill Depth (mm)', 13.10, 17.20, 21.50)
  flipper_length_mm = st.slider('Flipper Length (mm)', 172.00, 201.00, 231.00)
  body_mass_g	= st.slider('Body Mass (g)', 2700.00, 4207.00, 6300.00)
