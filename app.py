import streamlit as st
from components import *

h = handler.Handler()

s = sidebar.Sidebar()
page = s.main()
s.contact()
s.manage()
s.account()

if page == "generate":
    p = generate.GeneratePage()
    p.run()
elif page == "assignments":
    p = Assignments.AssignmentGeneratePage()
    p.run()