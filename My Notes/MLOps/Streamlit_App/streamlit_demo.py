import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt

st.set_page_config(page_title="Streamlit demo", page_icon="test.jpg") #used to set tab title and favicon

st.title("Hello World")
st.header("My lord")
st.subheader("My mans")
st.error("lol")

def sqrt(num):
    return np.sqrt(num)

num = st.number_input("Enter number here", min_value = 0.00, step=1.0, value = 100.00, format="%.2f")
num = sqrt(num)
st.write(f"sqrt of num is {num:.2f}")

date_inp = st.date_input("Enter a date", format="DD/MM/YYYY")
date_diff = date_inp - dt.date.today()

st.write(f"Date is: {date_diff}")

st.image(image="test.jpg")