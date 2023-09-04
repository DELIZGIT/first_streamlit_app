import streamlit
import pandas

streamlit.title('Breakfast Favorites')

streamlit.header('🥐🥨Breakfast Favorites')
streamlit.text('🥑Omega 3 & blueberry Oatmeal')
streamlit.text('🥦🥬kale, Spinach & Rocket smoothie')
streamlit.text('🥚🥚Hard-Boiled free-range egg')

streamlit.header('🍌🍍🍉Build your own fruit smoothie🥝🥑🥭')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
