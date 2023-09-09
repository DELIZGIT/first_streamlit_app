import streamlit
import pandas
import requests
import snowflake.connector


streamlit.title('Breakfast Favorites')

streamlit.header('🥐🥨Breakfast Favorites')
streamlit.text('🥑Omega 3 & blueberry Oatmeal')
streamlit.text('🥦🥬kale, Spinach & Rocket smoothie')
streamlit.text('🥚🥚Hard-Boiled free-range egg')

streamlit.header('🍌🍍🍉Build your own fruit smoothie🥝🥑🥭')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
# New section
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Display data in Frame
streamlit.dataframe(fruityvice_normalized)

### connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

