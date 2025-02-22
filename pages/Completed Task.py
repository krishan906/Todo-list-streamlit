import streamlit as st

with open(r'Database/deleted_tasks.txt','r') as f:
    tasks = f.readlines()
    for task in tasks:
        st.text(task.strip())
