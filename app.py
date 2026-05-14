import streamlit as st
from components import *

#st.error("app on maintanance")

handler.load_css("assets/style.css")

s = sidebar.Sidebar()
page = s.main()
s.contact()
s.manage()
s.account()

if page == "generate":
    page = generate.GeneratePage()
    page.render()