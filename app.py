# Import libraries
import streamlit as st
from backend import store_data,preprocess_data,predict

# Initialize Streamlit app
st.set_page_config('Campus Placement')

st.title('Placement Prediction')

subheader_text = "Fill the following details :"
style = f"<p style='font-size:18px;font-family:serif'> {subheader_text} </p>"
st.markdown(style, unsafe_allow_html=True)

inp1=st.number_input('HSC Percentage')
inp2=st.number_input('Employability Test Percentage')
inp3=st.selectbox('Board Of Secondary Education other than Central?',['Yes','No'])
inp4=st.selectbox('Stream Of Higher Secondary Education other than Science?',['Yes','No'])
inp5=st.selectbox('Undergraduate Degree type other than Science & Technology?',['Yes','No'])
inp6=st.selectbox('Have any Work Experience?',['Yes','No'])
inp7=st.selectbox('Specialization in Marketing & HR',['Yes','No'])

submit=st.button('SUBMIT')

# If submit button clicked...
if submit:
   data=store_data(inp1,inp2,inp3,inp4,inp5,inp6,inp7)
   pred=predict(preprocess_data(data))#Prediction
   if pred[0]==1:
      st.subheader('Placed')
   else:
      st.subheader('Not Placed')
