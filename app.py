import streamlit as st

st.title('Addition of two numbers')
st.subheader('Tomin J Vellackal')
st.text('21f1004496')

num1 = st.text_input('Enter the first number : ')
num2 = st.text_input('Enter the second number : ')

btn = st.button('Calculate')


if btn:
    if num1 and num2:
        try:
            num1 = float(num1)
            num2 = float(num2)
            st.markdown(f"## {num1} + {num2} = {float(num1) + float(num2)}")
        except ZeroDivisionError:
            st.error("Do not divide by zero!")
        except ValueError:
            st.error("Enter numbers only!")
    else:
        st.error('Please enter the numbers')
