import streamlit as st

all_tasks = []
with open (r'Database/task.txt','r') as f:
    tasks = f.readlines()
    all_tasks=[task.strip() for task in tasks]

st.write("### All Task list")
for i in all_tasks:
    st.text(i)

task_name = st.text_input("Enter the name of task",key="task_name")
modified_task_name = st.text_input("Enter the name of task",key="modified_task_name")


if st.button("Modify"):
    if task_name in all_tasks:
        index = all_tasks.index(task_name)
        all_tasks[index]=modified_task_name
        with open(r'Database/task.txt','w') as f:
            for i in all_tasks:
                f.write(i + '\n')
        st.success(f"{modified_task_name} Modified successfully")
    else:
        st.error(f"{modified_task_name} is not in list")

st.write("### Update Task list")
for i in all_tasks:
    st.text(i)