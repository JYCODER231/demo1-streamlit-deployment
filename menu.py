import streamlit as st
from streamlit_option_menu import option_menu

st.title('Hello, Students!')
st.write('This is your Python Programming course.')

with st.sidebar: #sidebar : create a new area on the lesft handside of the streamlit webpage
    selected=option_menu(
        menu_title = "Menu",
        options = ["Home", "About", "Contact"],
        icons = ["house","cloud-upload","list-task"],#选项前的小图标
        menu_icon= "emoji-sad-fill",
        default_index=0,
    )

if selected == "Home":
    st.title(f"Welcome to the {selected} page.")

if selected == "About":
    st.title(f"Welcome to the {selected} page.")

if selected == "Contact":
    st.title(f"Welcome to the {selected} page.")
