import streamlit as st

task=st.text_input ("Enter the Task")
if st.button("Add"):
    if task:
        with open(r'Database/task.txt','a') as f:
            f.write(task+'\n')
            st.success("Add Task Successfully")
    else:
        st.error("Enter something")