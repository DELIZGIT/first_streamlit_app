import streamlit
import pandas
import requests


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
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
