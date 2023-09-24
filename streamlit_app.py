import streamlit
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError

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

streamlit.header('Fruitvice fruit added')

input_text = streamlit.text_input('which fruit you want to choose ?', 'kiwi')
streamlit.write('the user entered', input_text)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + input_text)
streamlit.stop()
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('which fruit you would like to add ?', 'jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)

my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")

