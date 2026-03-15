import streamlit as st

st.set_page_config(page_title="AI To-Do App", page_icon="✅")

st.title("✅ Smart To-Do List")
st.write("Manage your tasks efficiently.")

# initialize task list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# add new task
st.subheader("Add New Task")

task_input = st.text_input("Enter your task")

if st.button("Add Task"):
    if task_input:
        st.session_state.tasks.append({"task": task_input, "done": False})

# task statistics
total_tasks = len(st.session_state.tasks)
completed_tasks = len([t for t in st.session_state.tasks if t["done"]])

st.write(f"📌 Total Tasks: {total_tasks}")
st.write(f"✅ Completed: {completed_tasks}")

st.divider()

# display tasks
st.subheader("Your Tasks")

for i, task in enumerate(st.session_state.tasks):

    col1, col2, col3 = st.columns([6,2,2])

    with col1:
        done = st.checkbox(task["task"], value=task["done"], key=i)
        st.session_state.tasks[i]["done"] = done

    with col2:
        if st.button("Delete", key=f"del{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()

    with col3:
        if task["done"]:
            st.write("✔ Done")