import streamlit as st
from components import *

h = handler.Handler()
h.load_css("assets/style.css")

s = sidebar.Sidebar()
page = s.main()
s.contact()
s.manage()
s.account()

if page == "generate":
    page = generate.GeneratePage()
    page.run()