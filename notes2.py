import streamlit as st
st.title("welcome to streamlit")
num1=st.number_input("enter number 1")

num2=st.number_input("enter number 2")
sum=num1+num2
if st.button("Add"):
    st.write("sum is:",sum)

sum=num1-num2
if st.button("sub"):
    st.write("sum is:",sum)

sum=num1*num2
if st.button("multi"):
    st.write("sum is:",sum)









