import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interative app")
st.write("Choose your fav. variety of chai")

chai = st.selectbox("Your fav chai: ", ["Masala chai", "Lemon Tea", "Adrak Tea", "Kesar Chai" ])
st.write(f"Your choose {chai}. Excellent choise")

st.success("Your chai is been brewed")