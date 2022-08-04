import streamlit as st
import pickle
import pandas as pd
import numpy as np



pipe = pickle.load(open('clay-latlong-small.pkl','rb'))
st.title('Lat - Long Based Clay Predictor')


coarse = st.number_input('coarse')
pH_in_H2O = st.number_input('pH_in_H2O')
pH_in_CaCl2 = st.number_input('pH_in_CaCl2')
OC = st.number_input('OC')
CaCO3 = st.number_input('CaCO3')
N = st.number_input('N')
P = st.number_input('P')
K = st.number_input('K')
CEC = st.number_input('CEC')
GPS_LAT = st.number_input('GPS_LAT')
GPS_LONG = st.number_input('GPS_LONG')


# 'pH(CaCl2)':[pH(CaCl2)],'pH(H2O)':[pH(H2O)],
if st.button('Predict'):
      input=pd.DataFrame({'coarse':[coarse],'pH_in_H2O':[pH_in_H2O],'pH_in_CaCl2':[pH_in_CaCl2],'OC':[OC],'CaCO3':[CaCO3],'N':[N],'P':[P],'K':[K],'CEC':[CEC],'GPS_LAT':[GPS_LAT],'GPS_LONG':[GPS_LONG]})
      result = pipe.predict(input)
      st.success('THE CLAY FOR GIVEN DATA WILL BE {}'.format(result))
# st.header(result)
