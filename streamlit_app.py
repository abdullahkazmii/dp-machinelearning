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
  bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill Depth (mm)', 13.10, 21.50, 17.20)
  flipper_length_mm = st.slider('Flipper Length (mm)', 172.00, 231.00, 201.00)
  body_mass_g	= st.slider('Body Mass (g)', 2700.00, 6300.00, 4207.00)
  sex = st.selectbox('Gender', ('male', 'female'))

#Create a Dataframe for the input features
data  = {
  'island': island,
  'bill_length_mm': bill_length_mm,
  'bill_depth_mm': bill_depth_mm,
  'flipper_length_mm': flipper_length_mm,
  'body_mass_g': body_mass_g,
  'sex': sex
}

input_df = pd.DataFrame(data, index=[0])
input_pen = pd.concat([input_df, X], axis = 0)

with st.expander('Input Features'):
  st.write("**Input Penguin**")
  input_df
  st.write("**Combined Penguins Data**")
  input_pen

  

