import streamlit as st
import pandas as pds
st.title("streamlit calculator")
num1=st.number_input("Enter first number")
num2=st.number_input("Enter second number")
operation=st.selectbox("Choose operation", ("Add","Subtract","Multiply","Divide"))
if operation=="Add":
 result=num1+num2
elif operation=="Subtract":
 result=num1-num2
elif operation=="Multiply":
 result=num1*num2
elif operation=="Divide":
 if num2 !=0:
  result=num1/num2
 else: 
   result="error of zero division"

st.write("Result :",result)


