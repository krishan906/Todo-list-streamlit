import streamlit as st

all_tasks=[]
with open(r'Database/task.txt','r') as f:
    tasks = f.readlines()
    all_tasks = [task.strip() for task in tasks]

for i in all_tasks:
    st.text(i)

delete_task = st.selectbox("Select the task",all_tasks)
if st.button("Delete"):
    if delete_task in all_tasks:
        all_tasks.remove(delete_task)

        with open(r'Database/task.txt','w') as f:
            for i in all_tasks:
                f.write(i + '\n')
        
        with open(r'Database/completed_tasks.txt','a') as f:
            f.write(delete_task + '\n')
        

        st.success(f'{delete_task} Delete Successfully')
    else:
        st.error(f"{delete_task} is not there")

