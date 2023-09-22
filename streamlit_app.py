import streamlit
import pandas

streamlit.title('My parents healthy dinner')
streamlit.text('Hi Trupti What are you making today in dinner ?? ')

list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(list)
