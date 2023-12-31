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


def get_fruitvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + input_text)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
streamlit.header('Fruitvice fruit advice')
try:
  input_text = streamlit.text_input('which fruit you want to choose ?')
  if not input_text:
    streamlit.error("please select a fruit to get a information.")
  else:
    back_from_function = get_fruitvice_data(input_text)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

streamlit.header("The fruit load list contains:")
#snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

#Add button to load fruit
if streamlit.button('View Our Fruit List - Add Your Favorites'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('"+new_fruit+"')")
    return "Thanks for adding" + new_fruit

add_my_fruit = streamlit.text_input('which fruit you would like to add ?', 'jackfruit')

if streamlit.button('Add fruit to a list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

