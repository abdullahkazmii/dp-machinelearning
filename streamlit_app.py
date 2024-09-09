import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title('🤖 Machine Learning App')

st.info("Abdullah's first Machine Learning App!")

with st.expander("Data"):
  st.write("**Raw Data:**")
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write("**X**")
  X_raw = df.drop('species', axis=1)
  X_raw
  
  st.write("**Y**")
  Y_raw = df['species']
  Y_raw

with st.expander("Data Visualization"):
  st.scatter_chart(data = df, x='bill_length_mm', y = 'body_mass_g', color = 'species')

#Input Features 
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
input_pen = pd.concat([input_df, X_raw], axis = 0)
with st.expander('Input Features'):
  st.write("**Input Penguin**")
  input_df
  st.write("**Combined Penguins Data**")
  input_pen

#Data Preperation
#encode X
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_pen, prefix=encode)
X = df_penguins[1:]
input_row = df_penguins[:1]

#encode Y
target_mapper = {'Adelie': 0, 'Chinstrap':1, 'Gentoo': 2}
def target_encode(val):
  return target_mapper[val]

y = Y_raw.apply(target_encode)

with st.expander("Data Preparation"):
  st.write("**Encoded X (input penguin)**")
  input_row
  st.write('**Encoded Y**')
  y

#Model Training
##Train the ML Model
clf  = RandomForestClassifier()
clf.fit(X, y)

#Apply model to make predictions
prediction = clf.predict(input_row)
prediction_probab = clf.predict_proba(input_row)
df_prediction_probab = pd.DataFrame(prediction_probab)
df_prediction_probab.columns = ['Adelie', 'Chinstrap', 'Gentoo']
df_prediction_probab.rename(columns = {
  0: 'Adelie',
  1: 'Chinstrap',
  2: 'Gentoo'
})

#Display Predicted Species
st.subheader('Predicted Species')
st.dataframe(df_prediction_probab,
            column_config = {
              'Adelie': st.column_config.ProgressColumn(
                'Adelie',
                format = '%f', 
                width= 'medium',
                min_value=0,
                max_value=1
              ),
              'Chinstrap': st.column_config.ProgressColumn(
                'Chinstrap',
                format = '%f', 
                width= 'medium',
                min_value=0,
                max_value=1
              ),
              'Gentoo': st.column_config.ProgressColumn(
                'Gentoo',
                format = '%f', 
                width= 'medium',
                min_value=0,
                max_value=1
              ),
            },  hide_index = True )
df_prediction_probab

penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.success(str(penguins_species[prediction]))



