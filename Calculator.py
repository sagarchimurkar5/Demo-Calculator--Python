import streamlit as ST

ST.title("calculator")
num1=ST.number_input("enter the 1st number")
num2=ST.number_input("enter the 2nd number")
operation=ST.radio("Operation:",["Add","Subtract"])

if ST.button("calculate"):  
  if operation=="Add":
    ST.write("Result",num1+num2)
  else:
    ST.write("Result",num1-num2)



    