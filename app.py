import streamlit as st
#streamlit UI
st.title("power Calculator")
st.write("enter a number to claclute its square,cude and fifth power,")


#get user input 
n =st.number_input("enter an interger", value=1, step=1)


#claculate results
square = n**2
cube = n**3

#calutlate results
st.write(f"the square of {n} is {n**2}")
st.write(f"the cube of {n} is {n**3}")