import streamlit as st

st.title("Simple To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Enter a task:")

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append(task)
        st.success("Task added successfully!")

st.subheader("Your Tasks:")

for i, t in enumerate(st.session_state.tasks, start=1):
    st.write(f"{i}. {t}")