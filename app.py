import streamlit as st
import joblib
model = joblib.load('spam-ham')
st.title('SPAM-HAM Classifier')
ip = st.text_input('Enter The message')#It Creates a text box
op = model.predict([ip])
if st.button('Predict'):
 st.title(op[0])# the 0th element in op variable is display as a title

 
 
 
 
