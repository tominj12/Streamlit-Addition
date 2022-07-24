import streamlit as st

string = "Subtraction of Two Numbers"
st.set_page_config(page_title=string, page_icon="➕")
st.title('Subtraction of Two Numbers')
#x = st.number_input('Enter a number')
num1 = st.number_input("Enter first number",min_value=0.0,max_value=100000000.0)
num2 = st.number_input("Enter second number",min_value=0.0,max_value=100000000.0)
if (num1).is_integer() and (num2).is_integer():
    sum=num1-num2
    st.write("the addition result is", sum)
else:st.write("please enter integer number")
