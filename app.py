import streamlit as st
def find_large(n1,n2,n3) :
  return max(n1,n2,n3)

st.title('Find the Largest number')
n1 = st.number_input("Enter the first number",value=0.0)
n2 = st.number_input("Enter the second number",value=0.0)
n3 = st.number_input("Enter the third number",value=0.0)

if st.button('Find Largest'):
  largest=find_large(n1,n2,n3)
  st.success(f'The largest number is: {largest}')
