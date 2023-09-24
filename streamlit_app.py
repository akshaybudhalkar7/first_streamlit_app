import streamlit
import pandas
import requests

streamlit.title('My parents healthy dinner')
streamlit.text('Hi Trupti What are you making today in dinner ?? ')

fruits_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruits_list = fruits_list.set_index('Fruit')

streamlit.dataframe(fruits_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(fruits_list.index), ['Banana','Avocado'])
fruit_to_show = fruits_list.loc[fruit_selected]


# Display the table on the page.
streamlit.dataframe(fruit_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
